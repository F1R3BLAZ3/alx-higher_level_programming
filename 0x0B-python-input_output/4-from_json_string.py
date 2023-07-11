#!/usr/bin/python3

"""
    Returns a Python data structure represented by a JSON string.
"""


import json


def from_json_string(my_str):
    """
    Returns a Python data structure represented by a JSON string.

    Args:
        my_str (str): The JSON string to convert to a Python object.

    Returns:
        object: The Python data structure represented by the JSON string.
    """
    return json.loads(my_str)


if __name__ == "__main__":
    my_list_str = '[1, 2, 3]'
    my_list = from_json_string(my_list_str)
    print(my_list)
    print(type(my_list))

    my_dict_str = '{"id": 12, "name": "John",
                    "places": ["San Francisco", "Tokyo"],
                    "is_active": true, "info": {"average": 3.14, "age": 36}}'
    my_dict = from_json_string(my_dict_str)
    print(my_dict)
    print(type(my_dict))
