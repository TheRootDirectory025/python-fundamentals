"""
Practical Python Decorators

This file demonstrates practical decorator patterns commonly used
in backend and software development.
"""

from functools import wraps
import logging
import time
import warnings
from datetime import datetime, timedelta


# ============================================================
# 1. Basic Logging Decorator
# ============================================================

def log_call(func):
    """Log function calls and their arguments."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        print(f"Arguments: args={args}, kwargs={kwargs}")

        result = func(*args, **kwargs)

        print(f"Finished {func.__name__}")
        return result

    return wrapper


@log_call
def add(a, b):
    return a + b


print(add(10, 20))


# ============================================================
# 2. Execution Time Decorator
# ============================================================

def measure_time(func):
    """Measure how long a function takes to execute."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()

        result = func(*args, **kwargs)

        end_time = time.perf_counter()
        elapsed_time = end_time - start_time

        print(
            f"{func.__name__} took "
            f"{elapsed_time:.4f} seconds"
        )

        return result

    return wrapper


@measure_time
def process_data():
    time.sleep(0.1)
    return "Data processed"


print(process_data())


# ============================================================
# 3. Authentication Decorator
# ============================================================

def require_login(func):
    """Allow execution only for authenticated users."""

    @wraps(func)
    def wrapper(user, *args, **kwargs):
        if not user.get("is_authenticated"):
            raise PermissionError("Authentication required.")

        return func(user, *args, **kwargs)

    return wrapper


@require_login
def get_profile(user):
    return f"Profile of {user['username']}"


authenticated_user = {
    "username": "mohsen",
    "is_authenticated": True,
}

print(get_profile(authenticated_user))


# ============================================================
# 4. Permission Decorator
# ============================================================

def require_permission(permission):
    """Require a specific permission."""

    def decorator(func):
        @wraps(func)
        def wrapper(user, *args, **kwargs):
            permissions = user.get("permissions", [])

            if permission not in permissions:
                raise PermissionError(
                    f"Missing permission: {permission}"
                )

            return func(user, *args, **kwargs)

        return wrapper

    return decorator


@require_permission("delete_users")
def delete_user(user, username):
    return f"User {username} deleted."


admin_user = {
    "username": "admin",
    "permissions": ["read_users", "delete_users"],
}

print(delete_user(admin_user, "john"))


# ============================================================
# 5. Role-Based Authorization
# ============================================================

def require_role(*allowed_roles):
    """Allow execution only for users with specific roles."""

    def decorator(func):
        @wraps(func)
        def wrapper(user, *args, **kwargs):
            if user.get("role") not in allowed_roles:
                raise PermissionError(
                    "You do not have permission to perform this action."
                )

            return func(user, *args, **kwargs)

        return wrapper

    return decorator


@require_role("admin", "manager")
def generate_report(user):
    return "Report generated."


manager = {
    "username": "manager01",
    "role": "manager",
}

print(generate_report(manager))


# ============================================================
# 6. Input Validation Decorator
# ============================================================

def validate_positive(func):
    """Validate that numeric arguments are positive."""

    @wraps(func)
    def wrapper(value, *args, **kwargs):
        if value <= 0:
            raise ValueError("Value must be positive.")

        return func(value, *args, **kwargs)

    return wrapper


@validate_positive
def calculate_square(value):
    return value ** 2


print(calculate_square(5))


# ============================================================
# 7. Retry Decorator
# ============================================================

def retry(max_attempts=3, delay=1):
    """Retry a function when an exception occurs."""

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_error = None

            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)

                except Exception as error:
                    last_error = error

                    print(
                        f"Attempt {attempt} failed: {error}"
                    )

                    if attempt < max_attempts:
                        time.sleep(delay)

            raise last_error

        return wrapper

    return decorator


attempt_counter = 0


@retry(max_attempts=3, delay=0.2)
def unstable_operation():
    global attempt_counter

    attempt_counter += 1

    if attempt_counter < 3:
        raise ConnectionError("Temporary connection failure.")

    return "Operation successful."


print(unstable_operation())


# ============================================================
# 8. Caching Decorator
# ============================================================

def simple_cache(func):
    """Cache function results based on arguments."""

    cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        key = (
            args,
            tuple(sorted(kwargs.items())),
        )

        if key in cache:
            print("Returning cached result.")
            return cache[key]

        result = func(*args, **kwargs)
        cache[key] = result

        print("Result stored in cache.")
        return result

    return wrapper


