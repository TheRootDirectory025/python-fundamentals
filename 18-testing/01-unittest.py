"""
Python Unit Testing with unittest

This file demonstrates the fundamentals of Python's
built-in unittest framework.

Unit tests help verify that individual pieces of code
work correctly and continue working after changes.
"""

import unittest


# ============================================================
# 1. Simple Function
# ============================================================

def add(a: int, b: int) -> int:
    """Return the sum of two numbers."""
    return a + b


def subtract(a: int, b: int) -> int:
    """Return the difference between two numbers."""
    return a - b


def multiply(a: int, b: int) -> int:
    """Return the product of two numbers."""
    return a * b


def divide(a: float, b: float) -> float:
    """Return the division result."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")

    return a / b


# ============================================================
# 2. Basic TestCase
# ============================================================

class TestMathFunctions(unittest.TestCase):
    """Tests for basic mathematical functions."""

    def test_add(self):
        result = add(10, 5)

        self.assertEqual(result, 15)

    def test_subtract(self):
        result = subtract(10, 5)

        self.assertEqual(result, 5)

    def test_multiply(self):
        result = multiply(10, 5)

        self.assertEqual(result, 50)

    def test_divide(self):
        result = divide(10, 5)

        self.assertEqual(result, 2)


# ============================================================
# 3. Common Assertions
# ============================================================

class TestAssertions(unittest.TestCase):
    """Demonstrate common unittest assertions."""

    def test_equal(self):
        self.assertEqual(10, 10)

    def test_not_equal(self):
        self.assertNotEqual(10, 20)

    def test_true(self):
        self.assertTrue(True)

    def test_false(self):
        self.assertFalse(False)

    def test_is_none(self):
        value = None

        self.assertIsNone(value)

    def test_is_not_none(self):
        value = "Python"

        self.assertIsNotNone(value)

    def test_in(self):
        languages = ["Python", "Kotlin", "C++"]

        self.assertIn("Python", languages)

    def test_not_in(self):
        languages = ["Python", "Kotlin", "C++"]

        self.assertNotIn("JavaScript", languages)


# ============================================================
# 4. Testing Exceptions
# ============================================================

class TestExceptions(unittest.TestCase):
    """Test functions that should raise exceptions."""

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)


# ============================================================
# 5. Testing Error Messages
# ============================================================

class TestExceptionMessages(unittest.TestCase):
    """Test both exception type and message."""

    def test_divide_by_zero_message(self):
        with self.assertRaisesRegex(
            ValueError,
            "Cannot divide by zero",
        ):
            divide(10, 0)


# ============================================================
# 6. setUp
# ============================================================

class TestWithSetup(unittest.TestCase):
    """Create shared test data before every test."""

    def setUp(self):
        self.numbers = [10, 20, 30]

    def test_length(self):
        self.assertEqual(
            len(self.numbers),
            3,
        )

    def test_first_item(self):
        self.assertEqual(
            self.numbers[0],
            10,
        )

    def test_total(self):
        self.assertEqual(
            sum(self.numbers),
            60,
        )


# ============================================================
# 7. tearDown
# ============================================================

class TestWithTeardown(unittest.TestCase):
    """Demonstrate cleanup after every test."""

    def setUp(self):
        self.resource = {
            "status": "open",
        }

    def tearDown(self):
        self.resource["status"] = "closed"

    def test_resource_is_open(self):
        self.assertEqual(
            self.resource["status"],
            "open",
        )


# ============================================================
# 8. setUpClass and tearDownClass
# ============================================================

class TestClassSetup(unittest.TestCase):
    """Demonstrate class-level setup and cleanup."""

    @classmethod
    def setUpClass(cls):
        cls.database = {
            "status": "connected",
        }

    @classmethod
    def tearDownClass(cls):
        cls.database = None

    def test_database_connection(self):
        self.assertEqual(
            self.database["status"],
            "connected",
        )


# ============================================================
# 9. Testing Strings
# ============================================================

class TestStrings(unittest.TestCase):
    """Test string-related behavior."""

    def test_upper(self):
        self.assertEqual(
            "python".upper(),
            "PYTHON",
        )

    def test_lower(self):
        self.assertEqual(
            "PYTHON".lower(),
            "python",
        )

    def test_contains(self):
        message = "Python Backend"

        self.assertIn(
            "Backend",
            message,
        )

    def test_starts_with(self):
        message = "https://example.com"

        self.assertTrue(
            message.startswith("https://")
        )


# ============================================================
# 10. Testing Lists
# ============================================================

class TestLists(unittest.TestCase):
    """Test list behavior."""

    def setUp(self):
        self.products = [
            "Keyboard",
            "Mouse",
            "Monitor",
        ]

    def test_product_count(self):
        self.assertEqual(
            len(self.products),
            3,
        )

    def test_product_exists(self):
        self.assertIn(
            "Mouse",
            self.products,
        )

    def test_product_order(self):
        self.assertEqual(
            self.products[0],
            "Keyboard",
        )


# ============================================================
# 11. Testing Dictionaries
# ============================================================

class TestDictionary(unittest.TestCase):
    """Test dictionary-based data."""

    def setUp(self):
        self.user = {
            "id": 1,
            "username": "mohsen",
            "is_active": True,
        }

    def test_username(self):
        self.assertEqual(
            self.user["username"],
            "mohsen",
        )

    def test_user_id(self):
        self.assertEqual(
            self.user["id"],
            1,
        )

    def test_active_status(self):
        self.assertTrue(
            self.user["is_active"]
        )


# ============================================================
# 12. Testing Boolean Logic
# ============================================================

def is_adult(age: int) -> bool:
    return age >= 18


class TestBooleanLogic(unittest.TestCase):
    def test_adult(self):
        self.assertTrue(is_adult(24))

    def test_not_adult(self):
        self.assertFalse(is_adult(16))


# ============================================================
# 13. Testing Multiple Inputs
# ============================================================

class TestMultipleCases(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-2, -3), -5)

    def test_add_zero(self):
        self.assertEqual(add(0, 10), 10)


# ============================================================
# 14. Testing Floating-Point Numbers
# ============================================================

class TestFloatingPoint(unittest.TestCase):
    def test_division(self):
        result = divide(10, 3)

        self.assertAlmostEqual(
            result,
            3.333333,
            places=5,
        )


# ============================================================
# 15. Testing Objects
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


class TestUser(unittest.TestCase):
    def test_user_creation(self):
        user = User(
            "mohsen",
            "mohsen@example.com",
        )

        self.assertEqual(
            user.username,
            "mohsen",
        )

    def test_valid_user(self):
        user = User(
            "mohsen",
            "mohsen@example.com",
        )

        self.assertTrue(
            user.is_valid()
        )

    def test_invalid_user(self):
        user = User(
            "",
            "invalid-email",
        )

        self.assertFalse(
            user.is_valid()
        )


# ============================================================
# 16. Testing a Service
# ============================================================

class OrderService:
    """Simple order service."""

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


class TestOrderService(unittest.TestCase):
    def setUp(self):
        self.service = OrderService()

    def test_calculate_total(self):
        result = self.service.calculate_total(
            20.0,
            3,
        )

        self.assertEqual(
            result,
            60.0,
        )

    def test_negative_price(self):
        with self.assertRaises(ValueError):
            self.service.calculate_total(
                -10.0,
                2,
            )

    def test_invalid_quantity(self):
        with self.assertRaises(ValueError):
            self.service.calculate_total(
                10.0,
                0,
            )


# ============================================================
# 17. Testing Authentication Logic
# ============================================================

def authenticate(
    username: str,
    password: str,
) -> bool:
    """Simple authentication example."""

    users = {
        "mohsen": "123456",
        "admin": "admin123",
    }

    return users.get(username) == password


class TestAuthentication(unittest.TestCase):
    def test_valid_credentials(self):
        self.assertTrue(
            authenticate(
                "mohsen",
                "123456",
            )
        )

    def test_invalid_password(self):
        self.assertFalse(
            authenticate(
                "mohsen",
                "wrong-password",
            )
        )

    def test_unknown_user(self):
        self.assertFalse(
            authenticate(
                "unknown",
                "123456",
            )
        )


# ============================================================
# 18. Testing a Repository
# ============================================================

class UserRepository:
    """Simple in-memory repository."""

    def __init__(self):
        self.users = {}

    def add(self, user: User) -> None:
        user_id = len(self.users) + 1
        self.users[user_id] = user

    def get_by_id(
        self,
        user_id: int,
    ) -> User | None:
        return self.users.get(user_id)

    def count(self) -> int:
        return len(self.users)


class TestUserRepository(unittest.TestCase):
    def setUp(self):
        self.repository = UserRepository()

    def test_add_user(self):
        user = User(
            "mohsen",
            "mohsen@example.com",
        )

        self.repository.add(user)

        self.assertEqual(
            self.repository.count(),
            1,
        )

    def test_get_user(self):
        user = User(
            "mohsen",
            "mohsen@example.com",
        )

        self.repository.add(user)

        result = self.repository.get_by_id(1)

        self.assertIsNotNone(result)
        self.assertEqual(
            result.username,
            "mohsen",
        )

    def test_unknown_user(self):
        result = self.repository.get_by_id(999)

        self.assertIsNone(result)


# ============================================================
# 19. Skipping Tests
# ============================================================

class TestSkipping(unittest.TestCase):
    @unittest.skip(
        "Demonstration of skipped tests."
    )
    def test_skipped(self):
        self.fail(
            "This test should not execute."
        )


# ============================================================
# 20. Conditional Skip
# ============================================================

import sys


class TestConditionalSkip(unittest.TestCase):
    @unittest.skipIf(
        sys.platform == "win32",
        "Skipped on Windows.",
    )
    def test_not_windows(self):
        self.assertTrue(True)


# ============================================================
# 21. Expected Failure
# ============================================================

class TestExpectedFailure(unittest.TestCase):
    @unittest.expectedFailure
    def test_known_problem(self):
        self.assertEqual(
            1,
            2,
        )


# ============================================================
# 22. SubTest
# ============================================================

class TestWithSubTest(unittest.TestCase):
    def test_multiple_values(self):
        test_cases = [
            (2, 2, 4),
            (3, 3, 6),
            (5, 5, 10),
        ]

        for a, b, expected in test_cases:
            with self.subTest(
                a=a,
                b=b,
            ):
                self.assertEqual(
                    add(a, b),
                    expected,
                )


# ============================================================
# 23. Custom Assertion Messages
# ============================================================

class TestCustomMessages(unittest.TestCase):
    def test_user_count(self):
        users = [
            "mohsen",
            "sara",
            "ali",
        ]

        self.assertEqual(
            len(users),
            3,
            "The number of users should be 3.",
        )


# ============================================================
# 24. Testing Edge Cases
# ============================================================

class TestEdgeCases(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(
            add(0, 0),
            0,
        )

    def test_negative_numbers(self):
        self.assertEqual(
            add(-10, 5),
            -5,
        )

    def test_empty_string(self):
        self.assertEqual(
            "".strip(),
            "",
        )

    def test_empty_list(self):
        self.assertEqual(
            len([]),
            0,
        )


# ============================================================
# 25. Test Discovery
# ============================================================

"""
unittest can automatically discover test files.

