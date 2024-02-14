#!/usr/bin/python3
"""
Determines the winner of a Prime Game.
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

    def is_prime(n):
        """
        Checks if a number is prime.

        Arguments:
            - `n`: The number to check

        Returns:
            - `True` if `n` is a prime number, `False` otherwise.
        """
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def next_prime(n):
        """
        Finds the next prime number after `n`.

        Arguments:
            - `n`: The number to start from

        Returns:
            - The next prime number after `n`.
        """
        while True:
            n += 1
            if is_prime(n):
                return n

    # Initialize scores
    scores = {"Maria": 0, "Ben": 0}

    # Play each round
    for n in nums:
        # Initialize the set of numbers and the current player
        numbers = set(range(2, n + 1))
        current_player = "Maria"

        while True:
            # Find the smallest prime in the set of numbers
            prime = min(p for p in numbers if is_prime(p))

            # Remove the prime and its multiples from the set of numbers
            numbers -= set(range(prime, n + 1, prime))

            # If there are no primes left, the current player loses
            if not any(is_prime(p) for p in numbers):
                scores["Ben" if current_player == "Maria" else "Maria"] += 1
                break

            # Switch to the other player
            current_player = "Ben" if current_player == "Maria" else "Maria"

    # Determine the winner
    if scores["Maria"] > scores["Ben"]:
        return "Maria"
    elif scores["Maria"] < scores["Ben"]:
        return "Ben"
    else:
        return None
