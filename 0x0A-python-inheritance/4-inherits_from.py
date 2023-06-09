#!/usr/bin/python3

"""
Checks an object.
"""


def inherits_from(obj, a_class):
    """
    Checks if the object is an instance of a class that inherited (directly or
    indirectly) from the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if the object is an instance of a class that inherited (directly
        or indirectly) from the specified class. False otherwise.

    """
    return isinstance(obj, a_class) and type(obj) is not a_class
