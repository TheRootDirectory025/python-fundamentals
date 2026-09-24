"""
Python Fundamentals
09 - Files
Topic: JSON Files

This file covers:
- What JSON is
- Python dictionaries and JSON objects
- json.dumps()
- json.loads()
- json.dump()
- json.load()
- Writing JSON files
- Reading JSON files
- Formatting JSON
- Updating JSON data
- Practical API-like examples
"""

import json


# ============================================================
# 1. What Is JSON?
# ============================================================

"""
JSON stands for JavaScript Object Notation.

It is a common format for storing and exchanging data.

Example JSON:

{
    "name": "Mohsen",
    "age": 24,
    "skills": [
        "Python",
        "Django"
    ]
}

JSON is very common in:
- REST APIs
- Web applications
- Configuration files
- Data exchange
- Backend development
"""


# ============================================================
# 2. Python Dictionary
# ============================================================

user = {
    "name": "Mohsen",
    "age": 24,
    "city": "Tehran"
}

print(user)


# ============================================================
# 3. Convert Python Object to JSON String
# ============================================================

json_data = json.dumps(user)

print(json_data)
print(type(json_data))


# json.dumps() converts a Python object into a JSON string.


# ============================================================
# 4. Pretty JSON
# ============================================================

json_data = json.dumps(
    user,
    indent=4
)

print(json_data)


# indent makes JSON easier to read.


# ============================================================
# 5. JSON with Different Data Types
# ============================================================

data = {
    "name": "Mohsen",
    "age": 24,
    "is_student": True,
    "skills": [
        "Python",
        "Django",
        "SQL"
    ],
    "address": None
}

json_data = json.dumps(
    data,
    indent=4
)

print(json_data)


# Python values are converted to JSON values:
#
# True  -> true
# False -> false
# None  -> null


# ============================================================
# 6. Convert JSON String to Python Object
# ============================================================

json_data = """
{
    "name": "Mohsen",
    "age": 24,
    "city": "Tehran"
}
"""

user = json.loads(json_data)

print(user)
print(type(user))


# json.loads() converts a JSON string into a Python object.


# ============================================================
# 7. Access JSON Data
# ============================================================

json_data = """
{
    "name": "Mohsen",
    "age": 24,
    "city": "Tehran"
}
"""

user = json.loads(json_data)

print(user["name"])
print(user["age"])
print(user["city"])


# ============================================================
# 8. JSON Arrays
# ============================================================

json_data = """
[
    "Python",
    "Django",
    "PostgreSQL"
]
"""

skills = json.loads(json_data)

print(skills)
print(type(skills))

for skill in skills:
    print(skill)


# ============================================================
# 9. Nested JSON
# ============================================================

user = {
    "name": "Mohsen",
    "age": 24,
    "address": {
        "city": "Tehran",
        "country": "Iran"
    }
}

json_data = json.dumps(
    user,
    indent=4
)

print(json_data)


# ============================================================
# 10. Access Nested Data
# ============================================================

print(user["address"]["city"])
print(user["address"]["country"])


# ============================================================
# 11. List of Objects
# ============================================================

users = [
    {
        "id": 1,
        "name": "Ali",
        "age": 22
    },
    {
        "id": 2,
        "name": "Sara",
        "age": 25
    },
    {
        "id": 3,
        "name": "Mohsen",
        "age": 24
    }
]

json_data = json.dumps(
    users,
    indent=4
)

print(json_data)


# ============================================================
# 12. Iterate Through JSON-like Data
# ============================================================

for user in users:
    print(
        f"{user['id']}: "
        f"{user['name']} - "
        f"{user['age']}"
    )


# ============================================================
# 13. Writing JSON to a File
# ============================================================

user = {
    "name": "Mohsen",
    "age": 24,
    "skills": [
        "Python",
        "Django",
        "SQL"
    ]
}

with open(
    "user.json",
    "w",
    encoding="utf-8"
) as file:
    json.dump(
        user,
        file,
        indent=4
    )


# json.dump() writes a Python object directly to a file.


# ============================================================
# 14. Reading JSON from a File
# ============================================================

try:
    with open(
        "user.json",
        "r",
        encoding="utf-8"
    ) as file:
        user = json.load(file)

    print(user)

except FileNotFoundError:
    print("JSON file not found.")


# json.load() reads JSON directly from a file.


# ============================================================
# 15. Access Data from JSON File
# ============================================================

