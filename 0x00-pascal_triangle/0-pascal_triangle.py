#!/usr/bin/python3
"""
Function that returns a list of lists of integers representing the
Pascal's triangle of `n`.
- Returns an empty list if n <= 0
- Assumes n will be always an integer
"""


def pascal_triangle(n: int):
    """
    Returns a list of lists of integers representing
    the Pascal's triangle of `n`.

    Arguments:
        - n: integer
    """

    triangle = []

    # Returns empty list
    if n <= 0:
        return triangle

    for i in range(n):

        # Creates a new row
        row = []

        for j in range(i + 1):

            if j == 0 or j == i:
                # Adds 1 to the start and end of the row
                row.append(1)
            else:
                # Adds the next 2 numbers on the previous row together
                element = triangle[i - 1][j - 1] + triangle[i - 1][j]
                row.append(element)

        triangle.append(row)

    return triangle
