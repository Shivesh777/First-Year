"""Test suite for testing function all_even."""


import even_lists


def test_len_3_all_even() -> None:
    """Test all_even on a length 3 list of even ints.
    """
    argument = [0, 2, 4]
    expected = True
    assert even_lists.all_even(argument) == expected


def test_len_3_middle_odd() -> None:
    """Test all_even on a length 3 list where middle number is odd.
    """
    argument = [0, 1, 2]
    expected = False
    assert even_lists.all_even(argument) == expected


def test_len_1_even() -> None:
    """Test all_even on a length 1 list that contains an even number.
    """
    argument = [2]
    expected = True
    assert even_lists.all_even(argument) == expected


if __name__ == '__main__':
    import pytest
    pytest.main(['test_all_even.py'])
