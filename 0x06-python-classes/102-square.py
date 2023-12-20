#!/usr/bin/python3
"""Module 102-square

This module contains the definition of the class Square with a private instance attribute size, along with its getter and setter, a method to calculate the square's area, and comparison operators based on the square's area.
"""

class Square:
    """Defines a square.

    This class represents a square with a private instance attribute for its size, along with a getter and setter for this attribute, a method to calculate its area, and comparison operators based on the square's area.

    Attributes:
        __size (float, int): The size of a side of the square.
    """

    def __init__(self, size=0):
        """Initializes the Square instance with a size.

        Args:
            size (float, int): The size of a side of the square.
        """
        self.size = size

    @property
    def size(self):
        """Retrieves the size of the square.

        Returns:
            float, int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square.

        Args:
            value (float, int): The size to set the square to.

        Raises:
            TypeError: If value is not a number (float or integer).
            ValueError: If value is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates the area of the square.

        Returns:
            float, int: The area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """Equal to.

        Args:
            other (Square): Another square to compare with.

        Returns:
            bool: True if squares have the same area, False otherwise.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """Not equal to.

        Args:
            other (Square): Another square to compare with.

        Returns:
            bool: True if squares have different areas, False otherwise.
        """
        return self.area() != other.area()

    def __lt__(self, other):
        """Less than.

        Args:
            other (Square): Another square to compare with.

        Returns:
            bool: True if this square is smaller than the other, False otherwise.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """Less than or equal to.

        Args:
            other (Square): Another square to compare with.

        Returns:
            bool: True if this square is smaller than or equal to the other, False otherwise.
        """
        return self.area() <= other.area()

    def __gt__(self, other):
        """Greater than.

        Args:
            other (Square): Another square to compare with.

        Returns:
            bool: True if this square is larger than the other, False otherwise.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """Greater than or equal to.

        Args:
            other (Square): Another square to compare with.

        Returns:
            bool: True if this square is larger than or equal to the other, False otherwise.
        """
        return self.area() >= other.area()
