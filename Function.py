# Function definition
def greet(name):
    """
    This function takes a name as input and prints a greeting message.
    """
    print("Hello, " + name + "! Welcome to Python.")

# Function call
greet("Kaushik")  # Output: Hello, Kaushik! Welcome to Python.


# Function with return value
def add(a, b):
    """
    This function takes two numbers as input and returns their sum.
    """
    return a + b

# Storing and printing the result
result = add(5, 3)
print("Sum:", result)  # Output: Sum: 8


# Default parameter values
def power(base, exponent=2):
    """
    This function calculates the power of a number.
    If the exponent is not provided, it defaults to 2.
    """
    return base ** exponent

print(power(4))     # Output: 16 (4^2)
print(power(4, 3))  # Output: 64 (4^3)


# Function with variable-length arguments (*args)
def multiply(*numbers):
    """
    This function takes multiple numbers as arguments and returns their product.
    """
    product = 1
    for num in numbers:
        product *= num
    return product

print(multiply(2, 3, 4))  # Output: 24 (2*3*4)


# Function with keyword arguments (**kwargs)
def introduce(**info):
    """
    This function takes keyword arguments and prints user information.
    """
    for key, value in info.items():
        print(f"{key}: {value}")

introduce(name="Kaushik", age=25, city="New York")
# Output:
# name: Kaushik
# age: 25
# city: New York


# Lambda function (anonymous function)
square = lambda x: x ** 2
print(square(5))  # Output: 25 (5^2)


# Nested function
def outer():
    """
    This function contains a nested function.
    """
    def inner():
        return "Inner function called!"
    return inner()

print(outer())  # Output: Inner function called!


# Function as an argument
def apply_function(func, value):
    """
    This function takes another function as an argument and applies it.
    """
    return func(value)

def cube(x):
    return x ** 3

print(apply_function(cube, 3))  # Output: 27 (3^3)


# Method in a class
class Person:
    """
    This class represents a person with a name.
    """
    def __init__(self, name):
        self.name = name
    
    def greet(self):
        """
        Method to greet the person.
        """
        return f"Hello, my name is {self.name}."

# Creating an object
p = Person("Kaushik")
print(p.greet())  # Output: Hello, my name is Kaushik.
