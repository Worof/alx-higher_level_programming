#!/usr/bin/python3
import sys

def is_safe(board, row, col):
    for i in range(col):
        if board[i] == row or abs(board[i] - row) == abs(i - col):
            return False
    return True

def solve_nqueens(board, col, n):
    if col >= n:
        print(str([[i, board[i]] for i in range(n)]))
        return

    for i in range(n):
        if is_safe(board, i, col):
            board[col] = i
            solve_nqueens(board, col + 1, n)

def nqueens(n):
    board = [-1] * n
    solve_nqueens(board, 0, n)

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    n = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

if n < 4:
    print("N must be at least 4")
    sys.exit(1)

nqueens(n)
