#!/usr/bin/python3
"""Prime Game"""


def isWinner(x, nums):
    """Return: name of the player that won the most rounds"""
    if not nums or x < 1:
        return None

    max_n = max(nums)
    sieve = [True] * (max_n + 1)
    sieve[0] = sieve[1] = False

    for i in range(2, int(max_n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, max_n + 1, i):
                sieve[j] = False

    primes_up_to = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        primes_up_to[i] = primes_up_to[i - 1] + (1 if sieve[i] else 0)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if primes_up_to[n] % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
