"""
Python Fundamentals
06 - Functions
Topic: Function Fundamentals

This file covers:
- Defining and calling functions
- Parameters and arguments
- Return values
- print() vs return
- Default parameters
- Local and global scope
- Multiple return values
- Function docstrings
- Basic type hints
- Functions with conditions and loops
- Practical function examples
"""


# ============================================================
# 1. Defining a Function
# ============================================================

def say_hello():
    print("Hello, Python!")


# ============================================================
# 2. Calling a Function
# ============================================================

say_hello()
say_hello()


# ============================================================
# 3. Function with a Parameter
# ============================================================

def greet(name):
    print(f"Hello, {name}!")


greet("Mohsen")
greet("Ali")


# ============================================================
# 4. Multiple Parameters
# ============================================================

def introduce(name, age):
    print(f"My name is {name} and I am {age} years old.")


introduce("Mohsen", 23)


# ============================================================
# 5. Return Values
# ============================================================

def add_numbers(a, b):
    return a + b


result = add_numbers(10, 20)

print(result)


# ============================================================
# 6. print() vs return
# ============================================================

def add_with_print(a, b):
    print(a + b)


def add_with_return(a, b):
    return a + b


# print() displays the result
add_with_print(5, 3)

# return gives the result back to the caller
result = add_with_return(5, 3)

print(result)


# A returned value can be reused
total = add_with_return(10, 20)

double_total = total * 2

print(double_total)


# ============================================================
# 7. Default Parameters
# ============================================================

def greet_user(name, message="Welcome"):
    print(f"{message}, {name}!")


greet_user("Mohsen")
greet_user("Ali", "Good morning")


# ============================================================
# 8. Local Variables
# ============================================================

def calculate_price():
    price = 100
    tax = 10

    total = price + tax

    return total


print(calculate_price())


# price only exists inside calculate_price()
# print(price)  # This would raise a NameError


# ============================================================
# 9. Global Variables
# ============================================================

tax_rate = 0.09


def calculate_tax(price):
    tax = price * tax_rate
    return tax


print(calculate_tax(1000))


# ============================================================
# 10. Local vs Global Scope
# ============================================================

name = "Global Mohsen"


def show_name():
    name = "Local Mohsen"
    print(name)


show_name()

print(name)


# ============================================================
# 11. Multiple Return Values
# ============================================================

def calculate_numbers(a, b):
    total = a + b
    difference = a - b
    product = a * b

    return total, difference, product


result = calculate_numbers(10, 5)

print(result)


total, difference, product = calculate_numbers(10, 5)

print(total)
print(difference)
print(product)


# ============================================================
# 12. Function with a Condition
# ============================================================

def check_age(age):
    if age >= 18:
        return "Adult"

    return "Minor"


print(check_age(20))
print(check_age(15))


# ============================================================
# 13. Function with Multiple Conditions
# ============================================================

def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"

    return "F"


print(get_grade(95))
print(get_grade(72))
print(get_grade(45))


# ============================================================
# 14. Function with a Loop
# ============================================================

def calculate_sum(numbers):
    total = 0

    for number in numbers:
        total += number

    return total


numbers = [10, 20, 30, 40]

print(calculate_sum(numbers))


# ============================================================
# 15. Calculate Average
# ============================================================

def calculate_average(numbers):
    if len(numbers) == 0:
        return 0

    total = 0

    for number in numbers:
        total += number

    return total / len(numbers)


scores = [18, 17, 20, 15, 19]

average = calculate_average(scores)

print(f"Average: {average}")


# ============================================================
# 16. Check Even Number
# ============================================================

def is_even(number):
    return number % 2 == 0


print(is_even(10))
print(is_even(7))


# ============================================================
# 17. Find Maximum Number
# ============================================================

def find_max(numbers):
    if len(numbers) == 0:
        return None

    maximum = numbers[0]

    for number in numbers:
        if number > maximum:
            maximum = number

    return maximum


numbers = [12, 45, 7, 89, 23]

print(find_max(numbers))


