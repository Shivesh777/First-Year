"""CSC110 Fall 2022: Simulation Event Queue

Module Description
==================

This module contains multiple implementations of a priority queue of events.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC110 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2022 David Liu and Mario Badr.
"""
import datetime

# Imports for alternate implementations of Priority Queues
import heapq

from events import Event


class EventQueue:
    """A priority queue of events.

    Events are dequeued in timestamp order (earlier timestamp = higher priority).
    """
    def is_empty(self) -> bool:
        """Return whether this event queue contains no items."""
        raise NotImplementedError

    def enqueue(self, event: Event) -> None:
        """Add event to this event queue, sorted by its timestamp."""
        raise NotImplementedError

    def dequeue(self) -> Event:
        """Remove and return the earliest event in this event queue.

        Preconditions:
        - not self.is_empty()
        """
        raise NotImplementedError


class EventQueueList(EventQueue):
    """A queue of events that can be dequeued in timestamp order.

    Right now this is the only implementation of EventQueue, but you'll see
    another in this week's tutorial.

    Note: this is related to the "PriorityQueueSorted" class
    we discussed last week.
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
        """Add event to this event queue."""
        index = 0
        while index < len(self._events) and \
                self._events[index].timestamp > event.timestamp:
            index = index + 1

        self._events.insert(index, event)

    def dequeue(self) -> Event:
        """Remove and return the earliest event in this event queue.

        Preconditions:
        - not self.is_empty()
        """
        return self._events.pop()


class EventQueueHeap(EventQueue):
    """A heap of events that can be dequeued in timestamp order."""
    # Private Instance Attributes:
    #   - _events: a heap of events
    #   - _entry_count: a non-decreasing counter storing all events ever
    #                   enqueued (used to break ties for heapq)
    _events: list[tuple[datetime.datetime, int, Event]]
    _entry_count: int

    def __init__(self) -> None:
        """Initialize a new and empty event queue."""
        self._events = []
        self._entry_count = 0

    def is_empty(self) -> bool:
        """Return whether this event queue contains no items."""
        return self._events == []

    def enqueue(self, event: Event) -> None:
        """Add an event to this event queue."""
        heapq.heappush(self._events, (event.timestamp, self._entry_count, event))
        self._entry_count += 1

    def dequeue(self) -> Event:
        """Remove and return the earliest event in this event queue.

        Preconditions:
        - not self.is_empty()
        """
        _, _, event = heapq.heappop(self._events)
        return event
