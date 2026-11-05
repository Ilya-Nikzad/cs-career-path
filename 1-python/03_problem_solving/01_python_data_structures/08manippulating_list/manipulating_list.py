# Task 1: Concatenation list
A_list = [1,2,3]
B_list = [4,5,6]
print(A_list + B_list)

# Task 2: Slicing list
slice_list = A_list[:2]
print(slice_list)

# Task 3: List Methods (Built-in Actions)

A = colors = ["red", "blue", "red", "green", "red"]

print("Original list:", A)

# append() → add one item at end
A.append(5)
print("After append:", A)

# count() → count occurrences of 2
print("Count of 2:", A.count(2))

# len() → total number of items
print("Length of list:", len(A))

# extend() → add multiple items
A.extend([6, 7])
print("After extend:", A)

# index() → find position of value 3
print("Index of 3:", A.index("red"))

# insert() → add 100 at position 1
A.insert(1, 100)
print("After insert:", A)

# pop() → remove last item
A.pop()
print("After pop:", A)

# remove() → remove first occurrence of 2
A.remove("red")
print("After remove:", A)
