#!/usr/bin/python3
"""Determine the fewest number of coins
needed to meet a given amount total
"""


def makeChange(coins, total):
    """Prototype: def makeChange(coins, total)
    Return: fewest number of coins needed to meet total
    If total is 0 or less, return 0
    If total cannot be met by any number of coins you have,
    return -1
    """
    if total <= 0:
        return 0

    # Coins validity check
    if (coins is None or len(coins) == 0):
        return -1

    change = 0
    coins_available = sorted(coins, reverse=True)
    left_change = total

    for coin in coins_available:
        while (left_change % coin >= 0 and left_change >= coin):
            change += int(left_change / coin)
            left_change = left_change % coin

    return change if left_change == 0 else -1
