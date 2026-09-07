"""
Python Fundamentals
08 - Error Handling
Topic: Custom Exceptions

This file covers:
- Why custom exceptions are useful
- Creating custom exception classes
- Raising custom exceptions
- Catching custom exceptions
- Custom exception messages
- Custom exception attributes
- Multiple custom exceptions
- Exception inheritance and hierarchy
- Practical examples for banking, users, products, orders, and authentication
"""

# ============================================================
# 1. Why Custom Exceptions?
# ============================================================

"""
Python already provides many built-in exceptions such as:
- ValueError
- TypeError
- ZeroDivisionError
- FileNotFoundError

However, in real applications we sometimes need errors that
describe our own business rules.

For example:
- A bank account does not have enough balance.
- A username already exists.
- A product is out of stock.
- A user entered an invalid age.

Custom exceptions make these errors easier to understand,
handle, and maintain.
"""


# ============================================================
# 2. Basic Custom Exception
# ============================================================

class InsufficientBalanceError(Exception):
    """Raised when an account does not have enough balance."""

    pass


try:
    balance = 100
    withdrawal = 150

    if withdrawal > balance:
        raise InsufficientBalanceError

    balance -= withdrawal

except InsufficientBalanceError:
    print("Error: Insufficient balance.")


# ============================================================
# 3. Custom Exception with a Message
# ============================================================

class InvalidAgeError(Exception):
    """Raised when a user's age is invalid."""

    pass


try:
    age = 12

    if age < 18:
        raise InvalidAgeError("User must be at least 18 years old.")

except InvalidAgeError as error:
    print(f"Error: {error}")


# ============================================================
# 4. Creating a Custom Exception with Attributes
# ============================================================

class InsufficientFundsError(Exception):
    """Raised when a withdrawal exceeds the available balance."""

    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount

        message = (
            f"Insufficient funds: balance={balance}, "
            f"requested={amount}"
        )

        super().__init__(message)


try:
    balance = 500
    withdrawal = 800

    if withdrawal > balance:
        raise InsufficientFundsError(balance, withdrawal)

except InsufficientFundsError as error:
    print(error)
    print(f"Available balance: {error.balance}")
    print(f"Requested amount: {error.amount}")


# ============================================================
# 5. Custom Exception with __str__
# ============================================================

class InvalidAmountError(Exception):
    """Raised when a transaction amount is invalid."""

    def __init__(self, amount):
        self.amount = amount

    def __str__(self):
        return f"Invalid transaction amount: {self.amount}"


try:
    amount = -50

    if amount <= 0:
        raise InvalidAmountError(amount)

except InvalidAmountError as error:
    print(error)


# ============================================================
# 6. Multiple Custom Exceptions
# ============================================================

class UsernameAlreadyExistsError(Exception):
    """Raised when a username is already registered."""

    pass


class InvalidAgeError(Exception):
    """Raised when the user's age is invalid."""

    pass


registered_users = ["ali", "sara", "mohsen"]

try:
    username = "ali"
    age = 20

    if username in registered_users:
        raise UsernameAlreadyExistsError(
            "This username is already registered."
        )

    if age < 18:
        raise InvalidAgeError(
            "User must be at least 18 years old."
        )

except UsernameAlreadyExistsError as error:
    print(f"Registration error: {error}")

except InvalidAgeError as error:
    print(f"Registration error: {error}")


# ============================================================
# 7. Exception Hierarchy
# ============================================================

"""
Custom exceptions can also have their own hierarchy.

Example:

Exception
    |
    ApplicationError
       |
       +-- AuthenticationError
       |
       +-- ValidationError
       |
       +-- PaymentError

This allows us to catch either a specific error or a group
of related errors.
"""


class ApplicationError(Exception):
    """Base exception for application-specific errors."""

    pass


class AuthenticationError(ApplicationError):
    """Base exception for authentication-related errors."""

    pass


class InvalidCredentialsError(AuthenticationError):
    """Raised when login credentials are incorrect."""

    pass


class AccountLockedError(AuthenticationError):
    """Raised when an account is locked."""

    pass


try:
    raise InvalidCredentialsError("Invalid username or password.")

except InvalidCredentialsError as error:
    print(f"Specific error: {error}")

except AuthenticationError as error:
    print(f"Authentication error: {error}")


# ============================================================
# 8. Catching a Parent Custom Exception
# ============================================================

try:
    raise AccountLockedError("Your account has been locked.")

except AuthenticationError as error:
    print(f"Authentication error: {error}")


# ============================================================
# 9. Bank Account Example
# ============================================================

class BankError(Exception):
    """Base exception for bank-related errors."""

    pass


class InvalidAmountError(BankError):
    """Raised when the transaction amount is invalid."""

    pass


class InsufficientBalanceError(BankError):
    """Raised when the account has insufficient balance."""

    pass


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise InvalidAmountError(
                "Deposit amount must be greater than zero."
            )

        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise InvalidAmountError(
                "Withdrawal amount must be greater than zero."
            )

        if amount > self.balance:
            raise InsufficientBalanceError(
                "Not enough balance for this withdrawal."
            )

        self.balance -= amount


account = BankAccount("Mohsen", 1000)

try:
    account.deposit(500)
    account.withdraw(200)

    print(f"Current balance: {account.balance}")

except InvalidAmountError as error:
    print(f"Transaction error: {error}")

except InsufficientBalanceError as error:
    print(f"Transaction error: {error}")


# ============================================================
# 10. User Registration Example
# ============================================================

class RegistrationError(Exception):
    """Base exception for registration errors."""

    pass


class UsernameAlreadyExistsError(RegistrationError):
    """Raised when a username already exists."""

    pass


class InvalidAgeError(RegistrationError):
    """Raised when the user's age is invalid."""

    pass