try:
    with open(
        "user.json",
        "r",
        encoding="utf-8"
    ) as file:
        user = json.load(file)

    print(f"Name: {user['name']}")
    print(f"Age: {user['age']}")

except FileNotFoundError:
    print("JSON file not found.")


# ============================================================
# 16. JSON File with a List
# ============================================================

users = [
    {
        "name": "Ali",
        "age": 22
    },
    {
        "name": "Sara",
        "age": 25
    },
    {
        "name": "Mohsen",
        "age": 24
    }
]

with open(
    "users.json",
    "w",
    encoding="utf-8"
) as file:
    json.dump(
        users,
        file,
        indent=4
    )


# ============================================================
# 17. Read a List from JSON
# ============================================================

try:
    with open(
        "users.json",
        "r",
        encoding="utf-8"
    ) as file:
        users = json.load(file)

    for user in users:
        print(user["name"])

except FileNotFoundError:
    print("Users file not found.")


# ============================================================
# 18. Updating JSON Data
# ============================================================

try:
    with open(
        "user.json",
        "r",
        encoding="utf-8"
    ) as file:
        user = json.load(file)

    user["age"] = 25

    with open(
        "user.json",
        "w",
        encoding="utf-8"
    ) as file:
        json.dump(
            user,
            file,
            indent=4
        )

    print("User updated successfully.")

except FileNotFoundError:
    print("User file not found.")


# ============================================================
# 19. Adding Data to JSON
# ============================================================

try:
    with open(
        "user.json",
        "r",
        encoding="utf-8"
    ) as file:
        user = json.load(file)

    user["skills"].append("Docker")

    with open(
        "user.json",
        "w",
        encoding="utf-8"
    ) as file:
        json.dump(
            user,
            file,
            indent=4
        )

except FileNotFoundError:
    print("User file not found.")


# ============================================================
# 20. Removing Data from JSON
# ============================================================

try:
    with open(
        "user.json",
        "r",
        encoding="utf-8"
    ) as file:
        user = json.load(file)

    if "age" in user:
        del user["age"]

    with open(
        "user.json",
        "w",
        encoding="utf-8"
    ) as file:
        json.dump(
            user,
            file,
            indent=4
        )

except FileNotFoundError:
    print("User file not found.")


# ============================================================
# 21. sort_keys
# ============================================================

data = {
    "z": 1,
    "a": 2,
    "m": 3
}

json_data = json.dumps(
    data,
    indent=4,
    sort_keys=True
)

print(json_data)


# ============================================================
# 22. ensure_ascii
# ============================================================

data = {
    "name": "محسن"
}

json_data = json.dumps(
    data,
    indent=4,
    ensure_ascii=False
)

print(json_data)


"""
ensure_ascii=False allows Unicode characters
such as Persian text to remain readable.
"""


# ============================================================
# 23. JSON Error Handling
# ============================================================

invalid_json = """
{
    "name": "Mohsen",
    "age":
}
"""

try:
    data = json.loads(invalid_json)

except json.JSONDecodeError as error:
    print(f"Invalid JSON: {error}")


# ============================================================
# 24. Safe JSON File Loading
# ============================================================

def load_json(filename):
    try:
        with open(
            filename,
            "r",
            encoding="utf-8"
        ) as file:
            return json.load(file)

    except FileNotFoundError:
        print(f"File '{filename}' not found.")

    except json.JSONDecodeError:
        print(f"File '{filename}' contains invalid JSON.")

    return None


data = load_json("user.json")

print(data)


# ============================================================
# 25. Safe JSON File Saving
# ============================================================

def save_json(filename, data):
    with open(
        filename,
        "w",
        encoding="utf-8"
    ) as file:
        json.dump(
            data,
            file,
            indent=4,
            ensure_ascii=False
        )


data = {
    "name": "Mohsen",
    "role": "Backend Developer"
}

save_json("profile.json", data)


# ============================================================
# 26. Practical Example: Product Data
# ============================================================

products = [
    {
        "id": 1,
        "name": "Keyboard",
        "price": 1250,
        "stock": 10
    },
    {
        "id": 2,
        "name": "Mouse",
        "price": 650,
        "stock": 25
    }
]

save_json(
    "products.json",
    products
)


# ============================================================
# 27. Read Product Data
# ============================================================

products = load_json("products.json")

if products is not None:
    for product in products:
        print(
            f"{product['name']}: "
            f"{product['price']}"
        )


# ============================================================
# 28. Update Product Stock
# ============================================================

products = load_json("products.json")