@simple_cache
def expensive_calculation(number):
    print("Calculating...")
    time.sleep(0.5)

    return number * number


print(expensive_calculation(10))
print(expensive_calculation(10))


# ============================================================
# 9. TTL Cache
# ============================================================

def ttl_cache(seconds):
    """Cache results for a limited amount of time."""

    def decorator(func):
        cache = {}

        @wraps(func)
        def wrapper(*args, **kwargs):
            key = (
                args,
                tuple(sorted(kwargs.items())),
            )

            now = time.time()

            if key in cache:
                result, timestamp = cache[key]

                if now - timestamp < seconds:
                    print("Returning valid cached result.")
                    return result

            result = func(*args, **kwargs)

            cache[key] = (result, now)

            return result

        return wrapper

    return decorator


@ttl_cache(seconds=5)
def get_exchange_rate():
    print("Fetching exchange rate...")
    return 1.08


print(get_exchange_rate())
print(get_exchange_rate())


# ============================================================
# 10. Rate Limiting
# ============================================================

def rate_limit(max_calls, period):
    """Limit how many times a function can be called."""

    def decorator(func):
        calls = []

        @wraps(func)
        def wrapper(*args, **kwargs):
            current_time = time.time()

            calls[:] = [
                timestamp
                for timestamp in calls
                if current_time - timestamp < period
            ]

            if len(calls) >= max_calls:
                raise RuntimeError(
                    "Rate limit exceeded."
                )

            calls.append(current_time)

            return func(*args, **kwargs)

        return wrapper

    return decorator


@rate_limit(max_calls=3, period=10)
def send_request():
    return "Request accepted."


print(send_request())
print(send_request())


# ============================================================
# 11. Exception Logging Decorator
# ============================================================

def log_exceptions(func):
    """Log exceptions raised by a function."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)

        except Exception as error:
            print(
                f"Error in {func.__name__}: {error}"
            )
            raise

    return wrapper


@log_exceptions
def divide(a, b):
    return a / b


try:
    divide(10, 0)
except ZeroDivisionError:
    print("Division failed.")


# ============================================================
# 12. Audit Logging
# ============================================================

def audit_log(func):
    """Record when an important action is performed."""

    @wraps(func)
    def wrapper(user, *args, **kwargs):
        timestamp = datetime.now()

        print(
            f"[AUDIT] "
            f"{timestamp} | "
            f"user={user['username']} | "
            f"action={func.__name__}"
        )

        return func(user, *args, **kwargs)

    return wrapper


@audit_log
def update_account(user, email):
    return f"Account updated for {email}"


user = {
    "username": "mohsen",
}

print(update_account(user, "mohsen@example.com"))


# ============================================================
# 13. Deprecation Decorator
# ============================================================

def deprecated(message):
    """Mark a function as deprecated."""

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            warnings.warn(
                f"{func.__name__} is deprecated. {message}",
                DeprecationWarning,
                stacklevel=2,
            )

            return func(*args, **kwargs)

        return wrapper

    return decorator


@deprecated(
    "Use calculate_total_v2 instead."
)
def calculate_total(items):
    return sum(items)


print(calculate_total([10, 20, 30]))


# ============================================================
# 14. Result Transformation
# ============================================================

def convert_to_dict(func):
    """Convert an object's result to a dictionary."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        if hasattr(result, "to_dict"):
            return result.to_dict()

        return result

    return wrapper


class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def to_dict(self):
        return {
            "id": self.product_id,
            "name": self.name,
            "price": self.price,
        }


@convert_to_dict
def get_product():
    return Product(
        product_id=1,
        name="Keyboard",
        price=50,
    )


print(get_product())


# ============================================================
# 15. Decorator Stacking
# ============================================================

def uppercase_result(func):
    """Convert string results to uppercase."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        if isinstance(result, str):
            return result.upper()

        return result

    return wrapper


@log_call
@uppercase_result
def get_message():
    return "hello backend"


print(get_message())


# ============================================================
# 16. Decorator Execution Order
# ============================================================

def first(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("First: before")
        result = func(*args, **kwargs)
        print("First: after")
        return result

    return wrapper


def second(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Second: before")
        result = func(*args, **kwargs)
        print("Second: after")
        return result

    return wrapper


@first
@second
def show_message():
    print("Function body")


show_message()


# ============================================================
# 17. Combining Authentication and Permission
# ============================================================

@require_login
@require_permission("create_posts")
def create_post(user, title):
    return f"Post '{title}' created."


author = {
    "username": "author01",
    "is_authenticated": True,
    "permissions": ["create_posts"],
}

print(create_post(author, "Python Decorators"))


# ============================================================
# 18. Backend Service Example
# ============================================================

def service_operation(func):
    """Combine logging and exception handling for a service."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        print(
            f"[SERVICE] Starting {func.__name__}"
        )

        try:
            result = func(*args, **kwargs)

            print(
                f"[SERVICE] "
                f"{func.__name__} completed successfully"
            )

            return result

        except Exception as error:
            print(
                f"[SERVICE] "
                f"{func.__name__} failed: {error}"
            )
            raise

    return wrapper


