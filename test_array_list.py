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

def test_insert_and_delete():
    lst = ArrayList()
    lst.append('a')
    lst.append('c')
    lst.insert('b', 1)
    assert lst.get(1) == 'b'
    removed = lst.delete(1)
    assert removed == 'b'
    assert lst.length() == 2

def test_insert_invalid_index():
    lst = ArrayList()
    with pytest.raises(IndexError):
        lst.insert('x', 5)

def test_delete_invalid_index():
    lst = ArrayList()
    with pytest.raises(IndexError):
        lst.delete(0)

def test_deleteAll():
    lst = ArrayList()
    for c in ['a', 'b', 'a', 'c']:
        lst.append(c)
    lst.deleteAll('a')
    assert lst.length() == 2
    assert lst.get(0) == 'b'

def test_findFirst_and_findLast():
    lst = ArrayList()
    for c in ['x', 'y', 'x', 'z']:
        lst.append(c)
    assert lst.findFirst('x') == 0
    assert lst.findLast('x') == 2
    assert lst.findFirst('q') == -1

def test_clone_independence():
    lst = ArrayList()
    lst.append('a')
    copy = lst.clone()
    copy.append('b')
    assert lst.length() == 1
    assert copy.length() == 2

def test_clear():
    lst = ArrayList()
    lst.append('a')
    lst.clear()
    assert lst.length() == 0

def test_reverse():
    lst = ArrayList()
    for c in ['a', 'b', 'c']:
        lst.append(c)
    lst.reverse()
    assert lst.get(0) == 'c'
    assert lst.get(1) == 'b'
    assert lst.get(2) == 'a'

def test_extend():
    lst1 = ArrayList()
    lst2 = ArrayList()
    lst1.append('x')
    lst2.append('y')
    lst1.extend(lst2)
    assert lst1.length() == 2
    assert lst1.get(1) == 'y'
    lst2.append('z')
    assert lst1.length() == 2  # lst1 should not be affected by lst2
