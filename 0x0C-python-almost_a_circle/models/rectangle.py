#!/usr/bin/python3
""" Defines Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """ A Rectangle defining class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initialize Rectangle class
        Args:
            width (int) - width of rectangle
            height (int) - height of rectangle
            x (int) - integer value
            y (int) - integer value
        Raises:
            TypeError - checks if width/height is integer
            ValueError - checks if a value is under or equal to zero
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ get method for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """ set method for width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ get method for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """ set method for height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ get method for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """ set method for x"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ get method for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """ set method for y"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Method to calculate area of rectangle"""
        return self.__width * self.__height

    def display(self):
        """ Method to print in stdout"""
        if self.width == 0 or self.height == 0:
            print("")
            return
        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

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
        """ overriding str method"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x,self.y, self.width, self.height)
