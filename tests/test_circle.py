import math

from my_project.shapes.shapes import Circle


class TestCircle:

    # https: // docs.pytest.org / en / 6.2.x / xunit_setup.html

    def setup_method(self, method):
        print(f"Setting up {method}")
        self.circle = Circle(10)

    def teardown_method(self, method):
        print(f"Tearing down {method}")

    def test_radius(self):
        assert self.circle.radius == 10

    def test_area(self):
        assert self.circle.area() == (math.pi * 10 ** 2)

    def test_perimeter(self):
        assert self.circle.perimeter() == (2 * math.pi * 10)

    def test_equals(self, circle):
        assert self.circle == circle

    def test_dimensions_not_equals(self, rectangle):
        assert self.circle != Circle(5)

    def test_instance_not_equals(self, rectangle):
        assert self.circle != rectangle
