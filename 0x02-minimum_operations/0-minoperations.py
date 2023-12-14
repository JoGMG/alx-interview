"""
In a text file, there is a single character `H`. Your text editor
can execute only two operations in this file: `Copy All` and `Paste`.
Given a number `n`, write a method that calculates the fewest number
of operations needed to result in exactly `n` `H` characters in the file.
- Prototype: `def minOperations(n)`
- Returns an integer
- If `n` is impossible to achieve, return `0`
"""


def minOperations(n):
    """
    Returns the fewest number of operations needed to get `n` `H`
    characters in a text file.

    Arguments:
        - `n`: desired number of `H` characters
    """

    if n <= 1:
        return 0

    operations = 0
    text_size = 1

    while text_size < n:
        if n % text_size == 0:
            # If text_size is a divisor of n, we can copy and paste current `H` characters
            operations += 2
            text_size *= 2
            current = text_size // 2 # already copied `H` characters
        else:
            # If text_size is not a divisor of n, we can only paste the already copied `H` characters
            operations += 1
            text_size += current

    return operations
