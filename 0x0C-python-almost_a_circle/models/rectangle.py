#!/usr/bin/python3
"""
Base Module

This is a simple module of the porpuse of
being familiar with <Unittest> in python.
"""
from models.base import Base


class Rectangle(Base):
    """Rectangle Class"""

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0 and name in ["width", "height"]:
            raise ValueError("{} must be > 0".format(name))
        if value < 0 and name in ["x", "y"]:
            raise ValueError("{} must be >= 0".format(name))

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialization with the class constructor"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.integer_validator("x", x)
        self.integer_validator("y", y)

        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    def area(self):
        """Returns the rectangle area"""
        return self.__width * self.__height

    def display(self):
        """Display on the stdout the rectangle"""
        for y in range(self.__y):
            print("")
        for row in range(self.__height):
            print((" " * self.__x) + ("#" * self.__width))

    def update(self, *args):
        """Method for updating an instance"""
        keys = list(self.__dict__.keys())
        idx = 0
        for arg in args:
            key = keys[idx]
            self.__dict__[key] = arg
            idx += 1

    def __str__(self):
        """String representation of an instance"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.__x,
                                                       self.__y,
                                                       self.__width,
                                                       self.__height)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.integer_validator("width", width)
        self.__width = width

    @property
    def height(self):
        return self__height

    @height.setter
    def height(self, height):
        self.integer_validator("height", height)
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.integer_validator("x", x)
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.integer_validator("y", y)
        self.__y = y
