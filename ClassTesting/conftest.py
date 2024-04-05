# Global file to create fixtures for all tests in directory, must be called conftest.py

import pytest
from shapes import Rectangle


# Fixture based testing

@pytest.fixture
def my_rectangle():  # Rectangle returned now used in other tests
    return Rectangle(10, 20)


@pytest.fixture
def weird_rectangle():
    return Rectangle(5, 6)
