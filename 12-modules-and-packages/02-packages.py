"""
Python Fundamentals
12 - Modules and Packages
Topic: Packages

This file covers:
- What a package is
- Module vs package
- Package structure
- __init__.py
- Importing from packages
- Nested packages
- Relative imports
- Absolute imports
- __all__
- Practical project structure
"""


# ============================================================
# 1. What Is a Package?
# ============================================================

"""
A package is a directory that organizes related Python modules.

For example:

shop/
├── __init__.py
├── products.py
├── users.py
└── orders.py


Here:

shop
    -> package

products.py
users.py
orders.py
    -> modules
"""


# ============================================================
# 2. Module vs Package
# ============================================================

"""
Module:

A single Python file.

Example:

users.py


Package:

A directory containing related modules.

Example:

users/
├── __init__.py
├── authentication.py
└── profile.py
"""


# ============================================================
# 3. Basic Package Structure
# ============================================================

"""
A simple project might look like this:

project/
│
├── main.py
│
└── calculator/
    ├── __init__.py
    ├── addition.py
    └── subtraction.py


calculator
    -> package

addition.py
    -> module

subtraction.py
    -> module
"""


# ============================================================
# 4. __init__.py
# ============================================================

"""
Traditionally, __init__.py marks a directory as a Python
package.

Modern Python also supports namespace packages without
__init__.py in some situations.

However, __init__.py is still very common and useful,
especially for controlling package behavior and exports.
"""


# ============================================================
# 5. Example Module Inside a Package
# ============================================================

"""
Imagine:

calculator/
├── __init__.py
└── operations.py


operations.py:

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b
"""


# ============================================================
# 6. Importing a Module from a Package
# ============================================================

"""
From main.py:

import calculator.operations

result = calculator.operations.add(10, 20)

print(result)
"""


# ============================================================
# 7. Importing with an Alias
# ============================================================

"""
We can also write:

import calculator.operations as operations

result = operations.add(10, 20)

print(result)
"""


# ============================================================
# 8. from Package import Module
# ============================================================

"""
Another option:

from calculator import operations

result = operations.add(10, 20)

print(result)
"""


# ============================================================
# 9. Importing a Function from a Module
# ============================================================

"""
We can import the function directly:

from calculator.operations import add

result = add(10, 20)

print(result)
"""


# ============================================================
# 10. Example Package
# ============================================================

"""
Imagine:

shop/
├── __init__.py
├── products.py
├── customers.py
└── orders.py


products.py:

class Product:
    ...


customers.py:

class Customer:
    ...


orders.py:

class Order:
    ...
"""


# ============================================================
# 11. Using the Package
# ============================================================

"""
main.py could contain:

from shop.products import Product
from shop.customers import Customer
from shop.orders import Order


product = Product()
customer = Customer()
order = Order()
"""


# ============================================================
# 12. Package Organization
# ============================================================

"""
Packages help separate responsibilities.

For example:

backend/
│
├── authentication/
├── users/
├── products/
├── orders/
├── payments/
└── notifications/


Each package can contain multiple modules.
"""


# ============================================================
# 13. Nested Packages
# ============================================================

"""
Packages can contain other packages.

Example:

project/
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
# 14. Importing from a Nested Package
# ============================================================

"""
Example:

from application.users.models import User

from application.products.models import Product
"""


# ============================================================
# 15. Absolute Imports
# ============================================================

"""
An absolute import starts from the project's import root.

Example:

from application.users.models import User


This is called an absolute import because it uses the
full package path.
"""


# ============================================================
# 16. Relative Imports
# ============================================================

"""
Suppose we have:

application/
├── users/
│   ├── __init__.py
│   ├── models.py
│   └── services.py


Inside services.py we can write:

from .models import User


The single dot means:

current package
"""


# ============================================================
# 17. Parent Package Relative Import
# ============================================================

"""
Two dots move one level upward.

Example:

from ..utils import validate_email


Meaning:

..
    parent package

utils
    module/package inside the parent
"""


# ============================================================
# 18. Relative Import Example
# ============================================================

"""
Structure:

application/
├── __init__.py
├── utils.py
│
└── users/
    ├── __init__.py
    ├── models.py
    └── services.py


Inside services.py:

from .models import User
from ..utils import validate_email
"""


# ============================================================
# 19. __init__.py Can Contain Code
# ============================================================

"""
__init__.py is a normal Python module.

For example:

shop/__init__.py

could contain:

VERSION = "1.0.0"
"""


# ============================================================
# 20. Accessing Package Variables
# ============================================================

"""
Then another file can use:

import shop

print(shop.VERSION)
"""


# ============================================================
# 21. Re-exporting Objects
# ============================================================

"""
Suppose:

shop/
├── __init__.py
└── products.py


products.py:

class Product:
    pass


We could expose Product through __init__.py:

from .products import Product


Then users can write:

from shop import Product

instead of:

from shop.products import Product
"""


# ============================================================
# 22. Why Re-export?
# ============================================================

"""
Re-exporting can create a cleaner public interface.

Instead of exposing the internal structure:

shop.products.Product

we can expose:

shop.Product


This means users don't need to know where Product
is internally implemented.
"""


# ============================================================
# 23. __all__
# ============================================================

"""
A module or package can define __all__.

Example:

__all__ = [
    "Product",
    "Customer"
]


This can define which names are considered public
for wildcard imports.
"""


# ============================================================
# 24. Example __all__
# ============================================================

"""
products.py:

