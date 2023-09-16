#!/usr/bin/python3

"""
A base geometry class.
"""


class BaseGeometry:
    """
    A base geometry class.
    """

    def area(self):
        """
        Computes the area of the geometry.

        Raises:
            Exception: Indicates that the area() method is not implemented.

        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the value as an integer for a given name.

        Args:
            name (str): The name of the value being validated.
            value: The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.

        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
