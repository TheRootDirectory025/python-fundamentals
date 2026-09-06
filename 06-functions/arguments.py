"""
Python Fundamentals
06 - Functions
Topic: Function Arguments

This file covers:
- Positional arguments
- Keyword arguments
- Default arguments
- Mixing positional and keyword arguments
- Argument order
- Passing lists and dictionaries to functions
- Mutable objects as arguments
- *args
- **kwargs
- Combining *args and **kwargs
"""


# ============================================================
# 1. Positional Arguments
# ============================================================

def introduce(name, age):
    print(f"Name: {name}")
    print(f"Age: {age}")


introduce("Mohsen", 24)


# ============================================================
# 2. Argument Order Matters
# ============================================================

def show_information(name, city):
    print(f"Name: {name}")
    print(f"City: {city}")


show_information("Mohsen", "Tehran")

# The following would produce a different result
# because the arguments are passed in a different order.
show_information("Tehran", "Mohsen")


# ============================================================
# 3. Keyword Arguments
# ============================================================

def create_user(name, age, city):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"City: {city}")


create_user(
    name="Mohsen",
    age=24,
    city="Tehran"
)


# ============================================================
# 4. Keyword Arguments Ignore Position
# ============================================================

create_user(
    city="Tehran",
    name="Mohsen",
    age=24
)


# ============================================================
# 5. Positional and Keyword Arguments Together
# ============================================================

def calculate_price(price, quantity, discount):
    total = price * quantity
    discount_amount = total * discount / 100

    return total - discount_amount


result = calculate_price(
    100,
    quantity=2,
    discount=10
)

print(result)


# ============================================================
# 6. Positional Arguments Must Come Before Keyword Arguments
# ============================================================

# Correct:
result = calculate_price(
    100,
    quantity=2,
    discount=10
)

print(result)

# Incorrect:
# calculate_price(
#     price=100,
#     2,
#     discount=10
# )

# Positional arguments cannot appear after keyword arguments.


# ============================================================
# 7. Default Arguments
# ============================================================

def greet(name, message="Welcome"):
    print(f"{message}, {name}!")


greet("Mohsen")

greet(
    "Mohsen",
    "Good morning"
)


# ============================================================
# 8. Multiple Default Arguments
# ============================================================

def create_profile(
    name,
    age=18,
    city="Unknown"
):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"City: {city}")


create_profile("Mohsen")

create_profile(
    "Ali",
    22
)

create_profile(
    "Sara",
    25,
    "Tehran"
)


# ============================================================
# 9. Overriding Default Arguments with Keyword Arguments
# ============================================================

create_profile(
    name="Mohsen",
    city="Tehran"
)


# ============================================================
# 10. Passing a List as an Argument
# ============================================================

def print_scores(scores):
    for score in scores:
        print(score)


scores = [18, 20, 15, 17]

print_scores(scores)


# ============================================================
# 11. Passing a Dictionary as an Argument
# ============================================================

def print_user(user):
    print(f"Name: {user['name']}")
    print(f"Email: {user['email']}")


user = {
    "name": "Mohsen",
    "email": "mohsen@example.com"
}

print_user(user)


# ============================================================
# 12. Passing Multiple Lists
# ============================================================

def calculate_average(scores):
    if not scores:
        return 0

    total = sum(scores)

    return total / len(scores)


student_scores = [18, 17, 20, 15, 19]

average = calculate_average(student_scores)

print(f"Average: {average}")


# ============================================================
# 13. Mutable Objects as Arguments
# ============================================================

def add_item(items, item):
    items.append(item)


shopping_list = ["Keyboard", "Mouse"]

add_item(shopping_list, "Headset")

print(shopping_list)


# Lists are mutable, so the original list is changed.


# ============================================================
# 14. Modifying a Dictionary Inside a Function
# ============================================================

def update_user(user):
    user["active"] = True


user = {
    "name": "Mohsen",
    "email": "mohsen@example.com"
}

update_user(user)

print(user)


# ============================================================
# 15. Immutable Objects as Arguments
# ============================================================

def increase_number(number):
    number += 10

    print(f"Inside function: {number}")


number = 20

increase_number(number)

print(f"Outside function: {number}")


# The original integer does not change because integers are immutable.


# ============================================================
# 16. Variable-Length Arguments with *args
# ============================================================

def calculate_sum(*numbers):
    total = 0

    for number in numbers:
        total += number

    return total


print(calculate_sum(1, 2))
print(calculate_sum(1, 2, 3))
print(calculate_sum(1, 2, 3, 4, 5))


# *args collects positional arguments into a tuple.


# ============================================================
# 17. Inspecting *args
# ============================================================

def show_args(*args):
    print(args)
    print(type(args))


show_args(10, 20, 30)


# ============================================================
# 18. Looping Through *args
# ============================================================

def print_numbers(*numbers):
    for number in numbers:
        print(number)


print_numbers(10, 20, 30, 40)


# ============================================================
# 19. Practical Example with *args
# ============================================================

