#!/usr/bin/python3
"""
This module contains the Square class.
"""

from .rectangle import Rectangle

class Square(Rectangle):
    """
    Square class that inherits from Rectangle.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a new Square instance.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return the string representation of the Square."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
    def update(self, *args, **kwargs):
        """Update the Square attributes."""
        attributes = ['id', 'size', 'x', 'y']

        if args and len(args) > 0:
            for i, arg in enumerate(args):
                if i < len(attributes):
                    if attributes[i] == 'size':
                        self.size = arg  # size is treated specially
                    else:
                        setattr(self, attributes[i], arg)
        else:
            for key, value in kwargs.items():
                if key in attributes:
                    if key == 'size':
                        self.size = value  # size is treated specially
                    else:
                        setattr(self, key, value)
    def to_dictionary(self):
        """Return the dictionary representation of a Square."""
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }

    @property
    def size(self):
        """Get the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the Square."""
        self.width = value
        self.height = value

    def __str__(self):
        """Return the string representation of the Square."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
