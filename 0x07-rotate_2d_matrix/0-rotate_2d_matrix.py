#!/usr/bin/python3
"""solve Rotate 2D Matrix"""


def rotate_2d_matrix(matrix):
    """rotate_2d_matrix function"""
    matrix.reverse()
    for i in range(len(matrix)):
        for x in range(i + 1, len(matrix)):
            matrix[i][x], matrix[x][i] = matrix[x][i], matrix[i][x]
