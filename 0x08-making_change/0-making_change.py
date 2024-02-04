#!/usr/bin/python3
"""
Given a pile of coins of different values, determine the fewest
number of coins needed to meet a given amount `total`.

- Prototype: `def makeChange(coins, total)`
- Return: fewest number of coins needed to meet `total`:
    - If `total` is `0` or less, return `0`
    - If `total` cannot be met by any number of coins you have,
      return `-1`
- `coins` is a list of the values of the coins in your possession
- The value of a coin will always be an integer greater than `0`
- You can assume you have an infinite number of each denomination
  of coin in the list
- Your solution's runtime will be evaluated in this task
"""


def makeChange(coins, total):
    if total <= 0:
        return 0

    # Sort coins in descending order
    coins.sort(reverse=True)

    # Initialize a list to store the minimum number of coins needed
    # for each value
    dp = [float('inf')] * (total + 1)

    # The number of coins needed to make change for 0 is always 0
    dp[0] = 0

    # Iterate over each coin
    for coin in coins:
        # Update the dp value for each total that can be made with
        # the current coin
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # If the total cannot be made by any number of coins, return -1
    if dp[total] == float('inf'):
        return -1

    # Return the minimum number of coins needed to make the total
    return dp[total]
