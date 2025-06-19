from array_list import ArrayList

lst = ArrayList()

print("Appending elements: a, b, c")
lst.append('a')
lst.append('b')
lst.append('c')
print(f"List length: {lst.length()}")  # 3

print("Inserting 'x' at position 1")
lst.insert('x', 1)
print(f"Element at index 1: {lst.get(1)}")  # x

print("Deleting element at index 2")
removed = lst.delete(2)
print(f"Removed element: {removed}")

print("Deleting all 'a'")
lst.deleteAll('a')
print(f"List length after deleteAll: {lst.length()}")

print("Finding first and last index of 'b'")
print(lst.findFirst('b'))  # should return index or -1
print(lst.findLast('b'))   # should return index or -1

print("Cloning list")
copy = lst.clone()
print(f"Original length: {lst.length()}, Clone length: {copy.length()}")

print("Reversing clone")
copy.reverse()
print("Extending original with reversed clone")
lst.extend(copy)
print(f"Final length: {lst.length()}")

print("Clearing list")
lst.clear()
print(f"Length after clear: {lst.length()}")
