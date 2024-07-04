#!/usr/bin/python3
"""
Function to determine if all the boxes can be opened
Prototype: def canUnlockAll(boxes)
"""


def canUnlockAll(boxes):
    """
    Check if boxes can be unlocked
    """
    for k in range(1, len(boxes) - 1):
        control = False
        for i in range(len(boxes)):
            control = (k in boxes[i] and k != i)
            if control:
                break
        if control is False:
            return control
    return True
