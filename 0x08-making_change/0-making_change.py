#!/usr/bin/python3
"""Making Change"""


def makeChange(coins, total):
    """
    Return: fewest number of coins needed to meet total
    - If total is 0 or less, return 0
    - If total cannot be met by any number of coins you have, return -1
    """
    sorted_coins = sorted(coins, reverse=True)
    count = 0
    if total <= 0:
        return 0
    for coin in sorted_coins:
        if total == 0:
            break
        num_of_coins = total // coin
        count += num_of_coins
        total -= num_of_coins * coin
    if total != 0:
        return -1
    return count
