#!/usr/bin/python3
""" Defines BaseGeometry class"""


class BaseGeometry:
    """ Base geometry class"""
    def area(self):
        """ area method that raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ method to validate value of a name

        Args:
            name (str) - string variable
            value (int) - integer value

        Exception:
            TypeError
            ValueError
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
