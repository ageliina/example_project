#!/usr/bin/env python3
# encoding: utf-8
# Author: Akke Viitanen
# Email: akke.viitanen@helsinki.fi
# Date: 2025-09-27 13:20:40

"""Utilities functions."""


def sum_two(a: int, b: int) -> int:
    """
    Sum two items.

    Sums two items together and returns the sum of the two.

    Parameters
    ----------
    a: int
        First argument to sum.
    b: int
        Second argument to sum.

    Returns
    -------
    c: int
        Sum of the two arguments.

    Raises
    ------
    TypeError
        If the sum of the two is undefined.

    Examples
    --------
    >>> sum_two(1, 3)
    4

    >>> sum_two("foo", "bar")
    'foobar'

    >>> sum_two("foo", 1)
    Traceback (most recent call last):
        ...
    TypeError: can only concatenate str (not "int") to str

    >>> sum_two(1, 2, 3)
    Traceback (most recent call last):
        ...
    TypeError: sum_two() takes 2 positional arguments but 3 were given

    """
    return a + b


def sum_two_with_branches(a: int, b: int) -> int:
    """
    Sum two numbers with branches.

    Test branching by adding some if clauses to the function.

    Examples
    --------
    >>> sum_two_with_branches(2, 1)
    3
    >>> sum_two_with_branches(3, 5)
    -2
    >>> sum_two_with_branches(5, 5)
    1
    >>> sum_two_with_branches(0, None)
    Traceback (most recent call last):
        ...
    TypeError: '>' not supported between instances of 'int' and 'NoneType'

    """
    ret = None
    if a > b:
        ret = a + b
    elif a < b:
        ret = a - b
    else:
        ret = a // b
    return ret
