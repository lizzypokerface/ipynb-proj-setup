import time

import pytest

from my_project.my_functions.my_functions import add, divide, multiply


def test_add():
    result = add(1, 4)
    assert result == 5


def test_add_strings():
    with pytest.raises(TypeError):
        add("I like", "burgers")


def test_divide():
    result = divide(10, 5)
    assert result == 2


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)


@pytest.mark.slow
def test_very_slow():
    time.sleep(2)
    result = divide(10, 5)
    assert result == 2


@pytest.mark.skip(reason="This feature is currently broken")
def test_multiply_broken():
    result = multiply(5, 4)
    assert result == 20


@pytest.mark.xfail(reason="We know we cannot divide by zero")
def test_divide_zero_broken():
    result = divide(10, 0)
    assert result == '?'
