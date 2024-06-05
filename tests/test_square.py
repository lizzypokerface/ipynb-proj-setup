import pytest

from my_project.shapes.shapes import Square


@pytest.mark.parametrize("length, expected_area", [(2, 4), (3, 9), (4, 16)])
def test_area(length, expected_area):
    assert Square(length).area() == expected_area


@pytest.mark.parametrize("length, expected_perimeter", [(2, 8), (3, 12), (4, 16)])
def test_perimeter(length, expected_perimeter):
    assert Square(length).perimeter() == expected_perimeter
