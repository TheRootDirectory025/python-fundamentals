"""
Python Fundamentals
12 - Modules and Packages
Topic: Modules

This file covers:
- What a module is
- Importing modules
- import statement
- from ... import
- Import aliases
- Multiple imports
- Standard library modules
- Using module members
- __name__
- if __name__ == "__main__"
"""


# ============================================================
# 1. What Is a Module?
# ============================================================

"""
A module is simply a Python file containing code.

For example:

math_utils.py

could contain:

def add(a, b):
    return a + b

Then another Python file can import it.

Modules help us:

- organize code
- reuse code
- avoid very large files
- separate responsibilities
"""


# ============================================================
# 2. Importing a Module
# ============================================================

import math


print(math.sqrt(25))


"""
import math

loads Python's built-in math module.

We then access its members using:

math.member
"""


# ============================================================
# 3. Accessing Module Functions
# ============================================================

import math


print(math.sqrt(16))
print(math.pow(2, 3))
print(math.ceil(4.2))
print(math.floor(4.8))


# ============================================================
# 4. Module Constants
# ============================================================

import math


print(math.pi)
print(math.e)


"""
Modules can contain more than functions.

They can also provide:

- constants
- classes
- variables
- other objects
"""


# ============================================================
# 5. Importing Multiple Modules
# ============================================================

import math
import random


print(math.pi)
print(random.randint(1, 10))


# ============================================================
# 6. Import Alias
# ============================================================

import math as m


print(m.sqrt(100))
print(m.pi)


"""
as allows us to give a module another name.

math -> m
"""


# ============================================================
# 7. Another Alias Example
# ============================================================

import datetime as dt


current_date = dt.date.today()

print(current_date)


"""
Aliases can make frequently used module names
shorter or avoid naming conflicts.
"""


# ============================================================
# 8. from ... import
# ============================================================

from math import sqrt


print(sqrt(81))


"""
Instead of:

math.sqrt(81)

we can import sqrt directly.
"""


# ============================================================
# 9. Importing Multiple Members
# ============================================================

from math import sqrt, pi, floor


print(sqrt(49))
print(pi)
print(floor(5.9))


# ============================================================
# 10. from ... import with Alias
# ============================================================

from math import sqrt as square_root


print(square_root(64))


"""
We can alias individual imported objects as well.
"""


# ============================================================
# 11. Importing a Class
# ============================================================

from datetime import datetime


now = datetime.now()

print(now)


"""
A module can provide classes that we can import directly.
"""


# ============================================================
# 12. Standard Library Modules
# ============================================================

import os
import sys
import json
import random
import statistics


print(os.getcwd())
print(sys.version)
print(random.randint(1, 100))
print(statistics.mean([10, 20, 30]))


"""
Python includes a large Standard Library.

Some useful modules:

os
    Operating system functionality.

sys
    Python interpreter and runtime information.

json
    Working with JSON data.

random
    Random number generation.

statistics
    Statistical calculations.
"""


# ============================================================
# 13. The random Module
# ============================================================

import random


print(random.randint(1, 10))

print(random.choice([
    "Python",
    "Django",
    "Kotlin"
]))


# ============================================================
# 14. The datetime Module
# ============================================================

from datetime import date, datetime, timedelta


today = date.today()

print(today)


now = datetime.now()

print(now)


tomorrow = today + timedelta(days=1)

print(tomorrow)


# ============================================================
# 15. The os Module
# ============================================================

import os


print(os.getcwd())


"""
getcwd()

returns the current working directory.
"""


# ============================================================
# 16. Working with Environment Variables
# ============================================================

import os


username = os.getenv("USER")

print(username)


"""
Environment variables are values provided by the operating
system or application environment.

os.getenv() safely retrieves an environment variable.
"""


# ============================================================
# 17. The sys Module
# ============================================================

import sys


print(sys.version)
print(sys.platform)


"""
sys provides information and functionality related
to the Python interpreter.
"""


# ============================================================
# 18. Module Namespace
# ============================================================

import math


print(math.__name__)


"""
Every module has its own namespace.

For example:

math.sqrt
math.pi

belong to the math module's namespace.
"""


# ============================================================
# 19. Your Own Module
# ============================================================

