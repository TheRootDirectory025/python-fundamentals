"""
Advanced Python Type Hints

This file covers advanced typing features commonly used
in larger Python projects and backend applications.

Type hints improve readability, IDE support, static analysis,
and maintainability. They are not runtime validation by default.
"""

from collections.abc import Callable, Iterable, Sequence
from typing import (
    Any,
    ClassVar,
    Final,
    Generic,
    NewType,
    Protocol,
    TypeAlias,
    TypeVar,
    ParamSpec,
    Self,
    TypedDict,
    cast,
    overload,
)


# ============================================================
# 1. TypeVar
# ============================================================

T = TypeVar("T")


def identity(value: T) -> T:
    """Return the same value while preserving its type."""
    return value


number = identity(100)
message = identity("Hello")

print(number)
print(message)


# ============================================================
# 2. TypeVar with Collections
# ============================================================

T = TypeVar("T")


def first_item(items: Sequence[T]) -> T:
    """Return the first item from a sequence."""
    if not items:
        raise ValueError("Sequence cannot be empty.")

    return items[0]


print(first_item([10, 20, 30]))
print(first_item(["Python", "Django"]))


# ============================================================
# 3. Constrained TypeVar
# ============================================================

Number = TypeVar("Number", int, float)


def double(value: Number) -> Number:
    """Double an integer or floating-point value."""
    return value * 2


print(double(10))
print(double(5.5))


# ============================================================
# 4. Bound TypeVar
# ============================================================

class BaseUser:
    def __init__(self, username: str):
        self.username = username


UserType = TypeVar("UserType", bound=BaseUser)


def get_username(user: UserType) -> str:
    """Work with BaseUser or any subclass."""
    return user.username


class AdminUser(BaseUser):
    pass


class CustomerUser(BaseUser):
    pass


admin = AdminUser("admin")
customer = CustomerUser("customer")

print(get_username(admin))
print(get_username(customer))


# ============================================================
# 5. Generic Classes
# ============================================================

T = TypeVar("T")


class Box(Generic[T]):
    """A generic container."""

    def __init__(self, value: T):
        self.value = value

    def get(self) -> T:
        return self.value


integer_box = Box(100)
string_box = Box("Python")

print(integer_box.get())
print(string_box.get())


# ============================================================
# 6. Generic Repository
# ============================================================

T = TypeVar("T")


class Repository(Generic[T]):
    """Simple in-memory generic repository."""

    def __init__(self):
        self.items: list[T] = []

    def add(self, item: T) -> None:
        self.items.append(item)

    def get_all(self) -> list[T]:
        return self.items.copy()

    def count(self) -> int:
        return len(self.items)


user_repository = Repository[BaseUser]()

user_repository.add(
    BaseUser("mohsen")
)

user_repository.add(
    AdminUser("admin")
)

print(user_repository.get_all())
print(user_repository.count())


# ============================================================
# 7. Generic API Response
# ============================================================

T = TypeVar("T")


class Response(Generic[T]):
    """Generic response container."""

    def __init__(
        self,
        data: T,
        status_code: int = 200,
    ):
        self.data = data
        self.status_code = status_code

    def is_success(self) -> bool:
        return 200 <= self.status_code < 300


user_response = Response(
    data={"id": 1, "username": "mohsen"}
)

product_response = Response(
    data=["Keyboard", "Mouse"]
)

print(user_response.data)
print(product_response.data)


# ============================================================
# 8. TypedDict with Optional Fields
# ============================================================

class UserData(TypedDict):
    id: int
    username: str
    email: str


class UpdateUserData(TypedDict, total=False):
    username: str
    email: str
    is_active: bool


user_update: UpdateUserData = {
    "email": "new@example.com",
    "is_active": True,
}

print(user_update)


# ============================================================
# 9. TypeAlias
# ============================================================

UserId: TypeAlias = int
ProductId: TypeAlias = int
Price: TypeAlias = float


def get_product(product_id: ProductId) -> dict[str, Any]:
    return {
        "id": product_id,
        "name": "Keyboard",
        "price": 49.99,
    }


product = get_product(10)

print(product)


# ============================================================
# 10. NewType
# ============================================================

UserId = NewType("UserId", int)
OrderId = NewType("OrderId", int)


def get_user(user_id: UserId) -> str:
    return f"User {user_id}"


def get_order(order_id: OrderId) -> str:
    return f"Order {order_id}"


user_id = UserId(100)
order_id = OrderId(500)

print(get_user(user_id))
print(get_order(order_id))


# ============================================================
# 11. Final
# ============================================================

MAX_CONNECTIONS: Final = 100
APPLICATION_NAME: Final[str] = "Backend API"


print(MAX_CONNECTIONS)
print(APPLICATION_NAME)

# A static type checker should report reassignment.
# MAX_CONNECTIONS = 200


# ============================================================
# 12. ClassVar
# ============================================================

class User:
    user_count: ClassVar[int] = 0

    def __init__(self, username: str):
        self.username = username
        User.user_count += 1


user1 = User("mohsen")
user2 = User("sara")

print(User.user_count)


# ============================================================
# 13. Self Type
# ============================================================

