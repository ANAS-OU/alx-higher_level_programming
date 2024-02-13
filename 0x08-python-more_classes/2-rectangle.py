#!/usr/bin/python3
"""Rectangle Module"""


class Rectangle:
    """Defines a rectangle
    """

    def __init__(self, width=0, height=0):
        """Initializes a Rectangle object with the given width and height

        Args:
            width: width of rectangle
            height: height of rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width of Rectangle object

        Returns:
            width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Setter Method for width
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """Getter Method for height

        Returns:
            height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Setter Method for height
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """Rectongale area

        Returns:
            area's value
        """
        return self.__width * self.__height

    def perimeter(self):
        """Rectongale perimeter
        
        Returns:
            perimeter's value
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
