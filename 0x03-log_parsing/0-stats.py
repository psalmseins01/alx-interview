#!/usr/bin/python3
"""
Read from stdin line by line and then computes metrics
Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
<status code> <file size>, skip line if not this format
After every 10 minutes or keyboard interrupt (CTRL + C)
print: number of lines by status code
Status codes: 200, 301, 400, 401, 404, 405, and 500
if status code isn't an integer, do not print it
format: <status code>: <number>
Print status codes in ascending order
"""
import sys


def print_msg(codes, file_size):
    print("File size: {}".format(file_size))
    for key, value in sorted(codes.items()):
        if value != 0:
            print("{}: {}".format(key, value))


file_size = 0
code = 0
count_lines = 0
codes = {
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
        parsed_line = line.split()
        parsed_line = parsed_line[::-1]

        if len(parsed_line) > 2:
            count_lines += 1

            if count_lines <= 10:
                file_size += int(parsed_line[0])
                code = parsed_line[1]

                if (code in codes.keys()):
                    codes[code] += 1

            if (count_lines == 10):
                print_msg(codes, file_size)
                count_lines = 0

finally:
    print_msg(codes, file_size)
