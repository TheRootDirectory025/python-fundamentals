"""
Python Fundamentals
11 - Object-Oriented Programming
Topic: Polymorphism

This file covers:
- What polymorphism means
- Same interface, different behavior
- Method overriding
- Duck typing
- Polymorphism with functions
- Polymorphism with classes
- Built-in polymorphism
- Operator polymorphism
- Practical examples
"""


# ============================================================
# 1. What Is Polymorphism?
# ============================================================

"""
Polymorphism means "many forms".

In programming, it means that different objects can respond
to the same operation or method in different ways.

For example:

Dog.speak()
    -> Woof

Cat.speak()
    -> Meow

Both objects have:

speak()

But they behave differently.
"""


# ============================================================
# 2. Basic Example
# ============================================================

class Dog:

    def speak(self):
        print("Woof!")


class Cat:

    def speak(self):
        print("Meow!")


dog = Dog()
cat = Cat()

dog.speak()
cat.speak()


# ============================================================
# 3. Same Method, Different Behavior
# ============================================================

class Dog:

    def speak(self):
        return "Woof!"


class Cat:

    def speak(self):
        return "Meow!"


animals = [
    Dog(),
    Cat()
]

for animal in animals:
    print(animal.speak())


"""
The loop does not need to know whether the object is
a Dog or Cat.

It only needs to know that the object provides speak().
"""


# ============================================================
# 4. Polymorphism Through Inheritance
# ============================================================

class Animal:

    def speak(self):
        print("Animal sound")


class Dog(Animal):

    def speak(self):
        print("Woof!")


class Cat(Animal):

    def speak(self):
        print("Meow!")


animals = [
    Dog(),
    Cat()
]

for animal in animals:
    animal.speak()


"""
Dog and Cat both inherit from Animal.

Each child class overrides speak().
"""


# ============================================================
# 5. A Common Interface
# ============================================================

class Payment:

    def pay(self, amount):
        raise NotImplementedError


class CreditCardPayment(Payment):

    def pay(self, amount):
        print(
            f"Paid ${amount} using credit card."
        )


class BankPayment(Payment):

    def pay(self, amount):
        print(
            f"Paid ${amount} using bank transfer."
        )


class CashPayment(Payment):

    def pay(self, amount):
        print(
            f"Paid ${amount} with cash."
        )


payments = [
    CreditCardPayment(),
    BankPayment(),
    CashPayment()
]

for payment in payments:
    payment.pay(100)


# ============================================================
# 6. Polymorphism with a Function
# ============================================================

def make_sound(animal):
    animal.speak()


class Dog:

    def speak(self):
        print("Woof!")


class Cat:

    def speak(self):
        print("Meow!")


make_sound(Dog())
make_sound(Cat())


"""
The function does not care about the exact class.

It only expects the object to provide speak().
"""


# ============================================================
# 7. Duck Typing
# ============================================================

"""
Python often follows the idea:

"If it walks like a duck and quacks like a duck,
treat it like a duck."

This is called duck typing.

Python generally cares more about what an object can do
than what its exact class is.
"""


class Dog:

    def speak(self):
        print("Woof!")


class Robot:

    def speak(self):
        print("Beep!")


def make_sound(object_):
    object_.speak()


make_sound(Dog())
make_sound(Robot())


"""
Dog and Robot are unrelated classes.

But both provide speak().

Therefore both can be used by make_sound().
"""


# ============================================================
# 8. Duck Typing Example
# ============================================================

class File:

    def read(self):
        print("Reading from file...")


class Database:

    def read(self):
        print("Reading from database...")


class API:

    def read(self):
        print("Reading from API...")


def load_data(source):
    source.read()


load_data(File())
load_data(Database())
load_data(API())


"""
The function only cares that source has read().
"""


# ============================================================
# 9. Polymorphism with Strings
# ============================================================

class User:

    def __str__(self):
        return "User object"


class Product:

    def __str__(self):
        return "Product object"


objects = [
    User(),
    Product()
]

for object_ in objects:
    print(str(object_))


"""
Both classes implement __str__.

Python can call str() on either object.
"""


# ============================================================
# 10. Built-in Polymorphism
# ============================================================

print(len("Python"))

print(len([1, 2, 3, 4, 5]))

print(len({
    "name": "Mohsen",
    "age": 24
}))


