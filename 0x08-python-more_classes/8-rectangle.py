#!/usr/bin/python3
"""
defining an empty class
"""


class Rectangle:
    """class Rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes the rectangle"""
        type(self).number_of_instances += 1
        self.height = height
        self.width = width

    @property
    def width(self):
        """getter for the private instance attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for the private instance attribute width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter for the private instance attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for the private instance attribute height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    """
    Calculate area of Rectangle.
    """
    def area(self):
        return self.__height * self.__width

    """
    Calculate perimeter of Rectangle object.
    """
    def perimeter(self):
        if self.__height == 0 or self.width == 0:
            return 0
        return (self.__height + self.width) * 2
    """
    str function
    """
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the Rectangle with the greater area.
        Args:
            rect_1 (Rectangle): The first Rectangle.
            rect_2 (Rectangle): The second Rectangle.
        Raises:
            TypeError: If either of rect_1 or rect_2 is not a Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

    """
    str
    """

    def __str__(self):
        '''method: __str__
        return: nice string representation of rectangle
        '''
        ret_str = ""
        if self.__height == 0 or self.__width == 0:
            return ""
        for idx in range(self.__height):
            ret_str += str(self.print_symbol) * self.width
            if idx + 1 < self.__height:
                ret_str += '\n'
        return ret_str
    """
    repr func
    """
    def __repr__(self):
        """Return the string representation of the Rectangle."""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)
    """
    del fun
    """
    def __del__(self):
        '''method: __del__
        deletes instance of Rectangle class, and prints "bye" message
        '''
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
