"""
Python Fundamentals
10 - Modules
Topic: Packages

This file covers:
- What packages are
- Package structure
- __init__.py
- Importing from packages
- Nested packages
- Package aliases
- Relative imports
- Practical project structure
- Packages in backend development
"""


# ============================================================
# 1. What Is a Package?
# ============================================================

"""
A package is a directory that contains Python modules.

For example:

project/
│
├── main.py
│
└── utils/
    ├── __init__.py
    ├── math_utils.py
    └── string_utils.py

Here:

utils
    is a package

math_utils.py
    is a module

string_utils.py
    is another module
"""


# ============================================================
# 2. Why Use Packages?
# ============================================================

"""
As a project becomes larger, putting everything into
one file becomes difficult.

Packages allow us to organize related modules together.

For example:

project/
│
├── users/
│   ├── models.py
│   ├── services.py
│   └── validators.py
│
├── products/
│   ├── models.py
│   ├── services.py
│   └── validators.py
│
└── orders/
    ├── models.py
    ├── services.py
    └── validators.py

Each directory groups related functionality.
"""


# ============================================================
# 3. __init__.py
# ============================================================

"""
Traditionally, a Python package contains a file called:

__init__.py

Example:

utils/
├── __init__.py
├── math_utils.py
└── string_utils.py

The file can be empty.

Its presence tells Python that the directory
is intended to be treated as a package.

Modern Python can also work with namespace packages
without __init__.py, but using __init__.py is still
very common and useful for regular packages.
"""


# ============================================================
# 4. Basic Package Structure
# ============================================================

"""
Example:

my_project/
│
├── main.py
│
└── calculator/
    ├── __init__.py
    ├── addition.py
    └── subtraction.py
"""


# ============================================================
# 5. Importing a Module from a Package
# ============================================================

"""
Suppose addition.py contains:

def add(a, b):
    return a + b

Then main.py can use:

from calculator import addition

result = addition.add(10, 5)

print(result)
"""


# ============================================================
# 6. Importing a Function from a Package Module
# ============================================================

"""
We can also import the function directly:

from calculator.addition import add

result = add(10, 5)

print(result)
"""


# ============================================================
# 7. Package Alias
# ============================================================

"""
We can give a package module an alias:

import calculator.addition as addition

result = addition.add(10, 5)

print(result)
"""


# ============================================================
# 8. Multiple Modules in a Package
# ============================================================

"""
Example:

calculator/
├── __init__.py
├── addition.py
├── subtraction.py
├── multiplication.py
└── division.py

Each module can have a specific responsibility.

This is better than creating one huge calculator.py
when the project becomes larger.
"""


# ============================================================
# 9. Example Package
# ============================================================

"""
Suppose we have:

utils/
├── __init__.py
├── math_utils.py
└── string_utils.py

math_utils.py:

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

string_utils.py:

def capitalize_name(name):
    return name.strip().title()
"""


# ============================================================
# 10. Using the Example Package
# ============================================================

"""
From another Python file:

from utils.math_utils import add
from utils.string_utils import capitalize_name

result = add(10, 20)

name = capitalize_name("mohsen")

print(result)
print(name)
"""


# ============================================================
# 11. Importing the Package
# ============================================================

"""
We can also import the module itself:

from utils import math_utils

result = math_utils.add(10, 20)

print(result)
"""


# ============================================================
# 12. __init__.py as Package Initialization
# ============================================================

"""
The __init__.py file can contain code.

For example:

utils/__init__.py

PACKAGE_NAME = "Utilities"

Then another file can use:

from utils import PACKAGE_NAME

print(PACKAGE_NAME)
"""


# ============================================================
# 13. Re-exporting Functions
# ============================================================

"""
Suppose:

utils/
├── __init__.py
└── math_utils.py

math_utils.py:

def add(a, b):
    return a + b


We can write inside __init__.py:

from .math_utils import add


Then another file can use:

from utils import add

result = add(10, 5)

print(result)

The "." means the current package.
"""


# ============================================================
# 14. Why Re-export?
# ============================================================

"""
Re-exporting can create a cleaner public interface.

Instead of:

from utils.math_utils import add

we can expose:

from utils import add

This can become useful when a package contains many modules.
"""


# ============================================================
# 15. Nested Packages
# ============================================================

"""
Packages can contain other packages.

Example:

project/
│
├── main.py
│
└── application/
    ├── __init__.py
    │
    ├── users/
    │   ├── __init__.py
    │   ├── models.py
    │   └── services.py
    │
    └── products/
        ├── __init__.py
        ├── models.py
        └── services.py
"""


# ============================================================
# 16. Importing from a Nested Package
# ============================================================

"""
Example:

from application.users.services import create_user

user = create_user("Mohsen")

print(user)
"""


# ============================================================
# 17. Absolute Imports
# ============================================================

"""
An absolute import describes the complete path.

Example:

from application.users.services import create_user

This is called an absolute import.
"""


# ============================================================
# 18. Relative Imports
# ============================================================

"""
Relative imports use dots.

Example:

from .models import User

The "." means:

from the current package

Another example:

from ..users.models import User

The ".." means:

go up one package level
"""


# ============================================================
# 19. Relative Import Example
# ============================================================

"""
Suppose:

application/
│
├── __init__.py
│
├── users/
│   ├── __init__.py
│   ├── models.py
│   └── services.py
│
└── orders/
    ├── __init__.py
    └── services.py

Inside orders/services.py:

from ..users.models import User

This means:

Go from orders up to application,
then enter users,
then import User from models.
"""


# ============================================================
# 20. Package Naming
# ============================================================

