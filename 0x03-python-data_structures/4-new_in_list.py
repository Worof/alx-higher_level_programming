#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """
    Replaces an element in a list at a specific position without modifying
    the original list.

    Args:
        my_list (list): The original list.
        idx (int): The index at which to replace an element.
        element: The new value to be placed at the specified index.

    Returns:
        A new list with the specified element replaced, or a copy of the
        original list if the index is out of range.
    """
    new_list = my_list.copy()
    if 0 <= idx < len(new_list):
        new_list[idx] = element
    return new_list

# Below is for your local testing and should not be pushed to your repo
# if __name__ == "__main__":
#     my_list = [1, 2, 3, 4, 5]
#     idx = 3
#     new_element = 9
#     new_list = new_in_list(my_list, idx, new_element)
#     print(new_list)
#     print(my_list)