# ============================================================
# 18. Function Documentation
# ============================================================

def calculate_discount(price, discount):
    """
    Calculate the final price after applying a discount.

    Args:
        price: Original price.
        discount: Discount percentage.

    Returns:
        Final price after applying the discount.
    """

    discount_amount = price * discount / 100

    return price - discount_amount


final_price = calculate_discount(1000, 20)

print(final_price)


# ============================================================
# 19. Basic Type Hints
# ============================================================

def multiply(a: int, b: int) -> int:
    return a * b


result = multiply(5, 4)

print(result)


def format_name(first_name: str, last_name: str) -> str:
    return f"{first_name} {last_name}"


full_name = format_name("Mohsen", "Bagheri")

print(full_name)


# ============================================================
# 20. Function Returning a Boolean
# ============================================================

def is_adult(age: int) -> bool:
    return age >= 18


age = 22

if is_adult(age):
    print("User is an adult.")
else:
    print("User is a minor.")


# ============================================================
# 21. Function with a List
# ============================================================

def calculate_total(prices):
    total = 0

    for price in prices:
        total += price

    return total


cart = [120, 350, 80, 200]

total = calculate_total(cart)

print(f"Cart total: {total}")


# ============================================================
# 22. Function with a Dictionary
# ============================================================

def format_user(user):
    return f"{user['name']} - {user['email']}"


user = {
    "name": "Mohsen",
    "email": "mohsen@example.com"
}

print(format_user(user))


# ============================================================
# 23. Practical Example: Shopping Cart
# ============================================================

def calculate_cart_total(cart):
    total = 0

    for item in cart:
        total += item["price"] * item["quantity"]

    return total


cart = [
    {"name": "Keyboard", "price": 50, "quantity": 2},
    {"name": "Mouse", "price": 25, "quantity": 1},
    {"name": "Headset", "price": 80, "quantity": 1},
]

cart_total = calculate_cart_total(cart)

print(f"Total: ${cart_total}")


# ============================================================
# 24. Practical Example: User Information
# ============================================================

def get_user_info(name, age, city):
    return {
        "name": name,
        "age": age,
        "city": city
    }


user = get_user_info("Mohsen", 24, "Tehran")

print(user)


# ============================================================
# 25. Practical Example: Login Check
# ============================================================

def check_login(username, password):
    correct_username = "admin"
    correct_password = "1234"

    if username == correct_username and password == correct_password:
        return True

    return False


if check_login("admin", "1234"):
    print("Login successful.")
else:
    print("Invalid username or password.")


# ============================================================
# 26. Placeholder Function with pass
# ============================================================

def future_feature():
    pass


# The function can be implemented later.


# ============================================================
# 27. Functions Calling Other Functions
# ============================================================

def calculate_total_price(price, quantity):
    return price * quantity


def calculate_order_total(items):
    total = 0

    for item in items:
        total += calculate_total_price(
            item["price"],
            item["quantity"]
        )

    return total


items = [
    {"price": 100, "quantity": 2},
    {"price": 50, "quantity": 3},
]

order_total = calculate_order_total(items)

print(f"Order total: {order_total}")


# ============================================================
# 28. Why Functions Matter
# ============================================================

"""
Functions help us:

- Reuse code
- Avoid repetition
- Organize programs
- Improve readability
- Make testing easier
- Separate responsibilities
- Build larger applications from smaller components

A good function should generally have one clear responsibility.
"""


# ============================================================
# 29. Final Practical Example
# ============================================================

def calculate_order_summary(items, discount=0):
    subtotal = calculate_order_total(items)

    discount_amount = subtotal * discount / 100

    final_total = subtotal - discount_amount

    return subtotal, discount_amount, final_total


items = [
    {"price": 120, "quantity": 2},
    {"price": 80, "quantity": 1},
    {"price": 50, "quantity": 3},
]

subtotal, discount_amount, final_total = calculate_order_summary(
    items,
    discount=10
)

print(f"Subtotal: {subtotal}")
print(f"Discount: {discount_amount}")
print(f"Final total: {final_total}")