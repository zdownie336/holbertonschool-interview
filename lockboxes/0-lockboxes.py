#!/usr/bin/python3 leetcode
"""Module for practising lockbox"""


def canUnlockAll(boxes):
    seen = []
    flag = 0
    for index, box in enumerate(boxes):
        if index == 0:
            duplication = list(set(box))
            for key in duplication:
                seen.append([key, 0])
        else:
            for element in seen:
                if element[0] == index:
                    open_box(box, seen)
                    element[1] = 1
                    break
    while flag == 0:
        flag = 1
        for index, element in enumerate(seen):
            if element[1] == 0:
                flag = 0
                try:
                    open_box(boxes[element[0]], seen)
                    element[1] = 1
                except IndexError:
                    del seen[index]

    seen.sort()
    if seen[0][0] == 0:
        del seen[0]
    for index in range(1, len(boxes)):
        try:
            if index != seen[index - 1][0]:
                return False
        except IndexError:
            return False
    return True


def open_box(box, seen):
    duplication = list(set(box))

    for key in duplication:
        if key == 0:
            opened_key = [key, 1]
        else:
            opened_key = [key, 0]
        try:
            if not any(sub[0] == opened_key[0] for sub in seen):
                seen.append(opened_key)
        except IndexError:
            pass
