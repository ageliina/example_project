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

    Returns the product of the two values. The product is defined as a
    piecewise function depending on the relative magnitude of 'a' and 'b'. It
    is defined as the sum a + b (if a > b), the difference 'a - b' (if a < b),
    and the ratio 'a // b' otherwise.

    Parameters
    ----------
    a: int
        First argument to sum.
    b: int
        Second argument to sum.

    Returns
    -------
    c: int
        Product of the two values (see above).

    Examples
    --------
    >>> # Return the sum of the two arguments
    >>> sum_two_with_branches(2, 1)
    3
    >>> # Return the difference of the two arguments
    >>> sum_two_with_branches(3, 5)
    -2
    >>> # Return the ratio of the two arguments
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
