#!/usr/bin/python3
""" Defines BaseGeometry class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Class which inherits from BaseGeometry parent class"""

    def __init__(self, width, height):
        """ function to initialize the class"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