if products is not None:
    for product in products:
        if product["id"] == 1:
            product["stock"] -= 1

    save_json(
        "products.json",
        products
    )


# ============================================================
# 29. Practical Example: API-like Response
# ============================================================

response = {
    "status": 200,
    "message": "Success",
    "data": {
        "id": 1,
        "username": "mohsen",
        "email": "mohsen@example.com"
    }
}

json_response = json.dumps(
    response,
    indent=4
)

print(json_response)


# ============================================================
# 30. Reading API-like JSON
# ============================================================

json_response = """
{
    "status": 200,
    "message": "Success",
    "data": {
        "id": 1,
        "username": "mohsen",
        "email": "mohsen@example.com"
    }
}
"""

response = json.loads(json_response)

print(response["status"])
print(response["message"])
print(response["data"]["username"])
print(response["data"]["email"])


# ============================================================
# 31. Practical Example: User Database
# ============================================================

users = [
    {
        "id": 1,
        "username": "ali",
        "active": True
    },
    {
        "id": 2,
        "username": "sara",
        "active": False
    },
    {
        "id": 3,
        "username": "mohsen",
        "active": True
    }
]

save_json(
    "users.json",
    users
)


# ============================================================
# 32. Find a User
# ============================================================

users = load_json("users.json")

if users is not None:
    username = "mohsen"

    found_user = None

    for user in users:
        if user["username"] == username:
            found_user = user
            break

    print(found_user)


# ============================================================
# 33. Filter Active Users
# ============================================================

users = load_json("users.json")

if users is not None:
    active_users = [
        user
        for user in users
        if user["active"]
    ]

    print(active_users)


# ============================================================
# 34. JSON and Python Type Conversion
# ============================================================

"""
Python -> JSON

dict       -> object
list       -> array
str        -> string
int        -> number
float      -> number
True       -> true
False      -> false
None       -> null
"""


# ============================================================
# 35. Practical Example: Configuration File
# ============================================================

config = {
    "app_name": "My Backend",
    "debug": True,
    "port": 8000,
    "database": {
        "host": "localhost",
        "port": 5432
    }
}

save_json(
    "config.json",
    config
)


# ============================================================
# 36. Load Configuration
# ============================================================

config = load_json("config.json")

if config is not None:
    print(f"Application: {config['app_name']}")
    print(f"Debug: {config['debug']}")
    print(f"Port: {config['port']}")


# ============================================================
# 37. Practical Example: Saving Skills
# ============================================================

skills = {
    "backend": [
        "Python",
        "Django",
        "REST API"
    ],
    "database": [
        "SQL",
        "PostgreSQL"
    ],
    "tools": [
        "Git",
        "Docker"
    ]
}

save_json(
    "skills.json",
    skills
)


# ============================================================
# 38. Load Skills
# ============================================================

skills = load_json("skills.json")

if skills is not None:
    for category, items in skills.items():
        print(f"{category}:")
        for item in items:
            print(f"- {item}")


# ============================================================
# 39. JSON and REST APIs
# ============================================================

"""
A typical REST API may return JSON like:

{
    "id": 1,
    "username": "mohsen",
    "email": "mohsen@example.com"
}

A backend application can:

1. Receive JSON from a client.
2. Parse it into Python data.
3. Validate the data.
4. Process the data.
5. Return JSON to the client.

This is one of the reasons JSON is important
for Django REST Framework.
"""


# ============================================================
# 40. Best Practices
# ============================================================

"""
Best practices:

1. Use json.load() for reading JSON from files.
2. Use json.dump() for writing JSON to files.
3. Use json.loads() for parsing a JSON string.
4. Use json.dumps() for creating a JSON string.
5. Use indent=4 when readability matters.
6. Use ensure_ascii=False for readable Unicode text.
7. Handle JSONDecodeError when input may be invalid.
8. Validate important data before using it.
9. Keep JSON structures consistent.
10. Use functions for repeated JSON file operations.
"""


# ============================================================
# 41. Summary
# ============================================================

"""
The four most important functions are:

json.dumps()
    Python object -> JSON string

json.loads()
    JSON string -> Python object

json.dump()
    Python object -> JSON file

json.load()
    JSON file -> Python object

Typical workflow:

Python data
    ↓
json.dump()
    ↓
JSON file

JSON file
    ↓
json.load()
    ↓
Python data

Python data
    ↓
json.dumps()
    ↓
JSON string

JSON string
    ↓
json.loads()
    ↓
Python data
"""