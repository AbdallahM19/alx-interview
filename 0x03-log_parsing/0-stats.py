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


def print_stats(total_size, status_codes):
    """Prints the accumulated statistics"""
    print("File size: {}".format(total_size))
    for key, value in sorted(status_codes.items()):
        if value > 0:
            print("{}: {}".format(key, value))


try:
    for line in sys.stdin:
        parts = line.split()

        if len(parts) != 9:
            continue

        ip = parts[0]
        date = ''.join(parts[2:4])
        request = ' '.join(parts[4:7])
        status = parts[7]
        file_size = parts[8]

        if ip and date.startswith('[') and date.endswith(']')\
            and request[1:-1] == "GET /projects/260 HTTP/1.1"\
                and status.isdigit() and file_size.isdigit():
            if status not in status_codes:
                continue
            status_codes[status] += 1
            total_size += int(file_size)
            line_count += 1

            if line_count == 10:
                print_stats(total_size, status_codes)
                line_count = 0
finally:
    print_stats(total_size, status_codes)
