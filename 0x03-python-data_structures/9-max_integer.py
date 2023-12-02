#!/usr/bin/python3

def max_integer(my_list=[]):
    """
    Finds the biggest integer in a list.

    Args:
        my_list (list): The list of integers.

    Returns:
        int: The biggest integer in the list, or None if the list is empty.
    """
    if not my_list:
        return None

    max_val = my_list[0]
    for num in my_list:
        if num > max_val:
            max_val = num

    return max_val

# Below is for your local testing and should not be pushed to your repo
# if __name__ == "__main__":
#     my_list = [1, 90, 2, 13, 34, 5, -13, 3]
#     max_value = max_integer(my_list)
#     print("Max: {}".format(max_value))
