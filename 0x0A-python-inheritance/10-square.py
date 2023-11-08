#!/usr/bin/python3
""" Defines BaseGeometry class"""
Rectangle = __import__('9-rectangle.py').Rectangle


class Square(Rectangle):
    """ Class defining square"""

    def __init__(self, size):

        """ Initialize Square

        Args:
            size (int): integer size of square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
