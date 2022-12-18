"""David Lecture 26 examples"""
from typing import Any


class Stack:
    """A last-in-first-out (LIFO) stack of items.

    Stores data in a last-in, first-out order. When removing an item from the
    stack, the most recently-added item is the one that is removed.

    Instance Attributes:
        - items: The elements contained in this stack (back of the list represents the
                 top of the stack)

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
    # items: list

    # Version with private instance attribute
    # Instance Attributes:
    #     - _items: The elements contained in this stack (back of the list represents the
    #               top of the stack)
    _items: list

    def __init__(self) -> None:
        """Initialize a new empty stack."""
        self._items = []  # Theta(1)

    def is_empty(self) -> bool:
        """Return whether this stack contains no items.
        """
        return self._items == []  # Theta(1)

    def push(self, item: Any) -> None:
        """Add a new element to the top of this stack."""
        # Version 1
        # list.append(self.items, item)

        # Version 2
        self._items.append(item)  # Theta(1)

    def pop(self) -> Any:
        """Remove and return the element at the top of this stack.

        Preconditions:
            - not self.is_empty()
        """
        # Version 1
        # return list.pop(self.items)

        # Version 2
        return self._items.pop()  # Theta(1)


# Exercise 1
def size_v1(s: Stack) -> int:
    """Return the number of items in s.
    """
    count = 0
    for _ in s:             # PROBLEM: stacks don't support "for loop iteration"
        count = count + 1
    return count


def size_v2(s: Stack) -> int:
    """Return the number of items in s.
    """
    count = 0
    while not s.is_empty():  # or, while not Stack.is_empty(s)
        s.pop()                # PROBLEM: mutates s!
        count = count + 1
    return count


def size_v3(s: Stack) -> int:
    """Return the number of items in s.
    """
    return len(s._items)       # PROBLEM: tries to access instance attribute _items, which isn't part of a Stack!


def size_v4(s: Stack) -> int:
    """Return the number of items in s.
    """
    s_copy = s                    # PROBLEM: this creates an alias of s, not a copy!
    count = 0
    while not s_copy.is_empty():
        s_copy.pop()              # PROBLEM: so mutating s_copy also will mutate s (they refer to the same object)
        count += 1
    return count


def size(s: Stack) -> int:
    """Return the number of items in s.

    >>> s = Stack()
    >>> size(s)
    0
    >>> s.push('hi')
    >>> s.push('more')
    >>> s.push('stuff')
    >>> size(s)
    3
    """
    temp_stack = Stack()

    # Count the items in s by popping them off, but store them in temp_stack
    count = 0
    while not s.is_empty():
        item = s.pop()
        temp_stack.push(item)
        temp_stack.push(s.pop())
        count = count + 1

    # Restore the items in s by popping them off of temp_stack
    while not temp_stack.is_empty():
        item = temp_stack.pop()
        s.push(item)

    # Return the count
    return count


class Stack2:
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
    #   - items: a list containing the items in the stack. The FRONT of the list
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
        self._items.insert(0, item)  # Theta(n), where n is the size of the stack

    def pop(self) -> Any:
        """Remove and return the element at the top of this stack.

        Preconditions:
            - not self.is_empty()
        """
        return self._items.pop(0)   # Theta(n), where n is the size of the stack
