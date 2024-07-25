#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """
    a method that determines if a given data
    set represents a valid UTF-8 encoding.
    """
    skip = 0
    n = len(data)

    for i in range(n):
        if skip > 0:
            skip -= 1
            continue

        # Check if data[i] is a valid integer within the UTF-8 range
        if not (0 <= data[i] <= 0x10ffff) and type(data[i]) != int:
            return False

        # 1-byte character (ASCII)
        if data[i] <= 0x7f:
            skip = 0

        # 4-byte character
        elif data[i] & 0b11111000 == 0b11110000:
            span = 4
            if n - i >= span and all(list(map(
                lambda x: x & 0b11000000 == 0b10000000,
                data[i + 1: i + span],
            ))):
                skip = span - 1
            else:
                return False

        # 3-byte character
        elif data[i] & 0b11110000 == 0b11100000:
            span = 3
            if n - i >= span and all(list(map(
                lambda x: x & 0b11000000 == 0b10000000,
                data[i + 1: i + span],
            ))):
                skip = span - 1
            else:
                return False

        # 2-byte character
        elif data[i] & 0b11100000 == 0b11000000:
            span = 2
            if n - i >= span and all(list(map(
                lambda x: x & 0b11000000 == 0b10000000,
                data[i + 1: i + span],
            ))):
                skip = span - 1
            else:
                return False
        else:
            return False

    return True
