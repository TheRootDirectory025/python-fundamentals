"""
Python Fundamentals
01 - Basics
Topic: Input and Output

This file covers:
- print()
- input()
- Output formatting
- Escape characters
- Type conversion
- Multiple inputs
- f-strings
"""

# ============================================================
# 1. Basic Output
# ============================================================

# print() is used to display information in the console.

print("Hello, Python!")
print("Welcome to Python Fundamentals.")

name = "Mohsen"
age = 24

print(name)
print(age)


# ============================================================
# 2. Printing Multiple Values
# ============================================================

# print() can display multiple values at the same time.

name = "Mohsen"
age = 24
language = "Python"

print(name, age, language)


# sep controls the separator between multiple values.
print(name, age, language, sep=" | ")


# end controls what is printed at the end.
print("Hello", end=" ")
print("World")


# ============================================================
# 3. Basic Input
# ============================================================

# input() reads data entered by the user.
# IMPORTANT: input() always returns a string.

name = input("Enter your name: ")

print("Hello", name)


# ============================================================
# 4. Input and Type Conversion
# ============================================================

# Since input() returns a string,
# numerical input must be converted before calculations.

age = input("Enter your age: ")

age = int(age)

print("Your age is:", age)
print(type(age))


# Another example:

price = float(input("Enter product price: "))

print("Product price:", price)


# ============================================================
# 5. Multiple Inputs
# ============================================================

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

print(first_name, last_name)


# ============================================================
# 6. Splitting Input
# ============================================================

# split() can be used to separate multiple values.

first_name, last_name = input(
    "Enter your first and last name: "
).split()

print("First name:", first_name)
print("Last name:", last_name)


# Multiple numbers:

numbers = input("Enter three numbers: ").split()

print(numbers)


# Convert each value to int.
a, b, c = map(int, input("Enter three numbers: ").split())

print("Sum:", a + b + c)


# ============================================================
# 7. Escape Characters
# ============================================================

# \n creates a new line.
print("Hello\nPython")

# \t creates a tab.
print("Name:\tMohsen")

# \" allows us to use quotation marks inside a string.
print("He said: \"Hello!\"")


# ============================================================
# 8. Formatted Output with f-strings
# ============================================================

# f-strings are the recommended way to format
# dynamic text in modern Python.

name = "Mohsen"
age = 24

print(f"My name is {name} and I am {age} years old.")


# Expressions can also be used inside f-strings.

price = 100
quantity = 3

print(f"Total price: {price * quantity}")


# ============================================================
# 9. Formatting Numbers
# ============================================================

price = 1250.5678

# Limit the number of decimal places.
print(f"Price: {price:.2f}")


# Add thousands separator.
large_number = 1000000

print(f"Number: {large_number:,}")


# ============================================================
# 10. Combining Input, Processing and Output
# ============================================================

# A common programming pattern is:
#
# Input → Processing → Output

name = input("Enter your name: ")
age = int(input("Enter your age: "))

next_year_age = age + 1

print(f"Hello {name}!")
print(f"Next year you will be {next_year_age} years old.")


# ============================================================
# 11. Real-World Example
# ============================================================

# Simple shopping calculator.

product_name = input("Product name: ")
price = float(input("Product price: "))
quantity = int(input("Quantity: "))

total_price = price * quantity

print("\n--- Order Summary ---")
print(f"Product: {product_name}")
print(f"Price: ${price:.2f}")
print(f"Quantity: {quantity}")
print(f"Total: ${total_price:.2f}")


# ============================================================
# 12. Mini Challenge
# ============================================================

# Build a simple user profile program.
#
# Ask the user for:
# - First name
# - Last name
# - Age
# - City
# - Programming language
#
# Then display the information in a clean format.
#
# Example:
#
# =========================
# User Profile
# =========================
# Name: Mohsen Bagheri
# Age: 24
# City: Tehran
# Favorite Language: Python
# =========================

first_name = input("First name: ")
last_name = input("Last name: ")
age = int(input("Age: "))
city = input("City: ")
favorite_language = input("Favorite programming language: ")

print("\n=========================")
print("User Profile")
print("=========================")
print(f"Name: {first_name} {last_name}")
print(f"Age: {age}")
print(f"City: {city}")
print(f"Favorite Language: {favorite_language}")
print("=========================")