def calculate_average_args(*scores):
    if not scores:
        return 0

    return sum(scores) / len(scores)


average = calculate_average_args(
    18,
    20,
    17,
    19
)

print(f"Average: {average}")


# ============================================================
# 20. Keyword Variable-Length Arguments with **kwargs
# ============================================================

def show_user(**kwargs):
    print(kwargs)
    print(type(kwargs))


show_user(
    name="Mohsen",
    age=24,
    city="Tehran"
)


# **kwargs collects keyword arguments into a dictionary.


# ============================================================
# 21. Looping Through **kwargs
# ============================================================

def print_user_info(**user):
    for key, value in user.items():
        print(f"{key}: {value}")


print_user_info(
    name="Mohsen",
    age=24,
    city="Tehran"
)


# ============================================================
# 22. Practical Example with **kwargs
# ============================================================

def create_product(**product):
    return product


product = create_product(
    name="Keyboard",
    price=50,
    category="Accessories"
)

print(product)


# ============================================================
# 23. Combining Normal Arguments and *args
# ============================================================

def greet_students(teacher, *students):
    print(f"Teacher: {teacher}")

    for student in students:
        print(f"Student: {student}")


greet_students(
    "Dr. Ahmadi",
    "Ali",
    "Sara",
    "Mohsen"
)


# ============================================================
# 24. Combining Normal Arguments and **kwargs
# ============================================================

def create_account(username, **details):
    print(f"Username: {username}")

    for key, value in details.items():
        print(f"{key}: {value}")


create_account(
    "mohsen",
    email="mohsen@example.com",
    city="Tehran",
    active=True
)


# ============================================================
# 25. Combining *args and **kwargs
# ============================================================

def show_data(*args, **kwargs):
    print("Positional arguments:")

    for value in args:
        print(value)

    print("Keyword arguments:")

    for key, value in kwargs.items():
        print(f"{key}: {value}")


show_data(
    10,
    20,
    30,
    name="Mohsen",
    city="Tehran"
)


# ============================================================
# 26. Unpacking a List into Function Arguments
# ============================================================

def add(a, b, c):
    return a + b + c


numbers = [10, 20, 30]

result = add(*numbers)

print(result)


# * unpacks the list into positional arguments.


# ============================================================
# 27. Unpacking a Dictionary into Keyword Arguments
# ============================================================

def create_user(name, age, city):
    return {
        "name": name,
        "age": age,
        "city": city
    }


user_data = {
    "name": "Mohsen",
    "age": 24,
    "city": "Tehran"
}

user = create_user(**user_data)

print(user)


# ** unpacks dictionary keys into keyword arguments.


# ============================================================
# 28. Practical Example: Shopping Cart
# ============================================================

def calculate_total(*prices):
    return sum(prices)


total = calculate_total(
    100,
    250,
    80,
    120
)

print(f"Total: {total}")


# ============================================================
# 29. Practical Example: Product Creation
# ============================================================

def create_product(name, price, **attributes):
    product = {
        "name": name,
        "price": price
    }

    product.update(attributes)

    return product


product = create_product(
    "Laptop",
    1200,
    brand="ASUS",
    ram="16GB",
    storage="512GB SSD"
)

print(product)


# ============================================================
# 30. Argument Passing in Real Applications
# ============================================================

def send_email(
    recipient,
    subject,
    message,
    priority="normal"
):
    print(f"To: {recipient}")
    print(f"Subject: {subject}")
    print(f"Priority: {priority}")
    print(f"Message: {message}")


send_email(
    "user@example.com",
    "Welcome",
    "Welcome to our platform!"
)


send_email(
    recipient="admin@example.com",
    subject="System Alert",
    message="Server requires attention.",
    priority="high"
)


# ============================================================
# 31. Argument Rules Summary
# ============================================================

"""
Important rules:

1. Required parameters must receive a value.
2. Positional arguments are matched by position.
3. Keyword arguments are matched by parameter name.
4. Positional arguments should come before keyword arguments.
5. Default parameters provide fallback values.
6. *args collects extra positional arguments into a tuple.
7. **kwargs collects extra keyword arguments into a dictionary.
8. * can unpack a sequence into positional arguments.
9. ** can unpack a dictionary into keyword arguments.
"""


# ============================================================
# 32. Final Practical Example
# ============================================================

def create_order(customer, *items, discount=0, **metadata):
    subtotal = sum(item["price"] * item["quantity"] for item in items)

    discount_amount = subtotal * discount / 100

    total = subtotal - discount_amount

    order = {
        "customer": customer,
        "items": items,
        "subtotal": subtotal,
        "discount": discount_amount,
        "total": total,
        "metadata": metadata
    }

    return order


order = create_order(
    "Mohsen",
    {"name": "Keyboard", "price": 50, "quantity": 2},
    {"name": "Mouse", "price": 25, "quantity": 1},
    discount=10,
    payment_method="card",
    status="pending"
)

print(order)