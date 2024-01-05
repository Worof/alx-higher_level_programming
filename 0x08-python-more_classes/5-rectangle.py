#!/usr/bin/python3
"""
Module 5-rectangle
Defines a class Rectangle with private instance attributes width and height,
property setters and getters for them, methods to calculate the area and perimeter,
methods for string representations, and a custom destructor.
"""


class Rectangle:
    """
    A class to represent a rectangle.

    Attributes:
    width (int): The width of the rectangle.
    height (int): The height of the rectangle.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle instance.

        Args:
        width (int): The width of the rectangle, defaults to 0.
        height (int): The height of the rectangle, defaults to 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Gets the width of the Rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the Rectangle.

        Args:
        value (int): The value to set the width to.

        Raises:
        TypeError: If the width is not an integer.
        ValueError: If the width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Gets the height of the Rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the Rectangle.

        Args:
        value (int): The value to set the height to.

        Raises:
        TypeError: If the height is not an integer.
        ValueError: If the height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Returns the area of the Rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Returns the perimeter of the Rectangle.
        If width or height is 0, perimeter is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Returns a string representation of the Rectangle.
        Represented by the character '#' for each unit of width and height.
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        rectangle_str = []
        for _ in range(self.__height):
            rectangle_str.append("#" * self.__width)
        return "\n".join(rectangle_str)

    def __repr__(self):
        """
        Returns a string representation of the Rectangle for repr().
        This string can be used with eval() to create a new instance.
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        Destructor method for a Rectangle instance.
        Prints a message when an instance is deleted.
        """
        print("Bye rectangle...")
