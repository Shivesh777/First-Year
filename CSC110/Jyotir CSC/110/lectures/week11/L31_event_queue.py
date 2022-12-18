"""CSC110 Fall 2020: Simulation Event Queue

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC110 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2020 David Liu and Mario Badr.
"""
from L31_events import Event


class EmptyEventQueueError(Exception):
    """Exception raised when calling dequeue on an empty event queue."""

    def __str__(self) -> str:
        """Return a string representation of this error."""
        return 'You called dequeue on an empty event queue.'


class EventQueue:
    """A priority queue of events.

    Events are dequeued in timestamp order (earlier timestamp = higher priority).
    """

    def is_empty(self) -> bool:
        """Return whether this event queue contains no items."""
        raise NotImplementedError

    def enqueue(self, event: Event) -> None:
        """Add event to this queue, sorted by its timestamp."""
        raise NotImplementedError

    def dequeue(self) -> Event:
        """Remove and return the earliest event in the queue.

        Raises an EmptyEventQueueError when the queue is empty.
        """
        raise NotImplementedError


class EventQueueList(EventQueue):
    """A queue of events that can be dequeued in timestamp order.

    Right now this is the only implementation of EventQueue, but you'll see
    another in this week's tutorial.
    """
    # Private Instance Attributes:
    #   _events: a list of the events in this queue

    _events: list[Event]

    def __init__(self) -> None:
        """Initialize a new and empty event queue."""
        self._events = []

    def is_empty(self) -> bool:
        """Return whether this event queue contains no items."""
        return self._events == []

    def enqueue(self, event: Event) -> None:
        """Add event to this queue, sorted by its timestamp."""
        index = 0
        while index < len(self._events) and \
                self._events[index].timestamp > event.timestamp:
            index = index + 1

        self._events.insert(index, event)

    def dequeue(self) -> Event:
        """Remove and return the earliest event in the queue.

        Raises an EmptyEventQueueError when the queue is empty.
        """
        if self.is_empty():
            raise EmptyEventQueueError
        else:
            return self._events.pop()
