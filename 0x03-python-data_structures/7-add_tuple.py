#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    """
    Adds two tuples.

    Args:
        tuple_a (tuple): The first tuple.
        tuple_b (tuple): The second tuple.

    Returns:
        tuple: A tuple containing the sum of the first and second elements of the input tuples.
    """
    # Ensure each tuple has at least two elements
    tuple_a += (0, 0)
    tuple_b += (0, 0)

    # Add the corresponding elements of the tuples
    new_tuple = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])

    return new_tuple

# Below is for your local testing and should not be pushed to your repo
# if __name__ == "__main__":
#     tuple_a = (1, 89)
#     tuple_b = (88, 11)
#     new_tuple = add_tuple(tuple_a, tuple_b)
#     print(new_tuple)
#     print(add_tuple(tuple_a, (1, )))
#     print(add_tuple(tuple_a, ()))
