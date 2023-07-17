#!/usr/bin/python3
"""Base class for objects.
"""
import json


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
        """Converts a list of dictionaries to a JSON string.

        Args:
            list_dictionaries: A list of dictionaries.

        Returns:
            A JSON string representing the list of dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Converts a JSON string to a list of dictionaries.

        Args:
            json_string: A JSON string.

        Returns:
            A list of dictionaries representing the JSON data.
        """
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Saves a list of instances to a JSON file.

        The instances are converted to dictionaries using their
        to_dictionary() method before being serialized to JSON.

        Args:
            list_objs: A list of instances.
        """
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        json_string = cls.to_json_string(
            [obj.to_dictionary() for obj in list_objs])
        with open(filename, 'w') as file:
            file.write(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Creates a new instance based on a dictionary of attributes.

        Args:
        **dictionary: Keyword arguments representing the attributes
        of the instance.

        Returns:
        A new instance with the specified attributes.
        """
        class_name = cls.__name__
        supported_classes = {"Rectangle": cls(1, 1), "Square": cls(1)}
        dummy_instance = supported_classes.get(class_name)
        if dummy_instance is None:
            raise ValueError("Unsupported class name")

        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """Loads instances from a JSON file.

        The JSON data is converted to a list of dictionaries, and each
        dictionary is used to create a new instance using the create()
        method.

        Returns:
            A list of instances loaded from the JSON file.
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as file:
                json_data = file.read()
                dict_list = cls.from_json_string(json_data)
                instances = [cls.create(**dictionary)
                             for dictionary in dict_list]
                return instances
        except FileNotFoundError:
            return []
