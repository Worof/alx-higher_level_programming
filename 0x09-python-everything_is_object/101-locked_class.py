#!/usr/bin/python3
"""
This module defines the LockedClass class.
The LockedClass prevents the dynamic creation of new instance attributes,
except if the new instance attribute is called 'first_name'.
"""

class LockedClass:
    """
    LockedClass only allows the creation of a 'first_name' instance attribute.
    Attempts to create any other attribute will raise an AttributeError.
    """
    __slots__ = ['first_name']
