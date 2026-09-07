"""
Python Fundamentals
07 - Strings
Topic: String Formatting

This file covers:
- String concatenation
- f-strings
- String placeholders
- Formatting numbers
- Decimal precision
- Width and alignment
- Padding
- Percentage formatting
- Formatting dates and times
- Practical string formatting examples
"""


# ============================================================
# 1. String Concatenation
# ============================================================

first_name = "Mohsen"
last_name = "Bagheri"

full_name = first_name + " " + last_name

print(full_name)


# ============================================================
# 2. Concatenating Different Data Types
# ============================================================

name = "Mohsen"
age = 24

# Strings and numbers cannot be concatenated directly.

# message = "My age is " + age
# This would raise a TypeError.

message = "My age is " + str(age)

print(message)


# ============================================================
# 3. Basic f-string
# ============================================================

name = "Mohsen"
age = 24

message = f"My name is {name} and I am {age} years old."

print(message)


# ============================================================
# 4. Expressions Inside f-strings
# ============================================================

price = 100
quantity = 3

message = f"Total: {price * quantity}"

print(message)


# ============================================================
# 5. Calling Functions Inside f-strings
# ============================================================

name = "mohsen"

message = f"Username: {name.upper()}"

print(message)


# ============================================================
# 6. Multiple Variables
# ============================================================

name = "Mohsen"
age = 24
city = "Tehran"

message = (
    f"Name: {name}, "
    f"Age: {age}, "
    f"City: {city}"
)

print(message)


# ============================================================
# 7. Formatting Decimal Numbers
# ============================================================

price = 1234.56789

print(f"Price: {price:.2f}")
print(f"Price: {price:.3f}")


# ============================================================
# 8. Rounding Numbers
# ============================================================

number = 12.98765

print(f"{number:.2f}")


# ============================================================
# 9. Thousands Separator
# ============================================================

price = 1234567.89

print(f"{price:,.2f}")


# ============================================================
# 10. Percentage Formatting
# ============================================================

progress = 0.85

print(f"Progress: {progress:.0%}")
print(f"Progress: {progress:.2%}")


# ============================================================
# 11. Currency-like Formatting
# ============================================================

price = 1250000

formatted_price = f"{price:,} تومان"

print(formatted_price)


# ============================================================
# 12. Width
# ============================================================

name = "Python"

print(f"{name:10}")


# The string occupies at least 10 characters.


# ============================================================
# 13. Left Alignment
# ============================================================

name = "Python"

print(f"{name:<10}")


# ============================================================
# 14. Right Alignment
# ============================================================

name = "Python"

print(f"{name:>10}")


# ============================================================
# 15. Center Alignment
# ============================================================

name = "Python"

print(f"{name:^10}")


# ============================================================
# 16. Padding with Zeros
# ============================================================

number = 42

print(f"{number:05}")


# Output:
# 00042


# ============================================================
# 17. Padding with Custom Characters
# ============================================================

number = 42

print(f"{number:*^10}")


# ============================================================
# 18. Formatting Positive and Negative Numbers
# ============================================================

balance = 1250

print(f"{balance:+}")


balance = -1250

print(f"{balance:+}")


# ============================================================
# 19. Scientific Notation
# ============================================================

number = 123456789

print(f"{number:e}")


# ============================================================
# 20. Binary, Octal and Hexadecimal
# ============================================================

number = 255

print(f"Binary: {number:b}")
print(f"Octal: {number:o}")
print(f"Hexadecimal: {number:x}")


# ============================================================
# 21. Format Method
# ============================================================

name = "Mohsen"
age = 24

message = "My name is {} and I am {} years old.".format(
    name,
    age
)

print(message)


# ============================================================
# 22. format() with Named Placeholders
# ============================================================

message = (
    "Name: {name}, Age: {age}"
    .format(
        name="Mohsen",
        age=24
    )
)

print(message)


# ============================================================
# 23. format() with Positions
# ============================================================

message = "Name: {0}, City: {1}".format(
    "Mohsen",
    "Tehran"
)

print(message)


# ============================================================
# 24. f-strings vs format()
# ============================================================

name = "Mohsen"
age = 24

message_one = f"{name} is {age} years old."

message_two = "{} is {} years old.".format(
    name,
    age
)

print(message_one)
print(message_two)


# f-strings are generally the preferred approach
# in modern Python code.


# ============================================================
# 25. Formatting Boolean Values
# ============================================================

is_active = True

message = f"User active: {is_active}"

print(message)


# ============================================================
# 26. Formatting Lists
# ============================================================

skills = [
    "Python",
    "Django",
    "PostgreSQL"
]

message = f"My skills: {skills}"

print(message)


# ============================================================
# 27. Formatting a Dictionary
# ============================================================

user = {
    "name": "Mohsen",
    "age": 24,
    "city": "Tehran"
}

message = (
    f"Name: {user['name']}, "
    f"Age: {user['age']}, "
    f"City: {user['city']}"
)

print(message)


# ============================================================
# 28. Practical Example: User Profile
# ============================================================

def format_user_profile(user):
    return (
        f"Name: {user['name']}\n"
        f"Age: {user['age']}\n"
        f"City: {user['city']}"
    )


user = {
    "name": "Mohsen",
    "age": 24,
    "city": "Tehran"
}

print(format_user_profile(user))


# ============================================================
# 29. Practical Example: Product Information
# ============================================================

product = {
    "name": "Keyboard",
    "price": 1250000,
    "stock": 15
}

message = (
    f"Product: {product['name']}\n"
    f"Price: {product['price']:,} تومان\n"
    f"Stock: {product['stock']}"
)