"""
len() works with different types:

str
list
dict
tuple
set
...

The operation is the same,
but the behavior depends on the object.
"""


# ============================================================
# 11. Operator Polymorphism
# ============================================================

print(10 + 20)

print("Hello " + "World")

print([1, 2] + [3, 4])


"""
The + operator works differently depending on the types.

Numbers:
    addition

Strings:
    concatenation

Lists:
    concatenation
"""


# ============================================================
# 12. More Operator Polymorphism
# ============================================================

print(5 * 3)

print("Python " * 3)

print([1, 2] * 3)


"""
The * operator also behaves differently
depending on the object.
"""


# ============================================================
# 13. Custom Operator Behavior
# ============================================================

class Product:

    def __init__(self, price):
        self.price = price

    def __add__(self, other):
        return self.price + other.price


product1 = Product(100)
product2 = Product(200)

total = product1 + product2

print(total)


"""
__add__ allows us to define what + means
for our own objects.
"""


# ============================================================
# 14. Custom Equality
# ============================================================

class User:

    def __init__(self, username):
        self.username = username

    def __eq__(self, other):
        return self.username == other.username


user1 = User("mohsen")
user2 = User("mohsen")

print(user1 == user2)


"""
__eq__ defines how == behaves for our objects.
"""


# ============================================================
# 15. Polymorphism with Shapes
# ============================================================

class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Square:

    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2


class Circle:

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        import math

        return math.pi * self.radius ** 2


shapes = [
    Rectangle(10, 5),
    Square(5),
    Circle(3)
]

for shape in shapes:
    print(shape.area())


"""
Every shape provides area().

The implementation is different for each class.
"""


# ============================================================
# 16. Function Working with Different Objects
# ============================================================

def calculate_area(shape):
    return shape.area()


rectangle = Rectangle(10, 5)
square = Square(5)
circle = Circle(3)

print(calculate_area(rectangle))
print(calculate_area(square))
print(calculate_area(circle))


# ============================================================
# 17. Practical Example: Notifications
# ============================================================

class EmailNotification:

    def send(self, message):
        print(
            f"Email sent: {message}"
        )


class SMSNotification:

    def send(self, message):
        print(
            f"SMS sent: {message}"
        )


class PushNotification:

    def send(self, message):
        print(
            f"Push notification sent: {message}"
        )


def notify(notification, message):
    notification.send(message)


notify(
    EmailNotification(),
    "Your order has been shipped."
)

notify(
    SMSNotification(),
    "Your order has been shipped."
)

notify(
    PushNotification(),
    "Your order has been shipped."
)


# ============================================================
# 18. Practical Example: Storage
# ============================================================

class LocalStorage:

    def save(self, data):
        print(
            f"Saved locally: {data}"
        )


class CloudStorage:

    def save(self, data):
        print(
            f"Saved to cloud: {data}"
        )


class DatabaseStorage:

    def save(self, data):
        print(
            f"Saved to database: {data}"
        )


def save_data(storage, data):
    storage.save(data)


data = {
    "username": "mohsen",
    "age": 24
}

save_data(
    LocalStorage(),
    data
)

save_data(
    CloudStorage(),
    data
)

save_data(
    DatabaseStorage(),
    data
)


# ============================================================
# 19. Practical Example: E-commerce
# ============================================================

class CreditCard:

    def pay(self, amount):
        print(
            f"Credit card payment: ${amount}"
        )


class PayPal:

    def pay(self, amount):
        print(
            f"PayPal payment: ${amount}"
        )


class BankTransfer:

    def pay(self, amount):
        print(
            f"Bank transfer payment: ${amount}"
        )


def process_payment(payment_method, amount):
    payment_method.pay(amount)


payment_methods = [
    CreditCard(),
    PayPal(),
    BankTransfer()
]

for method in payment_methods:
    process_payment(method, 250)


"""
The checkout system does not need separate logic such as:

if payment_type == "credit_card":
    ...

if payment_type == "paypal":
    ...

Instead, every payment method provides pay().
"""


# ============================================================
# 20. Polymorphism in Backend Architecture
# ============================================================

"""
Imagine an application supports several storage systems:

LocalStorage
CloudStorage
DatabaseStorage

The rest of the application can work with:

save(data)

without knowing how the data is actually stored.

This reduces coupling between different parts
of the application.
"""


