#!/usr/bin/python3
"""
Module 9-rectangle
Defines a class Rectangle with private instance attributes width and height,
property setters and getters for them, methods to calculate the area and perimeter,
methods for string representations, a custom destructor, a class attribute to keep
track of the number of instances, a class attribute for the print symbol, a
static method to compare rectangles based on their area, and a class method to create
a square (a rectangle with equal width and height).
"""


class Rectangle:
    """
    A class to represent a rectangle.

    Attributes:
    width (int): The width of the rectangle.
    height (int): The height of the rectangle.
    number_of_instances (int): The number of Rectangle instances.
    print_symbol (any type): Symbol used for string representation.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle instance.

        Args:
        width (int): The width of the rectangle, defaults to 0.
        height (int): The height of the rectangle, defaults to 0.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        Represented by the character(s) stored in print_symbol for each unit of width and height.
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        rectangle_str = []
        for _ in range(self.__height):
            rectangle_str.append(str(self.print_symbol) * self.__width)
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
        Prints a message when an instance is deleted and decrements the
        number_of_instances class attribute.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Returns the bigger rectangle based on the area.

        Args:
        rect_1 (Rectangle): The first rectangle to compare.
        rect_2 (Rectangle): The second rectangle to compare.

        Raises:
        TypeError: If either rect_1 or rect_2 is not an instance of Rectangle.

        Returns:
        Rectangle: The bigger rectangle, or rect_1 if both are equal.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """
        Returns a new Rectangle instance with width == height == size.

        Args:
        size (int): The size of the square sides.

        Returns:
        Rectangle: A new Rectangle instance with given size.
        """
        return cls(size, size)
