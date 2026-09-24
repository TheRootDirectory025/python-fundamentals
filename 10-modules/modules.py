"""
Python Fundamentals
10 - Modules
Topic: Modules

This file covers:
- What modules are
- Importing modules
- Importing specific functions
- Import aliases
- Built-in modules
- Creating and using modules
- __name__
- __main__
- Practical examples
"""


# ============================================================
# 1. What Is a Module?
# ============================================================

"""
A module is simply a Python file that contains code.

A module can contain:
- Variables
- Functions
- Classes
- Constants

Modules help us organize code into separate files
and reuse code across different programs.

For example:

math_utils.py
    contains mathematical functions

main.py
    uses those functions
"""


# ============================================================
# 2. Importing a Module
# ============================================================

import math


number = 25

print(math.sqrt(number))


"""
The math module is a built-in Python module.

After importing it, we can access its functions
using the module name:

math.sqrt()
math.floor()
math.ceil()
math.pi
"""


# ============================================================
# 3. Using Functions from a Module
# ============================================================

import math

print(math.ceil(4.2))
print(math.floor(4.8))
print(math.sqrt(64))


# ============================================================
# 4. Module Constants
# ============================================================

import math

print(math.pi)
print(math.e)


# ============================================================
# 5. Importing a Specific Function
# ============================================================

from math import sqrt

print(sqrt(100))


"""
When importing a specific function, we can use it
without writing the module name.
"""


# ============================================================
# 6. Importing Multiple Functions
# ============================================================

from math import ceil, floor

print(ceil(4.2))
print(floor(4.8))


# ============================================================
# 7. Import Alias
# ============================================================

import math as mathematics

print(mathematics.sqrt(81))


"""
An alias gives a module a shorter or more convenient name.
"""


# ============================================================
# 8. Function Alias
# ============================================================

from math import sqrt as square_root

print(square_root(144))


# ============================================================
# 9. The random Module
# ============================================================

import random

number = random.randint(1, 10)

print(number)


# ============================================================
# 10. Random Choice
# ============================================================

import random

skills = [
    "Python",
    "Django",
    "SQL",
    "Kotlin"
]

selected_skill = random.choice(skills)

print(selected_skill)


# ============================================================
# 11. The datetime Module
# ============================================================

import datetime

current_date = datetime.date.today()

print(current_date)


# ============================================================
# 12. Current Date and Time
# ============================================================

import datetime

current_time = datetime.datetime.now()

print(current_time)


# ============================================================
# 13. The os Module
# ============================================================

import os

current_directory = os.getcwd()

print(current_directory)


# ============================================================
# 14. Environment Information
# ============================================================

import os

print(os.name)


# ============================================================
# 15. Listing Directory Contents
# ============================================================

import os

files = os.listdir(".")

print(files)


# ============================================================
# 16. The pathlib Module
# ============================================================

from pathlib import Path

current_directory = Path.cwd()

print(current_directory)


# pathlib is useful for working with files and directories.


# ============================================================
# 17. Creating a Path
# ============================================================

from pathlib import Path

file_path = Path("data") / "users.json"

print(file_path)


# ============================================================
# 18. Checking if a File Exists
# ============================================================

from pathlib import Path

file_path = Path("example.txt")

if file_path.exists():
    print("File exists.")
else:
    print("File does not exist.")


# ============================================================
# 19. The statistics Module
# ============================================================

import statistics

numbers = [
    10,
    20,
    30,
    40,
    50
]

average = statistics.mean(numbers)

print(average)


# ============================================================
# 20. Using Several Modules
# ============================================================

import math
import random
import statistics

numbers = [
    random.randint(1, 100)
    for _ in range(5)
]

print(numbers)
print(f"Average: {statistics.mean(numbers)}")
print(f"Square root of first number: {math.sqrt(numbers[0])}")


# ============================================================
# 21. Creating Our Own Module
# ============================================================

"""
Suppose we have this project structure:

10-modules/
│
├── modules.py
└── math_utils.py

The math_utils.py file could contain:

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

Then modules.py can import it:

import math_utils

result = math_utils.add(10, 5)

print(result)

The imported file becomes a reusable module.
"""


# ============================================================
# 22. Importing Our Own Function
# ============================================================

"""
Example:

from math_utils import add

result = add(10, 5)

print(result)

This imports only the add function.
"""


# ============================================================
# 23. Module Aliases for Our Own Modules
# ============================================================

"""
Example:

import math_utils as utils

result = utils.add(10, 5)

print(result)
"""


# ============================================================
# 24. Why Modules Are Useful
# ============================================================

"""
Without modules, a large program could become one very
large Python file.

Instead, we can separate responsibilities:

database.py
    Database-related functions

authentication.py
    Login and authentication functions

users.py
    User-related functions

products.py
    Product-related functions

main.py
    Main application logic

This makes the project easier to:

- Read
- Maintain
- Test
- Reuse
- Debug
"""


