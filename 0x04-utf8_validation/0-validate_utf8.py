#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """
    a method that determines if a given data
    set represents a valid UTF-8 encoding.
    """
    num_bytes_to_follow = 0

    for i in data:
        if num_bytes_to_follow == 0:
            if (i >> 4) == 0b1110:
                num_bytes_to_follow = 2
            elif (i >> 3) == 0b11110:
                num_bytes_to_follow = 3
            elif (i >> 5) == 0b110:
                num_bytes_to_follow = 1
            elif (i >> 7):
                return False
        else:
            if (i >> 6) != 0b10:
                return False
            num_bytes_to_follow -= 1

    return num_bytes_to_follow == 0
