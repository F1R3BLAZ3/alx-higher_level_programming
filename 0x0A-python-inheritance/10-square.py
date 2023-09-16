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


class Rectangle(BaseGeometry):
    """
    A rectangle class inheriting from BaseGeometry.
    """

    def __init__(self, width, height):
        """
        Initializes a Rectangle instance with the given width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than or equal to 0.

        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculates and returns the area of the rectangle.

        Returns:
            int: The area of the rectangle.

        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns the string representation of the rectangle.

        Returns:
            str: The string representation of the rectangle.

        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


class Square(Rectangle):
    """
    A square class inheriting from Rectangle.
    """

    def __init__(self, size):
        """
        Initializes a Square instance with the given size.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than or equal to 0.

        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """
        Returns the string representation of the square.

        Returns:
            str: The string representation of the square.

        """
        return "[Square] {}/{}".format(self.__size, self.__size)
