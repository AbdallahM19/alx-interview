#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """
    a method that determines if a given data
    set represents a valid UTF-8 encoding.
    """
    count = 0

    for byte in data:
        if (byte & 0b10000000) == 0:
            if count > 0:
                return False
            elif byte < 0b11000000:
                continue
            elif byte < 0b11100000:
                count += 1
            elif byte < 0b11110000:
                count += 2
            else:
                count += 3
        else:
            count -= 1

    return count == 0
