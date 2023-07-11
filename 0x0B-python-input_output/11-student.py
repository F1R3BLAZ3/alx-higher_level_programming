#!/usr/bin/python3

"""
Represents a student.
"""


class Student:
    """
    Represents a student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new instance of the Student class.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Args:
            attrs (list): List of attribute names to retrieve (default is None)

        Returns:
            dict: A dictionary representation of the Student instance.
        """
        if attrs is None or not isinstance(attrs, list):
            return self.__dict__
        else:
            return {attr: getattr(self, attr)
                    for attr in attrs if hasattr(self, attr)}

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance with values from
        a dictionary.

        Args:
            json (dict): The dictionary containing attribute-value pairs.

        Returns:
            None
        """
        for attr, value in json.items():
            setattr(self, attr, value)
