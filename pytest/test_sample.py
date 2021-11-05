# content of text_sample.py
import pytest
from sample import inc, sys_exit


def test_inc():
    assert inc(4) == 5


# using context manager
def test_sys_exit():
    with pytest.raises(SystemExit):
        sys_exit()