Typical project structure:

project/
├── app/
│   ├── calculator.py
│   └── users.py
│
└── tests/
    ├── test_calculator.py
    └── test_users.py

Run test discovery with:

python -m unittest discover

Or specify a directory:

python -m unittest discover tests
"""


# ============================================================
# 26. Running Tests
# ============================================================

"""
Run this file directly:

python 18-testing/01-unittest.py

Run unittest:

python -m unittest 18-testing/01-unittest.py

Run with verbose output:

python -m unittest -v 18-testing/01-unittest.py

Run all discovered tests:

python -m unittest discover
"""


# ============================================================
# 27. Naming Conventions
# ============================================================

"""
Recommended naming:

Test file:
    test_calculator.py

Test class:
    TestCalculator

Test method:
    test_add_positive_numbers

Good names should describe the behavior being tested.
"""


# ============================================================
# 28. What Makes a Good Unit Test?
# ============================================================

"""
A good unit test should generally be:

- Small
- Focused
- Deterministic
- Easy to understand
- Fast
- Independent
- Repeatable

A test should ideally verify one behavior.
"""


# ============================================================
# 29. Arrange, Act, Assert
# ============================================================

class TestAAA(unittest.TestCase):
    def test_order_total(self):
        # Arrange
        service = OrderService()
        price = 25.0
        quantity = 4

        # Act
        result = service.calculate_total(
            price,
            quantity,
        )

        # Assert
        self.assertEqual(
            result,
            100.0,
        )


# ============================================================
# 30. Unit Tests vs Integration Tests
# ============================================================

"""
Unit Test:

    Function
       |
       v
    Test

Usually isolates one small unit of behavior.

Integration Test:

    API
      |
      v
    Service
      |
      v
    Database

Integration tests verify that multiple components
work together correctly.

Both are important in backend development.
"""


# ============================================================
# 31. Testing Best Practices
# ============================================================

"""
Best practices:

1. Test behavior, not implementation details.
2. Keep tests independent.
3. Use descriptive test names.
4. Test both normal and invalid inputs.
5. Include edge cases.
6. Keep tests fast.
7. Avoid unnecessary shared state.
8. Use setUp when common preparation is needed.
9. Use assertRaises for expected exceptions.
10. Run tests regularly during development.
11. Keep production code and tests organized separately.
12. Prefer readable tests over clever tests.
"""


# ============================================================
# 32. Main Entry Point
# ============================================================

if __name__ == "__main__":
    unittest.main()