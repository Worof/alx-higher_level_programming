#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """
    Prints all integers from a list in reverse order.

    Args:
        my_list (list): A list of integers.

    Returns:
        None: This function prints to stdout and returns nothing.
    """
    for i in reversed(my_list):
        print("{:d}".format(i))

# Below is for your local testing and should not be pushed to your repo
# if __name__ == "__main__":
#     my_list = [1, 2, 3, 4, 5]
#     print_reversed_list_integer(my_list)
