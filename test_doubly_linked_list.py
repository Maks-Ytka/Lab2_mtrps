import pytest
from doubly_linked_list import DoublyLinkedList

def test_append_and_length():
    dll = DoublyLinkedList()
    assert dll.length() == 0
    dll.append('a')
    dll.append('b')
    assert dll.length() == 2

def test_get_valid():
    dll = DoublyLinkedList()
    dll.append('x')
    assert dll.get(0) == 'x'

def test_get_invalid():
    dll = DoublyLinkedList()
    dll.append('z')
    with pytest.raises(IndexError):
        dll.get(2)

def test_insert_and_delete():
    dll = DoublyLinkedList()
    dll.append('a')
    dll.append('c')
    dll.insert('b', 1)
    assert dll.get(1) == 'b'
    deleted = dll.delete(1)
    assert deleted == 'b'
    assert dll.length() == 2

def test_insert_invalid():
    dll = DoublyLinkedList()
    with pytest.raises(IndexError):
        dll.insert('x', 5)

def test_delete_invalid():
    dll = DoublyLinkedList()
    with pytest.raises(IndexError):
        dll.delete(0)

def test_deleteAll():
    dll = DoublyLinkedList()
    for char in ['a', 'b', 'a', 'c', 'a']:
        dll.append(char)
    dll.deleteAll('a')
    assert dll.length() == 2
    assert dll.get(0) == 'b'
    assert dll.get(1) == 'c'

def test_clone_and_independence():
    dll = DoublyLinkedList()
    dll.append('a')
    copy = dll.clone()
    copy.append('b')
    assert dll.length() == 1
    assert copy.length() == 2

def test_reverse():
    dll = DoublyLinkedList()
    for c in ['a', 'b', 'c']:
        dll.append(c)
    dll.reverse()
    assert dll.get(0) == 'c'
    assert dll.get(2) == 'a'

def test_findFirst_and_findLast():
    dll = DoublyLinkedList()
    for c in ['x', 'y', 'x', 'z']:
        dll.append(c)
    assert dll.findFirst('x') == 0
    assert dll.findLast('x') == 2
    assert dll.findFirst('q') == -1

def test_clear():
    dll = DoublyLinkedList()
    dll.append('a')
    dll.clear()
    assert dll.length() == 0

def test_extend():
    dll1 = DoublyLinkedList()
    dll2 = DoublyLinkedList()
    dll1.append('a')
    dll2.append('b')
    dll1.extend(dll2)
    assert dll1.length() == 2
    assert dll1.get(1) == 'b'
