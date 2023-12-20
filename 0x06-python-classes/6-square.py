#!/usr/bin/python3
"""Module 6-square

This module contains the definition of the class Square with private instance attributes size and position, along with their getters and setters, a method to calculate the square's area, and a method to print the square.
"""

class Square:
    """Defines a square.

    This class represents a square with private instance attributes for its size and position, along with getters and setters for these attributes, a method to calculate its area, and a method to print the square.

    Attributes:
        __size (int): The size of a side of the square.
        __position (tuple): The position of the square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initializes the Square instance with a size and position.

        Args:
            size (int, optional): The size of a side of the square. Defaults to 0.
            position (tuple, optional): The position of the square. Defaults to (0, 0).
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Retrieves the position of the square.

        Returns:
            tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position of the square.

        Args:
            value (tuple): The position to set the square to.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
           not all(isinstance(num, int) and num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """Prints the square with the character # using the position attribute.

        If size is equal to 0, prints an empty line.
        """
        if self.__size == 0:
            print()
            return

        [print() for _ in range(self.__position[1])]
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
