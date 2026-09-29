"""
Python Fundamentals
13 - File Handling
Topic: JSON Files

This file covers:
- What JSON is
- JSON structure
- json.dumps()
- json.loads()
- json.dump()
- json.load()
- Reading JSON files
- Writing JSON files
- JSON objects and arrays
- Converting JSON to Python objects
- Converting Python objects to JSON
- Nested JSON data
- Pretty-printing JSON
- JSON validation basics
- Practical backend examples
- Best practices
"""


# ============================================================
# 1. What Is JSON?
# ============================================================

"""
JSON stands for JavaScript Object Notation.

JSON is a text-based format commonly used to store
and exchange structured data.

Example:

{
    "name": "Mohsen",
    "age": 24,
    "role": "Backend Developer"
}

JSON is widely used in:

- REST APIs
- Web applications
- Configuration files
- Data exchange
- Database exports
- Application settings
"""


# ============================================================
# 2. Importing the json Module
# ============================================================

import json


"""
The json module is part of Python's standard library.

No external package is required.
"""


# ============================================================
# 3. JSON Objects
# ============================================================

"""
A JSON object is similar to a Python dictionary.

JSON:

{
    "name": "Mohsen",
    "age": 24
}

Python:

{
    "name": "Mohsen",
    "age": 24
}
"""


# ============================================================
# 4. JSON Data Types
# ============================================================

"""
JSON supports:

String
Number
Boolean
Null
Object
Array

Examples:

String:
"name"

Number:
24

Boolean:
true

Null:
null

Object:
{
    "name": "Mohsen"
}

Array:
[
    "Python",
    "Django",
    "SQL"
]
"""


# ============================================================
# 5. Python Data Types and JSON
# ============================================================

"""
Python              JSON

dict                object
list                array
tuple               array
str                 string
int                 number
float               number
True                true
False               false
None                null
"""


# ============================================================
# 6. Python Dictionary to JSON String
# ============================================================

user = {
    "name": "Mohsen",
    "age": 24,
    "role": "Backend Developer"
}

json_string = json.dumps(user)

print(json_string)


"""
dumps() converts a Python object into a JSON string.
"""


# ============================================================
# 7. Pretty JSON
# ============================================================

json_string = json.dumps(
    user,
    indent=4
)

print(json_string)


"""
indent=4 makes the JSON easier to read.

Without indentation:

{"name": "Mohsen", "age": 24, "role": "Backend Developer"}

With indentation:

{
    "name": "Mohsen",
    "age": 24,
    "role": "Backend Developer"
}
"""


# ============================================================
# 8. Sorting JSON Keys
# ============================================================

json_string = json.dumps(
    user,
    indent=4,
    sort_keys=True
)

print(json_string)


"""
sort_keys=True sorts object keys alphabetically.
"""


# ============================================================
# 9. Python List to JSON
# ============================================================

skills = [
    "Python",
    "Django",
    "PostgreSQL",
    "Docker"
]

json_string = json.dumps(
    skills,
    indent=4
)

print(json_string)


# ============================================================
# 10. Python Boolean and None
# ============================================================

data = {
    "is_active": True,
    "is_admin": False,
    "last_login": None
}

json_string = json.dumps(
    data,
    indent=4
)

print(json_string)


"""
Python:

True
False
None

become:

true
false
null

in JSON.
"""


# ============================================================
# 11. JSON String to Python Object
# ============================================================

json_string = """
{
    "name": "Mohsen",
    "age": 24,
    "role": "Backend Developer"
}
"""

user = json.loads(json_string)

print(user)
print(type(user))


"""
loads() converts a JSON string into a Python object.

JSON string -> Python dictionary
"""


# ============================================================
# 12. Accessing Parsed JSON
# ============================================================

json_string = """
{
    "name": "Mohsen",
    "age": 24,
    "role": "Backend Developer"
}
"""

user = json.loads(json_string)

print(user["name"])
print(user["age"])
print(user["role"])


# ============================================================
# 13. JSON Array to Python List
# ============================================================

json_string = """
[
    "Python",
    "Django",
    "PostgreSQL",
    "Docker"
]
"""

skills = json.loads(json_string)

print(skills)
print(type(skills))


# ============================================================
# 14. Nested JSON
# ============================================================

