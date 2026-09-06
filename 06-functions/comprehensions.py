"""
Python Fundamentals
06 - Functions
Topic: Comprehensions

This file covers:
- List comprehensions
- Basic list comprehensions
- List comprehensions with conditions
- if/else inside comprehensions
- Nested list comprehensions
- Set comprehensions
- Dictionary comprehensions
- Practical examples
- When to use comprehensions
"""


# ============================================================
# 1. Basic List Comprehension
# ============================================================

numbers = [1, 2, 3, 4, 5]

squares = [number * number for number in numbers]

print(squares)


# The equivalent regular loop:

squares = []

for number in numbers:
    squares.append(number * number)

print(squares)


# ============================================================
# 2. List Comprehension with Strings
# ============================================================

names = [
    "mohsen",
    "ali",
    "sara",
    "reza"
]

uppercase_names = [
    name.upper()
    for name in names
]

print(uppercase_names)


# ============================================================
# 3. List Comprehension with range()
# ============================================================

numbers = [
    number
    for number in range(1, 11)
]

print(numbers)


# ============================================================
# 4. Squares from a Range
# ============================================================

squares = [
    number * number
    for number in range(1, 11)
]

print(squares)


# ============================================================
# 5. List Comprehension with a Condition
# ============================================================

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = [
    number
    for number in numbers
    if number % 2 == 0
]

print(even_numbers)


# ============================================================
# 6. Filtering Odd Numbers
# ============================================================

odd_numbers = [
    number
    for number in numbers
    if number % 2 != 0
]

print(odd_numbers)


# ============================================================
# 7. Filtering Positive Numbers
# ============================================================

numbers = [-5, 10, -2, 8, -1, 20]

positive_numbers = [
    number
    for number in numbers
    if number > 0
]

print(positive_numbers)


# ============================================================
# 8. Transforming and Filtering
# ============================================================

numbers = [1, 2, 3, 4, 5, 6]

squared_even_numbers = [
    number * number
    for number in numbers
    if number % 2 == 0
]

print(squared_even_numbers)


# ============================================================
# 9. if/else Inside List Comprehension
# ============================================================

numbers = [1, 2, 3, 4, 5]

labels = [
    "even" if number % 2 == 0 else "odd"
    for number in numbers
]

print(labels)


# ============================================================
# 10. Positive or Negative
# ============================================================

numbers = [-5, 10, -2, 8, -1]

results = [
    "positive" if number > 0 else "negative"
    for number in numbers
]

print(results)


# ============================================================
# 11. Convert Names to Uppercase
# ============================================================

names = [
    "mohsen",
    "ali",
    "sara"
]

formatted_names = [
    name.capitalize()
    for name in names
]

print(formatted_names)


# ============================================================
# 12. Filter Long Words
# ============================================================

words = [
    "Python",
    "Django",
    "API",
    "Backend",
    "SQL",
    "Programming"
]

long_words = [
    word
    for word in words
    if len(word) > 5
]

print(long_words)


# ============================================================
# 13. Nested List Comprehension
# ============================================================

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

flattened = [
    number
    for row in matrix
    for number in row
]

print(flattened)


# ============================================================
# 14. Nested Loops with Comprehension
# ============================================================

pairs = [
    (x, y)
    for x in range(1, 4)
    for y in range(1, 4)
]

print(pairs)


# ============================================================
# 15. Multiplication Table
# ============================================================

multiplication_table = [
    x * y
    for x in range(1, 6)
    for y in range(1, 6)
]

print(multiplication_table)


# ============================================================
# 16. Set Comprehension
# ============================================================

numbers = [1, 2, 2, 3, 3, 4, 5]

unique_squares = {
    number * number
    for number in numbers
}

print(unique_squares)


# ============================================================
# 17. Set Comprehension with Condition
# ============================================================

numbers = range(1, 11)

even_squares = {
    number * number
    for number in numbers
    if number % 2 == 0
}

print(even_squares)


# ============================================================
# 18. Dictionary Comprehension
# ============================================================

numbers = range(1, 6)

squares = {
    number: number * number
    for number in numbers
}

print(squares)


# ============================================================
# 19. Dictionary Comprehension with Condition
# ============================================================

numbers = range(1, 11)

even_squares = {
    number: number * number
    for number in numbers
    if number % 2 == 0
}

print(even_squares)


# ============================================================
# 20. Create a Dictionary from Two Lists
# ============================================================

names = ["Ali", "Sara", "Mohsen"]
scores = [18, 20, 17]

student_scores = {
    name: score
    for name, score in zip(names, scores)
}

print(student_scores)


# ============================================================
# 21. Transform a Dictionary
# ============================================================

prices = {
    "Keyboard": 50,
    "Mouse": 25,
    "Monitor": 200
}

