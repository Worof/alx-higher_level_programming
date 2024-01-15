#!/usr/bin/python3
"""
This module contains the Base class.
The Base class serves as the foundation for all other classes in this project.
It provides common attributes or methods that can be used across various derived classes.
"""

class Base:
    """
    The Base class from which all other classes in this project will inherit.
    """

    def __init__(self, id=None):
        """
        Initialize a new Base instance.

        Args:
            id (int): The identity of the instance, unique to each instance. If None, an id is generated automatically.
        """
        self.id = id

    def __str__(self):
        """
        Return the string representation of the Base instance.
        """
        return f"[Base] ({self.id})"

    @property
    def id(self):
        """
        id property to get the id value.
        """
        return self._id

    @id.setter
    def id(self, value):
        """
        id property setter to set the id value.
        """
        if value is not None and not isinstance(value, int):
            raise TypeError("id must be an integer")
        self._id = value

# Example usage
if __name__ == "__main__":
    base = Base()
    print(base)
