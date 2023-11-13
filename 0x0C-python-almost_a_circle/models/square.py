#!/usr/bin/python3
""" Defines Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class which inherits from rectangle class"""
    def __init__(self, size, x=0, y=0, id=None):
        """ Initialize Square class
        Args:
            size (int) - size of sides
            x (int) - x coordinate of square
            y (int) - y coordinate of square
            id (int) - identification for each process
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ get the size of square"""
        return self.width

    @size.setter
    def size(self, value):
        """ set value of size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ Public method to assign an argument to each attribute
        Args:
            *args (int) - attribute values
                - 1st argument represents id attribute
                - 2nd argument represents width attribute
                - 3rd argument represent height attribute
                - 4th argument represents x attribute
                - 5th argument represents y attribute
        """
        if args and len(args) != 0:
            i = 0
            for arg in args:
                if i == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif i == 1:
                    self.width = arg
                elif i == 2:
                    self.height = arg
                elif i == 3:
                    self.x = arg
                elif i == 4:
                    self.y = arg
                i += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def __str__(self):
        """ overloading str() method"""
        return "[Square] ({}) {}/{} - {}".format(id, self.x, self.y, self.size)
