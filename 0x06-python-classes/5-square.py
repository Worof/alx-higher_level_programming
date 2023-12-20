#!/usr/bin/python3
"""Module 5-square

This module contains the definition of the class Square with a private instance attribute size, along with its getter and setter, a method to calculate the square's area, and a method to print the square.
"""

class Square:
    """Defines a square.

    This class represents a square with a private instance attribute for its size, along with a getter and setter for this attribute, a method to calculate its area, and a method to print the square.

    Attributes:
        __size (int): The size of a side of the square.
    """

    def __init__(self, size=0):
        """Initializes the Square instance with a size.

        Args:
            size (int, optional): The size of a side of the square. Defaults to 0.
        """
        self.size = size

    @property
    def size(self):
        """Retrieves the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square.

        Args:
            value (int): The size to set the square to.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """Prints the square with the character #.

        If size is equal to 0, prints an empty line.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
