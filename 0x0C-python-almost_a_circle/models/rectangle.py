#!/usr/bin/python3
"""
This module contains the Rectangle class.
"""

from .base import Base

class Rectangle(Base):
    """
    Rectangle class that inherits from Base.
    """
    def area(self):
        """Return the area of the Rectangle."""
        return self.width * self.height
    def display(self):
        """Print the Rectangle instance with the character # taking care of x and y."""
        # Print the 'y' number of newline characters to move down
        print("\n" * self.y, end="")
        """Print the Rectangle instance with the character #."""
        for _ in range(self.height):
            print("#" * self.width)
    def __str__(self):
        """Return the string representation of the Rectangle."""
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"
    def update(self, *args):
        """Update the Rectangle attributes."""
        if len(args) > 0:
            attribute_names = ['id', 'width', 'height', 'x', 'y']
            for i, arg in enumerate(args):
                if i < len(attribute_names):
                    setattr(self, attribute_names[i], arg)

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a new Rectangle instance.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Get or set the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get or set the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get or set the x coordinate of the Rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get or set the y coordinate of the Rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
