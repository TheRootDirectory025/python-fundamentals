"""
Python Fundamentals
12 - Modules and Packages
Topic: Python Standard Library

This file covers:
- What the Standard Library is
- os
- pathlib
- sys
- json
- datetime
- collections
- itertools
- math
- random
- statistics
- functools
"""


# ============================================================
# 1. What Is the Python Standard Library?
# ============================================================

"""
Python comes with a large collection of modules that can be
used without installing external packages.

Examples:

os
pathlib
json
datetime
collections
itertools
math
random
statistics
functools

These modules provide functionality for common programming
tasks.
"""


# ============================================================
# 2. os Module
# ============================================================

import os


print(os.getcwd())


"""
os.getcwd()
    Returns the current working directory.
"""


# ============================================================
# 3. Environment Variables
# ============================================================

username = os.getenv("USER")

print(username)


"""
Environment variables are values provided by the operating
system or execution environment.

os.getenv() returns None if the variable does not exist.
"""


# ============================================================
# 4. Checking an Environment Variable
# ============================================================

debug_mode = os.getenv("DEBUG")

if debug_mode:
    print("Debug mode is enabled.")
else:
    print("Debug mode is disabled.")


"""
Environment variables are commonly used for configuration
in backend applications.
"""


# ============================================================
# 5. pathlib
# ============================================================

from pathlib import Path


current_directory = Path.cwd()

print(current_directory)


"""
pathlib provides an object-oriented way to work with
filesystem paths.
"""


# ============================================================
# 6. Creating Paths
# ============================================================

from pathlib import Path


project_path = Path("projects")

file_path = project_path / "python" / "main.py"

print(file_path)


"""
The / operator can be used with Path objects to build paths.

This is preferred over manually concatenating strings.
"""


# ============================================================
# 7. Checking Files and Directories
# ============================================================

path = Path("example.txt")

print(path.exists())
print(path.is_file())
print(path.is_dir())


# ============================================================
# 8. Creating a Directory
# ============================================================

folder = Path("example_folder")

folder.mkdir(
    exist_ok=True
)

print(folder.exists())


"""
exist_ok=True prevents an error if the directory
already exists.
"""


# ============================================================
# 9. Reading and Writing Text Files
# ============================================================

file_path = Path("example.txt")

file_path.write_text(
    "Hello from Python!",
    encoding="utf-8"
)

content = file_path.read_text(
    encoding="utf-8"
)

print(content)


"""
pathlib can handle basic file operations directly.
"""


# ============================================================
# 10. Listing Directory Contents
# ============================================================

current_directory = Path.cwd()

for item in current_directory.iterdir():
    print(item)


"""
iterdir() returns the items inside a directory.
"""


# ============================================================
# 11. Finding Python Files
# ============================================================

current_directory = Path.cwd()

for file in current_directory.glob("*.py"):
    print(file)


"""
glob() can find files matching a pattern.
"""


# ============================================================
# 12. JSON
# ============================================================

import json


user = {
    "name": "Mohsen",
    "age": 24,
    "skills": [
        "Python",
        "SQL",
        "Django"
    ]
}

json_data = json.dumps(user)

print(json_data)


"""
json.dumps()
    Converts a Python object into a JSON string.
"""


# ============================================================
# 13. JSON Formatting
# ============================================================

json_data = json.dumps(
    user,
    indent=4
)

print(json_data)


"""
indent makes JSON easier to read.
"""


# ============================================================
# 14. JSON String to Python Object
# ============================================================

json_text = """
{
    "name": "Mohsen",
    "age": 24,
    "role": "Backend Developer"
}
"""

user = json.loads(json_text)

print(user)
print(user["name"])


"""
json.loads()
    Converts a JSON string into a Python object.
"""


# ============================================================
# 15. Writing JSON to a File
# ============================================================

data = {
    "name": "Mohsen",
    "skills": [
        "Python",
        "Django"
    ]
}

with open(
    "user.json",
    "w",
    encoding="utf-8"
) as file:

    json.dump(
        data,
        file,
        indent=4
    )


# ============================================================
# 16. Reading JSON from a File
# ============================================================

with open(
    "user.json",
    "r",
    encoding="utf-8"
) as file:

    data = json.load(file)


