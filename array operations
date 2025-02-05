import numpy as np

# Generate a random array
a = np.random.randint(5, 9, (2, 4))
print(a)

# Sum of the array
print(np.sum(a))
print(np.sum(a, axis=0))
print(np.sum(a, axis=1))

# Calculate minimum
print(np.min(a))
print(np.min(a, axis=1))  # Across columns

# Sort the array
a = np.random.randint(0, 20, (3, 3))
print(a)

# Sort in ascending order
print(np.sort(a, axis=0))  # Ascending by columns
print(np.sort(a, axis=1))  # Ascending by rows

# Sort in descending order
print(-np.sort(-a, axis=1))  # Descending by rows

# Matrix operations
b = np.array([[14, 4, 2],
              [17, 11, 1],
              [15, 15, 13]])

# Sum of element-wise multiplication
print(np.sum(np.arange(3) * np.arange(3).transpose()))
