import pytest
import math

from shapes import Circle


# Class based testing
class TestCircle:  # Needs this syntax
    def setup_method(self, method):
        self.circle = Circle(10)  # Makes circle to be used in all tests

    def teardown_method(self, method):
        del self.circle  # Deletes circle after all tests completed

    def test_area(self):
        assert self.circle.area() == math.pi * self.circle.radius ** 2

    def test_perimeter(self):
        assert self.circle.perimeter() == 2 * math.pi * self.circle.radius

    def test_different(self, my_rectangle):
        assert self.circle.area() != my_rectangle.area()
