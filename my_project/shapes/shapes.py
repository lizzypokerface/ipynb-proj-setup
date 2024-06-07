import math
import logging
from abc import ABCMeta

# Configure logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)


class Shape(metaclass=ABCMeta):

    def area(self):
        pass

    def perimeter(self):
        pass


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius
        logger.debug(f"Circle created with radius: {radius}")

    def __eq__(self, other):
        if not isinstance(other, Circle):
            return False
        return self.radius == other.radius

    def area(self):
        area_value = math.pi * self.radius**2
        logger.debug(
            f"Calculating area for Circle with radius {self.radius}: {area_value}"
        )
        return area_value

    def perimeter(self):
        perimeter_value = 2 * math.pi * self.radius
        logger.debug(
            f"Calculating perimeter for Circle with radius {self.radius}: {perimeter_value}"
        )
        return perimeter_value


class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width
        logger.debug(f"Rectangle created with length: {length} and width: {width}")

    def __eq__(self, other):
        if not isinstance(other, Rectangle):
            return False
        return (self.width == other.width) and (self.length == other.length)

    def area(self):
        area_value = self.length * self.width
        logger.debug(
            f"Calculating area for Rectangle with length {self.length} and width {self.width}: {area_value}"
        )
        return area_value

    def perimeter(self):
        perimeter_value = (self.length * 2) + (self.width * 2)
        logger.debug(
            f"Calculating perimeter for Rectangle with length {self.length} and width {self.width}: {perimeter_value}"
        )
        return perimeter_value


class Square(Shape):
    def __init__(self, length):
        self.length = length
        logger.debug(f"Square created with length: {length}")

    def __eq__(self, other):
        if not isinstance(other, Square):
            return False
        return self.length == other.length

    def area(self):
        area_value = self.length**2
        logger.debug(
            f"Calculating area for Square with length {self.length}: {area_value}"
        )
        return area_value

    def perimeter(self):
        perimeter_value = self.length * 4
        logger.debug(
            f"Calculating perimeter for Square with length {self.length}: {perimeter_value}"
        )
        return perimeter_value
