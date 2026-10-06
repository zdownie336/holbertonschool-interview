#!/usr/bin/python3
"""Lockboxes Problem"""


def canUnlockAll(boxes):
    """Lockboxes Function"""
    aquired_keys = boxes[0]
    visited_boxes = {0}

    while aquired_keys:
        next_box = aquired_keys.pop()
        if next_box >= len(boxes):
            continue
        visited_boxes.add(next_box)
        aquired_keys += boxes[next_box]
        boxes[next_box] = []

    return len(visited_boxes) == len(boxes)
