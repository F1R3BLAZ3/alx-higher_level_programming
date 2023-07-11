#!/usr/bin/python3

"""
    Adds all arguments to a Python list and saves them to a file as
    a JSON representation.
"""


import sys
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


def add_args_to_list():
    """
    Adds all arguments to a Python list and saves them to a file as
    a JSON representation.
    """
    # Load existing list from file or create a new list
    try:
        existing_list = load_from_json_file("add_item.json")
    except FileNotFoundError:
        existing_list = []

    # Add arguments to the list
    new_items = sys.argv[1:]
    updated_list = existing_list + new_items

    # Save the updated list to file
    save_to_json_file(updated_list, "add_item.json")


if __name__ == "__main__":
    add_args_to_list()
