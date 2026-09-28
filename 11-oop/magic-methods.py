"""
Python Fundamentals
11 - Object-Oriented Programming
Topic: Magic Methods / Dunder Methods

This file covers:
- What magic methods are
- __init__
- __str__
- __repr__
- __len__
- __bool__
- __eq__
- __ne__
- __lt__
- __le__
- __gt__
- __ge__
- __add__
- __sub__
- __mul__
- __contains__
- __getitem__
- __setitem__
- __iter__
- __next__
- __call__
"""


# ============================================================
# 1. What Are Magic Methods?
# ============================================================

"""
Magic methods are special methods recognized by Python.

They usually start and end with double underscores:

__method__

For example:

__init__
__str__
__len__
__eq__

They allow our custom objects to work naturally with
Python's built-in syntax and functions.
"""


# ============================================================
# 2. __init__
# ============================================================

class User:

    def __init__(self, name, age):
        self.name = name
        self.age = age


user = User("Mohsen", 24)

print(user.name)
print(user.age)


"""
__init__ runs automatically when an object is created.

User("Mohsen", 24)

causes Python to initialize the object using __init__.
"""


# ============================================================
# 3. __str__
# ============================================================

class User:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"User(name={self.name}, age={self.age})"


user = User("Mohsen", 24)

print(user)


"""
__str__ defines a human-readable representation of an object.

When we use:

print(user)

Python calls:

user.__str__()
"""


# ============================================================
# 4. __repr__
# ============================================================

class User:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return (
            f"User(name={self.name!r}, age={self.age!r})"
        )


user = User("Mohsen", 24)

print(repr(user))


"""
__repr__ is intended to provide an unambiguous representation
of an object, especially for developers and debugging.
"""


# ============================================================
# 5. __str__ vs __repr__
# ============================================================

class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - ${self.price}"

    def __repr__(self):
        return (
            f"Product(name={self.name!r}, "
            f"price={self.price!r})"
        )


product = Product("Keyboard", 50)

print(str(product))
print(repr(product))


"""
A common convention:

__str__
    Human-friendly output.

__repr__
    Developer-friendly representation.
"""


# ============================================================
# 6. __len__
# ============================================================

class Team:

    def __init__(self, members):
        self.members = members

    def __len__(self):
        return len(self.members)


team = Team([
    "Mohsen",
    "Ali",
    "Sara"
])

print(len(team))


"""
len(team)

calls:

team.__len__()
"""


# ============================================================
# 7. __bool__
# ============================================================

class ShoppingCart:

    def __init__(self, items):
        self.items = items

    def __bool__(self):
        return len(self.items) > 0


empty_cart = ShoppingCart([])

cart = ShoppingCart(["Laptop"])


print(bool(empty_cart))
print(bool(cart))


if cart:
    print("Cart contains items.")


"""
__bool__ controls how an object behaves in a boolean context.

Examples:

if object:
    ...

bool(object)
"""


# ============================================================
# 8. __eq__
# ============================================================

class User:

    def __init__(self, username):
        self.username = username

    def __eq__(self, other):
        return self.username == other.username


user1 = User("mohsen")
user2 = User("mohsen")
user3 = User("ali")

print(user1 == user2)
print(user1 == user3)


"""
__eq__ defines the behavior of ==.
"""


# ============================================================
# 9. __ne__
# ============================================================

class Product:

    def __init__(self, product_id):
        self.product_id = product_id

    def __ne__(self, other):
        return self.product_id != other.product_id


product1 = Product(1)
product2 = Product(2)

print(product1 != product2)


"""
__ne__ defines the behavior of !=.
"""


# ============================================================
# 10. Comparison Magic Methods
# ============================================================

class Score:

    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        return self.value < other.value

    def __le__(self, other):
        return self.value <= other.value

    def __gt__(self, other):
        return self.value > other.value

    def __ge__(self, other):
        return self.value >= other.value


score1 = Score(80)
score2 = Score(90)

print(score1 < score2)
print(score1 <= score2)
print(score1 > score2)
print(score1 >= score2)


"""
Comparison methods:

__lt__  -> <
__le__  -> <=
__gt__  -> >
__ge__  -> >=
"""


# ============================================================
# 11. __add__
# ============================================================

