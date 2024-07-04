#!/usr/bin/python3
"""
Python script to create the method that determines if a given data set
represents a valid UTF-8 encoding
"""


def validUTF8(data):
    """
    Checks if a given list of integers represents a valid UTF-8 encoding.

    Args:
        data (list): A list of integers representing the UTF-8 encoding.

    Returns:
        bool: True if the encoding is valid, False otherwise.
    """

    if not data:
        return False

    num_bytes = 0

    for num in data:
        if num_bytes == 0:
            if (num >> 5) == 0b110:
                num_bytes = 1
            elif (num >> 4) == 0b1110:
                num_bytes = 2
            elif (num >> 3) == 0b11110:
                num_bytes = 3
            elif (num >> 7):
                return False
        else:
            if (num >> 6) != 0b10:
                return False
            num_bytes -= 1

    return num_bytes == 0
