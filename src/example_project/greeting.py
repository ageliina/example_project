#!/usr/bin/env python3
# encoding: utf-8
# Author: Akke Viitanen
# Email: akke.viitanen@helsinki.fi
# Date: 2025-09-28 17:31:34

"""A simple greeting module."""

import re


def greeting(time: str) -> str:
    """
    Greet the user based on the time.

    Parameters
    ----------
    time: str
        Time in format "hh:mm" where 'hh' is the hours and 'mm' is the minutes.

    Returns
    -------
    str
        A relevant greeting.

    Raises
    ------
    ValueError
        If time does not conform to the "hh:mm" format.
    ValueError
        If not hours in [0, 24] or not minutes in [0, 60].

    Examples
    --------
    >>> greeting('00:00')
    'Good night!'
    >>> greeting('06:15')
    'Good morning!'
    >>> greeting('12:34')
    'Good day!'
    >>> greeting('23:20')
    'Good evening!'
    >>> greeting('foobarbaz')
    Traceback (most recent call last):
        ...
    ValueError: Malformed input argument.
    >>> greeting('99:99')
    Traceback (most recent call last):
        ...
    ValueError: Hours must be 0-24 and minutes must be 0-60.

    """
    # Validate string input
    if not re.findall("[0-9][0-9]:[0-9][0-9]", time):
        raise ValueError("Malformed input argument.")

    # Validate hours and minutes
    hours, minutes = map(int, time.split(":"))
    if not (hours in range(24) and minutes in range(60)):
        raise ValueError("Hours must be 0-24 and minutes must be 0-60.")

    # Return the appropriate greeting
    time_of_day = ["night", "morning", "day", "evening"][hours // 6]
    return f"Good {time_of_day}!"
