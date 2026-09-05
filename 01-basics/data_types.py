"""
Python Fundamentals
01 - Basics
Topic: Data Types

This file covers:
- Numeric types
- Boolean
- Strings
- None
- Collections
- Type checking
- Type conversion
- Mutable vs Immutable objects
"""

# ============================================================
# 1. Numeric Types
# ============================================================

# int -> whole numbers
age = 24
score = -10

# float -> decimal numbers
price = 19.99
temperature = -2.5

print(age)
print(price)

print(type(age))
print(type(price))


# ============================================================
# 2. Boolean
# ============================================================

# bool can only have two values: True or False.

is_logged_in = True
has_permission = False

print(is_logged_in)
print(type(is_logged_in))


# Boolean values are commonly used in conditions.
if is_logged_in:
    print("User is logged in")


# ============================================================
# 3. Strings
# ============================================================

# str is used to represent text.

first_name = "Mohsen"
message = "Welcome to Python!"

print(first_name)
print(message)

# Strings support indexing.
language = "Python"

print(language[0])
print(language[-1])

# Strings support slicing.
print(language[0:3])


# ============================================================
# 4. None
# ============================================================

# None represents the absence of a value.

user_email = None

print(user_email)
print(type(user_email))

if user_email is None:
    print("Email has not been provided")


# ============================================================
# 5. Lists
# ============================================================

# list is an ordered and mutable collection.

skills = ["Python", "Django", "SQL"]

print(skills)

# Access an item
print(skills[0])

# Modify an item
skills[1] = "Django REST Framework"

print(skills)

# Add an item
skills.append("Docker")

print(skills)


# ============================================================
# 6. Tuples
# ============================================================

# tuple is an ordered but immutable collection.

coordinates = (35.6892, 51.3890)

print(coordinates)
print(coordinates[0])

# This would raise an error because tuples are immutable.
# coordinates[0] = 40


# ============================================================
# 7. Sets
# ============================================================

# set is an unordered collection of unique values.

programming_languages = {
    "Python",
    "Kotlin",
    "Python",
    "Java"
}

print(programming_languages)

# Duplicate values are automatically removed.


# ============================================================
# 8. Dictionaries
# ============================================================

# dict stores data as key-value pairs.

user = {
    "name": "Mohsen",
    "age": 24,
    "is_active": True
}

print(user)

# Access a value by its key.
print(user["name"])

# Add a new key-value pair.
user["country"] = "Azerbaijan"

print(user)


# ============================================================
# 9. Checking Types
# ============================================================

number = 100
text = "100"

print(type(number))
print(type(text))

print(isinstance(number, int))
print(isinstance(text, str))


# isinstance() is useful when we need to check
# whether a value belongs to a specific type.


# ============================================================
# 10. Type Conversion
# ============================================================

# Convert between compatible data types.

number_text = "100"
number = int(number_text)

print(number)
print(type(number))

decimal = float(number)

print(decimal)
print(type(decimal))

number_string = str(number)

print(number_string)
print(type(number_string))

# Convert values to boolean.
print(bool(1))
print(bool(0))
print(bool(""))
print(bool("Python"))


# ============================================================
# 11. Mutable vs Immutable
# ============================================================

# Mutable objects can be changed after creation.
# Examples: list, dict, set

skills = ["Python", "SQL"]

skills.append("Django")

print(skills)


# Immutable objects cannot be changed after creation.
# Examples: int, float, bool, str, tuple

name = "Mohsen"

# This creates a new string rather than modifying
# the original string object.
name = name.upper()

print(name)


# ============================================================
# 12. Nested Data Structures
# ============================================================

# Python data structures can contain other data structures.

users = [
    {
        "name": "Mohsen",
        "age": 24
    },
    {
        "name": "Ali",
        "age": 25
    }
]

print(users[0]["name"])
print(users[1]["age"])


# This kind of structure is very common when
# working with JSON and APIs.


# ============================================================
# 13. Real-World Example
# ============================================================

product = {
    "name": "Mechanical Keyboard",
    "price": 120.50,
    "quantity": 2,
    "tags": ["keyboard", "gaming", "mechanical"],
    "available": True,
    "discount": None
}

total_price = product["price"] * product["quantity"]

print("Product:", product["name"])
print("Quantity:", product["quantity"])
print("Total:", total_price)
print("Available:", product["available"])


# ============================================================
# 14. Mini Challenge
# ============================================================

# Create a user profile containing:
#
# - name
# - age
# - email
# - skills
# - is_active
# - address
#
# The address should contain:
# - city
# - country
#
# Then print each piece of information.

user_profile = {
    "name": "Mohsen",
    "age": 24,
    "email": "mohsen@example.com",
    "skills": ["Python", "Kotlin", "Django"],
    "is_active": True,
    "address": {
        "city": "Baku",
        "country": "Azerbaijan"
    }
}

print(user_profile["name"])
print(user_profile["skills"])
print(user_profile["address"]["city"])