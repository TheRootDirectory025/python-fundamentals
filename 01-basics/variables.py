"""
Python Fundamentals
01 - Basics
Topic: Variables

This file covers:
- Variable declaration
- Naming conventions
- Basic data types
- Multiple assignment
- Constants
- Checking variable types
"""

# ============================================================
# 1. Variables
# ============================================================

# A variable is a name that refers to a value stored in memory.
name = "Mohsen"
age = 23
is_student = True

print(name)
print(age)
print(is_student)


# ============================================================
# 2. Variable Naming
# ============================================================

# Use descriptive names that clearly explain what the value means.
first_name = "Mohsen"
last_name = "Bagheri"
birth_year = 2002

# Python uses snake_case for variable names.
user_name = "mohsen"
total_price = 150000


# Avoid unclear names when a descriptive name is possible.
# Bad:
x = 100

# Better:
user_score = 100


# Variable names cannot:
# - Start with a number
# - Contain spaces
# - Use Python reserved keywords

# 1name = "Invalid"
# user name = "Invalid"


# ============================================================
# 3. Basic Data Types
# ============================================================

name = "Mohsen"          # str
age = 24                 # int
height = 1.80            # float
is_developer = True      # bool

print(type(name))
print(type(age))
print(type(height))
print(type(is_developer))


# ============================================================
# 4. Dynamic Typing
# ============================================================

# Python is dynamically typed.
# The type of a variable is determined at runtime.

value = 10
print(type(value))

value = "Hello"
print(type(value))

value = 3.14
print(type(value))


# ============================================================
# 5. Multiple Assignment
# ============================================================

# Assign different values to multiple variables.
first_name, last_name, age = "Mohsen", "Bagheri", 24

print(first_name)
print(last_name)
print(age)


# Assign the same value to multiple variables.
x = y = z = 0

print(x, y, z)


# ============================================================
# 6. Reassigning Variables
# ============================================================

score = 80

# The value of the variable can be changed.
score = 95

print(score)


# ============================================================
# 7. Type Conversion
# ============================================================

age_text = "24"

# Convert string to integer.
age_number = int(age_text)

print(age_number)
print(type(age_number))


price = 99
price_text = str(price)

print(price_text)
print(type(price_text))


# Convert integer to float.
number = 10
decimal_number = float(number)

print(decimal_number)


# ============================================================
# 8. Constants
# ============================================================

# Python does not have a true constant keyword.
# By convention, uppercase names are used for values
# that should not be changed.

PI = 3.14159
MAX_LOGIN_ATTEMPTS = 5
APP_NAME = "My Backend App"

print(PI)
print(MAX_LOGIN_ATTEMPTS)
print(APP_NAME)


# ============================================================
# 9. Useful Practice
# ============================================================

# Create variables for a simple user profile.

user_name = "Mohsen"
user_age = 24
user_country = "Azerbaijan"
user_is_active = True

print("Name:", user_name)
print("Age:", user_age)
print("Country:", user_country)
print("Active:", user_is_active)


# ============================================================
# 10. Mini Challenge
# ============================================================

# TODO:
# Create variables for a product:
#
# - product_name
# - product_price
# - product_quantity
# - product_available
#
# Then calculate and print the total price.

product_name = "Keyboard"
product_price = 50
product_quantity = 2
product_available = True

total_price = product_price * product_quantity

print("Product:", product_name)
print("Total price:", total_price)
print("Available:", product_available)