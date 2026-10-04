
"""
Python Type Hints Fundamentals

Learn how to annotate variables, function parameters,
return values, collections, and optional values.

Type hints improve readability and tooling support.
Python does not enforce them automatically at runtime.
"""

from typing import Any


# ============================================================
# 1. Basic Variable Annotations
# ============================================================

name: str = "Mohsen"
age: int = 24
price: float = 49.99
is_active: bool = True

print(name, age, price, is_active)


# ============================================================
# 2. Function Parameter and Return Types
# ============================================================

def add(a: int, b: int) -> int:
    """Return the sum of two integers."""
    return a + b


def greet(name: str) -> str:
    """Return a greeting message."""
    return f"Hello, {name}!"


def display_message(message: str) -> None:
    """Print a message without returning a value."""
    print(message)


print(add(10, 20))
print(greet("Mohsen"))
display_message("Learning Python type hints")


# ============================================================
# 3. Type Hints Do Not Enforce Types at Runtime
# ============================================================

def multiply(a: int, b: int) -> int:
    return a * b


print(multiply(3, 4))

# Python still allows this call at runtime.
# A static type checker can report the mismatch.
print(multiply("ha", 3))


# ============================================================
# 4. Type Hints for Collections
# ============================================================

# Python 3.9+
scores: list[int] = [85, 90, 78]
tags: set[str] = {"python", "backend"}
coordinates: tuple[float, float] = (35.7, 51.4)
user: dict[str, str] = {
    "username": "mohsen",
    "email": "mohsen@example.com",
}

print(scores)
print(tags)
print(coordinates)
print(user)


# ============================================================
# 5. Functions That Accept Collections
# ============================================================

def calculate_average(numbers: list[float]) -> float:
    """Calculate the average of a non-empty list."""
    if not numbers:
        raise ValueError("The list must not be empty.")

    return sum(numbers) / len(numbers)


def get_usernames(users: list[dict[str, str]]) -> list[str]:
    """Extract usernames from a list of user dictionaries."""
    return [user["username"] for user in users]


print(calculate_average([10.0, 15.0, 20.0]))

users: list[dict[str, str]] = [
    {"username": "mohsen", "email": "mohsen@example.com"},
    {"username": "sara", "email": "sara@example.com"},
]

print(get_usernames(users))


# ============================================================
# 6. Optional Values with None
# ============================================================

def find_username(user_id: int) -> str | None:
    """Return a username or None when no user exists."""
    usernames: dict[int, str] = {
        1: "mohsen",
        2: "sara",
    }

    return usernames.get(user_id)


result = find_username(1)

if result is not None:
    print(result)
else:
    print("User not found.")


# ============================================================
# 7. Union Types
# ============================================================

def normalize_id(value: int | str) -> str:
    """Convert an integer or string identifier to a string."""
    return str(value).strip()


print(normalize_id(101))
print(normalize_id(" user-202 "))


# ============================================================
# 8. Type Narrowing
# ============================================================

def describe_value(value: int | str) -> str:
    """Handle each supported type explicitly."""
    if isinstance(value, int):
        return f"Integer: {value}"

    return f"String: {value}"


print(describe_value(42))
print(describe_value("Python"))


# ============================================================
# 9. Default Parameter Values
# ============================================================

def create_greeting(
    name: str,
    prefix: str = "Hello",
) -> str:
    return f"{prefix}, {name}!"


print(create_greeting("Mohsen"))
print(create_greeting("Sara", "Welcome"))


# ============================================================
# 10. Type Hints for Keyword Arguments
# ============================================================

def create_account(
    username: str,
    email: str,
    is_active: bool = True,
) -> dict[str, str | bool]:
    return {
        "username": username,
        "email": email,
        "is_active": is_active,
    }


account = create_account(
    username="mohsen",
    email="mohsen@example.com",
)

print(account)


# ============================================================
# 11. Type Hints with *args
# ============================================================

def calculate_sum(*numbers: int) -> int:
    """Accept any number of integer arguments."""
    return sum(numbers)


print(calculate_sum(1, 2, 3))
print(calculate_sum(10, 20, 30, 40))


# ============================================================
# 12. Type Hints with **kwargs
# ============================================================

def display_settings(**settings: Any) -> None:
    """Display settings whose values may have different types."""
    for key, value in settings.items():
        print(f"{key}: {value}")


display_settings(
    theme="dark",
    notifications=True,
    page_size=20,
)


# ============================================================
# 13. Type Aliases
# ============================================================

UserRecord = dict[str, str | int | bool]


def display_user(user: UserRecord) -> None:
    print(f"Username: {user['username']}")
    print(f"User ID: {user['id']}")


sample_user: UserRecord = {
    "id": 101,
    "username": "mohsen",
    "is_active": True,
}

display_user(sample_user)


# ============================================================
# 14. Literal Types
# ============================================================

from typing import Literal


OrderStatus = Literal[
    "pending",
    "paid",
    "shipped",
    "cancelled",
]


