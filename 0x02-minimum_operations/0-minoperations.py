#!/usr/bin/python3
"""
Minimum Operations
"""


def minOperations(n):
    """
    Function that calculates the fewest number of operations needed to
    result in exactly n H characters in the file.
    Args:
        n (int): The number of characters to be printed.
    Returns:
        int: The fewest number of operations needed to result in
        exactly n H characters in the file.
    """

    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        if n % divisor == 0:
            operations += divisor
            n //= divisor
        else:
            divisor += 1

    return operations
