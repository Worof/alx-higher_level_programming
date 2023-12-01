#!/usr/bin/env python3

def no_c(my_string):
    """
    Removes all characters 'c' and 'C' from a string.

    Args:
        my_string (str): The string to be modified.

    Returns:
        str: A new string with all 'c' and 'C' characters removed.
    """
    return ''.join(char for char in my_string if char not in ['c', 'C'])

# Below is for your local testing and should not be pushed to your repo
# if __name__ == "__main__":
#     print(no_c("Best School"))
#     print(no_c("Chicago"))
#     print(no_c("C is fun!"))
