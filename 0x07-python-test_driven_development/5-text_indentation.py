#!/usr/bin/python3

def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: '.', '?' and ':'.

    Args:
        text (str): The text to be formatted and printed.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while i < len(text):
        print(text[i], end="")
        if text[i] in ['.', '?', ':']:
            print("\n\n", end="")
            while i + 1 < len(text) and text[i + 1] == ' ':
                i += 1
        i += 1
