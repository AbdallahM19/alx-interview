#!/usr/bin/python3
"""
Write a script that reads stdin line
by line and computes metrics
"""
import re


def extract_input(input_line):
    """
    Extracts sections of Input format:
    <IP Address> - [<date>]
    "GET /projects/260 HTTP/1.1"
    <status code> <file size>
    (if the format is not this one, the line must be skipped)
    """
    fp = (
        r'\s*(?P<ip>\S+)\s*',
        r'\s*\[(?P<date>\d+\-\d+\-\d+ \d+:\d+:\d+\.\d+)\]',
        r'\s*"(?P<request>[^"]*)"\s*',
        r'\s*(?P<status_code>\S+)',
        r'\s*(?P<file_size>\d+)'
    )
    info = {
        'status_code': 0,
        'file_size': 0,
    }
    log_fmt = '{}\\-{}{}{}{}\\s*'.format(
        fp[0], fp[1], fp[2], fp[3], fp[4]
    )
    resp_match = re.fullmatch(log_fmt, input_line)
    if resp_match is not None:
        status_code = resp_match.group('status_code')
        file_size = int(resp_match.group('file_size'))
        info['status_code'] = status_code
        info['file_size'] = file_size
    return info


def print_statistics(total_size, status_stats):
    """Prints accumulated statistics"""
    print('File size: {}'.format(int(total_size)), flush=True)
    for status_code in sorted(status_stats.keys()):
        num = status_stats.get(status_code, 0)
        if num > 0:
            print('{}: {}'.format(str(status_code), int(num)), flush=True)


def update_metrics(line, total_size, status_stats):
    """Updates the metrics from a given HTTP request log."""
    line_info = extract_input(line)
    status_code = line_info.get('status_code', '0')
    if status_code in status_stats.keys():
        status_stats[status_code] += 1
    return total_size + line_info['file_size']


def run():
    """main function"""
    line_count = 0
    total_size = 0
    status_stats = {
        "200": 0,
        "301": 0,
        "400": 0,
        "401": 0,
        "403": 0,
        "404": 0,
        "405": 0,
        "500": 0,
    }

    try:
        while True:
            line = input()
            total_size = update_metrics(
                line,
                total_size,
                status_stats,
            )
            line_count += 1
            if line_count % 10 == 0:
                print_statistics(total_size, status_stats)
    except (KeyboardInterrupt, EOFError):
        print_statistics(total_size, status_stats)


if __name__ == '__main__':
    run()
