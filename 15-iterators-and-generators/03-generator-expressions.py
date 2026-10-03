"""
Python Generator Expressions
============================

This file covers:
- Generator expressions
- Generator expressions vs list comprehensions
- Lazy evaluation
- Filtering
- Transforming data
- any()
- all()
- sum()
- min()
- max()
- Practical backend examples
"""


# ============================================================
# 1. Basic Generator Expression
# ============================================================

numbers = (
    number
    for number in range(5)
)

print(numbers)


# A generator expression creates a generator object.


# ============================================================
# 2. Getting Values
# ============================================================

numbers = (
    number
    for number in range(5)
)

print(next(numbers))
print(next(numbers))
print(next(numbers))


# ============================================================
# 3. Iterating Over A Generator Expression
# ============================================================

numbers = (
    number
    for number in range(5)
)

for number in numbers:
    print(number)


# ============================================================
# 4. Generator Expression Syntax
# ============================================================

# General syntax:
#
# (expression for item in iterable)
#
# Example:

squares = (
    number ** 2
    for number in range(1, 6)
)

for square in squares:
    print(square)


# ============================================================
# 5. Generator Expression With Condition
# ============================================================

even_numbers = (
    number
    for number in range(10)
    if number % 2 == 0
)

for number in even_numbers:
    print(number)


# ============================================================
# 6. Transformation
# ============================================================

numbers = (
    number * 10
    for number in range(5)
)

for number in numbers:
    print(number)


# ============================================================
# 7. List Comprehension
# ============================================================

numbers = [
    number * 10
    for number in range(5)
]

print(numbers)


# A list comprehension immediately creates
# the complete list.


# ============================================================
# 8. Generator Expression
# ============================================================

numbers = (
    number * 10
    for number in range(5)
)

print(numbers)


# A generator expression produces values lazily.


# ============================================================
# 9. Main Difference
# ============================================================

list_result = [
    number ** 2
    for number in range(1_000)
]

generator_result = (
    number ** 2
    for number in range(1_000)
)

print(type(list_result))
print(type(generator_result))


# List:
# Stores all results.
#
# Generator:
# Produces results when requested.


# ============================================================
# 10. Memory-Friendly Processing
# ============================================================

numbers = (
    number ** 2
    for number in range(1_000_000)
)

for number in numbers:
    if number > 100:
        print(number)
        break


# Only the required values are produced.


# ============================================================
# 11. Generator Expression With Strings
# ============================================================

names = [
    "Ali",
    "Sara",
    "Mohsen",
    "Reza",
]

uppercase_names = (
    name.upper()
    for name in names
)

for name in uppercase_names:
    print(name)


# ============================================================
# 12. Filtering Strings
# ============================================================

names = [
    "Ali",
    "Sara",
    "Mohsen",
    "Reza",
]

long_names = (
    name
    for name in names
    if len(name) > 3
)

for name in long_names:
    print(name)


# ============================================================
# 13. Generator With Dictionaries
# ============================================================

users = [
    {"id": 1, "name": "Ali"},
    {"id": 2, "name": "Sara"},
    {"id": 3, "name": "Mohsen"},
]

usernames = (
    user["name"]
    for user in users
)

for username in usernames:
    print(username)


# ============================================================
# 14. Filtering Dictionaries
# ============================================================

users = [
    {"id": 1, "name": "Ali", "active": True},
    {"id": 2, "name": "Sara", "active": False},
    {"id": 3, "name": "Mohsen", "active": True},
]

active_users = (
    user
    for user in users
    if user["active"]
)

for user in active_users:
    print(user)


# ============================================================
# 15. Extracting Active Usernames
# ============================================================

users = [
    {"id": 1, "name": "Ali", "active": True},
    {"id": 2, "name": "Sara", "active": False},
    {"id": 3, "name": "Mohsen", "active": True},
]

active_usernames = (
    user["name"]
    for user in users
    if user["active"]
)

for username in active_usernames:
    print(username)


# ============================================================
# 16. sum()
# ============================================================

numbers = (
    number
    for number in range(1, 6)
)

total = sum(numbers)

print(total)


# sum() consumes the generator.


# ============================================================
# 17. sum() With Transformation
# ============================================================

