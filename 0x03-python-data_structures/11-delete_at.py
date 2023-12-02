#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    """
    Deletes the item at a specific position in a list.

    Args:
        my_list (list): The list from which to delete an item.
        idx (int): The index of the item to delete.

    Returns:
        list: The modified list with the specified item removed.
    """
    if 0 <= idx < len(my_list):
        my_list = my_list[:idx] + my_list[idx+1:]
    return my_list

# Below is for your local testing and should not be pushed to your repo
# if __name__ == "__main__":
#     my_list = [1, 2, 3, 4, 5]
#     idx = 3
#     new_list = delete_at(my_list, idx)
#     print(new_list)
#     print(my_list)
