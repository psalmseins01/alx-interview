#!/usr/bin/python3
"""
Module for pascal_triangle
"""


def pascal_triangle(n):
    """
    Function returns a list of integers
    representing the Pascal Triangle of n.
    Returns an empty list if n <= 0
    """
    matrix_rep = []

    if n <= 0:
        return matrix_rep
    matrix_rep = [[1]]

    for i in range(1, n):
        tmp = [1]
        for j in range(len(matrix_rep[i - 1]) - 1):
            curr = matrix_rep[i - 1]
            tmp.append(matrix_rep[i - 1][j] + matrix_rep[i - 1][j + 1])
        tmp.append(1)
        matrix_rep.append(tmp)
    return matrix_rep
