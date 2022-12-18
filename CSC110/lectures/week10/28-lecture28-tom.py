"""David and Tom Lecture 28 examples"""
from typing import Any


class Stack:
    def is_empty(self) -> bool:
        """Return whether this stack contains no items."""
        raise NotImplementedError

    def push(self, item: Any) -> None:
        """Add a new element to the top of this stack."""
        raise NotImplementedError

    def pop(self) -> Any:
        """Remove and return the element at the top of this stack.

        Preconditions:
            - not self.is_empty()
        """
        raise NotImplementedError


class Stack1(Stack):
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

    def __str__(self) -> str:
        """Return a string representation of this stack.

        >>> s = Stack1()
        >>> str(s)
        'Stack1: empty'
        >>> s.push(10)
        >>> s.push(20)
        >>> s.push(30)
        >>> str(s)
        'Stack1: 30 (top), 20, 10'

        Notes:
            - because this is a method, you may access the _items attribute
            - call str on each element of the stack to get string representations
              of the items
            - review the str.join method
            - you can reverse the items in a list by calling reversed on it
              (returns a new iterable) or the list.reverse method (mutates the list)
        """
        if self.is_empty():
            return ...
        else:
            # 1. The initial label
            start = 'Stack1: '

            # 2. Get the string representations of each item
            strings = [str(item) for item in reversed(self._items)]
            # Need to also add ' (top)' to the first string.
            strings[0] = strings[0] + ' (top)'

            # 3. Join the strings together and return
            joined_items = str.join(', ', strings)
            # or,
            # joined_items = ', '.join(strings)
            return start + joined_items


    def is_empty(self) -> bool:
        """Return whether this stack contains no items.
        """
        return self._items == []

    def push(self, item: Any) -> None:
        """Add a new element to the top of this stack."""
        self._items.append(item)

    def pop(self) -> Any:
        """Remove and return the element at the top of this stack.

        Preconditions:
            - not self.is_empty()
        """
        return self._items.pop()


class Stack2(Stack):
    """A last-in-first-out (LIFO) stack of items.

    Stores data in a last-in, first-out order. When removing an item from the
    stack, the most recently-added item is the one that is removed.

    >>> s = Stack2()
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
        self._items.insert(0, item)

    def pop(self) -> Any:
        """Remove and return the element at the top of this stack.

        Preconditions:
            - not self.is_empty()
        """
        return self._items.pop(0)


def push_and_pop(stack: Stack, item: Any) -> None:
    stack.push(item)
    stack.pop()
    # Stack.push(stack, item)
    # Stack.pop(stack)


def weird(stacks: list[Stack]) -> None:
    for stack in stacks:
        if stack.is_empty():
            stack.push('pancake')
        else:
            stack.pop()


class Donut:
    """Why not?"""
    def __init__(self, name:str) -> None:
        self.name = name
    def __str__(self) -> str:
        return 'donut of flavour ' + self.name
    def __eq__(self, other) -> bool:
        return self.name == other.name

if __name__ == '__main__':
    my_stack = Stack1()
    push_and_pop(my_stack, 10)
#
    my_stack2 = Stack2()
    push_and_pop(my_stack2, 10)
#
    list_of_stacks = [Stack1(), Stack2(), Stack1(), Stack2()]
    list_of_stacks[0].push('chocolate')
    list_of_stacks[2].push('chocolate')

    weird(list_of_stacks)
    # Iteration 0 -- Stack1.pop
    # Iteration 1 -- Stack2.push
    # Iteration 2 -- Stack1.pop
    # Iteration 3 -- Stack2.push
#
    # Q2
    list_of_stacks2 = [Stack1(), Stack2(), Stack1(), Stack2()]
    list_of_stacks2[2].push('chocolate')
    list_of_stacks2[3].push('chocolate')
    weird(list_of_stacks2)
    # Iteration 0 -- Stack1.push
    # Iteration 1 -- Stack2.push
    # Iteration 2 -- Stack1.pop
    # Iteration 3 -- Stack2.pop
#
    list_of_stacks3 = [Stack1(), Stack()]
    # weird(list_of_stacks3)
    # Iteration 0 -- Stack1.push (or something else)
    # Iteration 1 -- NotImplementedError --- Stack.is_empty
#
    d1 = Donut('maple')
    d2 = Donut('bc')
    d3 = Donut('maple')
    print(d1)
    print(d2)
    print(d1 == d1)
    print(d1 == d2)
    print(d1 == d3)
