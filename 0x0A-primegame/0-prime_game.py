#!/usr/bin/python3

def isWinner(x, nums):
    """
    Determines the winner of a prime game.

    Parameters:
    x (int): The number of rounds.
    nums (list): A list of integers representing the
    upper limit for each round.

    Returns:
    str: The name of the player who won the most rounds.
    If the winner cannot be determined, return None.
    """

    def is_prime(n):
        """
        Checks if a number is prime.

        Parameters:
        n (int): The number to check.

        Returns:
        bool: True if the number is prime, False otherwise.
        """

        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def get_primes(n):
        """
        Generates a list of prime numbers up to n (inclusive).

        Parameters:
        n (int): The upper limit to generate prime numbers.

        Returns:
        list: A list of prime numbers up to n.
        """
        primes = []
        for i in range(2, n + 1):
            if is_prime(i):
                primes.append(i)
        return primes

    def remove_multiples(nums, prime):
        """
        Removes multiples of a prime number from a list of numbers.

        Parameters:
        nums (list): A list of numbers.
        prime (int): The prime number to remove multiples of.

        Returns:
        list: A list of numbers with multiples of the prime number removed.
        """

        return [num for num in nums if num % prime != 0]

    def play_game(nums):
        """
        Plays a prime game with a list of numbers.

        Parameters:
        nums (list): A list of numbers.

        Returns:
        int: The winner of the game, 0 for Maria and 1 for Ben
        """

        if isinstance(nums, int):
            nums = [nums]  # Convert the integer to a list
        primes = get_primes(max(nums))
        player = 0
        while nums and primes:
            if player == 0:
                prime = max(primes)
                nums = remove_multiples(nums, prime)
                primes.remove(prime)
                player = 1
            else:
                prime = max(primes)
                nums = remove_multiples(nums, prime)
                primes.remove(prime)
                player = 0
        return player

    winners = []
    for i in range(x):
        winner = play_game(nums[i])
        winners.append(winner)

    maria_wins = winners.count(0)
    ben_wins = winners.count(1)

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

# print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
