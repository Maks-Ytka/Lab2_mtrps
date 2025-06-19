class ArrayList:
    def __init__(self):
        self.data = []

    def length(self):
        return len(self.data)

    def append(self, element):
        self.data.append(element)

    def get(self, index):
        if index < 0 or index >= len(self.data):
            raise IndexError("Index out of bounds")
        return self.data[index]

    def insert(self, element, index):
        if index < 0 or index > len(self.data):
            raise IndexError("Index out of bounds")
        self.data.insert(index, element)

    def delete(self, index):
        if index < 0 or index >= len(self.data):
            raise IndexError("Index out of bounds")
        return self.data.pop(index)

    def deleteAll(self, element):
        self.data = [x for x in self.data if x != element]

    def findFirst(self, element):
        for i, val in enumerate(self.data):
            if val == element:
                return i
        return -1

    def findLast(self, element):
        for i in range(len(self.data) - 1, -1, -1):
            if self.data[i] == element:
                return i
        return -1
