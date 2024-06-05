import math
from abc import ABCMeta


class Shape(metaclass=ABCMeta):

    def area(self):
        pass

    def perimeter(self):
        pass


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def __eq__(self, other):
        if not isinstance(other, Circle):
            return False
        return (self.radius == other.radius)

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def __eq__(self, other):
        if not isinstance(other, Rectangle):
            return False
        return (self.width == other.width) and (self.length == other.length)

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return (self.length * 2) + (self.width * 2)


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def __eq__(self, other):
        if not isinstance(other, Square):
            return False
        return (self.length == other.length)

    def area(self):
        return self.length ** 2

    def perimeter(self):
        return self.length * 4
