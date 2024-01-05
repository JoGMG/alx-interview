#!/usr/bin/python3
"""
A method that determines if a given data set represents a valid UTF-8 encoding.

- Prototype: `def validUTF8(data)`.
- Return: `True` if data is a valid UTF-8 encoding, else return `False`.
- A character in UTF-8 can be 1 to 4 bytes long.
- The data set can contain multiple characters.
- The data will be represented by a list of integers.
- Each integer represents 1 byte of data, therefore you only need to handle the
  8 least significant bits of each integer.
"""


def validUTF8(data: list) -> bool:
    """
    Returns True if `data` is a valid UTF-8 encoding, else False.

    Arguments:
        - `data`: List of integers to validate.
    """
    count = 0
    for num in data:
        bin_rep = format(num, '#010b')[-8:]
        if count == 0:
            for bit in bin_rep:
                if bit == '0':
                    break
                count += 1
            if count == 0:
                continue
            if count == 1 or count > 4:
                return False
        elif not (bin_rep[0] == '1' and bin_rep[1] == '0'):
            return False
        count -= 1
    return count == 0
