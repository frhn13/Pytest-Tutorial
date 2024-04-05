import pytest
from shapes import Square


# Contains parameters for multiple different test cases to run through
@pytest.mark.parametrize("side_length, expected_area", [(5, 25), (4, 16), (3, 9)])
def test_multiple_square_areas(side_length, expected_area):
    assert Square(side_length).area() == expected_area


@pytest.mark.parametrize("side_length, expected_perimeter", [(5, 20), (4, 16), (3, 12)])
def test_multiple_square_perimeters(side_length, expected_perimeter):
    assert Square(side_length).perimeter() == expected_perimeter