print(message)


# ============================================================
# 30. Practical Example: Shopping Receipt
# ============================================================

product_name = "Keyboard"
price = 1250000
quantity = 2

total = price * quantity

receipt = (
    f"Product : {product_name}\n"
    f"Price   : {price:,} تومان\n"
    f"Quantity: {quantity}\n"
    f"Total   : {total:,} تومان"
)

print(receipt)


# ============================================================
# 31. Practical Example: Discount
# ============================================================

price = 2500000
discount = 15

discount_amount = price * discount / 100
final_price = price - discount_amount

message = (
    f"Original price : {price:,.0f} تومان\n"
    f"Discount       : {discount:.0f}%\n"
    f"Discount amount: {discount_amount:,.0f} تومان\n"
    f"Final price    : {final_price:,.0f} تومان"
)

print(message)


# ============================================================
# 32. Practical Example: Student Report
# ============================================================

student_name = "Mohsen"
score = 18.75

report = (
    f"Student: {student_name}\n"
    f"Score  : {score:.2f}\n"
    f"Status : {'Passed' if score >= 10 else 'Failed'}"
)

print(report)


# ============================================================
# 33. Conditional Expressions in f-strings
# ============================================================

age = 22

message = (
    f"User is {'adult' if age >= 18 else 'minor'}."
)

print(message)


# ============================================================
# 34. Formatting Tables
# ============================================================

products = [
    ("Keyboard", 1250),
    ("Mouse", 650),
    ("Monitor", 8500)
]

print(f"{'Product':<15}{'Price':>10}")

for name, price in products:
    print(f"{name:<15}{price:>10,}")


# ============================================================
# 35. Formatting Numbers in a Table
# ============================================================

items = [
    ("Keyboard", 2, 1250),
    ("Mouse", 3, 650),
    ("Monitor", 1, 8500)
]

print(
    f"{'Product':<15}"
    f"{'Qty':>5}"
    f"{'Price':>10}"
)

for name, quantity, price in items:
    print(
        f"{name:<15}"
        f"{quantity:>5}"
        f"{price:>10,}"
    )


# ============================================================
# 36. Practical Example: API Response Message
# ============================================================

status_code = 200
username = "Mohsen"

message = (
    f"API response: "
    f"status={status_code}, "
    f"user={username}"
)

print(message)


# ============================================================
# 37. Formatting Floating-Point Values
# ============================================================

average = 18.73642

print(f"Average: {average:.1f}")
print(f"Average: {average:.2f}")
print(f"Average: {average:.3f}")


# ============================================================
# 38. Escape Braces in f-strings
# ============================================================

name = "Mohsen"

message = f"{{'name': '{name}'}}"

print(message)


# Double braces produce literal braces.


# ============================================================
# 39. Formatting with New Lines
# ============================================================

name = "Mohsen"
role = "Backend Developer"

profile = (
    f"Name: {name}\n"
    f"Role: {role}"
)

print(profile)


# ============================================================
# 40. Formatting with Tabs
# ============================================================

name = "Mohsen"
score = 18

print(f"Name:\t{name}")
print(f"Score:\t{score}")


# ============================================================
# 41. Practical Example: Login Message
# ============================================================

username = "mohsen"
is_authenticated = True

message = (
    f"User: {username}\n"
    f"Authenticated: {is_authenticated}\n"
    f"Status: {'Success' if is_authenticated else 'Failed'}"
)

print(message)


# ============================================================
# 42. Practical Example: File Information
# ============================================================

filename = "report.pdf"
size = 125.678

file_info = (
    f"Filename: {filename}\n"
    f"Size: {size:.2f} KB\n"
    f"Extension: {filename.split('.')[-1]}"
)

print(file_info)


# ============================================================
# 43. Practical Example: Progress
# ============================================================

completed = 73
total = 100

progress = completed / total

print(
    f"Progress: {progress:.0%} "
    f"({completed}/{total})"
)


# ============================================================
# 44. Practical Example: Backend Server Status
# ============================================================

server_name = "API Server"
uptime = 99.9876
requests = 1256789

status = (
    f"Server: {server_name}\n"
    f"Uptime: {uptime:.2f}%\n"
    f"Requests: {requests:,}"
)

print(status)


# ============================================================
# 45. Practical Example: Order Summary
# ============================================================

order = {
    "id": 1024,
    "customer": "Mohsen",
    "subtotal": 3500000,
    "discount": 10,
    "status": "paid"
}

discount_amount = (
    order["subtotal"] *
    order["discount"] /
    100
)

final_total = (
    order["subtotal"] -
    discount_amount
)

summary = (
    f"Order #{order['id']}\n"
    f"Customer: {order['customer']}\n"
    f"Subtotal: {order['subtotal']:,} تومان\n"
    f"Discount: {order['discount']}%\n"
    f"Final total: {final_total:,.0f} تومان\n"
    f"Status: {order['status']}"
)

print(summary)


# ============================================================
# 46. Summary
# ============================================================

"""
The most important formatting tool in modern Python is the f-string.

Basic syntax:

f"Hello, {name}"

Expressions:

f"Total: {price * quantity}"

Decimal precision:

f"{price:.2f}"

Thousands separator:

f"{price:,}"

Percentage:

f"{progress:.2%}"

Alignment:

f"{text:<10}"
f"{text:>10}"
f"{text:^10}"

Zero padding:

f"{number:05}"

f-strings make dynamic strings easier to read,
especially when building messages, logs, reports,
API responses, and user-facing output.
"""