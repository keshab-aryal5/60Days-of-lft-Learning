# Variables and Data Types
name = "John Doe"
age = 25
height = 5.9
is_student = True

print(f"Name: {name}, Age: {age}, Height: {height}, Is Student: {is_student}")

# List
fruits = ["apple", "banana", "cherry"]
print(fruits)

# Tuple
point = (10, 20)
print(point)

# Set
unique_numbers = {1, 2, 3, 3, 2, 1}
print(unique_numbers)

# Dictionary
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
print(person)

# Control Structures
# If-Else
if age > 18:
    print("Adult")
else:
    print("Minor")

# For Loop
for fruit in fruits:
    print(fruit)

# While Loop
count = 0
while count < 5:
    print(count)
    count += 1

# Functions
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))

# Lambda Functions
square = lambda x: x * x
print(square(5))

# List Comprehension
squares = [x * x for x in range(10)]
print(squares)

# Classes and Objects
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says Woof!"

dog = Dog("Buddy", 3)
print(dog.bark())

# Modules and Packages
import math
print(math.sqrt(16))

# File I/O
with open("example.txt", "w") as file:
    file.write("Hello, World!")

with open("example.txt", "r") as file:
    content = file.read()
    print(content)

# Error Handling
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("Execution completed.")

# Advanced Concepts
# Map, Filter, Reduce
from functools import reduce

numbers = [1, 2, 3, 4, 5]

mapped_numbers = list(map(lambda x: x * 2, numbers))
filtered_numbers = list(filter(lambda x: x % 2 == 0, numbers))
reduced_number = reduce(lambda x, y: x + y, numbers)

print(mapped_numbers)
print(filtered_numbers)
print(reduced_number)

# Decorators
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

# Generators
def simple_generator():
    yield 1
    yield 2
    yield 3

gen = simple_generator()
for value in gen:
    print(value)

# Context Managers
class MyContextManager:
    def __enter__(self):
        print("Entering the context.")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting the context.")

with MyContextManager():
    print("Inside the context.")

# Conclusion
print("This program demonstrates a variety of Python concepts.")
