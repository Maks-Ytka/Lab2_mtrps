import pytest
from array_list import ArrayList

def test_append_and_length():
    lst = ArrayList()
    assert lst.length() == 0
    lst.append('a')
    lst.append('b')
    assert lst.length() == 2

def test_get_valid_index():
    lst = ArrayList()
    lst.append('x')
    assert lst.get(0) == 'x'

def test_get_invalid_index():
    lst = ArrayList()
    lst.append('z')
    with pytest.raises(IndexError):
        lst.get(1)
