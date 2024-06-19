# 1. Lambda Functions
# Definition
# A lambda function is a small anonymous function defined with the lambda keyword. It can have any number of arguments but only one expression. Lambda functions are used when you need a simple function for a short period and don't want to formally define it using def.

# Regular function
def add(x, y):
    return x + y

# Lambda function
add_lambda = lambda x, y: x + y

print(add(2, 3))  # Output: 5
print(add_lambda(2, 3))  # Output: 5


# 2. Generators
# Definition
# Generators are a type of iterable, like lists or tuples, but instead of storing all the values in memory, they generate the values on the fly. Generators are defined using functions and the yield statement.

# Code Example
# Generator function
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Using the generator
for num in fibonacci(10):
    print(num, end=" ")  # Output: 0 1 1 2 3 5 8 13 21 34



# 3. Decorators
# Definition
# Decorators are a way to modify or extend the behavior of functions or methods without permanently modifying them. They are often used for logging, access control, instrumentation, or caching.

# Code Example
def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print(f"Wrapper executed this before {original_function.__name__}")
        return original_function(*args, **kwargs)
    return wrapper_function

@decorator_function
def display():
    print("Display function ran")

display()
# Output:
# Wrapper executed this before display
# Display function ran


# 4. List Comprehensions
# Definition
# List comprehensions provide a concise way to create lists. They consist of brackets containing an expression followed by a for clause and can also include if clauses.
# Code Example
# Regular way to create a list
squares = []
for x in range(10):
    squares.append(x**2)

# List comprehension
squares_comprehension = [x**2 for x in range(10)]

print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares_comprehension)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]



# 5. Context Managers
# Definition
# Context managers allow you to allocate and release resources precisely when you want to. The most common use of context managers is with the with statement.

# Code Example
# Using a context manager with the 'with' statement
with open('example.txt', 'w') as file:
    file.write('Hello, world!')

# Custom context manager using a class
class MyContextManager:
    def __enter__(self):
        print("Enter the context")
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        print("Exit the context")
        
    def do_something(self):
        print("Doing something")

with MyContextManager() as manager:
    manager.do_something()
# Output:
# Enter the context
# Doing something
# Exit the context
