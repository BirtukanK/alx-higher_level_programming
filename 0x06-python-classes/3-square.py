#!/usr/bin/python3
"""define Square class"""


class Square:
    """Defines Square class"""
    def __init__(self, size=0):
        """Initialization Square
        Args:
            size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self._Square__size = size

    def area(self):
        """A method that returns current square area

        Args:
            area(self): with no argument
        Return: area of square
        """
        area = self._Square__size * self._Square__size
        return (area)
