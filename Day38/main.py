import os

# Basic Syntax and Variables
name = input("Enter your name: ")
age = int(input("Enter your age: "))

# Control Structures
if age < 18:
    print(f"Hello {name}, you are a minor.")
else:
    print(f"Hello {name}, you are an adult.")

# Data Structures: List, Tuple, Dictionary, and Set
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(f"List of fruits: {fruits}")

coordinates = (10.0, 20.0)
print(f"Coordinates: {coordinates}")

person = {"name": name, "age": age, "location": "unknown"}
print(f"Person details: {person}")

unique_numbers = {1, 2, 3, 2, 1}
print(f"Unique numbers: {unique_numbers}")

# Functions
def greet_user(name, age):
    if age < 18:
        return f"Hello {name}, you are a minor."
    else:
        return f"Hello {name}, you are an adult."

greeting_message = greet_user(name, age)
print(greeting_message)

# File Handling
file_path = "user_data.txt"

# Writing to a file
with open(file_path, "w") as file:
    file.write(f"Name: {name}\n")
    file.write(f"Age: {age}\n")
    file.write(greeting_message)

# Reading from a file
with open(file_path, "r") as file:
    content = file.read()
    print(f"File content:\n{content}")

# Error Handling
try:
    os.remove("non_existent_file.txt")
except FileNotFoundError as e:
    print(f"Error: {e}")

# Mini Project: Simple Contact Book
contacts = {}

def add_contact(name, phone):
    contacts[name] = phone

def view_contacts():
    for name, phone in contacts.items():
        print(f"{name}: {phone}")

def save_contacts(file_path):
    with open(file_path, "w") as file:
        for name, phone in contacts.items():
            file.write(f"{name}: {phone}\n")

def load_contacts(file_path):
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            for line in file:
                name, phone = line.strip().split(": ")
                contacts[name] = phone

# Adding and Viewing Contacts
add_contact("Alice", "123-456-7890")
add_contact("Bob", "987-654-3210")
view_contacts()

# Saving and Loading Contacts
contact_file = "contacts.txt"
save_contacts(contact_file)
contacts.clear()
load_contacts(contact_file)
view_contacts()
