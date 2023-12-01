#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """
    Replaces an element in a list at a specific position.

    Args:
        my_list (list): The list to modify.
        idx (int): The index at which to replace an element.
        element: The new value to be placed at the specified index.

    Returns:
        The modified list if idx is within range, otherwise the original list.
    """
    if 0 <= idx < len(my_list):
        my_list[idx] = element
    return my_list

# Below is for your local testing and should not be pushed to your repo
# if __name__ == "__main__":
#     my_list = [1, 2, 3, 4, 5]
#     idx = 3
#     new_element = 9
#     new_list = replace_in_list(my_list, idx, new_element)
#     print(new_list)
#     print(my_list)
