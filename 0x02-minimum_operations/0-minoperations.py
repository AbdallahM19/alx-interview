#!/usr/bin/env python3
"""pycode"""


def minOperations(n):
    """minOperations function"""
    if type(n) != int or n == '' or n == 0:
        return 0

    h = 1
    x = 0
    operations = 0

    while h < n:
        if n % h == 0:
            x = h
            operations += 1  # Copy All
        h += x
        operations += 1  # Paste
    return operations
