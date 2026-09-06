"""
Python Fundamentals
05 - Data Structures
Topic: Dictionaries

This file covers:
- Creating dictionaries
- Key-value pairs
- Accessing values
- Adding and updating items
- Removing items
- Dictionary methods
- Checking keys and values
- Looping through dictionaries
- Nested dictionaries
- Dictionary unpacking
- Copying dictionaries
- Dictionary comprehensions
- Real-world examples
"""


# ============================================================
# 1. Creating a Dictionary
# ============================================================

student = {
    "name": "Ali",
    "age": 22,
    "major": "Computer Engineering"
}

print(student)


# ============================================================
# 2. Accessing Values
# ============================================================

print(student["name"])
print(student["age"])
print(student["major"])


# ============================================================
# 3. Accessing Values with get()
# ============================================================

# get() is useful when the key may not exist.

print(student.get("name"))
print(student.get("email"))

# We can provide a default value.

print(student.get("email", "Not provided"))


# ============================================================
# 4. Adding a New Item
# ============================================================

student["email"] = "ali@example.com"

print(student)


# ============================================================
# 5. Updating an Existing Item
# ============================================================

student["age"] = 23

print(student)


# ============================================================
# 6. Updating Multiple Items
# ============================================================

student.update({
    "age": 24,
    "city": "Tehran"
})

print(student)


# ============================================================
# 7. Removing an Item with pop()
# ============================================================

student = {
    "name": "Ali",
    "age": 22,
    "major": "Computer Engineering"
}

removed_value = student.pop("age")

print("Removed:", removed_value)
print(student)


# ============================================================
# 8. Removing the Last Item with popitem()
# ============================================================

student = {
    "name": "Ali",
    "age": 22,
    "major": "Computer Engineering"
}

removed_item = student.popitem()

print("Removed:", removed_item)
print(student)


# ============================================================
# 9. Using del
# ============================================================

student = {
    "name": "Ali",
    "age": 22,
    "major": "Computer Engineering"
}

del student["age"]

print(student)


# ============================================================
# 10. Clearing a Dictionary
# ============================================================

student = {
    "name": "Ali",
    "age": 22
}

student.clear()

print(student)


# ============================================================
# 11. Dictionary Length
# ============================================================

student = {
    "name": "Ali",
    "age": 22,
    "major": "Computer Engineering"
}

print("Number of items:", len(student))


# ============================================================
# 12. Checking if a Key Exists
# ============================================================

print("name" in student)
print("email" in student)


# ============================================================
# 13. Checking if a Key Does Not Exist
# ============================================================

print("email" not in student)


# ============================================================
# 14. Getting All Keys
# ============================================================

print(student.keys())


# ============================================================
# 15. Getting All Values
# ============================================================

print(student.values())


# ============================================================
# 16. Getting Key-Value Pairs
# ============================================================

print(student.items())


# ============================================================
# 17. Looping Through Keys
# ============================================================

for key in student:
    print(key)


# ============================================================
# 18. Looping Through Values
# ============================================================

for value in student.values():
    print(value)


# ============================================================
# 19. Looping Through Keys and Values
# ============================================================

for key, value in student.items():
    print(f"{key}: {value}")


# ============================================================
# 20. Nested Dictionaries
# ============================================================

user = {
    "name": "Mohsen",
    "age": 24,
    "address": {
        "city": "Tehran",
        "country": "Iran"
    }
}

print(user["name"])
print(user["address"]["city"])


# ============================================================
# 21. List of Dictionaries
# ============================================================

users = [
    {
        "name": "Ali",
        "age": 22
    },
    {
        "name": "Sara",
        "age": 24
    },
    {
        "name": "Reza",
        "age": 21
    }
]

for user in users:
    print(user["name"])


# ============================================================
# 22. Updating a Dictionary Inside a List
# ============================================================

users[0]["age"] = 23

print(users[0])


# ============================================================
# 23. Copying a Dictionary
# ============================================================

original = {
    "name": "Ali",
    "age": 22
}

copied = original.copy()

copied["age"] = 25

print("Original:", original)
print("Copied:", copied)


# ============================================================
# 24. Dictionary from Two Lists
# ============================================================

keys = ["name", "age", "city"]
values = ["Ali", 22, "Tehran"]

person = dict(zip(keys, values))

print(person)


# ============================================================
# 25. Dictionary Comprehension
# ============================================================

numbers = [1, 2, 3, 4, 5]

squares = {
    number: number ** 2
    for number in numbers
}

print(squares)


# ============================================================
# 26. Dictionary Comprehension with a Condition
# ============================================================

numbers = [1, 2, 3, 4, 5, 6]

even_squares = {
    number: number ** 2
    for number in numbers
    if number % 2 == 0
}

print(even_squares)


# ============================================================
# 27. Real-World Example: Product
# ============================================================

product = {
    "id": 101,
    "name": "Keyboard",
    "price": 50,
    "stock": 12
}

print(f"Product: {product['name']}")
print(f"Price: ${product['price']}")
print(f"Stock: {product['stock']}")


# ============================================================
# 28. Real-World Example: Shopping Cart
# ============================================================

cart = [
    {
        "name": "Keyboard",
        "price": 50,
        "quantity": 2
    },
    {
        "name": "Mouse",
        "price": 25,
        "quantity": 1
    }
]

total_price = 0

for item in cart:
    item_total = item["price"] * item["quantity"]
    total_price += item_total

print("Total price:", total_price)


# ============================================================
# 29. Real-World Example: User Profile
# ============================================================

user = {
    "username": "mohsen",
    "email": "mohsen@example.com",
    "is_active": True,
    "skills": ["Python", "Django", "SQL"]
}

print("Username:", user["username"])
print("Email:", user["email"])
print("Active:", user["is_active"])
print("Skills:", user["skills"])


# ============================================================
# 30. Real-World Example: API-Like Data
# ============================================================

response = {
    "status": "success",
    "data": {
        "id": 101,
        "username": "ali",
        "email": "ali@example.com"
    }
}

print(response["status"])
print(response["data"]["username"])


# ============================================================
# Important Notes
# ============================================================

"""
Dictionaries are:

- Mutable
- Key-value based
- Keys must be unique
- Keys must be hashable
- Values can be any data type

Common methods:

get()
keys()
values()
items()
update()
pop()
popitem()
clear()
copy()

Useful operations:

key in dictionary
key not in dictionary

Dictionaries are especially important when working with:

- JSON
- REST APIs
- Database records
- Configuration data
- User information
"""