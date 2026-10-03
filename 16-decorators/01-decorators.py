"""
Python Decorators
=================

This file covers:
- Functions as objects
- Passing functions as arguments
- Returning functions
- Nested functions
- Basic decorators
- @decorator syntax
- *args and **kwargs
- functools.wraps
- Decorator execution flow
- Practical backend examples
"""

from functools import wraps


# ============================================================
# 1. Functions Are Objects
# ============================================================

def greet():
    print("Hello")


greet()

function_reference = greet

function_reference()


# A function can be stored in a variable.


# ============================================================
# 2. Passing A Function As An Argument
# ============================================================

def say_hello():
    print("Hello")


def execute(function):
    function()


execute(say_hello)


# Functions can be passed to other functions.


# ============================================================
# 3. Returning A Function
# ============================================================

def create_greeting():
    def greeting():
        print("Hello from nested function")

    return greeting


greeting_function = create_greeting()

greeting_function()


# A function can return another function.


# ============================================================
# 4. Nested Functions
# ============================================================

def outer():
    print("Outer function")

    def inner():
        print("Inner function")

    inner()


outer()


# inner() only exists inside outer().


# ============================================================
# 5. Simple Function Wrapper
# ============================================================

def say_hello():
    print("Hello")


def wrapper():
    print("Before function")

    say_hello()

    print("After function")


wrapper()


# A decorator follows this general idea:
#
# Add behavior before and/or after another function.


# ============================================================
# 6. Basic Decorator
# ============================================================

def my_decorator(function):
    def wrapper():
        print("Before function")

        function()

        print("After function")

    return wrapper


def greet():
    print("Hello")


decorated_greet = my_decorator(greet)

decorated_greet()


# ============================================================
# 7. Decorator With @ Syntax
# ============================================================

def my_decorator(function):
    def wrapper():
        print("Before function")
        function()
        print("After function")

    return wrapper


@my_decorator
def greet():
    print("Hello")


greet()


# This:
#
# @my_decorator
# def greet():
#     ...
#
# is equivalent to:
#
# def greet():
#     ...
#
# greet = my_decorator(greet)


# ============================================================
# 8. Decorator Execution Flow
# ============================================================

def logger(function):
    print("Decorator is being applied")

    def wrapper():
        print("Function is starting")

        function()

        print("Function is finished")

    return wrapper


@logger
def say_hello():
    print("Hello")


print("Calling function")

say_hello()


# The decorator itself runs when the function
# is defined.
#
# The wrapper runs when the decorated function
# is called.


# ============================================================
# 9. Decorator With Arguments
# ============================================================

def logger(function):
    def wrapper(name):
        print("Calling function")

        function(name)

        print("Function completed")

    return wrapper


@logger
def greet(name):
    print(f"Hello, {name}")


greet("Mohsen")


# ============================================================
# 10. *args
# ============================================================

def logger(function):
    def wrapper(*args):
        print("Calling function")

        result = function(*args)

        print("Function completed")

        return result

    return wrapper


@logger
def add(a, b):
    return a + b


result = add(10, 20)

print(result)


# *args allows the decorator to work
# with different positional arguments.


# ============================================================
# 11. **kwargs
# ============================================================

def logger(function):
    def wrapper(*args, **kwargs):
        print("Calling function")

        result = function(
            *args,
            **kwargs,
        )

        print("Function completed")

        return result

    return wrapper


@logger
def create_user(name, role="user"):
    return {
        "name": name,
        "role": role,
    }


user = create_user(
    name="Mohsen",
    role="developer",
)

print(user)


# ============================================================
# 12. Returning The Function Result
# ============================================================

def decorator(function):
    def wrapper(*args, **kwargs):
        result = function(
            *args,
            **kwargs,
        )

        return result

    return wrapper


@decorator
def multiply(a, b):
    return a * b


result = multiply(5, 4)

print(result)


# A decorator should normally preserve
# the original function's return value.


