#!/usr/bin/python3
"""Module for testing and completing pascal's triangle"""


def pascal_triangle(n):
    """function for loping through n for pascal's triangle"""
    tri = []
    if n <= 0:
        return tri

    ind = 0
    while ind < n:
        list_row = []

        list_index = 0

        while list_index <= ind:
            if list_index == 0 or list_index == ind:
                list_row.append(1)
            else:
                sum = tri[ind - 1][list_index - 1] + tri[ind - 1][list_index]
                list_row.append(sum)
            list_index = list_index + 1

        tri.append(list_row)
        ind = ind + 1

    return tri
