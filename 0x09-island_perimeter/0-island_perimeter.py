#!/usr/bin/python3
"""
Create a function `def island_perimeter(grid):` that returns
the perimeter of the island described in `grid`:

- `grid` is a list of list of integers:
    - 0 represents water
    - 1 represents land
    - Each cell is square, with a side length of 1
    - Cells are connected horizontally/vertically
      (not diagonally).
    - `grid` is rectangular, with its width and height not
      exceeding 100
- The grid is completely surrounded by water
- There is only one island (or nothing).
- The island doesn't have "lakes" (water inside that isn't
  connected to the water surrounding the island).
"""


def island_perimeter(grid):
    """
    Returns the perimeter of the island described in `grid`.

    Arguments:
        - `grid`: A list of list of integers.
    """
    perimeter = 0

    for rows in range(len(grid)):
        for columns in range(len(grid[0])):
            # If the cell is land (1), assume all
            # four sides contribute to the perimeter
            if grid[rows][columns] == 1:
                perimeter += 4

                # If the cell above is also land, subtract 2
                # from the perimeter (because the two sides
                # touching each other do not contribute to
                # the perimeter)
                if rows > 0 and \
                        grid[rows - 1][columns] == 1:
                    perimeter -= 2

                # If the cell to the left is also land, subtract
                # 2 from the perimeter (for the same reason as
                # above)
                if columns > 0 and \
                        grid[rows][columns - 1] == 1:
                    perimeter -= 2

    return perimeter