# ============================================================
# 21. Polymorphism with Iteration
# ============================================================

items = [
    [1, 2, 3],
    "Python",
    (10, 20, 30),
    {1, 2, 3}
]

for item in items:
    for value in item:
        print(value)

    print("---")


"""
Different objects can support iteration.

The for loop works with all of them
because they provide the required behavior.
"""


# ============================================================
# 22. Polymorphism with Context Managers
# ============================================================

"""
Some objects support the context manager protocol:

with object:
    ...

Files are a common example.

Different context managers can provide different behavior
while following the same interface.
"""


# ============================================================
# 23. Polymorphism and Abstract Base Classes
# ============================================================

"""
Python also provides the abc module for defining
abstract base classes.

This can be useful when we want to explicitly require
child classes to implement certain methods.
"""


from abc import ABC, abstractmethod


class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class CreditCardPayment(Payment):

    def pay(self, amount):
        print(
            f"Paid ${amount} by credit card."
        )


class BankPayment(Payment):

    def pay(self, amount):
        print(
            f"Paid ${amount} by bank transfer."
        )


payments = [
    CreditCardPayment(),
    BankPayment()
]

for payment in payments:
    payment.pay(100)


"""
Payment defines the expected interface.

Each child class provides its own implementation.
"""


# ============================================================
# 24. Abstract Class Cannot Be Instantiated
# ============================================================

"""
Because Payment contains an abstract method,
we cannot normally create:

Payment()

directly.

The class is intended to be used as a blueprint
for concrete implementations.
"""


# ============================================================
# 25. Practical Example: Reports
# ============================================================

class Report:

    def generate(self):
        raise NotImplementedError


class PDFReport(Report):

    def generate(self):
        return "Generating PDF report."


class ExcelReport(Report):

    def generate(self):
        return "Generating Excel report."


class HTMLReport(Report):

    def generate(self):
        return "Generating HTML report."


reports = [
    PDFReport(),
    ExcelReport(),
    HTMLReport()
]

for report in reports:
    print(report.generate())


# ============================================================
# 26. Polymorphism vs Conditional Logic
# ============================================================

"""
Without polymorphism, code can become:

if payment_type == "card":
    process_card()

elif payment_type == "paypal":
    process_paypal()

elif payment_type == "bank":
    process_bank()


With polymorphism:

payment_method.pay()

Each class handles its own behavior.

This can make code easier to extend.
"""


# ============================================================
# 27. Adding a New Implementation
# ============================================================

class CryptocurrencyPayment:

    def pay(self, amount):
        print(
            f"Paid ${amount} using cryptocurrency."
        )


def process_payment(payment_method, amount):
    payment_method.pay(amount)


process_payment(
    CryptocurrencyPayment(),
    500
)


"""
The process_payment() function did not need to change.

We only added a new class that follows the same interface.
"""


# ============================================================
# 28. Polymorphism and Loose Coupling
# ============================================================

"""
Polymorphism can reduce coupling.

Instead of depending on a specific implementation:

process_credit_card_payment()

we can depend on a general behavior:

payment.pay()

This makes it easier to replace implementations.
"""


# ============================================================
# 29. Best Practices
# ============================================================

"""
Best practices:

1. Focus on a common interface or behavior.
2. Keep implementations responsible for their own behavior.
3. Avoid unnecessary if/elif chains for object types.
4. Use duck typing when explicit inheritance is unnecessary.
5. Use inheritance when there is a genuine relationship.
6. Use abstract base classes when an explicit contract is useful.
7. Keep polymorphic methods consistent in purpose.
8. Prefer simple and readable designs.
"""


# ============================================================
# 30. Summary
# ============================================================

"""
Important concepts:

Polymorphism
    Same interface, different behavior.

Method overriding
    Child classes provide their own implementation.

Duck typing
    Python cares about what an object can do,
    rather than only its exact type.

Operator polymorphism
    Operators behave differently for different types.

__add__
    Customizes +.

__eq__
    Customizes ==.

isinstance()
    Checks an object's type relationship.

Abstract Base Class
    Defines a common interface for subclasses.

The main idea:

Different objects can provide the same behavior
through a common interface.

Example:

for payment in payments:
    payment.pay(100)

The code does not need to know exactly
which payment implementation it is using.
"""