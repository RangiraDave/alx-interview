#!/usr/bin/python3
"""
Log Parsing
"""

import re
import sys


def print_stats(total_size, status_codes):
    """
    Print the log stats
    """
    print("Total file size: File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


def parse_line(line):
    """
    Parse a line from the input
    """
    line_format = re.compile(r'^\S+ - \[\S+ \S+\] "GET /projects/260 HTTP/1\.1" (\d{3}) (\d+)$')
    match = line_format.match(line)
    if match:
        status_code = int(match.group(1))
        file_size = int(match.group(2))
        return status_code, file_size
    return None, None


def main():
    total_size = 0
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    line_count = 0

    try:
        for line in sys.stdin:
            status_code, file_size = parse_line(line)
            if status_code is None:
                continue

            total_size += file_size
            if status_code in status_codes:
                status_codes[status_code] += 1

            line_count += 1
            if line_count % 10 == 0:
                print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        raise


if __name__ == "__main__":
    main()