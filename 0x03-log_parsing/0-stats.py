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


if __name__ == "__main__":
    try:
        for line in sys.stdin:
            parts = line.split()

            if len(parts) != 9:
                continue

            port = parts[0]
            date = ''.join(parts[2:4])
            request = ' '.join(parts[4:7])
            status = parts[7]
            file_size = parts[8]

            if port and date.startswith('[') and date.endswith(']')\
                and request[1:-1] == "GET /projects/260 HTTP/1.1"\
                    and status.isdigit() and file_size.isdigit():

                if status in status_codes:
                    status_codes[status] += 1
                total_size += int(file_size)
                line_count += 1

                if line_count / 10 == 1.0:
                    print_stats()
                    line_count = 0
    finally:
        print_stats()
