#!/usr/bin/python3
"""Defines print sorted function"""


class MyList(list):
    """ a class which inherits from List class"""

    def print_sorted(self):
        """ prints list in sorted way"""
        print(sorted(self))
