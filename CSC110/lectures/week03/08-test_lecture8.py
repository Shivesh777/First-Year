"""Lecture 8 examples for property-based testing"""
from lecture8 import is_even, divides
from hypothesis.strategies import integers
from hypothesis import given


# Unit test 1
def test_is_even_true() -> None:
    """Test is_even on an even number."""
    assert is_even(2)


# Unit test 2
def test_is_even_false() -> None:
    """Test is_even on an odd number."""
    assert not is_even(3)


# Property-based test
@given(x=integers())
def test_is_even_2x(x: int) -> None:
    """Test that is_even(2 * x) always returns True."""
    assert is_even(2 * x)


# Exercise 2
@given(n=integers())
def test_a(n: int) -> None:
    """Test the following property of the divides function:

    For all integers n, 2 divides (2 * n).
    (This is very similar to our `is_even` example.)
    """
    assert divides(2, 2 * n)


@given(n=integers(), d=integers())
def test_b(n: int, d: int) -> None:
    """Test the following property of the divides function:

    For all integers n and d, d divides (d * n).
    """
    assert divides(d, d * n)


# Note the use of integers(min_value=1) instead of just integers()
@given(n=integers(min_value=1), d=integers(min_value=1))
def test_c(n: int, d: int) -> None:
    """Test the following property of the divides function:

    For all POSITIVE integers n and d, if d divides n then d <= n.
    """
    assert (not divides(d, n)) or d <= n


if __name__ == '__main__':
    import pytest
    pytest.main(['test_lecture8.py', '-v'])
