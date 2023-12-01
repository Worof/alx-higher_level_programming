#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """
    Prints a matrix of integers.

    Args:
        matrix (list of lists): A matrix represented as a list of lists of integers.

    Returns:
        None: This function prints to stdout and returns nothing.
    """
    for row in matrix:
        print(" ".join("{:d}".format(elem) for elem in row))

# Below is for your local testing and should not be pushed to your repo
# if __name__ == "__main__":
#     matrix = [
#         [1, 2, 3],
#         [4, 5, 6],
#         [7, 8, 9]
#     ]
#     print_matrix_integer(matrix)
#     print("--")
#     print_matrix_integer()
