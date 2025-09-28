#!/usr/bin/env python3
# encoding: utf-8
# Author: Akke Viitanen
# Email: akke.viitanen@helsinki.fi
# Date: 2025-09-27 13:20:40

"""
Some python examples.

This line added just to launch a pre-commit hook.
"""

import numpy as np


class ExampleClass:
    """
    An example class with name and age.

    The example class has a name and an age. It knows how to print each
    property. Nothing more, nothing less.

    Attributes
    ----------
    name: str
        Name of the example class.
    age: int
        Age of the example class.
    seed: int
        Random number drawn at the time of creation.

    Examples
    --------
    >>> my_example_class = ExampleClass("foo", 42)
    >>> my_example_class.show()
    foo 42

    """

    def __init__(self, name: str, age: int):
        """Initialize ExampleClass."""
        self.name = name
        self.age = age
        self.seed = np.random.rand()

    def show(self) -> None:
        """Print name and age."""
        print(self.name, self.age)


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

    """
    return a + b
