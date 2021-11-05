"""Trying TTD"""
# all test are written before the function

from tdd import add, display_message


def test_add():
    assert add(2, 3) == 5


def test_message():
    assert display_message() == "Message works!"
