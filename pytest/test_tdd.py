"""Trying TTD"""
# all test are written before the function
import pytest
from tdd import add, display_message, show_message, check_length, divide


class TestCase:
    def test_add(self):
        assert add(2, 3) == 5
        assert add(-1, -1) == -2
        assert add(-2, 1) == -1

    def test_display_message(self):
        assert display_message() == "Message works!"

    def test_show_message(self):
        assert show_message("Hello") == "Hello"

    def test_check_length(self):
        assert check_length("hello") == 5

    def test_division(self):
        # valueError will be raise thus this test passes
        with pytest.raises(ValueError):
            assert divide(4, 0) == 2
