# Time and Space Complexity Examples

import time

def constant_time_example(arr):
    # O(1) - Constant Time: Accessing an element by index takes the same time regardless of input size
    return arr[0] if arr else None  # Returns the first element if the list is not empty


def linear_time_example(arr):
    # O(n) - Linear Time: Iterates through the entire list, taking time proportional to its size
    for item in arr:
        print(item)  # Prints each element in the array


def quadratic_time_example(arr):
    # O(n^2) - Quadratic Time: Nested loops result in a time complexity of n squared
    for i in arr:
        for j in arr:
            print(i, j)  # Prints all pairs of elements


def logarithmic_time_example(arr, target):
    # O(log n) - Logarithmic Time: Binary search reduces problem size in half each step
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def binary_search(arr, target):
    # O(log n) - Binary Search: A recursive implementation
    def search(left, right):
        if left > right:
            return -1
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return search(mid + 1, right)
        else:
            return search(left, mid - 1)
    return search(0, len(arr) - 1)


def factorial_time_example(n):
    # O(n!) - Factorial Time: Very slow growth due to recursive calls increasing exponentially
    if n == 0:
        return 1
    return n * factorial_time_example(n - 1)


def exponential_time_example(n):
    # O(2^n) - Exponential Time: Grows rapidly with input size, common in recursive problems
    if n <= 1:
        return n
    return exponential_time_example(n - 1) + exponential_time_example(n - 2)


def cubic_time_example(arr):
    # O(n^3) - Cubic Time: Triple nested loop leading to cubic growth
    for i in arr:
        for j in arr:
            for k in arr:
                print(i, j, k)


# Space Complexity Examples

def space_constant_example():
    # O(1) - Constant Space: Uses a fixed amount of memory regardless of input size
    x = 10  # Single integer variable
    return x


def space_linear_example(n):
    # O(n) - Linear Space: Creates a list of size 'n', requiring memory proportional to 'n'
    arr = [i for i in range(n)]  # List comprehension to create an array of size n
    return arr


def space_quadratic_example(n):
    # O(n^2) - Quadratic Space: Creates an n x n matrix, requiring n squared space
    matrix = [[0] * n for _ in range(n)]  # 2D list (matrix) of size n x n
    return matrix


def measure_execution_time(func, *args):
    # Helper function to measure execution time of a given function
    start = time.time()
    result = func(*args)
    end = time.time()
    print(f"Execution time for {func.__name__}: {end - start:.6f} seconds")
    return result


# Example usage
arr = [1, 2, 3, 4, 5]
measure_execution_time(constant_time_example, arr)
measure_execution_time(linear_time_example, arr)
measure_execution_time(quadratic_time_example, arr)
measure_execution_time(logarithmic_time_example, sorted(arr), 3)
measure_execution_time(binary_search, sorted(arr), 3)
measure_execution_time(factorial_time_example, 5)
measure_execution_time(exponential_time_example, 5)
measure_execution_time(cubic_time_example, arr)

measure_execution_time(space_constant_example)
measure_execution_time(space_linear_example, 5)
measure_execution_time(space_quadratic_example, 5)
