import pytest


@pytest.fixture
def numbers():
    a = 10
    b = 20
    c = 25

    return [a, b, c]


def test_method1(numbers):
    x = 11
    assert numbers[0] == x