class Product:
    pass


class InternalHelper:
    pass


__all__ = [
    "Product"
]


This communicates that Product is part of the intended
public interface while InternalHelper is internal.
"""


# ============================================================
# 25. Wildcard Import
# ============================================================

"""
You may encounter:

from products import *

When __all__ exists, Python uses it to determine
which names are imported.

However, wildcard imports are generally discouraged
because they make dependencies less explicit.
"""


# ============================================================
# 26. Package Public API
# ============================================================

"""
A package can expose a clean public API.

For example:

shop/
├── __init__.py
├── products.py
├── customers.py
└── orders.py


__init__.py:

from .products import Product
from .customers import Customer
from .orders import Order


Then:

from shop import Product, Customer, Order
"""


# ============================================================
# 27. Avoiding Circular Imports
# ============================================================

"""
A circular import happens when:

module_a imports module_b

and:

module_b imports module_a


Example:

a.py
    from b import something


b.py
    from a import something


This can cause import errors or partially initialized modules.

Good package design helps avoid circular dependencies.
"""


# ============================================================
# 28. Better Package Design
# ============================================================

"""
Instead of:

users.py
    imports orders.py

orders.py
    imports users.py

consider extracting shared functionality:

common.py

Then:

users.py
    -> common.py

orders.py
    -> common.py
"""


# ============================================================
# 29. Practical Backend Structure
# ============================================================

"""
A backend application might eventually look like:

backend/
│
├── main.py
│
├── users/
│   ├── __init__.py
│   ├── models.py
│   ├── services.py
│   └── validators.py
│
├── products/
│   ├── __init__.py
│   ├── models.py
│   ├── services.py
│   └── validators.py
│
├── orders/
│   ├── __init__.py
│   ├── models.py
│   └── services.py
│
└── database/
    ├── __init__.py
    ├── connection.py
    └── queries.py
"""


# ============================================================
# 30. Package Responsibilities
# ============================================================

"""
users/
    User-related functionality.

products/
    Product-related functionality.

orders/
    Order-related functionality.

database/
    Database-related functionality.

This organization makes a large project easier to navigate.
"""


# ============================================================
# 31. Package Initialization
# ============================================================

"""
When a package is imported, Python may execute its
__init__.py file.

For example:

import shop


The package initialization code can run at import time.

Because of this, avoid putting unnecessary side effects
inside __init__.py.
"""


# ============================================================
# 32. Keep __init__.py Simple
# ============================================================

"""
A good __init__.py usually contains:

- package metadata
- selected public exports
- small initialization logic when genuinely needed

Avoid putting large amounts of application logic there.
"""


# ============================================================
# 33. Packages and Reusability
# ============================================================

"""
Packages make it easier to create reusable components.

For example:

validators/
├── __init__.py
├── email.py
├── password.py
└── username.py


Different projects can potentially reuse these modules.
"""


# ============================================================
# 34. Packages and Separation of Concerns
# ============================================================

"""
A package should generally group related functionality.

For example:

authentication/
    login.py
    permissions.py
    tokens.py


rather than putting unrelated functionality
into one huge module.
"""


# ============================================================
# 35. Package Naming
# ============================================================

"""
Good package names are:

- lowercase
- descriptive
- short
- consistent

Examples:

users
products
database
authentication
payments
notifications
"""


# ============================================================
# 36. Module and Package Hierarchy
# ============================================================

"""
Think of the hierarchy like this:

Project
│
├── Package
│   ├── Module
│   ├── Module
│   └── Package
│       ├── Module
│       └── Module
│
└── Package
    └── Module
"""


# ============================================================
# 37. Package Import Examples
# ============================================================

"""
Different styles:

import shop.products

from shop import products

from shop.products import Product

import shop.products as products


Choose the style that makes dependencies
clear and readable.
"""


# ============================================================
# 38. Packages in Django
# ============================================================

"""
Django projects use packages extensively.

A Django application may contain modules such as:

models.py
views.py
urls.py
admin.py
forms.py
serializers.py


A larger project can also contain multiple packages
for different responsibilities.

Understanding Python packages is therefore essential
for Django development.
"""


# ============================================================
# 39. Common Mistakes
# ============================================================

"""
Common mistakes:

1. Using unclear package names.
2. Creating very deep package hierarchies unnecessarily.
3. Using wildcard imports.
4. Creating circular imports.
5. Putting too much logic in __init__.py.
6. Mixing unrelated responsibilities.
7. Using relative imports without understanding
   the package structure.
"""


# ============================================================
# 40. Best Practices
# ============================================================

"""
Best practices:

1. Group related modules together.
2. Keep package responsibilities clear.
3. Use explicit imports.
4. Avoid wildcard imports.
5. Keep __init__.py lightweight.
6. Avoid circular dependencies.
7. Use descriptive names.
8. Keep the hierarchy as simple as possible.
9. Define a clean public API when useful.
10. Separate application responsibilities.
"""


# ============================================================
# 41. Summary
# ============================================================

"""
Important concepts:

Module
    A single Python file.

Package
    A directory that organizes related modules.

__init__.py
    Package initialization module.

Absolute import
    Uses the full package path.

Relative import
    Uses . or .. to reference nearby modules.

__all__
    Defines intended public names for wildcard imports.

Public API
    The functionality a package intentionally exposes.

The main idea:

Modules organize code within files.

Packages organize related modules into a larger structure.

Together, they allow Python projects to grow without
becoming one huge, unmanageable file.
"""