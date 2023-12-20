#!/usr/bin/python3
"""Module 1-square

This module contains the definition of the class Square with a private instance attribute size.
"""

class Square:
    """Defines a square.

    Attributes:
        __size (int): The size of a side of the square.
    """

    def __init__(self, size):
        """Initializes the Square instance.

        Args:
            size (int): The size of a side of the square.
        """
        self.__size = size
