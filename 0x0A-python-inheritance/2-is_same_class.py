#!/usr/bin/python3
""" Defines a function"""


def is_same_class(obj, a_class):
    """ Function to check if an instance is in a class"""
    if type(obj) == a_class:
        return True
    return False
