#!/usr/bin/python3
"""
Given an `n` x `n` 2D matrix, rotate it 90 degrees clockwise.

- Prototype: `def rotate_2d_matrix(matrix):`
- Do not return anything. The matrix must be edited in-place.
- You can assume the matrix will have 2 dimensions and will not be empty.
"""


def rotate_2d_matrix(matrix):
    """
    Rotates a 2D Matrix (list of lists).

    Arguments:
        - `matrix`: A 2D list of list.
    """
    # Transpose the matrix
    for row in range(len(matrix)):
        for column in range(row, len(matrix)):
            matrix[row][column], matrix[column][row] \
                = matrix[column][row], matrix[row][column]

        # Reverse each row
        matrix[row] = matrix[row][::-1]
