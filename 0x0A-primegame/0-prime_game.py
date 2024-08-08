#!/usr/bin/python3
"""
    Determines the winner of a prime game session.
"""


def isWinner(x, nums):
    """
      Determines the winner of a prime game session with `x` rounds.
      The prime game is a game where players take turns removing
      prime numbers from a list of numbers.
      The player with the last prime number wins.
      Args:
        x (int): The number of rounds.
        nums (list): A list of integers.

      Returns:
        str: The name of the player that won the most rounds.
        None: If the winner cannot be determined.
    """

    if x < 1 or not nums:
        return None
    marias_wins, bens_wins = 0, 0
    # generate primes with a limit of the maximum number in nums
    n = max(nums)
    primes = [True for _ in range(1, n + 1, 1)]
    primes[0] = False
    for i, is_prime in enumerate(primes, 1):
        if i == 1 or not is_prime:
            continue
        for j in range(i + i, n + 1, i):
            primes[j - 1] = False
    # filter the number of primes less than n in nums for each round
    for _, n in zip(range(x), nums):
        primes_count = len(list(filter(lambda x: x, primes[0: n])))
        bens_wins += primes_count % 2 == 0
        marias_wins += primes_count % 2 == 1
    if marias_wins == bens_wins:
        return None
    return 'Maria' if marias_wins > bens_wins else 'Ben'
