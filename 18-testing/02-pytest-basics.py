"""
Pytest Fundamentals

This file demonstrates the basics of pytest:
- Test functions
- Assertions
- Fixtures
- Parametrization
- Exception testing
- Temporary data
- Test organization
- Mocking basics
- Backend-oriented examples

Install pytest:

    pip install pytest

Run tests:

    pytest

Run this file:

    pytest 18-testing/02-pytest-basics.py

Run with verbose output:

    pytest -v
"""

import pytest


# ============================================================
# 1. Simple Functions
# ============================================================

def add(a: int, b: int) -> int:
    """Return the sum of two numbers."""
    return a + b


def subtract(a: int, b: int) -> int:
    """Return the difference between two numbers."""
    return a - b


def divide(a: float, b: float) -> float:
    """Return the division result."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")

    return a / b


# ============================================================
# 2. Basic Test
# ============================================================

def test_add():
    result = add(10, 20)

    assert result == 30


def test_subtract():
    result = subtract(20, 10)

    assert result == 10


# ============================================================
# 3. Direct Assertions
# ============================================================

def test_string():
    username = "mohsen"

    assert username == "mohsen"


def test_boolean():
    is_active = True

    assert is_active


def test_list():
    languages = [
        "Python",
        "Kotlin",
        "C++",
    ]

    assert "Python" in languages
    assert len(languages) == 3


def test_dictionary():
    user = {
        "id": 1,
        "username": "mohsen",
    }

    assert user["username"] == "mohsen"
    assert user["id"] == 1


# ============================================================
# 4. Testing Exceptions
# ============================================================

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)


# ============================================================
# 5. Testing Exception Messages
# ============================================================

def test_divide_by_zero_message():
    with pytest.raises(
        ValueError,
        match="Cannot divide by zero",
    ):
        divide(10, 0)


# ============================================================
# 6. Fixtures
# ============================================================

@pytest.fixture
def numbers():
    """Provide reusable test data."""
    return [10, 20, 30]


def test_numbers_length(numbers):
    assert len(numbers) == 3


def test_numbers_sum(numbers):
    assert sum(numbers) == 60


def test_first_number(numbers):
    assert numbers[0] == 10


# ============================================================
# 7. Fixture for a User
# ============================================================

@pytest.fixture
def user():
    return {
        "id": 1,
        "username": "mohsen",
        "email": "mohsen@example.com",
        "is_active": True,
    }


def test_user_username(user):
    assert user["username"] == "mohsen"


def test_user_is_active(user):
    assert user["is_active"] is True


def test_user_email(user):
    assert "@" in user["email"]


# ============================================================
# 8. Fixture Scope
# ============================================================

@pytest.fixture(scope="module")
def application_config():
    """
    This fixture is created once per test module.
    """
    return {
        "debug": False,
        "environment": "testing",
    }


def test_config_environment(application_config):
    assert application_config["environment"] == "testing"


def test_config_debug(application_config):
    assert application_config["debug"] is False


# ============================================================
# 9. Fixture with setup and teardown
# ============================================================

@pytest.fixture
def temporary_resource():
    """
    Demonstrate fixture setup and teardown.
    """

    resource = {
        "status": "open",
    }

    yield resource

    resource["status"] = "closed"


def test_resource_is_open(temporary_resource):
    assert temporary_resource["status"] == "open"


# ============================================================
# 10. Parametrization
# ============================================================

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 2, 3),
        (10, 20, 30),
        (-5, 5, 0),
        (100, 50, 150),
    ],
)
def test_add_multiple_cases(a, b, expected):
    assert add(a, b) == expected


# ============================================================
# 11. Parametrized String Tests
# ============================================================

@pytest.mark.parametrize(
    "value, expected",
    [
        ("python", "PYTHON"),
        ("django", "DJANGO"),
        ("backend", "BACKEND"),
    ],
)
def test_uppercase(value, expected):
    assert value.upper() == expected


# ============================================================
# 12. Testing Invalid Inputs
# ============================================================

@pytest.mark.parametrize(
    "value",
    [
        -1,
        -10,
        -100,
    ],
)
def test_invalid_age(value):
    with pytest.raises(ValueError):
        validate_age(value)


def validate_age(age: int) -> None:
    if age < 0:
        raise ValueError(
            "Age cannot be negative."
        )


# ============================================================
# 13. Testing Floating Point Values
# ============================================================

def calculate_average(numbers: list[float]) -> float:
    if not numbers:
        raise ValueError("Numbers cannot be empty.")

    return sum(numbers) / len(numbers)


def test_average():
    result = calculate_average(
        [10.0, 20.0, 30.0]
    )

    assert result == pytest.approx(20.0)


def test_average_with_fraction():
    result = calculate_average(
        [10.0, 20.0, 25.0]
    )

    assert result == pytest.approx(
        18.333333,
        rel=1e-5,
    )


# ============================================================
# 14. Testing Classes
# ============================================================

class User:
    def __init__(
        self,
        username: str,
        email: str,
    ):
        self.username = username
        self.email = email

    def is_valid(self) -> bool:
        return (
            bool(self.username)
            and "@" in self.email
        )


def test_user_creation():
    user = User(
        "mohsen",
        "mohsen@example.com",
    )

    assert user.username == "mohsen"
    assert user.email == "mohsen@example.com"


def test_valid_user():
    user = User(
        "mohsen",
        "mohsen@example.com",
    )

    assert user.is_valid()


def test_invalid_user():
    user = User(
        "",
        "invalid-email",
    )

    assert not user.is_valid()


# ============================================================
# 15. Fixture Returning an Object
# ============================================================

@pytest.fixture
def active_user():
    return User(
        "mohsen",
        "mohsen@example.com",
    )


def test_active_user(active_user):
    assert active_user.is_valid()


# ============================================================
# 16. Backend Service Example
# ============================================================

class OrderService:
    def calculate_total(
        self,
        price: float,
        quantity: int,
    ) -> float:

        if price < 0:
            raise ValueError(
                "Price cannot be negative."
            )

        if quantity <= 0:
            raise ValueError(
                "Quantity must be positive."
            )

        return price * quantity


@pytest.fixture
def order_service():
    return OrderService()


def test_order_total(order_service):
    result = order_service.calculate_total(
        25.0,
        4,
    )

    assert result == 100.0


def test_negative_price(order_service):
    with pytest.raises(ValueError):
        order_service.calculate_total(
            -10.0,
            2,
        )


def test_invalid_quantity(order_service):
    with pytest.raises(ValueError):
        order_service.calculate_total(
            10.0,
            0,
        )


# ============================================================
# 17. Repository Example
# ============================================================

class UserRepository:
    def __init__(self):
        self.users = {}

    def add(self, user: User) -> int:
        user_id = len(self.users) + 1

        self.users[user_id] = user

        return user_id

    def get_by_id(
        self,
        user_id: int,
    ) -> User | None:

        return self.users.get(user_id)

    def count(self) -> int:
        return len(self.users)


@pytest.fixture
def user_repository():
    return UserRepository()


def test_repository_add(
    user_repository,
):
    user = User(
        "mohsen",
        "mohsen@example.com",
    )

    user_id = user_repository.add(user)

    assert user_id == 1
    assert user_repository.count() == 1


def test_repository_get(
    user_repository,
):
    user = User(
        "mohsen",
        "mohsen@example.com",
    )

    user_repository.add(user)

    result = user_repository.get_by_id(1)

    assert result is not None
    assert result.username == "mohsen"


def test_repository_missing_user(
    user_repository,
):
    result = user_repository.get_by_id(999)

    assert result is None


# ============================================================
# 18. Fixture Composition
# ============================================================

@pytest.fixture
def repository():
    return UserRepository()


@pytest.fixture
def repository_user(repository):
    user = User(
        "sara",
        "sara@example.com",
    )

    repository.add(user)

    return repository


def test_repository_user(
    repository_user,
):
    user = repository_user.get_by_id(1)

    assert user is not None
    assert user.username == "sara"


# ============================================================
# 19. Temporary Directory
# ============================================================

def test_temporary_directory(
    tmp_path,
):
    file_path = tmp_path / "test.txt"

    file_path.write_text(
        "Hello Python",
        encoding="utf-8",
    )

    assert file_path.exists()

    content = file_path.read_text(
        encoding="utf-8",
    )

    assert content == "Hello Python"


# ============================================================
# 20. Temporary Files
# ============================================================

def test_temporary_file(
    tmp_path,
):
    file_path = tmp_path / "users.txt"

    users = [
        "mohsen",
        "sara",
        "ali",
    ]

    file_path.write_text(
        "\n".join(users),
        encoding="utf-8",
    )

    content = file_path.read_text(
        encoding="utf-8",
    )

    assert "mohsen" in content
    assert "sara" in content
    assert "ali" in content


# ============================================================
# 21. Monkeypatch
# ============================================================

def get_environment():
    import os

    return os.getenv(
        "APP_ENV",
        "development",
    )


def test_environment(
    monkeypatch,
):
    monkeypatch.setenv(
        "APP_ENV",
        "testing",
    )

    assert get_environment() == "testing"


# ============================================================
# 22. Monkeypatching a Function
# ============================================================

def get_exchange_rate():
    return 1.08


def calculate_price_in_usd(
    price_eur: float,
) -> float:

    rate = get_exchange_rate()

    return price_eur * rate


def test_exchange_rate(
    monkeypatch,
):
    monkeypatch.setattr(
        __name__,
        "get_exchange_rate",
        lambda: 1.10,
    )

    result = calculate_price_in_usd(100)

    assert result == pytest.approx(110.0)


# ============================================================
# 23. Mocking with unittest.mock
# ============================================================

from unittest.mock import Mock


def send_email(
    email: str,
    message: str,
) -> bool:
    print(
        f"Sending email to {email}: {message}"
    )

    return True


def notify_user(
    email: str,
    email_sender,
) -> bool:
    return email_sender(
        email,
        "Your account was created.",
    )


def test_notify_user():
    mock_sender = Mock(
        return_value=True,
    )

    result = notify_user(
        "mohsen@example.com",
        mock_sender,
    )

    assert result is True

    mock_sender.assert_called_once_with(
        "mohsen@example.com",
        "Your account was created.",
    )


# ============================================================
# 24. Mock Objects
# ============================================================

def test_mock_object():
    user = Mock()

    user.username = "mohsen"
    user.is_active = True

    assert user.username == "mohsen"
    assert user.is_active is True


# ============================================================
# 25. Mock Method Calls
# ============================================================

def save_user(
    repository,
    user,
):
    repository.save(user)

    return True


def test_save_user():
    repository = Mock()

    user = {
        "username": "mohsen",
    }

    result = save_user(
        repository,
        user,
    )

    assert result is True

    repository.save.assert_called_once_with(
        user
    )


# ============================================================
# 26. API Client Example
# ============================================================

class PaymentClient:
    def charge(
        self,
        amount: float,
    ) -> bool:
        return True


def process_order(
    payment_client: PaymentClient,
    amount: float,
) -> str:

    success = payment_client.charge(
        amount
    )

    if not success:
        raise RuntimeError(
            "Payment failed."
        )

    return "Order completed."


def test_process_order():
    payment_client = Mock()

    payment_client.charge.return_value = True

    result = process_order(
        payment_client,
        100.0,
    )

    assert result == "Order completed."

    payment_client.charge.assert_called_once_with(
        100.0
    )


# ============================================================
# 27. Testing Failed External Services
# ============================================================

def test_failed_payment():
    payment_client = Mock()

    payment_client.charge.return_value = False

    with pytest.raises(
        RuntimeError,
        match="Payment failed",
    ):
        process_order(
            payment_client,
            100.0,
        )


# ============================================================
# 28. Marking Tests
# ============================================================

@pytest.mark.slow
def test_slow_operation():
    """
    Example of a custom marker.

    Configure custom markers in pytest.ini or pyproject.toml.
    """
    total = sum(range(100_000))

    assert total > 0


# ============================================================
# 29. Skip Tests
# ============================================================

@pytest.mark.skip(
    reason="Demonstration of skipped tests."
)
def test_skipped():
    assert False


# ============================================================
# 30. Conditional Skip
# ============================================================

import sys


@pytest.mark.skipif(
    sys.platform == "win32",
    reason="Demonstration of conditional skip.",
)
def test_not_windows():
    assert True


# ============================================================
# 31. Expected Failure
# ============================================================

@pytest.mark.xfail(
    reason="Known example failure.",
)
def test_expected_failure():
    assert 1 == 2


# ============================================================
# 32. Test Classes
# ============================================================

class TestCalculator:
    """Pytest test classes do not need to inherit from TestCase."""

    def test_add(self):
        assert add(2, 3) == 5

    def test_subtract(self):
        assert subtract(5, 3) == 2


# ============================================================
# 33. Fixture Factory
# ============================================================

@pytest.fixture
def make_user():
    def _make_user(
        username: str = "mohsen",
        email: str = "mohsen@example.com",
    ) -> User:
        return User(
            username,
            email,
        )

    return _make_user


def test_user_factory(make_user):
    user = make_user()

    assert user.username == "mohsen"


def test_custom_user_factory(make_user):
    user = make_user(
        username="sara",
        email="sara@example.com",
    )

    assert user.username == "sara"


# ============================================================
# 34. Test Organization
# ============================================================

"""
A real project should normally separate production code
from test code.

