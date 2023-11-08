#!/usr/bin/python3
""" Defines a function"""


def inherits_from(obj, a_class):
    """ Function checks if a class is inherited"""
    if isinstance(obj, a_class):
        return True
    return False
