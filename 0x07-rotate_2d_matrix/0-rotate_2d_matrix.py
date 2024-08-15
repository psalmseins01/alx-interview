#!/usr/bin/python3
""" Rotate 2D Matrix module"""


def rotate_2d_matrix(matrix):
    """ Given `n` x `n` 2D Matrix
    Rotate it 90 degrees clockwise
    Args:
        matix - 2 D matrix
    """
    # Matrix replica
    matrix_replica = matrix[:]

    for i in range(len(matrix)):
        # retract column from matrix_replica
        column = [row[i] for row in matrix_replica]
        # Replace in matrix in reverse order
        matrix[i] = column[::-1]
