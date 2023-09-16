#!/usr/bin/python3

"""
This module provides a function to add two integers,
these numbers can be integers or floats.
"""


def add_integer(a, b=98):
    """
    Adds two integers.
    Args:
        a (int or float): First integer or float value.
        b (int or float): Second integer or float value. Defaults to 98.
    Returns:
        int: The addition of a and b.
    Raises:
        TypeError: If a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or float")

    return int(a) + int(b)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
