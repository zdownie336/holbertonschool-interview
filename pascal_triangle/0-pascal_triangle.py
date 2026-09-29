#!/usr/bin/env python3


def pascal_triangle(n):
    tri = []
    if n <= 0:
        return tri

    index = 0
    while index < n:
        list_row = []

        list_index = 0

        while list_index <= index:
            if list_index == 0 or list_index == index:
                list_row.append(1)
            else:
                sum = tri[index - 1][list_index - 1] + tri[index - 1][list_index]
                list_row.append(sum)
            list_index = list_index + 1

        tri.append(list_row)
        index = index + 1

    return tri
