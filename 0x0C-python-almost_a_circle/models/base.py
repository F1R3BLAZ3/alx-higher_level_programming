#!/usr/bin/python3
import json
"""Base class for objects.
"""


class Base:
    """Base class for objects.

    This class serves as the base for other classes and provides an ID
    attribute for each instance.

    Attributes:
        id: An integer representing the unique identifier of the instance.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes the Base instance.

        Args:
            id: An optional integer representing the ID of the instance.
                If not provided, a new ID is assigned based on the number
                of existing instances.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        json_string = cls.to_json_string(
            [obj.to_dictionary() for obj in list_objs])
        with open(filename, 'w') as file:
            file.write(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)
        else:
            raise ValueError("Unsupported class name")

        dummy_instance.update(**dictionary)
        return dummy_instance