class Money:

    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        return Money(
            self.amount + other.amount
        )

    def __str__(self):
        return f"${self.amount}"


money1 = Money(100)
money2 = Money(50)

total = money1 + money2

print(total)


"""
money1 + money2

calls:

money1.__add__(money2)
"""


# ============================================================
# 12. __sub__
# ============================================================

class Money:

    def __init__(self, amount):
        self.amount = amount

    def __sub__(self, other):
        return Money(
            self.amount - other.amount
        )

    def __str__(self):
        return f"${self.amount}"


money1 = Money(100)
money2 = Money(30)

result = money1 - money2

print(result)


"""
__sub__ controls the - operator.
"""


# ============================================================
# 13. __mul__
# ============================================================

class Price:

    def __init__(self, value):
        self.value = value

    def __mul__(self, quantity):
        return self.value * quantity


price = Price(20)

print(price * 3)


"""
__mul__ controls the * operator.
"""


# ============================================================
# 14. __contains__
# ============================================================

class Playlist:

    def __init__(self, songs):
        self.songs = songs

    def __contains__(self, song):
        return song in self.songs


playlist = Playlist([
    "Song A",
    "Song B",
    "Song C"
])

print("Song A" in playlist)
print("Song X" in playlist)


"""
The expression:

"Song A" in playlist

calls:

playlist.__contains__("Song A")
"""


# ============================================================
# 15. __getitem__
# ============================================================

class ShoppingCart:

    def __init__(self, items):
        self.items = items

    def __getitem__(self, index):
        return self.items[index]


cart = ShoppingCart([
    "Laptop",
    "Mouse",
    "Keyboard"
])

print(cart[0])
print(cart[1])


"""
cart[0]

calls:

cart.__getitem__(0)
"""


# ============================================================
# 16. __setitem__
# ============================================================

class ShoppingCart:

    def __init__(self, items):
        self.items = items

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, value):
        self.items[index] = value


cart = ShoppingCart([
    "Laptop",
    "Mouse"
])

cart[1] = "Keyboard"

print(cart[1])


"""
cart[1] = "Keyboard"

calls:

cart.__setitem__(1, "Keyboard")
"""


# ============================================================
# 17. __iter__
# ============================================================

class Team:

    def __init__(self, members):
        self.members = members

    def __iter__(self):
        return iter(self.members)


team = Team([
    "Mohsen",
    "Ali",
    "Sara"
])

for member in team:
    print(member)


"""
__iter__ allows our object to work with:

for item in object:
"""


# ============================================================
# 18. __next__
# ============================================================

class Counter:

    def __init__(self, maximum):
        self.current = 0
        self.maximum = maximum

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.maximum:
            raise StopIteration

        self.current += 1

        return self.current


counter = Counter(3)

for number in counter:
    print(number)


"""
An iterator normally provides:

__iter__()
__next__()

When there are no more values,
__next__ raises StopIteration.
"""


# ============================================================
# 19. __call__
# ============================================================

class Greeter:

    def __init__(self, name):
        self.name = name

    def __call__(self):
        print(f"Hello, {self.name}!")


greeter = Greeter("Mohsen")

greeter()


"""
An object with __call__ can be called like a function.

greeter()

is equivalent to calling:

greeter.__call__()
"""


# ============================================================
# 20. __call__ with Arguments
# ============================================================

class Calculator:

    def __call__(self, a, b):
        return a + b


calculator = Calculator()

print(calculator(10, 20))


"""
Objects can behave similarly to functions.
"""


# ============================================================
# 21. __enter__ and __exit__
# ============================================================

class DemoContext:

    def __enter__(self):
        print("Entering context.")
        return self

    def __exit__(
        self,
        exc_type,
        exc_value,
        traceback
    ):
        print("Leaving context.")


with DemoContext():
    print("Inside context.")


"""
These methods allow an object to work with:

with object:
    ...

This is called the context manager protocol.
"""


# ============================================================
# 22. Practical Example: Database Connection
# ============================================================

class DatabaseConnection:

    def __enter__(self):
        print("Database connected.")
        return self

    def __exit__(
        self,
        exc_type,
        exc_value,
        traceback
    ):
        print("Database connection closed.")

    def execute(self, query):
        print(f"Executing: {query}")


