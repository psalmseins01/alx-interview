#!/usr/bin/python3
"""
Minimum Operations Module
Calculate the fewest number of operations with a given n
needed to result in exactly n H characters in a file
Prototype: def minOperations(n)
Returns an integer
Return an integer or 0
"""


def minOperations(n):
    """
    Function  Describes minOperations
    Returns an integer
    """
    result = 0
    x = 2
    while n > 1:
        while n % x == 0:
            result = result + x
            n = n / x
        x = x + 1
    return result
