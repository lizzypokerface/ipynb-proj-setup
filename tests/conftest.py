import pytest

from my_project.shapes.shapes import Circle, Rectangle


# Global fixtures


@pytest.fixture
def circle():
    return Circle(10)


@pytest.fixture
def rectangle():
    return Rectangle(10, 20)