Example:

project/
├── app/
│   ├── services/
│   │   └── order_service.py
│   ├── repositories/
│   │   └── user_repository.py
│   └── models/
│       └── user.py
│
├── tests/
│   ├── services/
│   │   └── test_order_service.py
│   ├── repositories/
│   │   └── test_user_repository.py
│   └── conftest.py
│
├── pyproject.toml
└── README.md
"""


# ============================================================
# 35. conftest.py
# ============================================================

"""
In larger pytest projects, reusable fixtures are usually
stored in conftest.py.

Example:

tests/
├── conftest.py
├── test_users.py
└── test_orders.py

A fixture in conftest.py can be shared by multiple tests
without importing it manually.
"""


# ============================================================
# 36. Useful Pytest Commands
# ============================================================

"""
Run all tests:

    pytest

Verbose output:

    pytest -v

Run a specific file:

    pytest tests/test_users.py

Run a specific test:

    pytest tests/test_users.py::test_create_user

Run tests matching a keyword:

    pytest -k "user"

Run only marked tests:

    pytest -m slow

Stop after first failure:

    pytest -x

Show print output:

    pytest -s

Show short test summary:

    pytest -ra
"""


# ============================================================
# 37. pytest.ini Example
# ============================================================

"""
A project can configure pytest with pytest.ini.

