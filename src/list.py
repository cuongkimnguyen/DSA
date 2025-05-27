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
print(type(a[2]))  # str
print(type(a[4]))  # bool    