class QueryBuilder:
    def __init__(self):
        self.conditions: list[str] = []

    def where(self, condition: str) -> Self:
        self.conditions.append(condition)
        return self

    def order_by(self, field: str) -> Self:
        self.conditions.append(
            f"ORDER BY {field}"
        )
        return self

    def build(self) -> str:
        return " ".join(self.conditions)


query = (
    QueryBuilder()
    .where("age > 18")
    .where("is_active = true")
    .order_by("created_at")
    .build()
)

print(query)


# ============================================================
# 14. Protocol
# ============================================================

class Serializable(Protocol):
    def to_dict(self) -> dict[str, Any]:
        ...


class Product:
    def __init__(
        self,
        product_id: int,
        name: str,
    ):
        self.product_id = product_id
        self.name = name

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": self.product_id,
            "name": self.name,
        }


class UserProfile:
    def __init__(
        self,
        user_id: int,
        username: str,
    ):
        self.user_id = user_id
        self.username = username

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": self.user_id,
            "username": self.username,
        }


def serialize(item: Serializable) -> dict[str, Any]:
    return item.to_dict()


product = Product(1, "Keyboard")
profile = UserProfile(10, "mohsen")

print(serialize(product))
print(serialize(profile))


# ============================================================
# 15. Protocol and Duck Typing
# ============================================================

class FileStorage:
    def save(self, data: str) -> None:
        print(f"Saving to file: {data}")


class DatabaseStorage:
    def save(self, data: str) -> None:
        print(f"Saving to database: {data}")


class Storage(Protocol):
    def save(self, data: str) -> None:
        ...


def save_data(
    storage: Storage,
    data: str,
) -> None:
    storage.save(data)


file_storage = FileStorage()
database_storage = DatabaseStorage()

save_data(file_storage, "Hello")
save_data(database_storage, "Hello")


# ============================================================
# 16. Protocol vs Inheritance
# ============================================================

"""
Inheritance requires an explicit relationship.

Protocol uses structural typing.

If an object provides the required methods,
it can satisfy the protocol without inheriting from it.

This is especially useful for:

- Services
- Repositories
- Storage systems
- Payment providers
- Notification systems
- External APIs
"""


# ============================================================
# 17. Callable with TypeVar
# ============================================================

T = TypeVar("T")


def transform(
    value: T,
    function: Callable[[T], T],
) -> T:
    return function(value)


def double_number(value: int) -> int:
    return value * 2


print(transform(10, double_number))


# ============================================================
# 18. ParamSpec
# ============================================================

P = ParamSpec("P")
T = TypeVar("T")


def logged(
    func: Callable[P, T],
) -> Callable[P, T]:
    """Decorator that preserves the function signature."""

    def wrapper(
        *args: P.args,
        **kwargs: P.kwargs,
    ) -> T:
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)

    return wrapper


@logged
def create_user(
    username: str,
    age: int,
) -> dict[str, Any]:
    return {
        "username": username,
        "age": age,
    }


print(create_user("mohsen", 24))


# ============================================================
# 19. ParamSpec and Decorators
# ============================================================

P = ParamSpec("P")
T = TypeVar("T")


def timing(
    func: Callable[P, T],
) -> Callable[P, T]:
    """
    Type-safe decorator signature.

    ParamSpec preserves the parameters of the original function.
    """

    import time

    def wrapper(
        *args: P.args,
        **kwargs: P.kwargs,
    ) -> T:
        start = time.perf_counter()

        result = func(*args, **kwargs)

        elapsed = time.perf_counter() - start

        print(
            f"{func.__name__}: "
            f"{elapsed:.6f}s"
        )

        return result

    return wrapper


@timing
def calculate_total(
    price: float,
    quantity: int,
) -> float:
    return price * quantity


print(calculate_total(19.99, 3))


# ============================================================
# 20. Overload
# ============================================================

@overload
def parse_id(value: int) -> int:
    ...


@overload
def parse_id(value: str) -> int:
    ...


def parse_id(value: int | str) -> int:
    if isinstance(value, int):
        return value

    return int(value)


print(parse_id(100))
print(parse_id("200"))


# ============================================================
# 21. Cast
# ============================================================

def get_value(data: dict[str, Any]) -> str:
    value = data.get("name")

    name = cast(str, value)

    return name


data = {
    "name": "Mohsen",
}

print(get_value(data))


# ============================================================
# 22. Any
# ============================================================

def log_value(value: Any) -> None:
    print(value)


log_value("Python")
log_value(100)
log_value([1, 2, 3])
log_value({"name": "Mohsen"})


"""
Any should be used carefully.

Too much Any removes the benefits of static typing.

Prefer specific types whenever possible.
"""


# ============================================================
# 23. Generic Pagination
# ============================================================

T = TypeVar("T")


class Page(Generic[T]):
    """Generic pagination container."""

    def __init__(
        self,
        items: list[T],
        page: int,
        total_pages: int,
    ):
        self.items = items
        self.page = page
        self.total_pages = total_pages

    def has_next(self) -> bool:
        return self.page < self.total_pages