@service_operation
def create_order(user_id, product_id):
    if product_id <= 0:
        raise ValueError("Invalid product ID.")

    return {
        "user_id": user_id,
        "product_id": product_id,
        "status": "created",
    }


print(create_order(101, 500))


# ============================================================
# 19. Decorator for API-like Functions
# ============================================================

def api_endpoint(func):
    """Provide a simple API-like response structure."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            data = func(*args, **kwargs)

            return {
                "success": True,
                "data": data,
                "error": None,
            }

        except Exception as error:
            return {
                "success": False,
                "data": None,
                "error": str(error),
            }

    return wrapper


@api_endpoint
def get_user(user_id):
    if user_id <= 0:
        raise ValueError("Invalid user ID.")

    return {
        "id": user_id,
        "username": "mohsen",
    }


print(get_user(10))
print(get_user(-1))


# ============================================================
# 20. Decorator with Metadata
# ============================================================

def endpoint(method, path):
    """Attach endpoint metadata to a function."""

    def decorator(func):
        func.http_method = method
        func.http_path = path

        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        return wrapper

    return decorator


@endpoint("GET", "/users")
def list_users():
    return ["mohsen", "ali", "sara"]


print(list_users())
print(list_users.http_method)
print(list_users.http_path)


# ============================================================
# 21. Practical Logging with logging Module
# ============================================================

logger = logging.getLogger(__name__)


def production_logging(func):
    """Use Python logging for production-style messages."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(
            "Calling function: %s",
            func.__name__,
        )

        try:
            result = func(*args, **kwargs)

            logger.info(
                "Function completed: %s",
                func.__name__,
            )

            return result

        except Exception:
            logger.exception(
                "Function failed: %s",
                func.__name__,
            )
            raise

    return wrapper


@production_logging
def fetch_data():
    return {"status": "ok"}


print(fetch_data())


# ============================================================
# 22. Why functools.wraps Matters
# ============================================================

def without_wraps(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper


def with_wraps(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper


@without_wraps
def function_without_wraps():
    """Original documentation."""

    return "without wraps"


@with_wraps
def function_with_wraps():
    """Original documentation."""

    return "with wraps"


print(function_without_wraps.__name__)
print(function_with_wraps.__name__)

print(function_without_wraps.__doc__)
print(function_with_wraps.__doc__)


# ============================================================
# 23. Decorators in Django
# ============================================================

"""
Django provides several decorators that follow the same concept.

Examples include:

from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    ...

The decorator checks whether the user is authenticated
before allowing the view to execute.

Other Django decorators include patterns for:

- HTTP method restrictions
- CSRF protection
- caching
- permissions
- authentication
"""

# The examples above are framework-independent so that
# this repository does not require Django as a dependency.


# ============================================================
# 24. Common Backend Use Cases
# ============================================================

"""
Decorators are commonly useful for:

- Authentication
- Authorization
- Logging
- Audit logging
- Performance measurement
- Caching
- Retry logic
- Rate limiting
- Validation
- Error handling
- Deprecation warnings
- API response formatting
- Permission checks
- Transaction boundaries

In real backend projects, many of these concerns are also
handled by framework features, middleware, libraries, or
infrastructure.

The goal here is to understand the underlying Python mechanism.
"""


# ============================================================
# 25. Decorator Best Practices
# ============================================================

"""
Best practices:

1. Use functools.wraps.
2. Keep decorators focused on one responsibility.
3. Preserve function arguments with *args and **kwargs.
4. Preserve the original return value unless transformation
   is intentional.
5. Avoid hiding important control flow.
6. Give decorators clear names.
7. Use configurable decorators when behavior must be customized.
8. Be careful with decorator order.
9. Avoid storing mutable global state unnecessarily.
10. Prefer framework-supported solutions in production when
    they already solve the problem.
"""


# ============================================================
# End of File
# ============================================================