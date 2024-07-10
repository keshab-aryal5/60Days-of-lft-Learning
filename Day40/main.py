# Importing Libraries
import math
import random
import datetime

# Functions and Basics
def greet(name):
    return f"Hello, {name}!"

print(greet("World"))

# Data Types and Variables
integer_var = 10
float_var = 10.5
string_var = "Python"
boolean_var = True

print(f"Integer: {integer_var}, Float: {float_var}, String: {string_var}, Boolean: {boolean_var}")

# Lists
fruits = ["Apple", "Banana", "Cherry"]
fruits.append("Date")
print(f"Fruits List: {fruits}")

# Loops
for fruit in fruits:
    print(fruit)

# Conditional Statements
number = random.randint(1, 10)
if number > 5:
    print(f"{number} is greater than 5")
else:
    print(f"{number} is 5 or less")

# Dictionary
student = {
    "name": "John",
    "age": 20,
    "courses": ["Math", "Science"]
}
print(f"Student Info: {student}")

# Working with Strings
sentence = "Python is amazing"
words = sentence.split()
print(f"Words in sentence: {words}")

# Functions
def calculate_area(radius):
    return math.pi * radius ** 2

print(f"Area of circle with radius 5: {calculate_area(5)}")

# Classes and Objects
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def make_sound(self):
        return f"{self.name} says Hello!"

dog = Animal("Buddy", "Dog")
print(dog.make_sound())

# Handling Exceptions
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")

# File I/O
with open("sample.txt", "w") as file:
    file.write("Hello, file!")

# Reading File
with open("sample.txt", "r") as file:
    content = file.read()
    print(f"File Content: {content}")

# Working with Dates
current_date = datetime.datetime.now()
print(f"Current Date and Time: {current_date}")

# List Comprehensions
squares = [x ** 2 for x in range(10)]
print(f"Squares: {squares}")

# Working with Modules
print(f"Square root of 16 is: {math.sqrt(16)}")

# Lambda Functions
add = lambda x, y: x + y
print(f"Sum of 5 and 3: {add(5, 3)}")

# Generators
def countdown(num):
    while num > 0:
        yield num
        num -= 1

for i in countdown(5):
    print(i)

# Decorators
def uppercase_decorator(func):
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result
    return wrapper

@uppercase_decorator
def greet_decorated():
    return "Hello, decorated function!"

print(greet_decorated())

# Using Zip
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
combined = list(zip(names, ages))
print(f"Combined List: {combined}")

# Sets
unique_numbers = {1, 2, 2, 3, 4, 5, 5}
print(f"Unique Numbers: {unique_numbers}")

# Nested Functions
def outer_function(msg):
    def inner_function():
        print(msg)
    return inner_function

inner_func = outer_function("Hello from inner function")
inner_func()

# Map and Filter
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(f"Squared Numbers: {squared_numbers}")

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even Numbers: {even_numbers}")