prices = [100, 200, 300, 400]

total = sum(
    price
    for price in prices
)

print(total)


# ============================================================
# 18. sum() With Filtering
# ============================================================

prices = [100, 250, 75, 400, 50]

total = sum(
    price
    for price in prices
    if price >= 100
)

print(total)


# ============================================================
# 19. any()
# ============================================================

numbers = [1, 3, 5, 8, 9]

has_even_number = any(
    number % 2 == 0
    for number in numbers
)

print(has_even_number)


# any() returns True when at least one
# generated condition is True.


# ============================================================
# 20. all()
# ============================================================

numbers = [2, 4, 6, 8]

all_even = all(
    number % 2 == 0
    for number in numbers
)

print(all_even)


# all() returns True when every condition is True.


# ============================================================
# 21. any() With Users
# ============================================================

users = [
    {"name": "Ali", "active": False},
    {"name": "Sara", "active": False},
    {"name": "Mohsen", "active": True},
]

has_active_user = any(
    user["active"]
    for user in users
)

print(has_active_user)


# ============================================================
# 22. all() With Users
# ============================================================

users = [
    {"name": "Ali", "verified": True},
    {"name": "Sara", "verified": True},
    {"name": "Mohsen", "verified": True},
]

all_verified = all(
    user["verified"]
    for user in users
)

print(all_verified)


# ============================================================
# 23. min()
# ============================================================

prices = [500, 250, 800, 150]

minimum = min(
    price
    for price in prices
)

print(minimum)


# ============================================================
# 24. max()
# ============================================================

prices = [500, 250, 800, 150]

maximum = max(
    price
    for price in prices
)

print(maximum)


# ============================================================
# 25. min() With Objects
# ============================================================

products = [
    {"name": "Laptop", "price": 1200},
    {"name": "Phone", "price": 800},
    {"name": "Tablet", "price": 500},
]

cheapest = min(
    product["price"]
    for product in products
)

print(cheapest)


# ============================================================
# 26. max() With Objects
# ============================================================

most_expensive = max(
    product["price"]
    for product in products
)

print(most_expensive)


# ============================================================
# 27. Average Using Generator Expression
# ============================================================

scores = [18, 15, 20, 17, 19]

total = sum(
    score
    for score in scores
)

average = total / len(scores)

print(average)


# ============================================================
# 28. Processing Orders
# ============================================================

orders = [
    {"id": 101, "total": 250, "status": "completed"},
    {"id": 102, "total": 500, "status": "pending"},
    {"id": 103, "total": 150, "status": "completed"},
]

completed_total = sum(
    order["total"]
    for order in orders
    if order["status"] == "completed"
)

print(completed_total)


# ============================================================
# 29. Checking Orders
# ============================================================

orders = [
    {"id": 101, "status": "completed"},
    {"id": 102, "status": "completed"},
    {"id": 103, "status": "pending"},
]

has_pending_order = any(
    order["status"] == "pending"
    for order in orders
)

print(has_pending_order)


# ============================================================
# 30. Checking Product Stock
# ============================================================

products = [
    {"name": "Laptop", "stock": 5},
    {"name": "Phone", "stock": 10},
    {"name": "Tablet", "stock": 0},
]

out_of_stock = any(
    product["stock"] == 0
    for product in products
)

print(out_of_stock)


# ============================================================
# 31. Checking All Products
# ============================================================

products = [
    {"name": "Laptop", "stock": 5},
    {"name": "Phone", "stock": 10},
    {"name": "Tablet", "stock": 3},
]

all_available = all(
    product["stock"] > 0
    for product in products
)

print(all_available)


# ============================================================
# 32. Generator Expression With Function
# ============================================================

def calculate_price(price):
    return price * 1.1


prices = [100, 200, 300]

final_prices = (
    calculate_price(price)
    for price in prices
)

for price in final_prices:
    print(price)


# ============================================================
# 33. Nested Generator Expression
# ============================================================

matrix = [
    [1, 2],
    [3, 4],
    [5, 6],
]

values = (
    number
    for row in matrix
    for number in row
)

for value in values:
    print(value)


# ============================================================
# 34. Generator Expression With enumerate()
# ============================================================

