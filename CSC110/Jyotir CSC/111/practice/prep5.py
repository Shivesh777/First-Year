"""CSC111 Winter 2022 Prep 5: Programming Exercises

Instructions (READ THIS FIRST!)
===============================

This file contains the BinarySearchTree class you read about in this week's prep,
as well a few different methods for you to implement. Each of these methods should
be implemented recursively, and you should use the BST property to ensure that you
are only making the recursive calls that are required to implement each function---
do not make any unnecessary calls! (The prep readings illustrate this idea in the
discussion of how __contains__ is implemented.)

Finally, one TIP: don't forget about self._root in the recursive step! This was
the most common mistake students made with Prep 4 last week. Even when you are
recursing on self._left and/or self._right, you'll often need to do something with
self._root as well, at least in some cases.

NOTE: the doctests access and assign to private attributes directly, which is
not good practice (although python_ta doesn't complain about it in doctests).
We'll fix this in this week when we implement a `BinarySearchTree.insert` method.

We have marked each place you need to write code with the word "TODO".
As you complete your work in this file, delete each TODO comment.

You may add additional doctests, but they will not be graded. You should test your work
carefully before submitting it!

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC111 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC111 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2022 Mario Badr, David Liu, and Diane Horton.
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

    ############################################################################
    # Prep exercises
    ############################################################################
    def maximum(self) -> Optional[int]:
        """Return the maximum number in this BST, or None if this BST is empty.

        Hint: Review the BST property to ensure you aren't making unnecessary
        recursive calls.

        Preconditions:
            - all items in this BST are integers

        >>> BinarySearchTree(None).maximum() is None   # Empty BST
        True
        >>> BinarySearchTree(10).maximum()
        10
        >>> bst = BinarySearchTree(7)
        >>> left = BinarySearchTree(3)
        >>> left._left = BinarySearchTree(3)
        >>> left._right = BinarySearchTree(5)
        >>> right = BinarySearchTree(11)
        >>> right._left = BinarySearchTree(9)
        >>> right._right = BinarySearchTree(13)
        >>> bst._left = left
        >>> bst._right = right
        >>> bst.maximum()
        13
        """
        if self.is_empty():
            return None
        elif self._right.is_empty():
            return self._root
        else:
            return self._right.maximum()

    def count(self, item: Any) -> int:
        """Return the number of occurrences of <item> in this BST.

        Hint: carefully review the BST property!

        >>> BinarySearchTree(None).count(148)  # An empty BST
        0
        >>> bst = BinarySearchTree(7)
        >>> left = BinarySearchTree(3)
        >>> left._left = BinarySearchTree(3)
        >>> left._right = BinarySearchTree(5)
        >>> right = BinarySearchTree(11)
        >>> right._left = BinarySearchTree(9)
        >>> right._right = BinarySearchTree(13)
        >>> bst._left = left
        >>> bst._right = right
        >>> bst.count(7)
        1
        >>> bst.count(3)
        2
        >>> bst.count(100)
        0
        """
        if self.is_empty():
            return 0
        elif self._root == item and self._root != self._left._root and \
                self._root != self._right._root:
            return 1
        else:
            count = 0
            if self._root == item:
                count += 1
            if item >= self._root:
                count += self._right.count(item)
            if item <= self._root:
                count += self._left.count(item)
            return count

    def items(self) -> list:
        """Return all of the items in the BST in sorted order.

        Do not remove duplicates.

        You should *not* need to sort the list yourself: instead, use the BST
        property and combine self._left.items(), self._root, and self._right.items()
        in the correct order!

        >>> BinarySearchTree(None).items()  # An empty BST
        []
        >>> bst = BinarySearchTree(7)
        >>> left = BinarySearchTree(3)
        >>> left._left = BinarySearchTree(2)
        >>> left._right = BinarySearchTree(5)
        >>> right = BinarySearchTree(11)
        >>> right._left = BinarySearchTree(9)
        >>> right._right = BinarySearchTree(13)
        >>> bst._left = left
        >>> bst._right = right
        >>> bst.items()
        [2, 3, 5, 7, 9, 11, 13]
        """
        if self.is_empty():
            return []
        else:
            items_so_far = []
            items_so_far.extend(self._left.items())
            items_so_far.append(self._root)
            items_so_far.extend(self._right.items())
            return items_so_far

    def smaller(self, item: Any) -> list:
        """Return all of the items in this BST less than <item> in sorted order.

        Preconditions:
            - all items in this BST can be compared with <item> using <.

        As with BinarySearchTree.items, you should *not* need to sort the list
        yourself!

        >>> bst = BinarySearchTree(7)
        >>> left = BinarySearchTree(3)
        >>> left._left = BinarySearchTree(2)
        >>> left._right = BinarySearchTree(5)
        >>> right = BinarySearchTree(11)
        >>> right._left = BinarySearchTree(9)
        >>> right._right = BinarySearchTree(13)
        >>> bst._left = left
        >>> bst._right = right
        >>> bst.smaller(6)
        [2, 3, 5]
        >>> bst.smaller(13)
        [2, 3, 5, 7, 9, 11]
        """
        if self.is_empty():
            return []
        elif self._root < item:
            small_so_far = []
            small_so_far.extend(self._left.smaller(item))
            small_so_far.append(self._root)
            small_so_far.extend(self._right.smaller(item))
            return small_so_far
        else:
            return self._left.smaller(item)


if __name__ == '__main__':
    import python_ta.contracts
    python_ta.contracts.check_all_contracts()

    import doctest
    doctest.testmod()

    import python_ta
    python_ta.check_all(config={
        'max-line-length': 100,
        'disable': ['E1136']
    })