print(data)


"""
json.dump()
    Python object -> file

json.load()
    file -> Python object
"""


# ============================================================
# 17. datetime
# ============================================================

from datetime import datetime


now = datetime.now()

print(now)


# ============================================================
# 18. Formatting Dates
# ============================================================

formatted_date = now.strftime(
    "%Y-%m-%d %H:%M:%S"
)

print(formatted_date)


"""
strftime() converts a datetime object into a formatted string.
"""


# ============================================================
# 19. Parsing Dates
# ============================================================

date_text = "2026-09-28"

parsed_date = datetime.strptime(
    date_text,
    "%Y-%m-%d"
)

print(parsed_date)


"""
strptime() converts a formatted string into a datetime object.
"""


# ============================================================
# 20. timedelta
# ============================================================

from datetime import timedelta


today = datetime.now()

tomorrow = today + timedelta(days=1)

next_week = today + timedelta(days=7)

print(today)
print(tomorrow)
print(next_week)


# ============================================================
# 21. Comparing Dates
# ============================================================

date1 = datetime(2026, 9, 1)
date2 = datetime(2026, 10, 1)

print(date1 < date2)


# ============================================================
# 22. collections.Counter
# ============================================================

from collections import Counter


letters = [
    "a",
    "b",
    "a",
    "c",
    "b",
    "a"
]

counter = Counter(letters)

print(counter)


"""
Counter counts how many times each value occurs.
"""


# ============================================================
# 23. Counter.most_common
# ============================================================

print(counter.most_common(2))


"""
Returns the most common elements.
"""


# ============================================================
# 24. defaultdict
# ============================================================

from collections import defaultdict


scores = defaultdict(list)

scores["Mohsen"].append(90)
scores["Mohsen"].append(85)
scores["Ali"].append(75)

print(scores)


"""
defaultdict automatically creates a default value
when a missing key is accessed.
"""


# ============================================================
# 25. namedtuple
# ============================================================

from collections import namedtuple


User = namedtuple(
    "User",
    ["name", "age"]
)

user = User(
    "Mohsen",
    24
)

print(user.name)
print(user.age)


"""
namedtuple creates tuple-like objects with named fields.
"""


# ============================================================
# 26. deque
# ============================================================

from collections import deque


queue = deque()

queue.append("User 1")
queue.append("User 2")
queue.append("User 3")

print(queue)

first_user = queue.popleft()

print(first_user)
print(queue)


"""
deque is useful for efficient insertion and removal
from both ends.
"""


# ============================================================
# 27. itertools.count
# ============================================================

from itertools import count


counter = count(start=1)

print(next(counter))
print(next(counter))
print(next(counter))


"""
count() creates an iterator that generates values
indefinitely.
"""


# ============================================================
# 28. itertools.chain
# ============================================================

from itertools import chain


first = [1, 2, 3]
second = [4, 5, 6]

for number in chain(first, second):
    print(number)


"""
chain() combines multiple iterables into one iterator.
"""


# ============================================================
# 29. itertools.combinations
# ============================================================

from itertools import combinations


items = ["A", "B", "C"]

pairs = combinations(
    items,
    2
)

for pair in pairs:
    print(pair)


"""
combinations() generates possible combinations
without repetition of positions.
"""


# ============================================================
# 30. math
# ============================================================

import math


print(math.sqrt(25))
print(math.ceil(4.2))
print(math.floor(4.8))
print(math.factorial(5))


# ============================================================
# 31. math Constants
# ============================================================

print(math.pi)
print(math.e)


# ============================================================
# 32. random
# ============================================================

import random


print(random.randint(1, 100))

print(
    random.choice([
        "Python",
        "Django",
        "Kotlin",
        "SQL"
    ])
)


# ============================================================
# 33. Shuffling
# ============================================================

numbers = [1, 2, 3, 4, 5]

random.shuffle(numbers)

print(numbers)


"""
shuffle() changes the list in place.
"""


# ============================================================
# 34. statistics
# ============================================================

import statistics


numbers = [
    10,
    20,
    30,
    40,
    50
]

print(statistics.mean(numbers))
print(statistics.median(numbers))


# ============================================================
# 35. functools.reduce
# ============================================================