names = [
    "Ali",
    "Sara",
    "Mohsen",
]

indexed_names = (
    (index, name)
    for index, name in enumerate(names, start=1)
)

for item in indexed_names:
    print(item)


# ============================================================
# 35. Generator Expression With zip()
# ============================================================

names = ["Ali", "Sara", "Mohsen"]
scores = [18, 19, 17]

students = (
    {
        "name": name,
        "score": score,
    }
    for name, score in zip(names, scores)
)

for student in students:
    print(student)


# ============================================================
# 36. Reusing A Generator
# ============================================================

numbers = (
    number
    for number in range(5)
)

print(list(numbers))

print(list(numbers))


# The second result is empty because
# the generator has already been consumed.


# ============================================================
# 37. Reusing The Source Data
# ============================================================

numbers = range(5)

first = (
    number
    for number in numbers
)

second = (
    number
    for number in numbers
)

print(list(first))
print(list(second))


# A new generator can be created from
# the original iterable.


# ============================================================
# 38. Converting Generator To List
# ============================================================

numbers = (
    number * 2
    for number in range(5)
)

result = list(numbers)

print(result)


# Converting to a list consumes the generator
# and stores all generated values.


# ============================================================
# 39. Generator With File Data
# ============================================================

def valid_lines(lines):
    return (
        line.strip()
        for line in lines
        if line.strip()
    )


lines = [
    "Python",
    "",
    "Django",
    "   ",
    "PostgreSQL",
]

for line in valid_lines(lines):
    print(line)


# ============================================================
# 40. Backend Data Pipeline
# ============================================================

orders = [
    {
        "id": 1,
        "status": "completed",
        "total": 250,
    },
    {
        "id": 2,
        "status": "cancelled",
        "total": 100,
    },
    {
        "id": 3,
        "status": "completed",
        "total": 500,
    },
]


completed_orders = (
    order
    for order in orders
    if order["status"] == "completed"
)

completed_totals = (
    order["total"]
    for order in completed_orders
)

total_sales = sum(completed_totals)

print("Total sales:", total_sales)


# ============================================================
# 41. Generator Expression With API Data
# ============================================================

api_response = [
    {"id": 1, "email": "ali@example.com"},
    {"id": 2, "email": "sara@example.com"},
    {"id": 3, "email": "mohsen@example.com"},
]

emails = (
    user["email"]
    for user in api_response
)

for email in emails:
    print(email)


# ============================================================
# 42. When To Use Generator Expressions
# ============================================================

# Generator expressions are useful when:
#
# - You only need to process values once.
# - The dataset can be large.
# - You want lazy evaluation.
# - You are passing data to sum(), any(), all(),
#   min(), or max().
# - You are building a processing pipeline.


# ============================================================
# 43. When To Use List Comprehensions
# ============================================================

# Use list comprehensions when:
#
# - You need all results immediately.
# - You need indexing.
# - You need to iterate multiple times.
# - You need list methods.
# - The dataset is reasonably small.


# ============================================================
# 44. Readability Matters
# ============================================================

# This is readable:

squares = (
    number ** 2
    for number in range(10)
)

for square in squares:
    print(square)


# Avoid creating extremely complicated
# generator expressions.
#
# If the expression becomes difficult to read,
# use a normal function or a generator function.


# ============================================================
# 45. Final Comparison
# ============================================================

numbers = range(10)

# List comprehension

list_result = [
    number * 2
    for number in numbers
]

print(list_result)


# Generator expression

generator_result = (
    number * 2
    for number in numbers
)

print(generator_result)

for number in generator_result:
    print(number)


# ============================================================
# 46. Key Rules
# ============================================================

# Rule 1:
# Generator expressions use parentheses.

# Rule 2:
# They produce values lazily.

# Rule 3:
# They are iterators.

# Rule 4:
# They are consumed during iteration.

# Rule 5:
# sum(), any(), all(), min(), and max()
# work naturally with generator expressions.

# Rule 6:
# Use list comprehensions when you need
# the complete collection immediately.

# Rule 7:
# Use generators when incremental processing
# is more appropriate.

# Rule 8:
# Prefer readability over unnecessarily
# complex generator expressions.