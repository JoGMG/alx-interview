#!/usr/bin/python3
"""
There are `n` number of locked boxes. Each box is numbered sequentially
from `0` to `n - 1` and each box may contain keys to the other boxes.

Write a method that determines if all the boxes can be opened.
- `boxes` is a list of lists
- A key with the same number as a box opens that box
- Assumes all keys will be positive integers
    • There can be keys that do not have boxes
- The first box `boxes[0]` is unlocked
- Return `True` if all boxes can be opened, else return `False`
"""


def canUnlockAll(boxes: list):
    """
    Returns `True` if all boxes within `boxes` can
    be opened, else returns `False`.

    Arguments:
        - `boxes`: A list of lists
    """

    # Set to keep track of the opened boxes
    opened_boxes = set([0])

    # Queue containing the keys
    queue = [0]

    while queue:

        # Removes first key from queue and use it to open a box
        current_box = queue.pop(0)

        # Check the keys in the current box
        for key in boxes[current_box]:

            # If the key opens a new box and the box is not opened yet
            if key not in opened_boxes and key < len(boxes):
                opened_boxes.add(key)
                queue.append(key)

    # Check if all boxes have been opened
    return len(opened_boxes) == len(boxes)
