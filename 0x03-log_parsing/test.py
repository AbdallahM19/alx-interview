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

        if len(parts) < 9:
            continue

        port = parts[0]
        date = ''.join(parts[2:4])
        request = ' '.join(parts[4:7])
        status = parts[7]
        file_size = parts[8]

        # print(port) 8.47.109.229
        # print(date) [2024-07-1809:11:20.157687]
        # print(request) "GET /projects/260 HTTP/1.1"
        # print(status) 405
        # print(file_size) 646
        # print('************************')

        if port and date.startswith('[') and date.endswith(']')\
            and request[1:-1] == "GET /projects/260 HTTP/1.1"\
            and status.isdigit() and file_size.isdigit():

            if status in status_codes:
                status_codes[status] += 1
            total_size += int(file_size)
            line_count += 1
            # print(line_count)  # 1
            # print(file_size)  # 646
            # print(total_size)  # 0

            if line_count / 10 == 1.0:
                print_stats()
except KeyboardInterrupt:
    print_stats()
    sys.exit(0)
finally:
    print_stats()


# <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>


# if __name__ == "__main__":
#     line_count = 1
#     while True:
#         print(line_count / 10)
#         print(line_count % 10)
#         if line_count / 10 == 1.0:
#             print(line_count)
#             print((line_count+1) % 10)
#             print('done')
#             break
#         line_count += 1
#     print('done')
