#!/usr/bin/python3
"""
Write a script that reads stdin line
by line and computes metrics
"""
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


try:
    for line in sys.stdin:
        parts = line.split()

        if len(parts) == 9:
            status = parts[7]
            file_size = parts[8]

            if status in status_codes.keys():
                status_codes[status] += 1

            total_size += int(file_size)
            line_count += 1

        if line_count == 10:
            line_count = 0
            print("File size: {}".format(total_size))
            for key, value in sorted(status_codes.items()):
                if value != 0:
                    print("{}: {}".format(key, value))
except Exception as e:
    pass
finally:
    print("File size: {}".format(total_size))
    for key, value in sorted(status_codes.items()):
        if value != 0:
            print("{}: {}".format(key, value))