"""
Good package names:

users
products
orders
authentication
database
services
utils

Avoid names like:

my_package_123
stuff
random_files
test123

A package name should describe its responsibility.
"""


# ============================================================
# 21. Packages and Separation of Responsibilities
# ============================================================

"""
A good project separates responsibilities.

Example:

application/
│
├── authentication/
│   ├── models.py
│   ├── services.py
│   └── validators.py
│
├── users/
│   ├── models.py
│   ├── services.py
│   └── validators.py
│
└── products/
    ├── models.py
    ├── services.py
    └── validators.py

Each package has a clear purpose.
"""


# ============================================================
# 22. Package vs Module
# ============================================================

"""
Module:
    Usually one .py file.

Example:

users.py


Package:
    A directory containing related modules.

Example:

users/
├── __init__.py
├── models.py
└── services.py


Simple idea:

.py file
    -> module

directory of related modules
    -> package
"""


# ============================================================
# 23. Package vs Library
# ============================================================

"""
A package is a Python code organization structure.

A library is reusable software that provides functionality.

A library can contain one or many packages.

For example, a large third-party library may have
many packages and modules inside it.
"""


# ============================================================
# 24. Standard Library Packages
# ============================================================

"""
Python's standard library contains many modules and packages.

Examples:

json
datetime
collections
pathlib
email
http

You can import them without installing anything separately.
"""


# ============================================================
# 25. Third-Party Packages
# ============================================================

"""
Third-party packages are created outside the Python
standard library.

Examples:

Django
requests
pytest
Django REST Framework

These packages usually need to be installed separately.

For example:

pip install django
"""


# ============================================================
# 26. pip
# ============================================================

"""
pip is Python's package installer.

Example:

pip install requests

This downloads and installs the requests package.

To see installed packages:

pip list

To show package information:

pip show requests
"""


# ============================================================
# 27. requirements.txt
# ============================================================

"""
A Python project often keeps its dependencies in:

requirements.txt

Example:

Django==5.2
requests==2.32.0
pytest==8.3.0

Another developer can install them with:

pip install -r requirements.txt

This makes project setup easier.
"""


# ============================================================
# 28. Virtual Environments
# ============================================================

"""
A virtual environment creates an isolated Python environment
for a project.

Example:

python -m venv .venv

Activate it depending on your operating system.

Then install packages inside that environment.

This prevents dependencies from different projects
from interfering with each other.
"""


# ============================================================
# 29. Package Structure for a Backend Project
# ============================================================

"""
A simple backend project could eventually look like:

backend_project/
│
├── manage.py
│
├── users/
│   ├── __init__.py
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   └── urls.py
│
├── products/
│   ├── __init__.py
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   └── urls.py
│
└── orders/
    ├── __init__.py
    ├── models.py
    ├── views.py
    ├── serializers.py
    └── urls.py
"""


# ============================================================
# 30. Packages in Django
# ============================================================

"""
Django projects use Python modules and packages everywhere.

For example:

myproject/
│
├── manage.py
│
├── myproject/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
└── users/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── tests.py
    └── views.py

Understanding packages now will make this structure
much easier to understand later.
"""


# ============================================================
# 31. Avoid Circular Imports
# ============================================================

"""
A circular import happens when:

module_a imports module_b

and

module_b imports module_a

Example:

a.py
    from b import something

b.py
    from a import something

This can cause import errors and confusing behavior.

A better project structure should avoid circular dependencies.
"""


# ============================================================
# 32. Package __init__.py Should Stay Clean
# ============================================================

"""
Do not put a large amount of application logic inside
__init__.py.

Usually it should contain:

- Package metadata
- Selected public imports
- Small initialization code when necessary

Keep the main application logic in dedicated modules.
"""


# ============================================================
# 33. Example: Utility Package
# ============================================================

"""
A useful structure:

utils/
│
├── __init__.py
├── math_utils.py
├── string_utils.py
├── date_utils.py
└── file_utils.py

Responsibilities:

math_utils.py
    Mathematical functions

string_utils.py
    String-related functions

date_utils.py
    Date-related functions

file_utils.py
    File-related functions
"""


# ============================================================
# 34. Example: E-commerce Package Structure
# ============================================================

"""
A larger backend project might look like:

ecommerce/
│
├── users/
│   ├── models.py
│   ├── services.py
│   └── validators.py
│
├── products/
│   ├── models.py
│   ├── services.py
│   └── validators.py
│
├── cart/
│   ├── models.py
│   └── services.py
│
├── orders/
│   ├── models.py
│   └── services.py
│
└── payments/
    ├── services.py
    └── validators.py

This kind of organization becomes very important
as applications grow.
"""


# ============================================================
# 35. Best Practices
# ============================================================

"""
Best practices:

1. Keep related modules together.
2. Give packages meaningful names.
3. Keep each module focused on a responsibility.
4. Avoid very large modules.
5. Avoid circular imports.
6. Prefer absolute imports for clarity in many projects.
7. Use relative imports when they improve package structure.
8. Keep __init__.py simple.
9. Use virtual environments for projects.
10. Track third-party dependencies.
"""


# ============================================================
# 36. Summary
# ============================================================

"""
Important concepts:

Module
    A Python file containing reusable code.

Package
    A directory used to organize related Python modules.

__init__.py
    Commonly used to define and initialize a package.

Absolute import
    from application.users.models import User

Relative import
    from .models import User

Nested package
    A package inside another package.

pip
    Python package installer.

requirements.txt
    File containing project dependencies.

Virtual environment
    Isolated Python environment for a project.


The main idea:

Modules organize code into files.

Packages organize modules into directories.

Together, they allow large Python applications
to remain organized and maintainable.
"""