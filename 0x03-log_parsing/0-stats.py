#!/usr/bin/python3

import sys


total_size = 0
line_count = 0
status_codes = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}


def print_stats():
    """Prints the accumulated statistics"""
    print("File size: {}".format(total_size))
    for key, value in sorted(status_codes.items()):
        if value > 0:
            print("{}: {}".format(key, value))


try:
    for line in sys.stdin:
        parts = line.split()

        status = parts[7]
        file_size = parts[8]

        if len(parts[::-1]) > 2:
            line_count += 1

            if line_count <= 10:
                total_size += int(file_size)
                print(type(status))

                if status in status_codes.keys():
                    status_codes[status] += 1

            if line_count == 10:
                print_stats()
                line_count = 0
finally:
    print_stats()
