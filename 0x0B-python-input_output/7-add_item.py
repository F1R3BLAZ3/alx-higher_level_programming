#!/usr/bin/python3

"""
    Adds all arguments to a Python list and saves them to a file.
"""


from sys import argv
from os.path import exists
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using a JSON representation.

    Args:
        my_obj: The object to be serialized and written to the file.
        filename (str): The name of the file to write to.

    Returns:
        None
    """
    with open(filename, mode='w') as file:
        json.dump(my_obj, file)


def load_from_json_file(filename):
    """
    Creates an object from a JSON file.

    Args:
        filename (str): The name of the JSON file to load from.

    Returns:
        object: The object created from the JSON file.
    """
    with open(filename, mode='r') as file:
        return json.load(file)


def add_arguments_to_list_and_save():
    """
    Adds all arguments to a Python list and saves them to a file.

    The list is saved as a JSON representation in a file named add_item.json.
    If the file doesn’t exist, it is created.

    Returns:
        None
    """
    filename = "add_item.json"

    if exists(filename):
        my_list = load_from_json_file(filename)
    else:
        my_list = []

    my_list.extend(argv[1:])

    save_to_json_file(my_list, filename)


if __name__ == "__main__":
    add_arguments_to_list_and_save()
