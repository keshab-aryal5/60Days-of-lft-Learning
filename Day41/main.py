# Using map() to apply a function to each element in a list
def square(x):
    return x ** 2

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(square, numbers))
print(f"Squared Numbers: {squared_numbers}")

# Using map() with a lambda function
squared_numbers_lambda = list(map(lambda x: x ** 2, numbers))
print(f"Squared Numbers with lambda: {squared_numbers_lambda}")

# Using filter() to filter elements in a list
def is_even(x):
    return x % 2 == 0

even_numbers = list(filter(is_even, numbers))
print(f"Even Numbers: {even_numbers}")

# Using filter() with a lambda function
even_numbers_lambda = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even Numbers with lambda: {even_numbers_lambda}")