with DatabaseConnection() as database:
    database.execute(
        "SELECT * FROM users"
    )


"""
The context manager can automatically handle setup
and cleanup operations.
"""


# ============================================================
# 23. __hash__
# ============================================================

class User:

    def __init__(self, user_id):
        self.user_id = user_id

    def __hash__(self):
        return hash(self.user_id)


user = User(100)

print(hash(user))


"""
__hash__ defines the hash value of an object.

Hashable objects can be used in certain collections
such as sets and as dictionary keys.

Be careful when implementing __hash__ together with
__eq__.
"""


# ============================================================
# 24. __format__
# ============================================================

class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __format__(self, format_spec):
        return (
            f"{self.name}: "
            f"${self.price:{format_spec}}"
        )


product = Product("Laptop", 1500)

print(f"{product:.2f}")


"""
__format__ controls how an object behaves when used
with format() or formatted string syntax.
"""


# ============================================================
# 25. __dict__
# ============================================================

class User:

    def __init__(self, name, age):
        self.name = name
        self.age = age


user = User("Mohsen", 24)

print(user.__dict__)


"""
Many normal Python objects expose their instance attributes
through __dict__.

It is useful for inspection and debugging.
"""


# ============================================================
# 26. Magic Methods Work Behind Normal Python Syntax
# ============================================================

class Number:

    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Number(
            self.value + other.value
        )

    def __str__(self):
        return str(self.value)


a = Number(10)
b = Number(20)

c = a + b

print(c)


"""
This:

c = a + b

is conceptually handled through:

c = a.__add__(b)

And:

print(c)

uses:

c.__str__()
"""


# ============================================================
# 27. Combining Multiple Magic Methods
# ============================================================

class Cart:

    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)

    def __getitem__(self, index):
        return self.items[index]

    def __contains__(self, item):
        return item in self.items

    def __str__(self):
        return f"Cart({self.items})"


cart = Cart([
    "Laptop",
    "Mouse",
    "Keyboard"
])

print(cart)
print(len(cart))
print(cart[0])
print("Mouse" in cart)


"""
By implementing several magic methods,
our custom object behaves naturally like a built-in collection.
"""


# ============================================================
# 28. Practical Example: Product Comparison
# ============================================================

class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __lt__(self, other):
        return self.price < other.price

    def __eq__(self, other):
        return self.price == other.price


product1 = Product("Mouse", 30)
product2 = Product("Keyboard", 80)

print(product1 < product2)
print(product1 == product2)


# ============================================================
# 29. Important Magic Methods
# ============================================================

"""
Some important dunder methods:

Object lifecycle:
    __init__

String representation:
    __str__
    __repr__

Size and truth:
    __len__
    __bool__

Comparison:
    __eq__
    __ne__
    __lt__
    __le__
    __gt__
    __ge__

Arithmetic:
    __add__
    __sub__
    __mul__
    __truediv__

Collections:
    __contains__
    __getitem__
    __setitem__

Iteration:
    __iter__
    __next__

Callable objects:
    __call__

Context managers:
    __enter__
    __exit__

Hashing:
    __hash__
"""


# ============================================================
# 30. Best Practices
# ============================================================

"""
Best practices:

1. Only implement magic methods when they make the object
   behave naturally.

2. Keep the behavior intuitive.

3. Make sure return types match what Python expects.

4. Use __str__ for readable output.

5. Use __repr__ for useful developer-oriented representation.

6. Be careful when implementing __eq__ and __hash__ together.

7. Don't implement every magic method just because it exists.

8. Follow Python's data model conventions.

9. Keep custom behavior predictable.

10. Prefer readable code over clever code.
"""


# ============================================================
# 31. Summary
# ============================================================

"""
Magic methods are special methods that allow custom classes
to integrate with Python's syntax and built-in operations.

Examples:

print(object)
    -> __str__

len(object)
    -> __len__

object1 == object2
    -> __eq__

object1 + object2
    -> __add__

item in object
    -> __contains__

object[index]
    -> __getitem__

for item in object
    -> __iter__

object()
    -> __call__

with object:
    -> __enter__ / __exit__

The main idea:

Magic methods let our classes behave like natural
Python objects instead of simple containers of data.
"""