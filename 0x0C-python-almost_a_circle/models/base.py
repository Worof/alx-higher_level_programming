#!/usr/bin/python3
import json
"""
This module contains the Base class.
The Base class will serve as the foundation for all other classes in this project.
It manages the id attribute in all future classes and avoids duplicating code.
"""

class Base:
    """A base class for future models."""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base instance."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)
    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file."""
        filename = f"{cls.__name__}.json"
        list_dicts = []
        if list_objs is not None:
            list_dicts = [obj.to_dictionary() for obj in list_objs]
        with open(filename, 'w') as f:
            f.write(cls.to_json_string(list_dicts))

# For testing purposes, the code below can be in a separate file, like 0-main.py
# if __name__ == "__main__":
#     b1 = Base()
#     print(b1.id)
#     b2 = Base()
#     print(b2.id)
#     b3 = Base()
#     print(b3.id)
#     b4 = Base(12)
#     print(b4.id)
#     b5 = Base()
#     print(b5.id)
