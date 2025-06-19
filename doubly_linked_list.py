class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._length = 0

    def length(self):
        return self._length

    def append(self, element):
        new_node = Node(element)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self._length += 1

    def get(self, index):
        if index < 0 or index >= self._length:
            raise IndexError("Index out of bounds")
        current = self.head
        for _ in range(index):
            current = current.next
        return current.value

    def insert(self, element, index):
        if index < 0 or index > self._length:
            raise IndexError("Index out of bounds")

        new_node = Node(element)

        if index == self._length:
            self.append(element)
            return

        if index == 0:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        else:
            current = self.head
            for _ in range(index):
                current = current.next
            prev_node = current.prev

            prev_node.next = new_node
            new_node.prev = prev_node

            new_node.next = current
            current.prev = new_node

        self._length += 1

    def delete(self, index):
        if index < 0 or index >= self._length:
            raise IndexError("Index out of bounds")

        if index == 0:
            value = self.head.value
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None
        elif index == self._length - 1:
            value = self.tail.value
            self.tail = self.tail.prev
            if self.tail:
                self.tail.next = None
            else:
                self.head = None
        else:
            current = self.head
            for _ in range(index):
                current = current.next
            value = current.value
            current.prev.next = current.next
            current.next.prev = current.prev

        self._length -= 1
        return value

    def deleteAll(self, element):
        current = self.head
        while current:
            if current.value == element:
                next_node = current.next
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                self._length -= 1
                current = next_node
            else:
                current = current.next

    def clone(self):
        new_list = DoublyLinkedList()
        current = self.head
        while current:
            new_list.append(current.value)
            current = current.next
        return new_list

    def reverse(self):
        current = self.head
        self.head, self.tail = self.tail, self.head
        while current:
            current.prev, current.next = current.next, current.prev
            current = current.prev

    def findFirst(self, element):
        current = self.head
        index = 0
        while current:
            if current.value == element:
                return index
            current = current.next
            index += 1
        return -1

    def findLast(self, element):
        current = self.tail
        index = self._length - 1
        while current:
            if current.value == element:
                return index
            current = current.prev
            index -= 1
        return -1

    def clear(self):
        self.head = None
        self.tail = None
        self._length = 0

    def extend(self, other):
        if not isinstance(other, DoublyLinkedList):
            raise TypeError("extend expects a DoublyLinkedList")
        current = other.head
        while current:
            self.append(current.value)
            current = current.next
