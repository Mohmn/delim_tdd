# test_app.py
# import pytest
from app.main import add


# int add(string numbers)
def test_add():
    assert add("") == 0
    assert add("1") == 1
    assert add("1,2,3") == 6