users = {
    "ali": 22,
    "sara": 25,
}


def register_user(username, age):
    if username in users:
        raise UsernameAlreadyExistsError(
            f"Username '{username}' already exists."
        )

    if age < 18:
        raise InvalidAgeError(
            "User must be at least 18 years old."
        )

    users[username] = age

    return "User registered successfully."


try:
    result = register_user("mohsen", 23)
    print(result)

except RegistrationError as error:
    print(f"Registration failed: {error}")


# ============================================================
# 11. Product and Order Example
# ============================================================

class OrderError(Exception):
    """Base exception for order-related errors."""

    pass


class OutOfStockError(OrderError):
    """Raised when a product is out of stock."""

    pass


class InvalidQuantityError(OrderError):
    """Raised when the requested quantity is invalid."""

    pass


products = {
    "laptop": {
        "price": 1000,
        "stock": 3,
    },
    "mouse": {
        "price": 30,
        "stock": 10,
    },
}


def create_order(product_name, quantity):
    if quantity <= 0:
        raise InvalidQuantityError(
            "Quantity must be greater than zero."
        )

    if product_name not in products:
        raise OrderError(
            f"Product '{product_name}' does not exist."
        )

    product = products[product_name]

    if quantity > product["stock"]:
        raise OutOfStockError(
            f"Only {product['stock']} units are available."
        )

    total_price = product["price"] * quantity
    product["stock"] -= quantity

    return total_price


try:
    total = create_order("laptop", 2)

    print(f"Order created successfully.")
    print(f"Total price: ${total}")

except InvalidQuantityError as error:
    print(f"Order error: {error}")

except OutOfStockError as error:
    print(f"Order error: {error}")

except OrderError as error:
    print(f"Order error: {error}")


# ============================================================
# 12. Authentication Example
# ============================================================

class AuthenticationError(Exception):
    """Base exception for authentication errors."""

    pass


class InvalidCredentialsError(AuthenticationError):
    """Raised when username or password is incorrect."""

    pass


class AccountLockedError(AuthenticationError):
    """Raised when an account is locked."""

    pass


users = {
    "mohsen": {
        "password": "1234",
        "locked": False,
    }
}


def login(username, password):
    if username not in users:
        raise InvalidCredentialsError(
            "Invalid username or password."
        )

    user = users[username]

    if user["locked"]:
        raise AccountLockedError(
            "This account is locked."
        )

    if password != user["password"]:
        raise InvalidCredentialsError(
            "Invalid username or password."
        )

    return "Login successful."


try:
    result = login("mohsen", "1234")
    print(result)

except InvalidCredentialsError as error:
    print(f"Login failed: {error}")

except AccountLockedError as error:
    print(f"Login failed: {error}")

except AuthenticationError as error:
    print(f"Authentication error: {error}")


# ============================================================
# 13. Raising Custom Exceptions from Functions
# ============================================================

class NegativeNumberError(Exception):
    """Raised when a negative number is not allowed."""

    pass


def calculate_square_root(number):
    if number < 0:
        raise NegativeNumberError(
            "Square root cannot be calculated for a negative number."
        )

    return number ** 0.5


try:
    result = calculate_square_root(25)
    print(f"Result: {result}")

except NegativeNumberError as error:
    print(f"Calculation error: {error}")


# ============================================================
# 14. Using a Base Custom Exception
# ============================================================

class PaymentError(Exception):
    """Base exception for payment-related errors."""

    pass


class InvalidCardError(PaymentError):
    """Raised when the card information is invalid."""

    pass


class InsufficientCreditError(PaymentError):
    """Raised when the card has insufficient credit."""

    pass


def process_payment(card_number, amount):
    if len(card_number) != 16:
        raise InvalidCardError("Card number must contain 16 digits.")

    available_credit = 100

    if amount > available_credit:
        raise InsufficientCreditError(
            "Insufficient credit for this payment."
        )

    return "Payment successful."


try:
    result = process_payment("1234567890123456", 50)
    print(result)

except InvalidCardError as error:
    print(f"Payment failed: {error}")

except InsufficientCreditError as error:
    print(f"Payment failed: {error}")

except PaymentError as error:
    print(f"Payment error: {error}")


# ============================================================
# 15. Custom Exceptions with Multiple Attributes
# ============================================================

class OutOfStockError(Exception):
    """Raised when requested quantity exceeds stock."""

    def __init__(self, product_name, requested, available):
        self.product_name = product_name
        self.requested = requested
        self.available = available

        message = (
            f"Product '{product_name}' is out of stock for "
            f"the requested quantity. "
            f"Requested: {requested}, Available: {available}"
        )

        super().__init__(message)


try:
    product_name = "Keyboard"
    requested = 8
    available = 3

    if requested > available:
        raise OutOfStockError(
            product_name,
            requested,
            available,
        )

except OutOfStockError as error:
    print(error)
    print(f"Product: {error.product_name}")
    print(f"Requested: {error.requested}")
    print(f"Available: {error.available}")


# ============================================================
# 16. Best Practices
# ============================================================

"""
Best practices for custom exceptions:

1. Inherit from Exception.
2. Give exceptions clear and descriptive names.
3. Usually end exception names with "Error".
4. Use custom exceptions for business rules.
5. Keep exception classes simple.
6. Use a base exception for related application errors.
7. Catch specific exceptions before general exceptions.
8. Add useful attributes when extra information is needed.
9. Do not use exceptions for normal program flow.
10. Do not create a custom exception when a built-in exception
   already describes the problem well.

Good examples:

- InsufficientBalanceError
- InvalidAmountError
- OutOfStockError
- InvalidCredentialsError
- UsernameAlreadyExistsError

These names immediately tell us what went wrong.
"""