discounted_prices = {
    product: price * 0.9
    for product, price in prices.items()
}

print(discounted_prices)


# ============================================================
# 22. Filter a Dictionary
# ============================================================

prices = {
    "Keyboard": 50,
    "Mouse": 25,
    "Monitor": 200,
    "Laptop": 1200
}

expensive_products = {
    product: price
    for product, price in prices.items()
    if price > 100
}

print(expensive_products)


# ============================================================
# 23. Transform and Filter a Dictionary
# ============================================================

prices = {
    "Keyboard": 50,
    "Mouse": 25,
    "Monitor": 200,
    "Laptop": 1200
}

discounted_expensive_products = {
    product: price * 0.9
    for product, price in prices.items()
    if price > 100
}

print(discounted_expensive_products)


# ============================================================
# 24. Practical Example: Student Scores
# ============================================================

scores = {
    "Ali": 18,
    "Sara": 20,
    "Reza": 9,
    "Nima": 16
}

passed_students = {
    name: score
    for name, score in scores.items()
    if score >= 10
}

print(passed_students)


# ============================================================
# 25. Practical Example: Active Users
# ============================================================

users = [
    {"name": "Ali", "active": True},
    {"name": "Sara", "active": False},
    {"name": "Reza", "active": True},
    {"name": "Nima", "active": False}
]

active_users = [
    user["name"]
    for user in users
    if user["active"]
]

print(active_users)


# ============================================================
# 26. Practical Example: Product Names
# ============================================================

products = [
    {"name": "Keyboard", "price": 50},
    {"name": "Mouse", "price": 25},
    {"name": "Monitor", "price": 200}
]

product_names = [
    product["name"]
    for product in products
]

print(product_names)


# ============================================================
# 27. Practical Example: Products Above a Price
# ============================================================

expensive_products = [
    product["name"]
    for product in products
    if product["price"] > 50
]

print(expensive_products)


# ============================================================
# 28. Practical Example: Calculate Cart Items
# ============================================================

cart = [
    {"name": "Keyboard", "price": 50, "quantity": 2},
    {"name": "Mouse", "price": 25, "quantity": 3},
    {"name": "Monitor", "price": 200, "quantity": 1}
]

item_totals = [
    item["price"] * item["quantity"]
    for item in cart
]

print(item_totals)


# ============================================================
# 29. Practical Example: Cart Total
# ============================================================

cart_total = sum(
    item["price"] * item["quantity"]
    for item in cart
)

print(f"Cart total: {cart_total}")


# ============================================================
# 30. Practical Example: API-Like Data
# ============================================================

api_users = [
    {
        "id": 1,
        "name": "Ali",
        "active": True
    },
    {
        "id": 2,
        "name": "Sara",
        "active": False
    },
    {
        "id": 3,
        "name": "Mohsen",
        "active": True
    }
]

active_user_names = [
    user["name"]
    for user in api_users
    if user["active"]
]

print(active_user_names)


# ============================================================
# 31. Comprehension vs map() and filter()
# ============================================================

numbers = [1, 2, 3, 4, 5, 6]

squares_comprehension = [
    number * number
    for number in numbers
]

squares_map = list(
    map(
        lambda number: number * number,
        numbers
    )
)

print(squares_comprehension)
print(squares_map)


even_comprehension = [
    number
    for number in numbers
    if number % 2 == 0
]

even_filter = list(
    filter(
        lambda number: number % 2 == 0,
        numbers
    )
)

print(even_comprehension)
print(even_filter)


# ============================================================
# 32. Calling a Function Inside a Comprehension
# ============================================================

def square(number):
    return number * number


numbers = [1, 2, 3, 4, 5]

squares = [
    square(number)
    for number in numbers
]

print(squares)


# ============================================================
# 33. Practical Example: Formatting User Names
# ============================================================

def format_name(name):
    return name.strip().title()


names = [
    "  mohsen",
    "ali  ",
    "  sara "
]

formatted_names = [
    format_name(name)
    for name in names
]

print(formatted_names)


# ============================================================
# 34. Avoid Overly Complex Comprehensions
# ============================================================

"""
Comprehensions are useful when the logic is simple.

Good:

squares = [
    number * number
    for number in numbers
]

If a comprehension becomes difficult to read,
a normal for loop is often a better choice.

Readable code is more important than writing
everything in one line.
"""


# ============================================================
# 35. Summary
# ============================================================

"""
List comprehension:

[expression for item in iterable]

With condition:

[expression for item in iterable if condition]

With if/else:

[value_if_true if condition else value_if_false
 for item in iterable]

Set comprehension:

{expression for item in iterable}

Dictionary comprehension:

{key: value for item in iterable}

Comprehensions are useful for:

- Transforming data
- Filtering data
- Creating new collections
- Working with lists, sets, and dictionaries
- Writing concise and readable code
"""