#!/usr/bin/python3

def element_at(my_list, idx):
    """
    Retrieves an element from a list at a specific index.

    Args:
        my_list (list): The list from which to retrieve the element.
        idx (int): The index of the element to retrieve.

    Returns:
        The element at the specified index in my_list if idx is within the
        range of my_list, otherwise None.
    """
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]

# Below is for your local testing and should not be pushed to your repo
# if __name__ == "__main__":
#     my_list = [1, 2, 3, 4, 5]
#     idx = 3
#     print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))
