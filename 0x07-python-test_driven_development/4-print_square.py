#!/usr/bin/python3
"""Defince function to print #"""


def print_square(size):
    """ function to print #
    Args:
        size (int): the size length of the square
    Raises:
        TypeError
        ValueError
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if ((not isinstance(size, float)) and (size < 0)):
        raise TypeError("size must be an integer")
    for i in range
