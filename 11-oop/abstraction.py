"""
Python Fundamentals
11 - Object-Oriented Programming
Topic: Abstraction

This file covers:
- What abstraction is
- Why abstraction is useful
- Abstract base classes
- @abstractmethod
- Abstract properties
- Abstract class methods
- Abstract static methods
- Concrete implementations
- Practical examples
"""


# ============================================================
# 1. What Is Abstraction?
# ============================================================

"""
Abstraction means hiding unnecessary implementation details
and exposing only the important interface.

For example, when we use:

car.start()

we don't need to know exactly how the engine, fuel system,
battery, and other components work internally.

We only need to know that the car provides a start() operation.
"""


# ============================================================
# 2. Abstraction in Everyday Programming
# ============================================================

numbers = [10, 20, 30, 40]

total = sum(numbers)

print(total)


"""
We use sum() without needing to know exactly how Python
calculates the result internally.

The implementation is hidden behind a simple interface.
"""


# ============================================================
# 3. Abstract Base Classes
# ============================================================

from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def speak(self):
        pass


"""
Animal is now an Abstract Base Class.

It defines that subclasses must provide speak().
"""


# ============================================================
# 4. Implementing an Abstract Class
# ============================================================

class Dog(Animal):

    def speak(self):
        print("Woof!")


class Cat(Animal):

    def speak(self):
        print("Meow!")


dog = Dog()
cat = Cat()

dog.speak()
cat.speak()


# ============================================================
# 5. Abstract Classes Cannot Normally Be Instantiated
# ============================================================

class Animal(ABC):

    @abstractmethod
    def speak(self):
        pass


"""
The following would raise a TypeError:

animal = Animal()

because Animal contains an abstract method.
"""


# ============================================================
# 6. Abstract Method
# ============================================================

class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


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


credit_card = CreditCardPayment()
bank = BankPayment()

credit_card.pay(100)
bank.pay(200)


"""
Payment defines the required interface.

Each subclass decides how pay() actually works.
"""


# ============================================================
# 7. Multiple Abstract Methods
# ============================================================

class Animal(ABC):

    @abstractmethod
    def speak(self):
        pass

    @abstractmethod
    def move(self):
        pass


class Dog(Animal):

    def speak(self):
        print("Woof!")

    def move(self):
        print("Dog is running.")


dog = Dog()

dog.speak()
dog.move()


"""
A concrete child class must implement all required
abstract methods.
"""


# ============================================================
# 8. Partial Implementation in an Abstract Class
# ============================================================

class Animal(ABC):

    def sleep(self):
        print("Animal is sleeping.")

    @abstractmethod
    def speak(self):
        pass


class Dog(Animal):

    def speak(self):
        print("Woof!")


dog = Dog()

dog.sleep()
dog.speak()


"""
An abstract class can contain normal methods as well as
abstract methods.
"""


# ============================================================
# 9. Shared Logic + Required Behavior
# ============================================================

class Employee(ABC):

    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(
            f"My name is {self.name}."
        )

    @abstractmethod
    def work(self):
        pass


class Developer(Employee):

    def work(self):
        print(
            f"{self.name} is writing code."
        )


class Designer(Employee):

    def work(self):
        print(
            f"{self.name} is designing."
        )


developer = Developer("Mohsen")
designer = Designer("Sara")

developer.introduce()
developer.work()

designer.introduce()
designer.work()


# ============================================================
# 10. Abstract Property
# ============================================================

class Product(ABC):

    @property
    @abstractmethod
    def price(self):
        pass


class Book(Product):

    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price


book = Book(25)

print(book.price)


"""
The child class must provide the price property.
"""


# ============================================================
# 11. Abstract Property with Setter
# ============================================================

class Product(ABC):

    @property
    @abstractmethod
    def price(self):
        pass

    @price.setter
    @abstractmethod
    def price(self, value):
        pass


class Book(Product):

    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError(
                "Price cannot be negative."
            )

        self._price = value


book = Book(30)

print(book.price)

book.price = 35

print(book.price)


# ============================================================
# 12. Abstract Class Method
# ============================================================

