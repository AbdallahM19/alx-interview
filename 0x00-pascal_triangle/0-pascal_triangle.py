#!/usr/bin/python3
"""pascal triangle"""


def pascal_triangle(n):
    """pascal function"""
    if n <= 0 or type(n) is not int:
        return []
    triangle = []
    for i in range(n):
        r = []
        for x in range(i + 1):
            if x == 0 or x == i:
                r.append(1)
            else:
                r.append(triangle[i - 1][x - 1] + triangle[i - 1][x])
        triangle.append(r)
    return triangle
