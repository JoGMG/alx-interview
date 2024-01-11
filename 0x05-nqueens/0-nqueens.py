#!/usr/bin/python3
"""
The N queens puzzle is the challenge of placing N non-attacking queens
on an NxN chessboard. Write a program that solves the N queens problem.

- Usage: `nqueens N`:
  • If the user called the program with the wrong number of arguments,
    print `Usage: nqueens N`, followed by a new line, and exit with
    the status `1`.
- where N must be an integer greater or equal to `4`:
  • If N is not an integer, print `N must be a number`, followed by a
    new line, and exit with the status `1`.
  • If N is smaller than `4`, print `N must be at least 4`, followed by
    a new line, and exit with the status `1`.
- The program should print every possible solution to the problem:
  • One solution per line.
  • Format: see example.
  • You don't have to print the solutions in a specific order.
- You are only allowed to import the `sys` module.
"""
import sys


def solve(n: int, i: int, a: list, b: list, c: list):
    """
    A generator function that solves the N-queens problem using
    backtracking.

    Arguments:
    n: The size of the chessboard.
    i: The current row.
    a: The positions of the queens in the previous rows.
    b: The diagonals from top-left to bottom-right that are
    already occupied by queens.
    c: The diagonals from top-right to bottom-left that are
    already occupied by queens.

    Yields:
    A solution to the N-queens problem, represented as a list of
    column positions for the queens.
    """
    if i < n:
        for j in range(n):
            if j not in a and i+j not in b and i-j not in c:
                for solution in solve(n, i+1, a+[j], b+[i+j], c+[i-j]):
                    yield solution
    else:
        yield a


def main():
    """
    The main function that parses the command-line arguments and
    solves the N-queens problem.

    It expects one command-line argument, which is the size of
    the chessboard. It checks that this argument is a number
    greater than or equal to 4. If the argument is valid, it
    calls the `solve` function to find all solutions to the
    N-queens problem and prints them. If the argument is not
    valid, it prints an error message and exits with status 1.
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N\n")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number\n")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4\n")
        sys.exit(1)
    solutions = list(solve(n, 0, [], [], []))
    for solution in solutions:
        result = [[i, j] for i, j in enumerate(solution)]
        print(result)


if __name__ == "__main__":
    main()
