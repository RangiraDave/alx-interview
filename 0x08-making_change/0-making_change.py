#!/usr/bin/python3
"""
Python script to create a function to calculate the fewest
number of coins needed
"""


def makeChange(coins, total):
    """
    Calculate the fewest number of coins needed to meet a given amount total.

    Args:
        coins (list): List of coin values in your possession.
        total (int): The target amount to be met.

    Returns:
        int: The fewest number of coins needed to meet the total.
             Returns -1 if the total cannot be met by any number of coins.

    """

    if total <= 0:
        return 0

    # Initialize a list to store the minimum number of coins
    # needed for each amount
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Iterate through each amount from 1 to the target total
    for i in range(1, total + 1):
        # Iterate through each coin value
        for coin in coins:
            # Check if the current coin value can be used to
            # make change for the current amount
            if i - coin >= 0:
                # Update the minimum number of coins needed for
                # the current amount
                dp[i] = min(dp[i], dp[i - coin] + 1)

    # Return the fewest number of coins needed for the target total
    return dp[total] if dp[total] != float('inf') else -1
