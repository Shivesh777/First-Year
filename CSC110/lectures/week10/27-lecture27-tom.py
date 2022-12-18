"""David and Tom Lecture 27 examples"""
from typing import Any


class Stack:
    """A last-in-first-out (LIFO) stack of items.

    Stores data in a last-in, first-out order. When removing an item from the
    stack, the most recently-added item is the one that is removed.

    >>> s = Stack()
    >>> s.is_empty()
    True
    >>> s.push('hello')
    >>> s.is_empty()
    False
    >>> s.push('goodbye')
    >>> s.pop()
    'goodbye'
    """
    # Private Instance Attributes:
    #   - items: a list containing the items in the stack. The end of the list
    #            represents the top of the stack.
    _items: list

    def __init__(self) -> None:
        """Initialize a new empty stack."""
        self._items = []

    def is_empty(self) -> bool:
        """Return whether this stack contains no items.
        """
        return self._items == []

    def push(self, item: Any) -> None:
        """Add a new element to the top of this stack."""
        self._items.append(item)

    def pop(self) -> Any:
        """Remove and return the element at the top of this stack.
        """
        return self._items.pop()


class EmptyStackError(Exception):
    """Exception raised when calling pop on an empty stack."""


class Stack1:
    """A last-in-first-out (LIFO) stack of items.

    Stores data in a last-in, first-out order. When removing an item from the
    stack, the most recently-added item is the one that is removed.

    >>> s = Stack1()
    >>> s.is_empty()
    True
    >>> s.push('hello')
    >>> s.is_empty()
    False
    >>> s.push('goodbye')
    >>> s.pop()
    'goodbye'
    """
    # Private Instance Attributes:
    #   - items: a list containing the items in the stack. The end of the list
    #            represents the top of the stack.
    _items: list

    def __init__(self) -> None:
        """Initialize a new empty stack."""
        self._items = []

    def is_empty(self) -> bool:
        """Return whether this stack contains no items.
        """
        return self._items == []

    def push(self, item: Any) -> None:
        """Add a new element to the top of this stack."""
        self._items.append(item)

    def pop(self) -> Any:
        """Remove and return the element at the top of this stack.

        Raise an EmptyStackError if this stack is empty.
        """
        if self.is_empty():
            raise EmptyStackError  # Could also raise a built-in error, like ValueError/IndexError
        else:
            return self._items.pop()


###############################################################################
# Queues
###############################################################################
class Queue:
    """A first-in-first-out (FIFO) queue of items.

    Stores data in a first-in, first-out order. When removing an item from the
    queue, the most recently-added item is the one that is removed.

    >>> q = Queue()
    >>> q.is_empty()
    True
    >>> q.enqueue('hello')
    >>> q.is_empty()
    False
    >>> q.enqueue('goodbye')
    >>> q.dequeue()
    'hello'
    >>> q.dequeue()
    'goodbye'
    >>> q.is_empty()
    True
    """
    # Private Instance Attributes:
    #   - _items: The items stored in this queue. The front of the list represents
    #             the front of the queue.
    _items: list

    def __init__(self) -> None:
        """Initialize a new empty queue."""
        self._items = []  # Theta(1)

    def is_empty(self) -> bool:
        """Return whether this queue contains no items.
        """
        return self._items == []  # Theta(1)
        # In general, if you have two lists lst1, lst2
        # lst1 == lst2 has worst-case running time of 
        # Theta(min(len(lst1), len(lst2))).

    def enqueue(self, item: Any) -> None:
        """Add item to the back of this queue.
        """
        self._items.append(item)  # list.append takes CONSTANT TIME (Theta(1))

        # Using the back of the list:
        # self._items.insert(0, item)

    def dequeue(self) -> Any:
        """Remove and return the item at the front of this queue.

        Preconditions:
            - not self.is_empty()
        """
        return self._items.pop(0)  # list.pop with index 0 takes Theta(n) time

        # Using the back of the list:
        # return self._items.pop()

        # could also add and use an EmptyQueueError exception

###############################################################################
# Priority Queues
###############################################################################
class PriorityQueueUnsorted:
    """A queue of items that can be dequeued in priority order.

    When removing an item from the queue, the highest-priority item is the one
    that is removed.

    >>> pq = PriorityQueueUnsorted()
    >>> pq.is_empty()
    True
    >>> pq.enqueue(1, 'hello')
    >>> pq.is_empty()
    False
    >>> pq.enqueue(5, 'goodbye')
    >>> pq.enqueue(2, 'hi')
    >>> pq.dequeue()
    'goodbye'
    """
    # Private Instance Attributes:
    #   - _items: A list of the items in this priority queue.
    #             Each element is a 2-element tuple where the first element is
    #             the priority and the second is the item.

    # EXERCISE: could try to implement with a _items: dict[int, Any] instead

    _items: list[tuple[int, Any]]

    def __init__(self) -> None:
        """Initialize a new and empty priority queue."""
        self._items = []

    def is_empty(self) -> bool:
        """Return whether this priority queue contains no items.
        """
        return self._items == []

    def enqueue(self, priority: int, item: Any) -> None:
        """Add the given item with the given priority to this priority queue.
        """
        self._items.append((priority, item))  # Note the two pairs of parentheses!

    def dequeue(self) -> Any:
        """Remove and return the element of this priority queue with the highest priority.

        Preconditions:
            - not self.is_empty()
        """

        # could also add and use an EmptyQueueError exception

        # 1. Find the maximum priority element of the list
        max_index_so_far = 0  # index of the maximum priority pair so far

        for i in range(1, len(self._items)):
            # If the priority at index i is > the max priority so far,
            # update max_index_so_far
            if self._items[i][0] > self._items[max_index_so_far][0]:
                max_index_so_far = i

        # 2. Get the pair and remove it from the list.
        max_pair = self._items.pop(max_index_so_far)

        # 3. Return the item
        return max_pair[1]

        # Analysis. Let n be the size of the priority queue.
        #
        # The first statement max_index_so_far = 0 takes 1 step.
        # The for loop:
        #   - takes n - 1 iterations
        #   - each iteration takes 1 step
        #   - so there are a total of n - 1 steps
        #
        # The statement max_pair = self._items.pop(max_index_so_far)
        #   takes n - k steps, where k is the value of max_index_so_far
        #
        # The final return statement takes 1 step.
        #
        # So the total running time is
        #   1 + (n - 1) + (n - k) + 1 = 2n - k + 1.
        # But we know that k is a valid index into self._items!
        # And so 0 <= k < n, and so k is O(n).
        #
        # And so 2n - k + 1 is Theta(n).
        #
        # (Alternate last step):
        #   because 0 <= k < n, we know that n + 1 < 2n - k + 1 <= 2n + 1.
        #   And so 2n - k + 1 is Theta(n).
