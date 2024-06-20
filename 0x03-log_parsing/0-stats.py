#!/usr/bin/python3

"""
Log Parsing
"""

import sys
import re
from typing import Dict, List, Tuple


def print_logs(stats: Dict[str, int], size: int) -> None:
    """
    Print logs
    """
    print(f"File size: {size}")
    for key, value in sorted(stats.items()):
        if value != 0:
            print(f"{key}: {value}")

    return None
