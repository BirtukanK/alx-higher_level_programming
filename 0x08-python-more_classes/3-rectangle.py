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
        self.height = height
        self.width = width

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

    def area(self):
        """Method to calculate area of a rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Method to calculate perimeter of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)
    def __str__(self):
        """Return the printable representation of the Rectangle.

        Represents the rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))