class Factory(ABC):

    @classmethod
    @abstractmethod
    def create(cls):
        pass


class UserFactory(Factory):

    @classmethod
    def create(cls):
        return "Creating a User."


print(UserFactory.create())


"""
An abstract class method requires subclasses
to provide a class-level implementation.
"""


# ============================================================
# 13. Abstract Static Method
# ============================================================

class Validator(ABC):

    @staticmethod
    @abstractmethod
    def validate(value):
        pass


class EmailValidator(Validator):

    @staticmethod
    def validate(value):
        return "@" in value


print(
    EmailValidator.validate(
        "mohsen@example.com"
    )
)


# ============================================================
# 14. Practical Example: Storage System
# ============================================================

class Storage(ABC):

    @abstractmethod
    def save(self, data):
        pass

    @abstractmethod
    def load(self):
        pass


class FileStorage(Storage):

    def __init__(self):
        self.data = None

    def save(self, data):
        self.data = data
        print("Data saved to file.")

    def load(self):
        print("Loading data from file.")
        return self.data


class MemoryStorage(Storage):

    def __init__(self):
        self.data = None

    def save(self, data):
        self.data = data
        print("Data saved in memory.")

    def load(self):
        print("Loading data from memory.")
        return self.data


file_storage = FileStorage()

file_storage.save(
    {"username": "mohsen"}
)

print(file_storage.load())


memory_storage = MemoryStorage()

memory_storage.save(
    {"username": "sara"}
)

print(memory_storage.load())


"""
The application knows that Storage provides:

save()
load()

It does not need to know exactly how the data is stored.
"""


# ============================================================
# 15. Practical Example: Notification System
# ============================================================

class Notification(ABC):

    @abstractmethod
    def send(self, message):
        pass


class EmailNotification(Notification):

    def send(self, message):
        print(
            f"Sending email: {message}"
        )


class SMSNotification(Notification):

    def send(self, message):
        print(
            f"Sending SMS: {message}"
        )


class PushNotification(Notification):

    def send(self, message):
        print(
            f"Sending push notification: {message}"
        )


def notify(notification, message):
    notification.send(message)


notify(
    EmailNotification(),
    "Welcome!"
)

notify(
    SMSNotification(),
    "Your code is 1234."
)

notify(
    PushNotification(),
    "You have a new message."
)


"""
notify() depends on the Notification interface,
not on a specific implementation.
"""


# ============================================================
# 16. Practical Example: Payment System
# ============================================================

class PaymentMethod(ABC):

    @abstractmethod
    def pay(self, amount):
        pass

    @abstractmethod
    def refund(self, amount):
        pass


class CreditCard(PaymentMethod):

    def pay(self, amount):
        print(
            f"Charged ${amount} to credit card."
        )

    def refund(self, amount):
        print(
            f"Refunded ${amount} to credit card."
        )


class PayPal(PaymentMethod):

    def pay(self, amount):
        print(
            f"Charged ${amount} through PayPal."
        )

    def refund(self, amount):
        print(
            f"Refunded ${amount} through PayPal."
        )


payment_methods = [
    CreditCard(),
    PayPal()
]

for method in payment_methods:
    method.pay(100)
    method.refund(50)


# ============================================================
# 17. Practical Example: Database Interface
# ============================================================

class Database(ABC):

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass

    @abstractmethod
    def execute(self, query):
        pass


class PostgreSQLDatabase(Database):

    def connect(self):
        print("Connected to PostgreSQL.")

    def disconnect(self):
        print("Disconnected from PostgreSQL.")

    def execute(self, query):
        print(
            f"Executing PostgreSQL query: {query}"
        )


class MySQLDatabase(Database):

    def connect(self):
        print("Connected to MySQL.")

    def disconnect(self):
        print("Disconnected from MySQL.")

    def execute(self, query):
        print(
            f"Executing MySQL query: {query}"
        )


databases = [
    PostgreSQLDatabase(),
    MySQLDatabase()
]

for database in databases:
    database.connect()
    database.execute(
        "SELECT * FROM users"
    )
    database.disconnect()


