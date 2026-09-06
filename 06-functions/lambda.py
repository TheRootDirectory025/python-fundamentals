"""
Python Fundamentals
06 - Functions
Topic: Lambda Functions

This file covers:
- What lambda functions are
- Lambda syntax
- Lambda with one argument
- Lambda with multiple arguments
- Lambda with conditions
- Lambda with built-in functions
- Lambda with sorted()
- Lambda with map()
- Lambda with filter()
- Practical examples
"""


# ============================================================
# 1. What Is a Lambda Function?
# ============================================================

"""
A lambda function is a small anonymous function.

Normal function:

def square(number):
    return number * number

Lambda equivalent:

lambda number: number * number

Lambda functions are useful when we need a small function
for a short operation.
"""


# ============================================================
# 2. Basic Lambda Syntax
# ============================================================

square = lambda number: number * number

print(square(5))
print(square(10))


# ============================================================
# 3. Lambda with Multiple Arguments
# ============================================================

add = lambda a, b: a + b

print(add(10, 20))


multiply = lambda a, b: a * b

print(multiply(5, 4))


# ============================================================
# 4. Lambda with Three Arguments
# ============================================================

calculate_total = lambda price, quantity, tax: (
    price * quantity + tax
)

print(calculate_total(100, 2, 20))


# ============================================================
# 5. Lambda vs Normal Function
# ============================================================

def square_function(number):
    return number * number


square_lambda = lambda number: number * number


print(square_function(5))
print(square_lambda(5))


# Lambda is usually better for short and simple operations.


# ============================================================
# 6. Lambda with a Condition
# ============================================================

check_even = lambda number: number % 2 == 0

print(check_even(10))
print(check_even(7))


# ============================================================
# 7. Lambda with if/else
# ============================================================

get_status = lambda age: "Adult" if age >= 18 else "Minor"

print(get_status(20))
print(get_status(15))


# ============================================================
# 8. Lambda with Strings
# ============================================================

get_length = lambda text: len(text)

print(get_length("Python"))
print(get_length("Backend Development"))


# ============================================================
# 9. Lambda with Uppercase
# ============================================================

to_upper = lambda text: text.upper()

print(to_upper("python"))
print(to_upper("django"))


# ============================================================
# 10. Lambda with sorted()
# ============================================================

numbers = [40, 10, 30, 20]

sorted_numbers = sorted(
    numbers,
    key=lambda number: number
)

print(sorted_numbers)


# ============================================================
# 11. Sorting by Absolute Value
# ============================================================

numbers = [-10, 5, -3, 8, -1]

result = sorted(
    numbers,
    key=lambda number: abs(number)
)

print(result)


# ============================================================
# 12. Sorting Strings by Length
# ============================================================

words = [
    "Python",
    "Django",
    "API",
    "Backend",
    "SQL"
]

result = sorted(
    words,
    key=lambda word: len(word)
)

print(result)


# ============================================================
# 13. Sorting in Descending Order
# ============================================================

numbers = [10, 50, 20, 40, 30]

result = sorted(
    numbers,
    key=lambda number: number,
    reverse=True
)

print(result)


# ============================================================
# 14. Sorting a List of Dictionaries
# ============================================================

students = [
    {"name": "Ali", "score": 18},
    {"name": "Sara", "score": 20},
    {"name": "Reza", "score": 15},
]

sorted_students = sorted(
    students,
    key=lambda student: student["score"]
)

print(sorted_students)


# ============================================================
# 15. Sorting Products by Price
# ============================================================

products = [
    {"name": "Keyboard", "price": 50},
    {"name": "Mouse", "price": 25},
    {"name": "Monitor", "price": 200},
    {"name": "Headset", "price": 80},
]

sorted_products = sorted(
    products,
    key=lambda product: product["price"]
)

for product in sorted_products:
    print(product)


# ============================================================
# 16. Sorting Products by Price Descending
# ============================================================

sorted_products = sorted(
    products,
    key=lambda product: product["price"],
    reverse=True
)

for product in sorted_products:
    print(product)


# ============================================================
# 17. map()
# ============================================================

"""
map() applies a function to every item in an iterable.

Example:

map(function, iterable)

The result is a map object, which can be converted to a list.
"""


numbers = [1, 2, 3, 4, 5]

squared_numbers = map(
    lambda number: number * number,
    numbers
)

print(list(squared_numbers))


# ============================================================
# 18. map() with Strings
# ============================================================

names = [
    "mohsen",
    "ali",
    "sara"
]

uppercase_names = map(
    lambda name: name.upper(),
    names
)

print(list(uppercase_names))


# ============================================================
# 19. map() with Prices
# ============================================================

prices = [100, 200, 300, 400]

prices_with_tax = map(
    lambda price: price * 1.09,
    prices
)

print(list(prices_with_tax))


# ============================================================
# 20. map() with Multiple Lists
# ============================================================

numbers_a = [1, 2, 3]
numbers_b = [10, 20, 30]

results = map(
    lambda a, b: a + b,
    numbers_a,
    numbers_b
)

print(list(results))


# ============================================================
# 21. filter()
# ============================================================

"""
filter() keeps only the items for which the function
returns True.
"""

numbers = [1, 2, 3, 4, 5, 6]

even_numbers = filter(
    lambda number: number % 2 == 0,
    numbers
)

