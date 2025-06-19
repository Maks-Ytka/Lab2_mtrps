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