users_page = Page(
    items=[
        {"id": 1, "username": "mohsen"},
        {"id": 2, "username": "sara"},
    ],
    page=1,
    total_pages=5,
)

print(users_page.items)
print(users_page.has_next())


# ============================================================
# 24. Generic Service
# ============================================================

T = TypeVar("T")


class Service(Generic[T]):
    """Generic service layer example."""

    def __init__(self, repository: Repository[T]):
        self.repository = repository

    def create(self, item: T) -> T:
        self.repository.add(item)
        return item

    def list_all(self) -> list[T]:
        return self.repository.get_all()


user_repo = Repository[BaseUser]()
user_service = Service(user_repo)

created_user = user_service.create(
    BaseUser("mohsen")
)

print(created_user.username)
print(user_service.list_all())


# ============================================================
# 25. Advanced Backend Example
# ============================================================

class PaymentProvider(Protocol):
    def charge(
        self,
        amount: float,
    ) -> bool:
        ...


class StripePayment:
    def charge(self, amount: float) -> bool:
        print(f"Stripe charge: ${amount:.2f}")
        return True


class LocalPayment:
    def charge(self, amount: float) -> bool:
        print(f"Local payment: ${amount:.2f}")
        return True


def process_payment(
    provider: PaymentProvider,
    amount: float,
) -> bool:
    return provider.charge(amount)


stripe = StripePayment()
local = LocalPayment()

print(process_payment(stripe, 100.0))
print(process_payment(local, 200.0))


# ============================================================
# 26. Type Hints for Dependency Injection
# ============================================================

class UserRepositoryProtocol(Protocol):
    def get_by_id(
        self,
        user_id: int,
    ) -> UserData | None:
        ...


class InMemoryUserRepository:
    def __init__(self):
        self.users: dict[int, UserData] = {
            1: {
                "id": 1,
                "username": "mohsen",
                "email": "mohsen@example.com",
            }
        }

    def get_by_id(
        self,
        user_id: int,
    ) -> UserData | None:
        return self.users.get(user_id)


def find_user(
    repository: UserRepositoryProtocol,
    user_id: int,
) -> UserData | None:
    return repository.get_by_id(user_id)


repository = InMemoryUserRepository()

print(find_user(repository, 1))


# ============================================================
# 27. Why Protocol Is Useful in Backend Projects
# ============================================================

"""
Protocols are useful when a service depends on behavior
instead of a concrete implementation.

For example:

    UserService
        |
        v
    UserRepository Protocol
        |
        +---- PostgreSQLRepository
        |
        +---- InMemoryRepository
        |
        +---- MockRepository

The service does not need to know the concrete implementation.

This improves:

- Testing
- Dependency injection
- Loose coupling
- Maintainability
"""


# ============================================================
# 28. Generic Repository Pattern
# ============================================================

T = TypeVar("T")


class GenericRepository(Generic[T]):
    def __init__(self):
        self._items: list[T] = []

    def add(self, item: T) -> None:
        self._items.append(item)

    def get(self, index: int) -> T:
        return self._items[index]

    def all(self) -> list[T]:
        return self._items.copy()


product_repository = GenericRepository[Product]()

product_repository.add(
    Product(1, "Keyboard")
)

product_repository.add(
    Product(2, "Mouse")
)

print(
    product_repository
    .get(0)
    .to_dict()
)

print(
    [
        product.to_dict()
        for product in product_repository.all()
    ]
)


# ============================================================
# 29. Type Hints and Clean Architecture
# ============================================================

"""
Advanced type hints are especially useful in larger projects.

Example architecture:

    API / Views
         |
         v
    Service Layer
         |
         v
    Repository Protocol
         |
         +---- PostgreSQL Repository
         |
         +---- Test Repository

Protocols and generics help keep these layers loosely coupled.
"""


# ============================================================
# 30. Common Mistakes
# ============================================================

"""
Common mistakes:

1. Using Any everywhere.
2. Creating unnecessary complex generic types.
3. Using cast() to hide real type errors.
4. Assuming type hints validate data at runtime.
5. Overusing TypeVar when a simple type is enough.
6. Using Protocol when a normal interface is sufficient.
7. Making annotations harder to understand than the code itself.
8. Ignoring the actual runtime behavior of Python.
9. Using type hints without a static type checker.
10. Sacrificing readability for overly clever typing.
"""


# ============================================================
# 31. Recommended Tools
# ============================================================

"""
Useful static type checking tools:

- mypy
- Pyright
- Pylance

Editors such as VS Code and PyCharm can use type hints
to provide:

- Autocomplete
- Error detection
- Refactoring support
- Navigation
- Documentation
"""


# ============================================================
# 32. Best Practices
# ============================================================

"""
Best practices:

1. Start with simple annotations.
2. Add types to public functions and methods.
3. Use TypeVar for reusable generic logic.
4. Use Generic for reusable typed containers.
5. Use Protocol for behavior-based abstractions.
6. Use TypedDict for structured dictionaries.
7. Use Callable for function parameters.
8. Use ParamSpec for type-safe decorators.
9. Use Any only when necessary.
10. Keep the type system understandable.
"""


# ============================================================
# End of File
# ============================================================