json_string = """
{
    "name": "Mohsen",
    "profile": {
        "age": 24,
        "city": "Tehran"
    },
    "skills": [
        "Python",
        "Django",
        "SQL"
    ]
}
"""

user = json.loads(json_string)

print(user["name"])
print(user["profile"]["age"])
print(user["profile"]["city"])
print(user["skills"])


# ============================================================
# 15. Nested Python Dictionary
# ============================================================

user = {
    "id": 1,
    "name": "Mohsen",
    "profile": {
        "age": 24,
        "city": "Tehran"
    },
    "skills": [
        "Python",
        "Django",
        "SQL"
    ]
}

json_string = json.dumps(
    user,
    indent=4
)

print(json_string)


# ============================================================
# 16. Writing JSON to a File
# ============================================================

user = {
    "id": 1,
    "name": "Mohsen",
    "age": 24,
    "role": "Backend Developer"
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


"""
dump() writes a Python object directly
into a JSON file.
"""


# ============================================================
# 17. Reading JSON from a File
# ============================================================

with open(
    "user.json",
    "r",
    encoding="utf-8"
) as file:

    user = json.load(file)

    print(user)


"""
load() reads JSON directly from a file
and converts it into a Python object.
"""


# ============================================================
# 18. dump() vs dumps()
# ============================================================

"""
json.dump()

Python object -> JSON file

Example:

json.dump(data, file)


json.dumps()

Python object -> JSON string

Example:

json_string = json.dumps(data)
"""


# ============================================================
# 19. load() vs loads()
# ============================================================

"""
json.load()

JSON file -> Python object

Example:

data = json.load(file)


json.loads()

JSON string -> Python object

Example:

data = json.loads(json_string)
"""


# ============================================================
# 20. Pretty JSON File
# ============================================================

data = {
    "project": "Python Fundamentals",
    "language": "Python",
    "topics": [
        "Functions",
        "OOP",
        "File Handling"
    ]
}

with open(
    "project.json",
    "w",
    encoding="utf-8"
) as file:

    json.dump(
        data,
        file,
        indent=4
    )


# ============================================================
# 21. Preserving Non-ASCII Characters
# ============================================================

data = {
    "name": "محسن",
    "role": "مهندس نرم افزار"
}

with open(
    "persian-user.json",
    "w",
    encoding="utf-8"
) as file:

    json.dump(
        data,
        file,
        indent=4,
        ensure_ascii=False
    )


"""
ensure_ascii=False keeps non-ASCII characters readable.

Without it, Persian characters may be represented
using Unicode escape sequences.
"""


# ============================================================
# 22. Reading Persian JSON
# ============================================================

with open(
    "persian-user.json",
    "r",
    encoding="utf-8"
) as file:

    user = json.load(file)

    print(user["name"])
    print(user["role"])


# ============================================================
# 23. List of Users
# ============================================================

users = [
    {
        "id": 1,
        "name": "Mohsen",
        "role": "Backend Developer"
    },
    {
        "id": 2,
        "name": "Ali",
        "role": "Android Developer"
    },
    {
        "id": 3,
        "name": "Sara",
        "role": "Frontend Developer"
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
# 24. Reading a List of Users
# ============================================================

with open(
    "users.json",
    "r",
    encoding="utf-8"
) as file:

    users = json.load(file)

    for user in users:

        print(
            f"{user['id']} - "
            f"{user['name']} - "
            f"{user['role']}"
        )


# ============================================================
# 25. Searching JSON Data
# ============================================================

with open(
    "users.json",
    "r",
    encoding="utf-8"
) as file:

    users = json.load(file)

    for user in users:

        if user["role"] == "Backend Developer":
            print(user)


# ============================================================
# 26. Updating JSON Data
# ============================================================

with open(
    "users.json",
    "r",
    encoding="utf-8"
) as file:

    users = json.load(file)


for user in users:

    if user["id"] == 1:
        user["role"] = "Python Backend Developer"


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
# 27. Adding an Item to JSON Data
# ============================================================

with open(
    "users.json",
    "r",
    encoding="utf-8"
) as file:

    users = json.load(file)


new_user = {
    "id": 4,
    "name": "Reza",
    "role": "Python Developer"
}

users.append(new_user)


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
# 28. Removing an Item from JSON Data
# ============================================================

with open(
    "users.json",
    "r",
    encoding="utf-8"
) as file:

    users = json.load(file)


users = [
    user
    for user in users
    if user["id"] != 4
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
# 29. Handling FileNotFoundError
# ============================================================

try:

    with open(
        "missing.json",
        "r",
        encoding="utf-8"
    ) as file:

        data = json.load(file)

except FileNotFoundError:

    print("JSON file was not found.")


# ============================================================
# 30. Handling JSONDecodeError
# ============================================================

invalid_json = """
{
    "name": "Mohsen",
    "age":
}
"""

try:

    data = json.loads(invalid_json)

except json.JSONDecodeError:

    print("Invalid JSON data.")


"""
JSONDecodeError occurs when Python cannot parse
the provided JSON data.
"""


# ============================================================
# 31. Handling Invalid JSON File
# ============================================================

try:

    with open(
        "data.json",
        "r",
        encoding="utf-8"
    ) as file:

        data = json.load(file)

except FileNotFoundError:

    print("File does not exist.")

except json.JSONDecodeError:

    print("File contains invalid JSON.")


# ============================================================
# 32. Practical Example: Application Configuration
# ============================================================

config = {
    "application": {
        "name": "My Backend",
        "version": "1.0.0"
    },
    "database": {
        "host": "localhost",
        "port": 5432,
        "name": "my_database"
    },
    "debug": True
}


with open(
    "config.json",
    "w",
    encoding="utf-8"
) as file:

    json.dump(
        config,
        file,
        indent=4
    )


# ============================================================
# 33. Reading Application Configuration
# ============================================================

try:

    with open(
        "config.json",
        "r",
        encoding="utf-8"
    ) as file:

        config = json.load(file)

        database = config["database"]

        print(
            database["host"]
        )

        print(
            database["port"]
        )

except (
    FileNotFoundError,
    json.JSONDecodeError
):

    print(
        "Could not load configuration."
    )


# ============================================================
# 34. Practical Example: Product Data
# ============================================================

products = [
    {
        "id": 1,
        "name": "Laptop",
        "price": 1200,
        "stock": 5
    },
    {
        "id": 2,
        "name": "Keyboard",
        "price": 80,
        "stock": 20
    },
    {
        "id": 3,
        "name": "Mouse",
        "price": 40,
        "stock": 30
    }
]


with open(
    "products.json",
    "w",
    encoding="utf-8"
) as file:

    json.dump(
        products,
        file,
        indent=4
    )


# ============================================================
# 35. Filtering Products
# ============================================================

with open(
    "products.json",
    "r",
    encoding="utf-8"
) as file:

    products = json.load(file)


for product in products:

    if product["price"] < 100:

        print(
            product["name"]
        )


# ============================================================
# 36. Updating Product Stock
# ============================================================

with open(
    "products.json",
    "r",
    encoding="utf-8"
) as file:

    products = json.load(file)


for product in products:

    if product["id"] == 1:
        product["stock"] -= 1


with open(
    "products.json",
    "w",
    encoding="utf-8"
) as file:

    json.dump(
        products,
        file,
        indent=4
    )


# ============================================================
# 37. JSON and APIs
# ============================================================

"""
A typical REST API response may look like:

{
    "id": 1,
    "name": "Mohsen",
    "role": "Backend Developer"
}

A client application can receive this data and
convert it into an object.

For example:

Python backend
        |
        | JSON
        v
Android / Flutter / Web client

JSON is one of the most common formats for
communication between backend and frontend.
"""


# ============================================================
# 38. Example API-Like Response
# ============================================================

api_response = {
    "status": "success",
    "data": {
        "id": 1,
        "name": "Mohsen",
        "role": "Backend Developer"
    }
}


json_response = json.dumps(
    api_response,
    indent=4
)

print(json_response)


# ============================================================
# 39. JSON Serialization
# ============================================================

"""
Serialization means converting an object into a format
that can be stored or transmitted.

Example:

Python dictionary
        |
        v
JSON string
        |
        v
File / API / Network


json.dumps() performs JSON serialization.
"""


# ============================================================
# 40. JSON Deserialization
# ============================================================

"""
Deserialization means converting stored or transmitted
data back into a Python object.

Example:

JSON string
        |
        v
Python dictionary


json.loads() performs JSON deserialization.
"""


# ============================================================
# 41. Serialization and Deserialization Example
# ============================================================

user = {
    "id": 1,
    "name": "Mohsen",
    "skills": [
        "Python",
        "Django",
        "SQL"
    ]
}


serialized_user = json.dumps(user)

print(serialized_user)


deserialized_user = json.loads(
    serialized_user
)

print(deserialized_user)

print(
    deserialized_user["skills"]
)


# ============================================================
# 42. Handling Unsupported Python Objects
# ============================================================

from datetime import datetime


data = {
    "created_at": datetime.now()
}


"""
The standard JSON encoder cannot automatically serialize
every Python object.

For example, datetime objects require conversion
before being stored as JSON.
"""


# ============================================================
# 43. Converting datetime to String
# ============================================================

data = {
    "created_at": datetime.now().isoformat()
}


json_string = json.dumps(
    data,
    indent=4
)

print(json_string)


"""
A common solution is converting datetime into
an ISO 8601 string before JSON serialization.
"""


# ============================================================
# 44. JSON and None
# ============================================================

data = {
    "name": "Mohsen",
    "email": None
}


json_string = json.dumps(
    data,
    indent=4
)

print(json_string)


"""
Python:

None

becomes JSON:

null
"""


# ============================================================
# 45. JSON and Boolean Values
# ============================================================

data = {
    "is_active": True,
    "is_verified": False
}


json_string = json.dumps(
    data,
    indent=4
)

print(json_string)


"""
Python:

True
False

become JSON:

true
false
"""


# ============================================================
# 46. Compact JSON
# ============================================================

data = {
    "name": "Mohsen",
    "age": 24
}


json_string = json.dumps(
    data,
    separators=(
        ",",
        ":"
    )
)

print(json_string)


"""
Compact JSON can be useful when reducing unnecessary
whitespace in transmitted data.
"""


# ============================================================
# 47. JSON File Structure
# ============================================================

"""
A JSON file can contain an object:

{
    "name": "Mohsen"
}


or an array:

[
    {
        "id": 1,
        "name": "Mohsen"
    },
    {
        "id": 2,
        "name": "Ali"
    }
]
"""


# ============================================================
# 48. JSON Best Practices
# ============================================================

"""
Best practices:

1. Use the json module instead of manually creating
   JSON strings.
2. Use json.dump() for JSON files.
3. Use json.load() to read JSON files.
4. Use json.dumps() for JSON strings.
5. Use json.loads() for JSON strings received as input.
6. Use UTF-8 for text files.
7. Use ensure_ascii=False when Persian or other
   non-ASCII text should remain readable.
8. Handle JSONDecodeError when parsing external data.
9. Validate external JSON before trusting its content.
10. Keep JSON structures consistent.
11. Avoid unnecessarily deep nested structures.
12. Use databases instead of large JSON files for
    application data that needs querying and relationships.
13. Never store secrets such as passwords or API keys
    in publicly exposed JSON files.
"""


# ============================================================
# 49. Backend Development Relevance
# ============================================================

"""
JSON is extremely important in backend development.

You will encounter JSON when working with:

- REST APIs
- Django REST Framework
- HTTP requests
- HTTP responses
- Authentication APIs
- Configuration
- Frontend communication
- Mobile applications
- Third-party APIs

A typical backend flow:

Client
    |
    | HTTP Request
    v
Django / DRF
    |
    | JSON Response
    v
Client


Understanding JSON is therefore an essential foundation
before learning REST APIs and Django REST Framework.
"""


# ============================================================
# 50. Summary
# ============================================================

"""
Important functions:

json.dumps()
    Python object -> JSON string

json.loads()
    JSON string -> Python object

json.dump()
    Python object -> JSON file

json.load()
    JSON file -> Python object


Important concepts:

Serialization
    Python object -> JSON

Deserialization
    JSON -> Python object

indent
    Makes JSON easier to read.

ensure_ascii=False
    Keeps non-ASCII characters readable.

JSONDecodeError
    Indicates invalid JSON data.

The most important distinction:

dumps / loads
    Work with strings.

dump / load
    Work with files.
"""