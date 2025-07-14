fruits = ["Apples", "Bananas", "cherry", "Strawberry"]

fruits.append("Kiwi")
print(fruits)

# Output: ['Apples', 'Bananas', 'cherry', 'Strawberry', 'Kiwi']
# The append() method adds an item to the end of the list.

fruits.insert(1, "Orange")
print(fruits)

# Output: ['Apples', 'Orange', 'Bananas', 'cherry', 'Strawberry', 'Kiwi']
# The insert() method adds an item at the specified index.

fruits.remove("Bananas")
print(fruits)

# Output: ['Apples', 'Orange', 'cherry', 'Strawberry', 'Kiwi']
# The remove() method removes the first occurrence of a specified value.

fruits.sort()
print(fruits)

# Output: ['Apples', 'Kiwi', 'Orange', 'Strawberry', 'cherry']
# The sort() method sorts the list in ascending order.