#!/usr/bin/python3
"""Define Square class"""


class Square:
    """Square Class"""

    def __init__(self, size=0):
        """Initialize Square
        Args:
            size (int): size of square
        """
        self.size = size

    @property
    def size(self):
        """get method"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Method to compute area of square
        Args: none
        Return: area of square
        """
        return (self.__size * self.__size)

    def my_print(self):
        """function to print # in square"""
        if self.size == 0:
            print("")
        else:
            for i in range(0, self.__size):
                [print("#", end="") for j in range(self.__size)]
                print("")
