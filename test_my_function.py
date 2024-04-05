import pytest
import time
from my_functions import add, multiply, divide


# pytest <File path> used for normal test running
# pytest <File path> -s used to see results of each test
# pytest <File path> -m <mark> used to run tests with specified mark

def test_add():
    assert add(4, 5) == 9


def test_multiply():
    assert multiply(4, 5) == 20


def test_multiply_fail():  # Will fail
    assert multiply(4, 5) == 29


@pytest.mark.xfail(reason="Will throw zero error")
def test_divide_fail():  # Will fail
    assert multiply(4, 0) == 0


def test_divide():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)  # Zero error is expected


@pytest.mark.slow  # Marks test as a slow test
def test_very_slow():
    time.sleep(5)
    assert divide(10, 5) == 2


@pytest.mark.skip  # Test will be skipped
def test_add_broken(reason="Broken test"):
    assert add(3, 2) == 6
