import pytest

from my_project.shapes.shapes import Rectangle


# Local fixture


@pytest.fixture
def different_rectangle():
    return Rectangle(1, 2)


class TestRectangle:
    def test_area(self, rectangle):
        assert rectangle.area() == (10 * 20)

    def test_perimeter(self, rectangle):
        assert rectangle.perimeter() == (10 + 20) * 2

    def test_equals(self, rectangle):
        assert rectangle == Rectangle(10, 20)

    def test_dimensions_not_equals(self, rectangle, different_rectangle):
        assert rectangle != different_rectangle

    def test_instance_not_equals(self, rectangle, circle):
        assert rectangle != circle
