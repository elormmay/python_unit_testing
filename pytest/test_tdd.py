"""Trying TTD"""
# all test are written before the function
# used pytest.mark to group tests. a pytest.ini file created in  rootdir shows the custom markers
import pytest
from tdd import (
    add,
    display_message,
    show_message,
    check_length,
    divide,
    custom_num_list,
    custom_func,
)


class TestCase:
    @pytest.mark.calc
    def test_add(self):
        assert add(2, 3) == 5
        assert add(-1, -1) == -2
        assert add(-2, 1) == -1

    @pytest.mark.messages
    def test_display_message(self):
        assert display_message() == "Message works!"

    @pytest.mark.messages
    def test_show_message(self):
        assert show_message("Hello") == "Hello"

    @pytest.mark.calc
    def test_check_length(self):
        assert check_length("hello") == 5

    @pytest.mark.calc
    def test_division(self):
        # valueError will be raised thus this test passes
        with pytest.raises(ValueError):
            assert divide(4, 0) == 2

    @pytest.mark.skip
    def test_custom_num_list(self):
        assert len(custom_num_list(10)) == 10

    @pytest.mark.xfail
    def test_custom_func(self):
        assert custom_func(3, 2, 4) == 27

    def test_hello(self):
        assert "hello" in "hello is", "No it"

