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