"""
Imagine we have this project:

project/
│
├── main.py
└── calculator.py


calculator.py:

def add(a, b):
    return a + b


main.py can use:

import calculator

print(calculator.add(10, 20))
"""


# ============================================================
# 20. Importing Your Own Module
# ============================================================

"""
Example:

calculator.py
"""

# The following code demonstrates how another file
# would import the module:

#
# import calculator
#
# result = calculator.add(10, 20)
# print(result)


# ============================================================
# 21. from Module import Function
# ============================================================

"""
Instead of:

import calculator

we could use:

from calculator import add

Then:

print(add(10, 20))

This can make code shorter when only a few members
are required.
"""


# ============================================================
# 22. Why Modules Matter
# ============================================================

"""
Without modules, a large project might look like:

main.py

containing:

- database code
- authentication
- API logic
- business logic
- validation
- utilities
- configuration
- file handling

This quickly becomes difficult to maintain.

Instead, we can separate responsibilities:

database.py
authentication.py
api.py
validation.py
utils.py
config.py
"""


# ============================================================
# 23. __name__
# ============================================================

print(__name__)


"""
Every Python module has a special variable:

__name__

When a file is executed directly,
its value is:

"__main__"

When it is imported,
its value is normally the module's name.
"""


# ============================================================
# 24. __name__ == "__main__"
# ============================================================

def main():
    print("Program started.")


if __name__ == "__main__":
    main()


"""
This pattern means:

Run main() only when this file is executed directly.

If another file imports this module,
main() will not automatically execute.
"""


# ============================================================
# 25. Why __name__ == "__main__" Matters
# ============================================================

"""
Imagine:

calculator.py

contains:

def add(a, b):
    return a + b


def main():
    print(add(10, 20))


if __name__ == "__main__":
    main()


When we run:

python calculator.py

main() runs.

But if another file does:

import calculator

the main() function does not automatically run.

This makes modules reusable.
"""


# ============================================================
# 26. Importing Everything with *
# ============================================================

"""
You may see:

from math import *

This imports many names directly.

However, it is generally better to avoid this style because
it makes it harder to know where a name came from.

Prefer:

import math

or:

from math import sqrt
"""


# ============================================================
# 27. Module Naming
# ============================================================

"""
Good module names are:

- lowercase
- descriptive
- concise
- easy to understand

Examples:

database.py
authentication.py
validators.py
utils.py
config.py


Avoid unclear names such as:

stuff.py
things.py
random_code.py
"""


# ============================================================
# 28. Import Organization
# ============================================================

"""
A common style is:

1. Standard library imports
2. Third-party imports
3. Local application imports

Example:

import os
import json

import requests
import django

from .models import User
from .utils import validate_email
"""


# ============================================================
# 29. Module Reusability
# ============================================================

"""
One of the biggest benefits of modules is reuse.

For example:

validators.py

could contain:

def is_valid_email(email):
    ...


Then many parts of an application can use:

from validators import is_valid_email

without rewriting the validation logic.
"""


# ============================================================
# 30. Modules and Backend Development
# ============================================================

"""
Modules are extremely important in backend development.

A Django project may contain modules for:

- models
- views
- serializers
- services
- utilities
- authentication
- database logic
- configuration

Understanding imports and modules is therefore essential
before working seriously with Django.
"""


# ============================================================
# 31. Best Practices
# ============================================================

"""
Best practices:

1. Keep modules focused on one responsibility.
2. Use descriptive module names.
3. Avoid unnecessary wildcard imports.
4. Prefer explicit imports.
5. Use aliases only when they improve readability.
6. Avoid circular imports.
7. Keep reusable functionality inside modules.
8. Use __name__ == "__main__" for executable entry points.
9. Organize imports consistently.
10. Avoid putting unrelated functionality into one module.
"""


# ============================================================
# 32. Summary
# ============================================================

"""
Important concepts:

Module
    A Python file containing reusable code.

import
    Imports a module.

from ... import
    Imports specific members from a module.

as
    Creates an alias.

__name__
    Special variable identifying how a module is being used.

__main__
    Indicates that a file is being executed directly.

if __name__ == "__main__":
    Protects executable code from running automatically
    when the module is imported.

The main idea:

Break large programs into smaller, focused,
reusable Python files.
"""