print(list(even_numbers))


# ============================================================
# 22. filter() with Positive Numbers
# ============================================================

numbers = [-5, 10, -2, 8, -1, 20]

positive_numbers = filter(
    lambda number: number > 0,
    numbers
)

print(list(positive_numbers))


# ============================================================
# 23. filter() with Strings
# ============================================================

words = [
    "Python",
    "Java",
    "Django",
    "C",
    "Kotlin"
]

long_words = filter(
    lambda word: len(word) > 4,
    words
)

print(list(long_words))


# ============================================================
# 24. filter() with Dictionaries
# ============================================================

students = [
    {"name": "Ali", "score": 18},
    {"name": "Sara", "score": 20},
    {"name": "Reza", "score": 12},
    {"name": "Nima", "score": 16},
]

successful_students = filter(
    lambda student: student["score"] >= 15,
    students
)

print(list(successful_students))


# ============================================================
# 25. Practical Example: Active Users
# ============================================================

users = [
    {"name": "Ali", "active": True},
    {"name": "Sara", "active": False},
    {"name": "Reza", "active": True},
]

active_users = filter(
    lambda user: user["active"],
    users
)

print(list(active_users))


# ============================================================
# 26. Practical Example: Expensive Products
# ============================================================

products = [
    {"name": "Keyboard", "price": 50},
    {"name": "Monitor", "price": 200},
    {"name": "Mouse", "price": 25},
    {"name": "Laptop", "price": 1200},
]

expensive_products = filter(
    lambda product: product["price"] > 100,
    products
)

print(list(expensive_products))


# ============================================================
# 27. Combining filter() and map()
# ============================================================

numbers = [1, 2, 3, 4, 5, 6]

even_numbers = filter(
    lambda number: number % 2 == 0,
    numbers
)

squared_even_numbers = map(
    lambda number: number * number,
    even_numbers
)

print(list(squared_even_numbers))


# ============================================================
# 28. Combining sorted() and lambda
# ============================================================

employees = [
    {"name": "Ali", "salary": 3000},
    {"name": "Sara", "salary": 5000},
    {"name": "Reza", "salary": 4000},
]

sorted_employees = sorted(
    employees,
    key=lambda employee: employee["salary"],
    reverse=True
)

for employee in sorted_employees:
    print(employee)


# ============================================================
# 29. Practical Example: E-commerce
# ============================================================

products = [
    {"name": "Laptop", "price": 1200, "stock": 5},
    {"name": "Mouse", "price": 25, "stock": 20},
    {"name": "Keyboard", "price": 50, "stock": 0},
    {"name": "Monitor", "price": 200, "stock": 3},
]

available_products = filter(
    lambda product: product["stock"] > 0,
    products
)

available_products = list(available_products)

sorted_products = sorted(
    available_products,
    key=lambda product: product["price"]
)

for product in sorted_products:
    print(product)


# ============================================================
# 30. Practical Example: Student Scores
# ============================================================

scores = [12, 18, 15, 9, 20, 14, 17]

passed_scores = filter(
    lambda score: score >= 10,
    scores
)

passed_scores = list(passed_scores)

print("Passed scores:", passed_scores)


# ============================================================
# 31. Lambda with min() and max()
# ============================================================

students = [
    {"name": "Ali", "score": 18},
    {"name": "Sara", "score": 20},
    {"name": "Reza", "score": 15},
]

best_student = max(
    students,
    key=lambda student: student["score"]
)

worst_student = min(
    students,
    key=lambda student: student["score"]
)

print("Best:", best_student)
print("Worst:", worst_student)


# ============================================================
# 32. Lambda with any() and all()
# ============================================================

numbers = [2, 4, 6, 8]

has_odd_number = any(
    map(lambda number: number % 2 != 0, numbers)
)

all_even = all(
    map(lambda number: number % 2 == 0, numbers)
)

print("Has odd number:", has_odd_number)
print("All numbers are even:", all_even)


# ============================================================
# 33. When Not to Use Lambda
# ============================================================

"""
Lambda functions should remain simple.

Avoid complicated lambda expressions like:

lambda x: complicated_logic_here

If the operation becomes difficult to understand,
a normal function with a meaningful name is usually better.

Example:
"""


def calculate_final_price(price, discount, tax):
    discounted_price = price - (price * discount / 100)
    final_price = discounted_price + (
        discounted_price * tax / 100
    )

    return final_price


print(calculate_final_price(1000, 20, 9))


# ============================================================
# 34. Lambda vs Named Function
# ============================================================

def is_adult(age):
    return age >= 18


check_adult = lambda age: age >= 18


print(is_adult(20))
print(check_adult(20))


# A named function is usually clearer when the logic
# has a meaningful role in the application.


# ============================================================
# 35. Summary
# ============================================================

"""
Lambda:

lambda arguments: expression

Useful tools:

sorted()
    Sort items using a custom rule.

map()
    Transform every item.

filter()
    Keep items that satisfy a condition.

min()
    Find the minimum item using a custom rule.

max()
    Find the maximum item using a custom rule.

any()
    Check whether at least one item satisfies a condition.

all()
    Check whether every item satisfies a condition.

Use lambda for short, simple operations.
Use normal def functions when the logic becomes complex
or needs a meaningful name.
"""