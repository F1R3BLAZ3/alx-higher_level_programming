class Rectangle:
    """
    This class represents a rectangle.
    """
    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle instance with an optional height and width.

        Args:
            height (int, optional): The height of the rectangle. Defaults to 0.
            width (int, optional): The width of the rectangle. Defaults to 0.

        Raises:
            TypeError: If the width or height is not an integer.
            ValueError: If the width or height is less than 0.
        """
        self.__width = 0
        self.__height = 0
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Get the width of the rectangle.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle.

        Args:
            value (int): The width of the rectangle.

        Raises:
            TypeError: If the width is not an integer.
            ValueError: If the width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        Get the height of the rectangle.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle.

        Args:
            value (int): The height of the rectangle.

        Raises:
            TypeError: If the height is not an integer.
            ValueError: If the height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        Compute the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Compute the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle.
        """
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Returns a string representation of the rectangle using the '#' character.

        Returns:
            str: A string representation of the rectangle with '#' characters for the width and height.
                 If either width or height is 0, it returns an empty string.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            rectangle_str = ""
            for _ in range(self.__height):
                rectangle_str += "#" * self.__width + "\n"
            return rectangle_str

    def __repr__(self):
        """
        Returns a string representation of the rectangle object.

        Returns:
            str: A string representation of the rectangle object.
        """
        return f"<{self.__class__.__name__}({self.__width}, {self.__height})>"
