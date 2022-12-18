"""CSC111 W04 - Starter File

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC111 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC111 materials,
please consult our Course Syllabus.
"""
from __future__ import annotations
from typing import Any, Optional


class Tree:
    """A recursive tree data structure.

    Representation Invariants:
        - self._root is not None or self._subtrees == []
    """
    # Private Instance Attributes:
    #   - _root:
    #       The item stored at this tree's root, or None if the tree is empty.
    #   - _subtrees:
    #       The list of subtrees of this tree. This attribute is empty when
    #       self._root is None (representing an empty tree). However, this attribute
    #       may be empty when self._root is not None, which represents a tree consisting
    #       of just one item.
    _root: Optional[Any]
    _subtrees: list[Tree]

    ################################################################################################
    # From the Notes - 13.1
    ################################################################################################
    def __init__(self, root: Optional[Any], subtrees: list[Tree]) -> None:
        """Initialize a new Tree with the given root value and subtrees.

        If root is None, the tree is empty.

        Preconditions:
            - root is not none or subtrees == []
        """
        self._root = root
        self._subtrees = subtrees

    def is_empty(self) -> bool:
        """Return whether this tree is empty."""
        return self._root is None

    ################################################################################################
    # From the Notes - 13.2
    ################################################################################################
    def __len__(self) -> int:
        """Return the number of items contained in this tree.

        >>> t1 = Tree(None, [])
        >>> len(t1)
        0
        >>> t2 = Tree(3, [Tree(4, []), Tree(1, [])])
        >>> len(t2)
        3
        """
        if self.is_empty():
            return 0
        else:
            return 1 + sum(subtree.__len__() for subtree in self._subtrees)

    ################################################################################################
    # Exercise 1
    ################################################################################################
    def first_at_depth(self, d: int) -> Optional[Any]:
        """Return the leftmost value at depth d in this tree.

        Return None if there are NO items at depth d in this tree.

        Preconditions:
            - d >= 0  # depth 0 is the root of the tree
        """
        if self.is_empty():
            return None
        elif self._subtrees == []:
            if d == 0:
                return self._root
            else:
                return None
        else:
            if d == 0:
                return self._root
            else:
                for subtree in self._subtrees:
                    rec_val = subtree.first_at_depth(d - 1)
                    if rec_val is not None:
                        return rec_val
                return None
    ################################################################################################
    # Demo 1
    ################################################################################################

    def __str__(self) -> str:
        """Return a string representation of this tree."""
        return self._str_indented(0)

    def _str_indented(self, depth: int = 0) -> str:
        """Return a string representation of this tree."""
        if self.is_empty():
            return ''
        else:
            s = '  ' * depth + f'{self._root}\n'
            for subtree in self._subtrees:
                # Note that the 'depth' argument to the recursive call is modified.
                s += subtree._str_indented(depth + 1)
            return s
    ################################################################################################
    # Demo 2
    ################################################################################################

    def average(self) -> float:
        """Return the average of the numbers in this tree.

        Return 0.0 if this tree is empty.

        Preconditions:
            - this tree contains only numbers
        """
        if self.is_empty():
            return 0.0
        else:
            # Homework: complete this method by defining
            # a recursive helper function
            sum_items, num_items = self.sum(), len(self)
            return sum_items / num_items

    def sum(self) -> float:
        if self.is_empty():
            return 0.0
        elif self._subtrees == []:
            return self._root
        else:
            sum_so_far = self._root
            for subtree in self._subtrees:
                sum_so_far += subtree.sum()
            return sum_so_far

    ################################################################################################
    # From the W04 Preparation Exercise
    ################################################################################################
    def __contains__(self, item: Any) -> bool:
        """Return whether the given item is in this tree."""
        if self.is_empty():
            return False
        elif self._root == item:
            return True
        else:
            for subtree in self._subtrees:
                if subtree.__contains__(item):
                    return True

            return False

    ################################################################################################
    # Exercise 2
    ################################################################################################
    def remove(self, item: Any) -> bool:
        """Delete *one* occurrence of the given item from this tree.

        Do nothing if the item is not in this tree.
        Return whether the given item was deleted.
        """
        if self.is_empty():
            return False
        elif self._root == item:
            self._delete_root()
            return True
        else:
            for subtree in self._subtrees:
                deleted = subtree.remove(item)
                if deleted:
                    # One occurrence of the item was deleted, so we're done.
                    return True

            # If the loop doesn't return early, the item was not deleted from
            # any of the subtrees. In this case, the item does not appear
            # in this tree.
            return False

    def _delete_root(self) -> None:
        """Remove the root of this tree.

        Preconditions:
            - not self.is_empty()
        """
        if self._subtrees == []:
            self._root = None
        else:
            self._root = self._subtrees[0]
            self._subtrees.pop(0)

    def _extract_leaf(self):
        if self._subtrees == []:
            root = self._root
            self._root = None
            return root
        else:
            return self._subtrees[0]._extract_leaf()


if __name__ == '__main__':
    my_tree = Tree(5, [
        Tree(8, [Tree(3, []), Tree(2, []), Tree(6, [])]),
        Tree(10, []),
        Tree(7, [Tree(0, [Tree(111, [])])])
    ])