# ============================================================
# 13. Before And After Logic
# ============================================================

def log_execution(function):
    def wrapper(*args, **kwargs):
        print("Starting...")

        result = function(
            *args,
            **kwargs,
        )

        print("Finished.")

        return result

    return wrapper


@log_execution
def calculate_total(price, quantity):
    return price * quantity


total = calculate_total(100, 3)

print(total)


# ============================================================
# 14. Measuring Execution
# ============================================================

import time


def measure_time(function):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()

        result = function(
            *args,
            **kwargs,
        )

        end = time.perf_counter()

        print(
            f"Execution time: "
            f"{end - start:.6f} seconds"
        )

        return result

    return wrapper


@measure_time
def calculate():
    total = 0

    for number in range(1_000_000):
        total += number

    return total


print(calculate())


# ============================================================
# 15. functools.wraps
# ============================================================

def logger(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print("Calling function")

        return function(
            *args,
            **kwargs,
        )

    return wrapper


@logger
def greet(name):
    """Greet a user by name."""

    print(f"Hello, {name}")


greet("Mohsen")

print(greet.__name__)
print(greet.__doc__)


# functools.wraps preserves metadata
# from the original function.


# ============================================================
# 16. Why functools.wraps Matters
# ============================================================

def bad_decorator(function):
    def wrapper(*args, **kwargs):
        return function(
            *args,
            **kwargs,
        )

    return wrapper


@bad_decorator
def example():
    """Example function."""

    pass


print(example.__name__)
print(example.__doc__)


# Without wraps, metadata can be replaced
# by the wrapper's metadata.


# ============================================================
# 17. Correct Decorator Pattern
# ============================================================

def decorator(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        return function(
            *args,
            **kwargs,
        )

    return wrapper


# This is a common reusable decorator pattern.


# ============================================================
# 18. Authentication Example
# ============================================================

def require_auth(function):
    @wraps(function)
    def wrapper(user, *args, **kwargs):
        if not user["authenticated"]:
            print("Access denied")
            return None

        return function(
            user,
            *args,
            **kwargs,
        )

    return wrapper


@require_auth
def dashboard(user):
    print(
        f"Welcome {user['name']}"
    )


authenticated_user = {
    "name": "Mohsen",
    "authenticated": True,
}

guest_user = {
    "name": "Guest",
    "authenticated": False,
}

dashboard(authenticated_user)
dashboard(guest_user)


# ============================================================
# 19. Permission Example
# ============================================================

def require_role(required_role):
    def decorator(function):
        @wraps(function)
        def wrapper(user, *args, **kwargs):
            if user["role"] != required_role:
                print("Permission denied")
                return None

            return function(
                user,
                *args,
                **kwargs,
            )

        return wrapper

    return decorator


@require_role("admin")
def delete_user(user, user_id):
    print(
        f"User {user_id} deleted"
    )


admin = {
    "name": "Admin",
    "role": "admin",
}

regular_user = {
    "name": "Mohsen",
    "role": "user",
}

delete_user(admin, 101)
delete_user(regular_user, 101)


# ============================================================
# 20. Decorator With Configuration
# ============================================================

def repeat(times):
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            result = None

            for _ in range(times):
                result = function(
                    *args,
                    **kwargs,
                )

            return result

        return wrapper

    return decorator


@repeat(3)
def say_hello():
    print("Hello")


say_hello()


# ============================================================
# 21. Multiple Decorators
# ============================================================

def first(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print("First")
        return function(
            *args,
            **kwargs,
        )

    return wrapper


def second(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print("Second")
        return function(
            *args,
            **kwargs,
        )

    return wrapper


@first
@second
def greet():
    print("Hello")


greet()


# Decorators are applied from bottom to top.
#
# second is applied first.
# first wraps the result of second.


# ============================================================
# 22. Logging Decorator
# ============================================================

def log_call(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print(
            f"Calling: {function.__name__}"
        )

        result = function(
            *args,
            **kwargs,
        )

        print(
            f"Finished: {function.__name__}"
        )

        return result

    return wrapper


@log_call
def create_order(order_id):
    return {
        "id": order_id,
        "status": "created",
    }


print(create_order(1001))


# ============================================================
# 23. Validation Decorator
# ============================================================

def require_positive(function):
    @wraps(function)
    def wrapper(value, *args, **kwargs):
        if value <= 0:
            raise ValueError(
                "Value must be positive"
            )

        return function(
            value,
            *args,
            **kwargs,
        )

    return wrapper


@require_positive
def calculate_discount(price):
    return price * 0.9


print(calculate_discount(100))


# ============================================================
# 24. Exception Logging Decorator
# ============================================================

def log_errors(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        try:
            return function(
                *args,
                **kwargs,
            )

        except Exception as error:
            print(
                f"Error in "
                f"{function.__name__}: {error}"
            )
            raise

    return wrapper


@log_errors
def divide(a, b):
    return a / b


print(divide(10, 2))

# Example:
#
# divide(10, 0)


# ============================================================
# 25. Cache-Like Example
# ============================================================

def simple_cache(function):
    cache = {}

    @wraps(function)
    def wrapper(value):
        if value in cache:
            print("Returning cached value")
            return cache[value]

        result = function(value)

        cache[value] = result

        return result

    return wrapper


@simple_cache
def square(number):
    print("Calculating...")
    return number ** 2


print(square(5))
print(square(5))


# ============================================================
# 26. Decorator And Closures
# ============================================================

def create_multiplier(multiplier):
    def decorator(function):
        @wraps(function)
        def wrapper(value):
            result = function(value)
            return result * multiplier

        return wrapper

    return decorator


@create_multiplier(2)
def get_price():
    return 100


print(get_price())


# The decorator remembers multiplier
# through a closure.


# ============================================================
# 27. Practical API Permission Example
# ============================================================

def require_permission(permission):
    def decorator(function):
        @wraps(function)
        def wrapper(user, *args, **kwargs):
            permissions = user.get(
                "permissions",
                [],
            )

            if permission not in permissions:
                raise PermissionError(
                    "Permission denied"
                )

            return function(
                user,
                *args,
                **kwargs,
            )

        return wrapper

    return decorator


@require_permission("delete_users")
def delete_account(user, account_id):
    return {
        "account_id": account_id,
        "deleted": True,
    }


admin = {
    "id": 1,
    "permissions": [
        "delete_users",
    ],
}

print(
    delete_account(
        admin,
        500,
    )
)


# ============================================================
# 28. Decorators In Django
# ============================================================

# Django uses decorators extensively.
#
# Examples include:
#
# @login_required
# @permission_required
# @require_http_methods
#
# The exact decorators depend on the Django component
# being used.


# ============================================================
# 29. Decorators In Web Development
# ============================================================

# Decorators can be used for:
#
# - Authentication
# - Authorization
# - Logging
# - Validation
# - Caching
# - Rate limiting
# - Measuring execution time
# - Error handling
# - Transaction management
# - Access control


# ============================================================
# 30. Important Decorator Pattern
# ============================================================

def decorator(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        # Before

        result = function(
            *args,
            **kwargs,
        )

        # After

        return result

    return wrapper


# This pattern is worth remembering.


# ============================================================
# 31. Key Rules
# ============================================================

# Rule 1:
# Functions are first-class objects.

# Rule 2:
# Functions can be passed to other functions.

# Rule 3:
# Functions can return other functions.

# Rule 4:
# A decorator wraps another function
# to add or modify behavior.

# Rule 5:
# @decorator is syntactic sugar.

# Rule 6:
# Use *args and **kwargs for flexible wrappers.

# Rule 7:
# Use functools.wraps in decorators.

# Rule 8:
# Decorators can accept their own configuration.

# Rule 9:
# Multiple decorators are applied from
# bottom to top.

# Rule 10:
# Decorators are heavily used in web frameworks.