#!/usr/bin/python3
"""
a square that inhirits from rectangle
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    square class that inhirits from rectangle class
    """
    def __init__(self, size):
        self.__size = size
        super().integer_validator("size", self.__size)
        super().__init__(self.__size, self.__size)

    def area(self):
        """
        calculates the area
        """
        return self.__size * self.__size

    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"