# ============================================================
# 25. __name__
# ============================================================

"""
Every Python module has a special variable called __name__.

When a file is executed directly:

__name__ == "__main__"

When the file is imported:

__name__ == "module_name"
"""


# ============================================================
# 26. __name__ Example
# ============================================================

print(f"Module name: {__name__}")


# ============================================================
# 27. if __name__ == "__main__"
# ============================================================

def greet():
    print("Hello from the module.")


if __name__ == "__main__":
    greet()


"""
This block runs only when the file itself is executed.

It does not run automatically when the module is imported.

This pattern is very common in Python projects.
"""


# ============================================================
# 28. Practical Module Structure
# ============================================================

"""
Example project:

project/
│
├── main.py
├── calculator.py
└── user.py

calculator.py:

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

user.py:

def create_user(name):
    return {
        "name": name
    }

main.py:

from calculator import add
from user import create_user

print(add(10, 5))

user = create_user("Mohsen")

print(user)
"""


# ============================================================
# 29. Importing a Module Multiple Times
# ============================================================

"""
Python normally loads a module once during program execution.

After that, Python can reuse the already loaded module.

This helps avoid unnecessary repeated work.
"""


# ============================================================
# 30. Standard Library
# ============================================================

"""
Python includes a large standard library.

Some useful modules:

math
    Mathematical operations

random
    Random numbers and choices

datetime
    Dates and times

os
    Operating system functionality

pathlib
    Filesystem paths

json
    JSON data

statistics
    Statistical calculations

re
    Regular expressions

collections
    Specialized data structures

sys
    Python runtime information

These modules are available without installing
third-party packages.
"""


# ============================================================
# 31. The sys Module
# ============================================================

import sys

print(sys.version)


# ============================================================
# 32. Command-Line Arguments
# ============================================================

"""
sys.argv contains arguments passed to a Python program.

For example:

python program.py hello

sys.argv might contain:

[
    "program.py",
    "hello"
]

Example:
"""

import sys

print(sys.argv)


# ============================================================
# 33. Practical Example: Random Password
# ============================================================

import random
import string

characters = string.ascii_letters + string.digits

password = ""

for _ in range(8):
    password += random.choice(characters)

print(password)


# ============================================================
# 34. Practical Example: Generate a Random Number
# ============================================================

import random


def generate_number(start, end):
    return random.randint(start, end)


number = generate_number(1, 100)

print(f"Generated number: {number}")


# ============================================================
# 35. Practical Example: Date
# ============================================================

from datetime import date

today = date.today()

print(f"Today: {today}")


# ============================================================
# 36. Practical Example: Path
# ============================================================

from pathlib import Path

project_directory = Path.cwd()

print(f"Project directory: {project_directory}")

for item in project_directory.iterdir():
    print(item)


# ============================================================
# 37. Importing Everything
# ============================================================

"""
You may see this syntax:

from math import *

It imports everything from the module.

However, this is generally discouraged because it can:

- Make the source code harder to understand
- Cause name conflicts
- Make it unclear where a function came from

Prefer explicit imports such as:

from math import sqrt
"""


# ============================================================
# 38. Import Organization
# ============================================================

"""
A clean Python file usually organizes imports near
the top of the file.

Example:

import math
import random
import os

from datetime import date
from pathlib import Path

Then the rest of the program follows.
"""


# ============================================================
# 39. Practical Example: Simple Utility Module
# ============================================================

"""
Imagine a file named string_utils.py:

def capitalize_name(name):
    return name.strip().title()


def is_empty(value):
    return not value.strip()


Then another file can use:

from string_utils import capitalize_name

name = capitalize_name("mohsen")

print(name)
"""


# ============================================================
# 40. Modules and Backend Development
# ============================================================

"""
Modules are extremely important in backend development.

A Django project is not one huge Python file.

Instead, code is organized into modules and packages.

For example:

users/
    models.py
    views.py
    serializers.py
    urls.py

products/
    models.py
    views.py
    serializers.py
    urls.py

orders/
    models.py
    views.py
    serializers.py
    urls.py

Understanding imports and modules now will make
working with Django much easier later.
"""


# ============================================================
# 41. Best Practices
# ============================================================

"""
Best practices:

1. Keep imports near the top of the file.
2. Use meaningful module names.
3. Avoid "from module import *".
4. Use aliases when they improve readability.
5. Keep modules focused on a specific responsibility.
6. Avoid circular imports.
7. Use if __name__ == "__main__" when appropriate.
8. Prefer the standard library before installing
   third-party packages when it solves the problem.
"""


# ============================================================
# 42. Summary
# ============================================================

"""
Important concepts:

import module
    Import an entire module.

from module import function
    Import a specific function.

import module as alias
    Give a module an alias.

__name__
    Special variable identifying the current module.

if __name__ == "__main__":
    Code that runs when the file is executed directly.

Modules allow us to split large programs into smaller,
reusable and maintainable pieces.
"""