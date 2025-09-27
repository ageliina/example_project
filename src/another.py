#!/usr/bin/env python3
# encoding: utf-8
# Author: Akke Viitanen
# Email: akke.viitanen@helsinki.fi
# Date: 2025-09-27 13:20:40

"""Another python example module."""


class AnotherExampleClass:
    """
    Another python example class.

    This class is another python example class with just the name argument.

    Attributes
    ----------
    name: str
        Name of the example class.

    Examples
    --------
    >>> my_example_class = AnotherExampleClass("foo")
    >>> my_example_class.show()
    foo

    """

    def __init__(self, name: str):
        """Initialize ExampleClass."""
        self.name = name

    def show(self) -> None:
        """Print name and age."""
        print(self.name)
