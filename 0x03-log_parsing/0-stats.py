#!/usr/bin/python3
"""
Write a script that reads stdin line
by line and computes metrics
"""

import sys
import re


def print_stats(dict_stats: dict) -> None:
    """Prints the stats of the dict_stats dictionary"""
    print("File size: {}".format(dict_stats["total_size"]))
    for status_frequency in sorted(dict_stats["status_file"]):
        if dict_stats["status_file"][status_frequency]:
            print("{}: {}".format(
                status_frequency, dict_stats["status_file"][status_frequency]
            ))


if __name__ == "__main__":
    regex = re.compile(
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d+\] "GET /projects/260 HTTP/1.1" (.{3}) (\d+)'  # nopep8
    )

    line_count = 0
    dict_stats = {}
    dict_stats["total_size"] = 0
    dict_stats["status_file"] = {
        str(status): 0 for status in [
            200, 301, 400, 401, 403, 404, 405, 500]
    }

    try:
        for line in sys.stdin:
            line = line.strip()
            match = regex.fullmatch(line)

            if match:
                line_count += 1
                status = match.group(1)
                file_size = int(match.group(2))
                dict_stats["total_size"] += file_size

                if status.isdecimal():
                    dict_stats["status_file"][status] += 1

                if line_count == 10:
                    print_stats(dict_stats)
    finally:
        print_stats(dict_stats)
