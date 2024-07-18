#!/usr/bin/python3

import sys


def print_stats(status_codes, total_size):
    """
    Print the accumulated statistics.
    """
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


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

        # Check if the line has the correct number of parts
        if len(parts) < 9:
            continue

        ip = parts[0]
        date = parts[3] + " " + parts[4]
        request = " ".join(parts[5:8])
        status = parts[8]
        file_size = parts[9]

        # Validate the format of the line
        if date.startswith("[") and date.endswith("]") and\
                request == '"GET /projects/260 HTTP/1.1"' and\
                status.isdigit() and file_size.isdigit():
            status = str(status)
            file_size = int(file_size)

            # Update counters
            total_size += file_size
            if status in status_codes:
                status_codes[status] += 1
            line_count += 1

            # Print stats every 10 lines
            if line_count == 10:
                print_stats(status_codes, total_size)
                line_count = 0
finally:
    # Print final stats
    print_stats(status_codes, total_size)
