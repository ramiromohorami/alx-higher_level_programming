#!/usr/bin/python3
"""Square module."""


class Square:
    """Defining a square."""

    def __init__(self, size=0):
        """Constructor.

        Args:
            size: length of the square.

        Raises:
            TypeEroor: If size is not an integer
            ValueError: If size is less than 0
        """
        if type(size) is not int:
            raise TypeError('size must be an integer')
        else:
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size
