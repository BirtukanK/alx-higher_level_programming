#!/usr/bin/python3
"""Defines square class"""


class Square:
    """A class to define a square"""
    def __init__(self, size=0):
        """Initialize a Square.
            Args:
        size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self._Square__size = size
