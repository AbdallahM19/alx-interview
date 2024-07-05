#!/usr/bin/python3
"""python"""


def canUnlockAll(boxes):
    """canUnlockAll function"""
    n = len(boxes)

    opened_boxes = []
    opened_boxes.append(0)
    keys = list(boxes[0])

    while keys:
        key = keys.pop()
        if key < n and key not in opened_boxes:
            opened_boxes.append(key)
            keys.extend(boxes[key])

    return len(opened_boxes) == n
