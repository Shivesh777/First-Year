"""CSC111 Winter 2022 Prep 4: Programming Exercises

Instructions (READ THIS FIRST!)
===============================

Your task in this prep is to implement each of the unimplemented Tree methods in this file.
Use the recursive Tree method code template---decide whether to include the "size-one" base case
by determining whether it would be redundant.

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


class Tree:
    """A recursive tree data structure.

    Note the relationship between this class and RecursiveList; the only major
    difference is that _rest has been replaced by _subtrees to handle multiple
    recursive sub-parts.

    Representation Invariants:
        - self._root is not None or self._subtrees == []
        - all(not subtree.is_empty() for subtree in self._subtrees)
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

    def __init__(self, root: Optional[Any], subtrees: list[Tree]) -> None:
        """Initialize a new Tree with the given root value and subtrees.

        If root is None, the tree is empty.

        Preconditions:
            - root is not none or subtrees == []
        """
        self._root = root
        self._subtrees = subtrees

    def is_empty(self) -> bool:
        """Return whether this tree is empty.

        >>> t1 = Tree(None, [])
        >>> t1.is_empty()
        True
        >>> t2 = Tree(3, [])
        >>> t2.is_empty()
        False
        """
        return self._root is None

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
            size = 1  # count the root
            for subtree in self._subtrees:
                size += subtree.__len__()  # could also write len(subtree)
            return size

    ############################################################################
    # Prep exercises start here
    ############################################################################
    def num_negatives(self) -> int:
        """Return the number of negative integers in this tree.

        Preconditions:
            - all items in this tree are integers

        Remember, 0 is *not* negative.

        >>> t1 = Tree(17, [])
        >>> t1.num_negatives()
        0
        """
        if self.is_empty():
            return 0
        elif self._subtrees == []:
            if self._root < 0:
                return 1
            else:
                return 0
        else:
            neg_so_far = 0
            if self._root < 0:
                neg_so_far += 1
            for subtree in self._subtrees:
                neg_so_far += subtree.num_negatives()
            return neg_so_far

    def maximum(self: Tree) -> int:
        """Return the maximum value stored in this tree.

        Return 0 if this tree is empty.

        Preconditions:
            - all values in this tree are positive integers.

        >>> t1 = Tree(17, [])
        >>> t1.maximum()
        17
        """
        if self.is_empty():
            return 0
        elif self._subtrees == []:
            return self._root
        else:
            max_so_far = 0
            if self._root > max_so_far:
                max_so_far = self._root
            for subtree in self._subtrees:
                max_so_far = max(max_so_far, subtree.maximum())
            return max_so_far

    def height(self: Tree) -> int:
        """Return the height of this tree.

        Please refer to the prep readings for the definition of tree height.

        >>> t1 = Tree(17, [])
        >>> t1.height()
        1
        >>> t1 = Tree(17, [])
        >>> t2 = Tree(11, [])
        >>> t3 = Tree(11, [t1, t2])
        >>> t4 = Tree(11, [])
        >>> t5 = Tree(11, [t4, t3])
        >>> t5.height()
        3
        """

        if self.is_empty():
            return 0
        elif self._subtrees == []:
            return 1
        else:
            max_height = []
            for subtree in self._subtrees:
                max_height = max_height + [subtree.height()]
            height_so_far = 1 + max(max_height)
            return height_so_far

    def __contains__(self, item: Any) -> bool:
        """Return whether this tree contains <item>.

        >>> t = Tree(1, [])
        >>> t.__contains__(-30)  # Could also write -30 in t
        False
        >>> t1 = Tree(17, [])
        >>> t2 = Tree(11, [])
        >>> t3 = Tree(11, [t1, t2])
        >>> t4 = Tree(11, [])
        >>> t5 = Tree(11, [t4, t3])
        >>> t5.__contains__(17)
        True
        >>> t1 = Tree(17, [])
        >>> t2 = Tree(11, [])
        >>> t3 = Tree(11, [t1, t2])
        >>> t4 = Tree(11, [])
        >>> t5 = Tree(11, [t4, t3])
        >>> t5.__contains__(9)
        False
        """
        if self.is_empty():
            return False
        elif self._subtrees == []:
            if self._root == item:
                return True
            else:
                return False
        else:
            boolean = False
            for subtree in self._subtrees:
                boolean = subtree.__contains__(item)
                if boolean is True:
                    return True
            return boolean


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
