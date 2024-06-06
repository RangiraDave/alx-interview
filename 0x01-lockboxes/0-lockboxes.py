#!/usr/bin/python3
"""
Having N number of locked boxes,
each box is numbered sequentially from 0 to N-1,
and each box may contain keys to the other boxes.

Here is a method to open all the boxes:
1. Start with box 0
2. Open it and take the keys to the other boxes
3. Open the boxes with the keys you find inside
4. Repeat step 2 and 3 until all boxes have been opened
"""


def canUnlockAll(boxes):
    """ Method to determine if all the boxes can be opened. """

    if not boxes:
        return False

    keys = [0]
    for key in keys:
        for new_key in boxes[key]:
            if new_key not in keys and new_key < len(boxes):
                keys.append(new_key)

    return len(keys) == len(boxes)
