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
