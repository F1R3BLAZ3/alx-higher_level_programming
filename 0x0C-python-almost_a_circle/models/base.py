#!/usr/bin/python3

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
