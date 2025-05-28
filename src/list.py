# Creating a list
# Creating a list
my_list = [1, 2, 3, 4, 5]
print("Original list:", my_list)

# Accessing elements
print("First element:", my_list[0])  # Indexing starts at 0
print("Last element:", my_list[-1])  # Negative indexing

# Adding elements
my_list.append(6)  # Adds 6 to the end of the list
print("After appending 6:", my_list)

my_list.insert(2, 99)  # Inserts 99 at index 2
print("After inserting 99 at index 2:", my_list)

# Removing elements
my_list.remove(3)  # Removes the first occurrence of 3
print("After removing 3:", my_list)

popped_element = my_list.pop()  # Removes and returns the last element
print("After popping an element:", my_list)
print("Popped element:", popped_element)

# Slicing a list
sub_list = my_list[1:4]  # Gets elements from index 1 to 3 (4 is excluded)
print("Sliced list (index 1 to 3):", sub_list)

# Iterating through a list
print("Iterating through the list:")
for item in my_list:
    print(item)

# Creating a Python list with different data types
a = [10, 20, "GfG", 40, True]

print(a)

# Checking types of elements
print(type(a[2]))  # str, as "GfG" is a string
print(type(a[4]))  # bool, as True is a boolean

# Noted: Lists Store References, Not Values
# In Python, lists store references to objects, not the actual values.
# This means that if a mutable object (e.g., a list or dictionary) inside a list is modified,
# the change will be reflected in all references to that object.
mutable_object = [1, 2, 3]
list_with_reference = [mutable_object, 4, 5]
print("Before modification:", list_with_reference)

# Modify the mutable object
mutable_object.append(6)
print("After modification:", list_with_reference)

a = [2] * 5
print(a)  # Output: [2, 2, 2, 2, 2]

# Lists can contain other lists
nested_list = [1, 2, [3] * 5, 5]
print(nested_list)  # Output: [1, 2, [3, 3, 3, 3, 3], 5]

b = [1, 2, 3, "B", 5.5, True]

# Compare 2 list
print(a == b)

# Extend list
print("Original list b:", b)
a = b.extend([6, 7, 8])  # Extends list b with new elements
print("After extending b with [6, 7, 8]:", b)

#Nested list
nested_list = [[1, 2], [3, 4], [5, 6]]
# Accessing elements in a nested list
print("First element of first sub-list:", nested_list[0][0])  # Output: 1
print("Second element of second sub-list:", nested_list[1][1])  # Output: 4

# List Traversal
for sublist in nested_list:
    for item in sublist:
        print(item, end=' ')  # Output: 1 2 3 4 5 6
print()

# List Comprehension
s = [x**2 for x in range(10)]  # Creates a list of squares from 0 to 9
print("List of squares from 0 to 9:", s)

# List comprehension with condition
even_squares = [x**2 for x in range(10) if x % 2 == 0] # Squares of even numbers
not_even_squares = [x**2 for x in range(10) if x % 2 != 0] # Squares of odd numbers
print("Squares of odd numbers from 0 to 9:", not_even_squares)
print("Squares of even numbers from 0 to 9:", even_squares)


arr =  [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = [str(item) for index, item in enumerate(arr) if index % 2 == 0]
print(" ".join(result))  # Output: 1 3 5 7 9