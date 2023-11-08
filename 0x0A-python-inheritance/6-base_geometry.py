#!/usr/bin/python3
""" Defines BaseGeometry class"""


class BaseGeometry:
    """ Base geometry class"""
    
    def area(self):
        """ area method that raises an exception"""
        raise Exception("area() is not implemented")