Example:

[pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
markers =
    slow: marks slow tests

This keeps test discovery and configuration consistent.
"""


# ============================================================
# 38. unittest vs pytest
# ============================================================

"""
unittest:

- Built into Python
- Uses TestCase classes
- Uses self.assertEqual(...)
- Uses setUp and tearDown

pytest:

- Third-party package
- Usually simpler syntax
- Uses plain assert
- Powerful fixtures
- Parametrization
- Plugins
- Excellent failure messages
- Widely used in Python projects

Both are useful to know.
"""


# ============================================================
# 39. Backend Testing Pyramid
# ============================================================

"""
A backend project commonly contains:

Unit Tests
    ↓
Service and business logic

Integration Tests
    ↓
Database + repository + service

API Tests
    ↓
HTTP endpoints

End-to-End Tests
    ↓
Complete user workflows

Unit tests are usually the fastest and most numerous.
"""


# ============================================================
# 40. Best Practices
# ============================================================

"""
Best practices:

1. Keep tests independent.
2. Use fixtures for reusable setup.
3. Use parametrization for repeated scenarios.
4. Test success and failure paths.
5. Test edge cases.
6. Mock external services when appropriate.
7. Avoid mocking everything.
8. Keep unit tests fast.
9. Use descriptive test names.
10. Organize tests by application responsibility.
11. Keep reusable fixtures in conftest.py.
12. Run tests before committing changes.
13. Add tests when fixing bugs.
14. Test behavior instead of implementation details.
"""


# ============================================================
# End of File
# ============================================================