"""
The application can work with the Database abstraction
without depending directly on one database implementation.
"""


# ============================================================
# 18. Abstraction and Polymorphism
# ============================================================

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        import math

        return math.pi * self.radius ** 2


shapes = [
    Rectangle(10, 5),
    Circle(3)
]

for shape in shapes:
    print(shape.area())


"""
Abstraction defines the expected behavior.

Polymorphism allows different implementations
of that behavior.
"""


# ============================================================
# 19. Abstraction vs Encapsulation
# ============================================================

"""
Encapsulation:

Focuses on controlling access to internal data
and implementation details.

Example:

BankAccount
    -> balance
    -> deposit()
    -> withdraw()


Abstraction:

Focuses on exposing the important interface
while hiding unnecessary implementation details.

Example:

Payment
    -> pay()

The two concepts are related, but they solve
different design problems.
"""


# ============================================================
# 20. Abstraction vs Inheritance
# ============================================================

"""
Inheritance:

A mechanism for creating a relationship between classes.

Example:

Dog inherits from Animal.


Abstraction:

A design concept for defining what an object should provide.

Example:

Animal requires speak().
"""


# ============================================================
# 21. Abstraction in Real Applications
# ============================================================

"""
A backend application might define:

class EmailService(ABC):

    @abstractmethod
    def send(self, message):
        pass


Then different implementations can exist:

SMTPEmailService
SendGridEmailService
AmazonSESEmailService


The rest of the application can depend on:

send()

instead of knowing the details of each provider.
"""


# ============================================================
# 22. Adding Another Implementation
# ============================================================

class MessageService(ABC):

    @abstractmethod
    def send(self, message):
        pass


class EmailService(MessageService):

    def send(self, message):
        print(
            f"Email: {message}"
        )


class SMSService(MessageService):

    def send(self, message):
        print(
            f"SMS: {message}"
        )


class PushService(MessageService):

    def send(self, message):
        print(
            f"Push: {message}"
        )


class TelegramService(MessageService):

    def send(self, message):
        print(
            f"Telegram: {message}"
        )


services = [
    EmailService(),
    SMSService(),
    PushService(),
    TelegramService()
]

for service in services:
    service.send("Hello!")


"""
Adding TelegramService does not require changing the
existing service interface.
"""


# ============================================================
# 23. When to Use Abstraction
# ============================================================

"""
Abstraction is useful when:

1. Several classes share a common interface.
2. You want to enforce required methods.
3. Different implementations may exist.
4. You want to reduce coupling.
5. You want the rest of the application to depend
   on a general contract instead of a concrete implementation.
"""


# ============================================================
# 24. When Not to Overuse Abstraction
# ============================================================

"""
Not every class needs to inherit from ABC.

For a small and simple program, creating an abstract class
may add unnecessary complexity.

Use abstraction when it makes the design clearer,
more maintainable, or easier to extend.
"""


# ============================================================
# 25. Best Practices
# ============================================================

"""
Best practices:

1. Keep abstract interfaces focused.
2. Define only behavior that subclasses genuinely share.
3. Keep implementations independent from each other.
4. Use @abstractmethod when a method is required.
5. Don't create abstract classes without a clear reason.
6. Prefer simple interfaces.
7. Use abstraction to reduce coupling.
8. Combine abstraction with polymorphism when appropriate.
9. Avoid putting too much implementation into an interface.
10. Choose the simplest design that solves the problem.
"""


# ============================================================
# 26. Summary
# ============================================================

"""
Important concepts:

Abstraction
    Exposing important behavior while hiding implementation
    details.

ABC
    Abstract Base Class.

@abstractmethod
    Marks a method as required for concrete subclasses.

Abstract class
    A class intended to define an interface or shared design
    rather than be instantiated directly.

Concrete class
    A class that provides implementations for all required
    abstract methods.

Abstract property
    A property that subclasses are required to implement.

The main idea:

Application code should depend on:

    what an object can do

rather than:

    how the object does it.

Example:

payment.pay(100)

The application does not need to know whether payment is
implemented through a credit card, PayPal, bank transfer,
or another payment provider.
"""