#!/usr/bin/python3
"""
Determines the winner of a Prime Game.
See README for full details.
"""


def isWinner(x, nums):
    """
    Determines the winner of a game played between two players, Maria and Ben.

    Arguments:
        - x (int): The number of rounds to be played.
        - nums (list of int): A list of integers representing the maximum
        number (n) for each round.

    Returns:
        - The name of the player that won the most rounds. If the winner cannot
        be determined, returns None.
    """

    def sieve(n):
        """
        Generates all primes up to n using the Sieve of Eratosthenes algorithm.

        Parameters:
        n (int): The upper limit for generating prime numbers.

        Returns:
            - list: A list of all prime numbers up to n.
        """
        primes = [True for _ in range(n+1)]
        p = 2
        while p * p <= n:
            if primes[p] is True:
                for i in range(p * p, n+1, p):
                    primes[i] = False
            p += 1
        return [p for p in range(2, n) if primes[p]]

    # Initialize scores for both players
    scores = {"Maria": 0, "Ben": 0}

    # Play each round
    for n in nums:
        # Generate all primes up to and including n
        primes = sieve(n+1)

        # If the number of primes is odd, Maria wins the round; otherwise,
        # Ben wins
        scores["Maria" if len(primes) % 2 == 1 else "Ben"] += 1

    # Determine the overall winner
    if scores["Maria"] > scores["Ben"]:
        return "Maria"
    elif scores["Maria"] < scores["Ben"]:
        return "Ben"
    else:
        return None
