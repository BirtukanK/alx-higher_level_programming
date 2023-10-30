#!/usr/bin/python3
"""compiling python code"""


class Rectangle:
    """Defines rectangle class"""
    def __init__(self, width=0, height=0):
        """Initialize new rectangle object

        Args:
        width (int): width of rectangle
        height (int): height of rectangle
        """
        self.__height = height
        self.__width = width

    @property
    def height(self):
        """Get value of height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """setting height value"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def width(self):
        """Get value of width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """setting width value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value