def update_order_status(status: OrderStatus) -> str:
    return f"Order status updated to {status}"


print(update_order_status("paid"))

# A static type checker should reject unsupported values.
# update_order_status("unknown")


# ============================================================
# 15. Typed Dictionaries
# ============================================================

from typing import TypedDict


class Product(TypedDict):
    id: int
    name: str
    price: float
    in_stock: bool


def display_product(product: Product) -> None:
    print(
        f"{product['name']}: "
        f"${product['price']:.2f}"
    )


keyboard: Product = {
    "id": 1,
    "name": "Keyboard",
    "price": 49.99,
    "in_stock": True,
}

display_product(keyboard)


# ============================================================
# 16. Callable Type Hints
# ============================================================

from collections.abc import Callable


def apply_operation(
    a: int,
    b: int,
    operation: Callable[[int, int], int],
) -> int:
    """Apply a function to two integer arguments."""
    return operation(a, b)


def subtract(a: int, b: int) -> int:
    return a - b


print(apply_operation(10, 4, add))
print(apply_operation(10, 4, subtract))
print(apply_operation(10, 4, lambda a, b: a * b))


# ============================================================
# 17. Type Hints for Iterables
# ============================================================

from collections.abc import Iterable


def print_items(items: Iterable[str]) -> None:
    """Accept lists, tuples, sets, and other string iterables."""
    for item in items:
        print(item)


print_items(["Python", "Django", "PostgreSQL"])
print_items(("Kotlin", "Android"))


# ============================================================
# 18. Type Hints for Iterators
# ============================================================

from collections.abc import Iterator


def countdown(start: int) -> Iterator[int]:
    """Yield integers from start down to one."""
    while start > 0:
        yield start
        start -= 1


for number in countdown(3):
    print(number)


# ============================================================
# 19. Type Hints for Exceptions and Validation
# ============================================================

def validate_age(age: int) -> None:
    """Raise an exception when the age is invalid."""
    if age < 0:
        raise ValueError("Age cannot be negative.")


validate_age(24)


# ============================================================
# 20. Type Hints for Class Attributes and Methods
# ============================================================

class ShoppingCart:
    def __init__(self) -> None:
        self.items: list[str] = []

    def add_item(self, item: str) -> None:
        self.items.append(item)

    def get_items(self) -> list[str]:
        return self.items

    def item_count(self) -> int:
        return len(self.items)


cart = ShoppingCart()
cart.add_item("Keyboard")
cart.add_item("Mouse")

print(cart.get_items())
print(cart.item_count())


# ============================================================
# 21. Type Hints for Database-Like Results
# ============================================================

class UserRecordData(TypedDict):
    id: int
    username: str
    email: str


def get_user_by_id(user_id: int) -> UserRecordData | None:
    """Simulate looking up a user in a database."""
    database: dict[int, UserRecordData] = {
        1: {
            "id": 1,
            "username": "mohsen",
            "email": "mohsen@example.com",
        }
    }

    return database.get(user_id)


database_user = get_user_by_id(1)

if database_user is not None:
    print(database_user["email"])


# ============================================================
# 22. Type Hints for API Responses
# ============================================================

class ApiResponse(TypedDict):
    success: bool
    message: str
    data: dict[str, str] | None


def build_response(
    success: bool,
    message: str,
    data: dict[str, str] | None = None,
) -> ApiResponse:
    return {
        "success": success,
        "message": message,
        "data": data,
    }


response = build_response(
    success=True,
    message="User retrieved successfully.",
    data={"username": "mohsen"},
)

print(response)


# ============================================================
# 23. Type Hints and Readability
# ============================================================

# Without type hints:
def process_order(order):
    return order["price"] * order["quantity"]


# With type hints:
class OrderData(TypedDict):
    price: float
    quantity: int


def calculate_order_total(order: OrderData) -> float:
    return order["price"] * order["quantity"]


order: OrderData = {
    "price": 25.5,
    "quantity": 3,
}

print(calculate_order_total(order))


# ============================================================
# 24. Common Type Hint Mistakes
# ============================================================

# Use list[int], not list[int, int], for a list of integers.
numbers: list[int] = [1, 2, 3]

# Use tuple[int, str] for a tuple with fixed positions.
user_summary: tuple[int, str] = (1, "mohsen")

# Use int | None when a value can be an integer or None.
user_id: int | None = 101

# -> None means the function does not return a useful value.
def save_record() -> None:
    print("Record saved.")


save_record()


# ============================================================
# 25. Type Hints Best Practices
# ============================================================

"""
Best practices:

1. Annotate public functions and methods.
2. Use descriptive names for type aliases.
3. Use collections such as list[str] and dict[str, int].
4. Use | None when a value may be absent.
5. Prefer specific types over Any when possible.
6. Use TypedDict for dictionary-shaped data.
7. Use Callable for function parameters.
8. Keep annotations accurate as code changes.
9. Remember that annotations do not automatically validate input.
10. Use a static type checker for larger projects.
"""


# ============================================================
# End of File
# ============================================================