from functools import reduce


numbers = [1, 2, 3, 4]

total = reduce(
    lambda a, b: a + b,
    numbers
)

print(total)


"""
reduce() repeatedly applies a function to values
in an iterable.

For simple summation, sum() is usually clearer.

The purpose here is to understand the tool,
not to replace simpler built-in functions.
"""


# ============================================================
# 36. functools.lru_cache
# ============================================================

from functools import lru_cache


@lru_cache
def fibonacci(n):
    if n <= 1:
        return n

    return (
        fibonacci(n - 1)
        + fibonacci(n - 2)
    )


print(fibonacci(10))


"""
lru_cache stores previous results so repeated calls
can be much faster for suitable functions.
"""


# ============================================================
# 37. sys
# ============================================================

import sys


print(sys.version)
print(sys.platform)


# ============================================================
# 38. Command-Line Arguments
# ============================================================

"""
sys.argv contains command-line arguments.

For example:

python main.py hello

would make:

sys.argv[0] -> "main.py"
sys.argv[1] -> "hello"

Example code:

if len(sys.argv) > 1:
    print(sys.argv[1])
"""


# ============================================================
# 39. Combining Standard Library Tools
# ============================================================

from pathlib import Path
import json


data = {
    "project": "Python Fundamentals",
    "language": "Python",
    "status": "learning"
}

file_path = Path("project.json")

file_path.write_text(
    json.dumps(
        data,
        indent=4
    ),
    encoding="utf-8"
)

loaded_data = json.loads(
    file_path.read_text(
        encoding="utf-8"
    )
)

print(loaded_data)


"""
This example combines:

pathlib
+
json

to store structured data in a file.
"""


# ============================================================
# 40. Useful Standard Library Categories
# ============================================================

"""
Files and operating system:

os
pathlib
shutil

Data formats:

json
csv
configparser

Dates and time:

datetime
time
zoneinfo

Collections:

collections

Iteration:

itertools

Mathematics:

math
statistics
decimal

Functional programming:

functools

System:

sys
argparse
subprocess

Random data:

random
secrets

Regular expressions:

re

Testing:

unittest

Logging:

logging
"""


# ============================================================
# 41. Standard Library vs External Packages
# ============================================================

"""
Standard Library:

    import json
    import pathlib
    import datetime


These are included with Python.

External packages:

    Django
    requests
    pandas

These normally need to be installed separately.

For example:

pip install django
"""


# ============================================================
# 42. Why Standard Library Matters
# ============================================================

"""
Before installing an external package, check whether
Python's Standard Library already provides what you need.

Using the Standard Library can:

- reduce dependencies
- simplify deployment
- reduce project complexity
- improve portability
"""


# ============================================================
# 43. Standard Library in Backend Development
# ============================================================

"""
Even when working with Django, Standard Library modules
remain useful.

Examples:

pathlib
    File and path handling.

json
    JSON data.

datetime
    Dates and timestamps.

logging
    Application logs.

os
    Environment variables.

re
    Pattern matching.

collections
    Useful data structures.

functools
    Caching and functional utilities.
"""


# ============================================================
# 44. Best Practices
# ============================================================

"""
Best practices:

1. Learn the most useful Standard Library modules.
2. Prefer built-in functionality when it solves the problem.
3. Don't use a complex module when a simple built-in works.
4. Keep imports organized.
5. Use pathlib for modern path handling.
6. Use environment variables for configuration.
7. Use json for structured JSON data.
8. Use datetime for date/time operations.
9. Use collections when specialized data structures help.
10. Understand a module before adding it to a project.
"""


# ============================================================
# 45. Summary
# ============================================================

"""
The Python Standard Library provides ready-to-use tools
for many common programming tasks.

Important modules covered here:

os
    Operating system and environment variables.

pathlib
    Filesystem paths and file operations.

json
    JSON encoding and decoding.

datetime
    Dates and times.

collections
    Specialized data structures.

itertools
    Iterator utilities.

math
    Mathematical operations.

random
    Random values and selections.

statistics
    Statistical calculations.

functools
    Higher-order functions and caching.

sys
    Python runtime and command-line information.

The main idea:

Before installing an external package,
know what Python already provides.
"""