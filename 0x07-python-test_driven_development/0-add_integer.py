#!/usr/bin/python3

def add_integer(a, b=98):
    """
    Adds two integers or floats.

    Args:
        a (int or float): The first number.
        b (int or float, optional): The second number. Defaults to 98.

    Raises:
        TypeError: If either `a` or `b` is neither an integer nor a float.

    Returns:
        int: The sum of `a` and `b` as integers.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
