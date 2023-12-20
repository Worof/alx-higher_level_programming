#!/usr/bin/python3
"""Module 3-square

This module contains the definition of the class Square with a private instance attribute size and a public method to calculate the square's area.
"""

class Square:
    """Defines a square.

    This class represents a square with a private instance attribute for its size and a method to calculate its area.

    Attributes:
        __size (int): The size of a side of the square.
    """

    def __init__(self, size=0):
        """Initializes the Square instance with a size.

        Args:
            size (int, optional): The size of a side of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
