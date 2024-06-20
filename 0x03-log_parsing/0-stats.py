#!/usr/bin/python3
"""
Log Parsing
"""

import sys


def print_stats(total_size, status_codes):
    """
    Print the log stats
    """
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


def parse_line(line):
    """
    Parse a line from the input
    """
    try:
        parts = line.split()
        ip_address = parts[0]
        status_code = int(parts[-2])
        file_size = int(parts[-1])
        return ip_address, status_code, file_size
    except (IndexError, ValueError):
        return None, None, None


def main():
    """
    Main function
    """
    total_size = 0
    status_codes = {
        200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0
        }
    line_count = 0

    try:
        for line in sys.stdin:
            ip_address, status_code, file_size = parse_line(line)
            if ip_address is None:
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
