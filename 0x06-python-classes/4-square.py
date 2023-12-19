#!/usr/bin/python3
"""Square module."""


class Square:
    """Defining a square."""

    def __init__(self, size=0):
        """Constructor.

        Args:
            size: length of the square.      
        """
        self.__size = size
        
    @property
    def size(self):
        """Property for the length of a side of this square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        return self.__size
    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError('size must be an integer')
        else:
            if value < 0:
                raise ValueError('size must be => 0')
            else:
                self.__size = value
    def area(self):
        """Area of the square.

        Returns:
            The size of the square.
        """
        return self.__size ** 2
