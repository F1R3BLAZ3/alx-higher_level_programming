#!/usr/bin/python3

"""
    Creates an object from a JSON file.
"""


import json


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


if __name__ == "__main__":
    obj = load_from_json_file("input.json")
    print(obj)
