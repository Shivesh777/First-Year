"""CSC111 W05 - Starter File

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


class BinarySearchTree:
    """Binary Search Tree class.

    Representation Invariants:
      - (self._root is None) == (self._left is None)
      - (self._root is None) == (self._right is None)
      - (BST Property) if self._root is not None, then
          all items in self._left are <= self._root, and
          all items in self._right are >= self._root

    Note that duplicates of the root can appear in *either* the left or right subtrees.
    """
    # Private Instance Attributes:
    #   - _root:
    #       The item stored at the root of this tree, or None if this tree is empty.
    #   - _left:
    #       The left subtree, or None if this tree is empty.
    #   - _right:
    #       The right subtree, or None if this tree is empty.
    _root: Optional[Any]
    _left: Optional[BinarySearchTree]
    _right: Optional[BinarySearchTree]

    def __init__(self, root: Optional[Any]) -> None:
        """Initialize a new BST containing only the given root value.

        If <root> is None, initialize an empty tree.
        """
        if root is None:
            self._root = None
            self._left = None
            self._right = None
        else:
            self._root = root
            self._left = BinarySearchTree(None)
            self._right = BinarySearchTree(None)

    def is_empty(self) -> bool:
        """Return whether this BST is empty.

        >>> bst = BinarySearchTree(None)
        >>> bst.is_empty()
        True
        >>> bst = BinarySearchTree(10)
        >>> bst.is_empty()
        False
        """
        return self._root is None

    def __contains__(self, item: Any) -> bool:
        """Return whether <item> is in this BST.

        >>> bst = BinarySearchTree(3)
        >>> bst._left = BinarySearchTree(2)
        >>> bst._right = BinarySearchTree(5)
        >>> bst.__contains__(3)  # or, 3 in bst
        True
        >>> bst.__contains__(5)
        True
        >>> bst.__contains__(2)
        True
        >>> bst.__contains__(4)
        False
        """
        if self.is_empty():
            return False
        elif item == self._root:
            return True
        elif item < self._root:
            return self._left.__contains__(item)  # or, item in self._left
        else:
            return self._right.__contains__(item)  # or, item in self._right

    def __str__(self) -> str:
        """Return a string representation of this BST.

        This string uses indentation to show depth.

        We've provided this method for debugging purposes, if you choose to print a BST.
        """
        return self._str_indented(0)

    def _str_indented(self, depth: int) -> str:
        """Return an indented string representation of this BST.

        The indentation level is specified by the <depth> parameter.

        Preconditions:
            - depth >= 0
        """
        if self.is_empty():
            return ''
        else:
            return (
                depth * '  ' + f'{self._root}\n'
                + self._left._str_indented(depth + 1)
                + self._right._str_indented(depth + 1)
            )

    ################################################################################################
    # Exercise 1
    ################################################################################################
    def insert(self, item: Any) -> None:
        """Insert <item> into this tree.

        Do not change positions of any other values.

        >>> bst = BinarySearchTree(10)
        >>> bst.insert(3)
        >>> bst.insert(20)
        >>> bst._root
        10
        >>> bst._left._root
        3
        >>> bst._right._root
        20
        """
        if self.is_empty():
            self._root = item
            self._left = BinarySearchTree(None)
            self._right = BinarySearchTree(None)
        elif self._root < item:
            self._right.insert(item)
        else:
            self._left.insert(item)

    ################################################################################################
    # Exercise 2
    ################################################################################################
    def remove(self, item: Any) -> None:
        """Remove *one* occurrence of <item> from this BST.

        Do nothing if <item> is not in the BST.
        """
        if self.is_empty():
            pass
        elif item == self._root:
            self._delete_root()
        elif item < self._root:
            self._left.remove(item)
        else:
            self._right.remove(item)

    ################################################################################################
    # Exercise 2
    ################################################################################################
    def _delete_root(self) -> None:
        """Remove the root of this BST.


        Preconditions:
            - not self.is_empty()
        >>> bst = BinarySearchTree(10)
        >>> bst.insert(12)
        >>> bst.insert(11)
        >>> bst.insert(13)
        >>> bst.insert(5)
        >>> bst.insert(3)
        >>> bst.insert(6)
        >>> bst.remove(10)
        >>> print(bst)
        True
        """

        if self._right.is_empty() and self._left.is_empty():
            self._root = None
            self._right = None
            self._left = None
        elif self._left.is_empty():
            self._root, self._left, self._right = self._right,\
                                                  self._right._left, self._right._right
        elif self._right.is_empty():
            self._root, self._left, self._right = self._left, \
                                                  self._left._left, self._left._right
        else:
            self._root = self._left.extract()

    def extract(self):
        """
        >>> bst = BinarySearchTree(10)
        >>> bst.insert(12)
        >>> bst.insert(11)
        >>> bst.insert(13)
        >>> bst.insert(5)
        >>> bst.insert(3)
        >>> bst.insert(6)
        >>> bst.extract()
        5

        """

        if self._right.is_empty():
            return self._root
        else:
            return self._right.extract()


def big_selections(lst: list[int], n: int) -> list[list[int]]:
    """ Return ait seiections of <tst> whose sum is >- n.
    The seiections may be returned in any order.
    Notes:
    1. The sum of an empty List is 0 (i.e., sum([]) == 0).
    2. <tst> can contain negative integers, and <n> can also be negative.
    >>> sorted(big_selections([1, 2, 3], 4))
    [[1, 2, 3], [1, 3], [2, 3]]
    """
    if len(lst) == 0:
        return [[]]
    else:
        selection = big_selections(lst[1:], n - lst[0])
        result = selection[:]
        for s in selection:
            result.append([lst[0]] + s)
        bigger = []
        for item in result:
            if sum(item) >= n:
                bigger.append(item)
        return bigger

