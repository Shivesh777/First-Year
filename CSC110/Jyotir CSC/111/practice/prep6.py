"""CSC111 Winter 2022 Prep 6: Programming Exercises

Instructions (READ THIS FIRST!)
===============================

This module contains the code for a set of classes used to represent expressions
that you would see in a Python program.

It includes the three classes Expr, Num, and BinOp covered in the prep readings.
Note that in addition to the initializer and evaluate methods, we've also
included a __str__ implementation for each class that shows the corresponding
Python expression that the tree represents.

Your task is to complete the implementations of three new classes:

1.  Bool: a constant boolean (similar to Num).
2.  BoolOp: a sequence of `and` or `or` expressions (similar to BinOp).
3.  Compare: a sequence of `<` and `<=` expressions (for simplicity, we'll
    ignore other forms of expressions like `>` and `==`).

Note that BoolOp and Compare are a bit more challenging than BinOp, because
both of them can have an *arbitrary number* of subtrees, rather than being
limited to exactly two subtrees. However, you can use the same recursive
"evaluate each subexpression recursively" idea as BinOp.

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
from typing import Any, Union


class Expr:
    """An abstract class representing a Python expression.
    """

    def evaluate(self) -> Any:
        """Return the *value* of this expression.

        The returned value should the result of how this expression would be
        evaluated by the Python interpreter.
        """
        raise NotImplementedError


class Num(Expr):
    """A numeric literal.

    Instance Attributes:
        - n: the value of the literal
    """
    n: Union[int, float]

    def __init__(self, number: Union[int, float]) -> None:
        """Initialize a new numeric literal."""
        self.n = number

    def evaluate(self) -> Any:
        """Return the *value* of this expression.

        The returned value should the result of how this expression would be
        evaluated by the Python interpreter.

        >>> expr = Num(10.5)
        >>> expr.evaluate()
        10.5
        """
        return self.n  # Simply return the value itself!

    def __str__(self) -> str:
        """Return a string representation of this expression.

        One feature we'll stick with for all Expr subclasses here is that we'll
        want to return a string that is valid Python code representing the same
        expression.

        >>> str(Num(5))
        '5'
        """
        return str(self.n)


class BinOp(Expr):
    """An arithmetic binary operation.

    Instance Attributes:
        - left: the left operand
        - op: the name of the operator
        - right: the right operand

    Representation Invariants:
        - self.op in {'+', '*'}
    """
    left: Expr
    op: str
    right: Expr

    def __init__(self, left: Expr, op: str, right: Expr) -> None:
        """Initialize a new binary operation expression.

        Preconditions:
            - op in {'+', '*'}
        """
        self.left = left
        self.op = op
        self.right = right

    def evaluate(self) -> Any:
        """Return the *value* of this expression.

        The returned value should the result of how this expression would be
        evaluated by the Python interpreter.

        >>> expr = BinOp(Num(10.5), '+', Num(30))
        >>> expr.evaluate()
        40.5
        """
        left_val = self.left.evaluate()
        right_val = self.right.evaluate()

        if self.op == '+':
            return left_val + right_val
        elif self.op == '*':
            return left_val * right_val
        else:
            # We shouldn't reach this branch because of our representation invariant
            raise ValueError(f'Invalid operator {self.op}')

    def __str__(self) -> str:
        """Return a string representation of this expression.
        """
        return f'({str(self.left)} {self.op} {str(self.right)})'


################################################################################
# Prep exercises
################################################################################
class Bool(Expr):
    """A boolean literal.

    Instance Attributes:
        - b: the value of the literal
    """
    b: bool

    def __init__(self, b: bool) -> None:
        """Initialize a new boolean literal."""
        self.b = b

    def evaluate(self) -> Any:
        """Return the *value* of this expression.

        The returned value should the result of how this expression would be
        evaluated by the Python interpreter.

        >>> expr = Bool(True)
        >>> expr.evaluate()
        True
        """
        return self.b

    def __str__(self) -> str:
        """Return a string representation of this expression.
        """
        return str(self.b)


class BoolOp(Expr):
    """A boolean operation.

    Represents either a sequence of `and`s or a sequence of `or`s.
    Unlike BinOp, this expression can contains more than two operands,
    each separated by SAME operator:

        True and False and True and False
        True or False or True or False

    Instance Attributes:
        - op: the name of the boolean operation
        - operands: a list of operands that the operation is applied to

    Representation Invariants:
        - self.op in {'and', 'or'}
        - len(self.operands) >= 2
        - every expression in self.operands evaluates to a boolean value
    """
    op: str
    operands: list[Expr]

    def __init__(self, op: str, operands: list[Expr]) -> None:
        """Initialize a new boolean operation expression.

        Preconditions:
            - op in {'and', 'or'}
            - len(operands) >= 2
            - every expression in operands evaluates to a boolean value
        """
        self.op = op
        self.operands = operands

    def evaluate(self) -> Any:
        """Return the *value* of this expression.

        The returned value should the result of how this expression would be
        evaluated by the Python interpreter.

        >>> expr = BoolOp('and', [Bool(True), Bool(True), Bool(False)])
        >>> expr.evaluate()
        False
        """
        if self.op == 'and':
            return all(x.evaluate() for x in self.operands)
        else:
            return any(x.evaluate() for x in self.operands)

    def __str__(self) -> str:
        """Return a string representation of this boolean expression.

        >>> expr = BoolOp('and', [Bool(True), Bool(True), Bool(False)])
        >>> str(expr)
        '(True and True and False)'
        """
        op_string = f' {self.op} '
        return f'({op_string.join([str(v) for v in self.operands])})'


class Compare(Expr):
    """A sequence of comparison operations.

    In Python, it is possible to chain together comparison operations:
        x1 <= x2 < x3 <= x4

    This is logically equivalent to the more explicit binary form:
        (x1 <= x2) and (x2 <= x3) and (x3 <= x4),
    except each expression (x1, x2, x3, x4) is only evaluated once.

    Instance Attributes:
        - left: The leftmost value being compared. (In the example above, this is `x1`.)
        - comparisons: A list of tuples, where each tuple stores an operation and
            expression. (In the example above, this is [(<=, x2), (<, x3), (<= x4)].)

    Note: for the purpose of this prep, we'll only allow the comparison operators <= and <
    for this class (see representation invariant below).

    Representation Invariants:
        - len(self.comparisons) >= 1
        - all(comp[0] in {'<=', '<'} for comp in self.comparisons)
        - self.left and every expression in self.comparisons evaluate to a number value
    """
    left: Expr
    comparisons: list[tuple[str, Expr]]

    def __init__(self, left: Expr,
                 comparisons: list[tuple[str, Expr]]) -> None:
        """Initialize a new comparison expression.

        Preconditions:
            - len(comparisons) >= 1
            - all(comp[0] in {'<=', '<'} for comp in comparisons)
            - left and every expression in comparisons evaluate to a number value
        """
        self.left = left
        self.comparisons = comparisons

    def evaluate(self) -> Any:
        """Return the *value* of this expression.

        The returned value should the result of how this expression would be
        evaluated by the Python interpreter.

        >>> expr = Compare(Num(1), [
        ...            ('<=', Num(2)),
        ...            ('<', Num(4.5)),
        ...            ('<=', Num(4.5))])
        >>> expr.evaluate()
        True
        """
        val = True
        number = self.left
        for x in self.comparisons:
            if x[0] == "<=":
                val = number.evaluate() <= x[1].evaluate()
                number = x[1]
            else:
                val = number.evaluate() < x[1].evaluate()
                number = x[1]
            if val is False:
                return False
        return val

    def __str__(self) -> str:
        """Return a string representation of this comparison expression.

        >>> expr = Compare(Num(1), [
        ...            ('<=', Num(2)),
        ...            ('<', Num(4.5)),
        ...            ('<=', Num(4.5))])
        >>> str(expr)
        '(1 <= 2 < 4.5 <= 4.5)'
        """
        s = str(self.left)
        for operator, subexpr in self.comparisons:
            s += f' {operator} {str(subexpr)}'
        return '(' + s + ')'


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
