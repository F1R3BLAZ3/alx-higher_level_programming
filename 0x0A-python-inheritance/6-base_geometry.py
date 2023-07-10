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
