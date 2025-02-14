# List Comprehensions in Python 

# Basic List Comprehension
# This creates a new list where each element is squared.
numbers = [1, 2, 3, 4, 5]
squared_numbers = [x ** 2 for x in numbers]  # Squaring each number in the list
print("Squared Numbers:", squared_numbers)

# List Comprehension with a Condition
# This filters out only even numbers from the list.
even_numbers = [x for x in numbers if x % 2 == 0]
print("Even Numbers:", even_numbers)

# Using List Comprehension with an if-else Condition
# This creates a new list where even numbers remain the same and odd numbers are doubled.
modified_numbers = [x if x % 2 == 0 else x * 2 for x in numbers]
print("Modified Numbers:", modified_numbers)

# Nested List Comprehension
# This flattens a 2D list (list of lists) into a single list.
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print("Flattened List:", flattened)

# List Comprehension with Function Calls
# This converts a list of strings to uppercase.
names = ["alice", "bob", "charlie"]
uppercase_names = [name.upper() for name in names]
print("Uppercase Names:", uppercase_names)

# Dictionary Comprehension
# This creates a dictionary with numbers as keys and their squares as values.
squares_dict = {x: x ** 2 for x in range(1, 6)}
print("Squares Dictionary:", squares_dict)

# Set Comprehension
# This removes duplicates and squares each number.
numbers_with_duplicates = [1, 2, 2, 3, 4, 4, 5]
squared_set = {x ** 2 for x in numbers_with_duplicates}
print("Squared Set:", squared_set)

# Generator Comprehension
# This creates a generator that lazily computes squared values.
gen = (x ** 2 for x in range(1, 6))
print("Generated Squared Values:", list(gen))  # Converting generator to list for display
