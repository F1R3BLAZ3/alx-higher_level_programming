#!/usr/bin/python3

"""
    Returns the dictionary description with a simple data structure
    for JSON serialization of an object.
"""


def class_to_json(obj):
    """
    Returns the dictionary description with a simple data structure
    for JSON serialization of an object.

    Args:
        obj: An instance of a class.

    Returns:
        dict: The dictionary description of the object with a simple
                data structure.
    """
    return obj.__dict__
