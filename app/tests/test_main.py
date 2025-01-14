# test_app.py
# import pytest
from app.main import add


# int add(string numbers)
def test_add():
    assert add("") == 0
    assert add("1") == 1
    assert add("1,2,3") == 6
    assert add("1\n2,3") == 6
    assert add("//[*][%]\n1*2%3") == 6
    assert add("//[***][%]\n1***2%3%4") == 10
    assert add("//[>][%]\n1>2%3%4") == 10
