"""
Python Fundamentals
11 - Object-Oriented Programming
Topic: Encapsulation

This file covers:
- What encapsulation is
- Public attributes
- Protected attributes
- Private attributes
- Name mangling
- Getters
- Setters
- @property
- Property setters
- Data validation
- Practical examples
"""


# ============================================================
# 1. What Is Encapsulation?
# ============================================================

"""
Encapsulation means keeping data and the methods that work
with that data together inside a class.

It also means controlling how important data is accessed
or modified.

For example, a bank account should control how its balance
changes.

Instead of allowing:

account.balance = -5000

we can provide methods such as:

deposit()
withdraw()

and validate the data before changing the balance.
"""


# ============================================================
# 2. Public Attributes
# ============================================================

class User:

    def __init__(self, name, age):
        self.name = name
        self.age = age


user = User("Mohsen", 24)

print(user.name)
print(user.age)


"""
Attributes without an underscore are considered public.

They can be accessed and changed directly.
"""


user.age = 25

print(user.age)


# ============================================================
# 3. The Problem with Direct Access
# ============================================================

class BankAccount:

    def __init__(self, balance):
        self.balance = balance


account = BankAccount(1000)

account.balance = -5000

print(account.balance)


"""
The class has no control over the value.

A bank account should not normally allow an invalid balance
without some kind of validation.

Encapsulation helps us solve this problem.
"""


# ============================================================
# 4. Protected Attributes
# ============================================================

class User:

    def __init__(self, name):
        self._name = name


user = User("Mohsen")

print(user._name)


"""
A single underscore means:

"This attribute is intended for internal use."

Python does not actually prevent access.

It is mainly a convention between developers.
"""


# ============================================================
# 5. Protected Attributes with Methods
# ============================================================

class BankAccount:

    def __init__(self, balance):
        self._balance = balance

    def show_balance(self):
        print(self._balance)


account = BankAccount(1000)

account.show_balance()


# ============================================================
# 6. Private Attributes
# ============================================================

class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def show_balance(self):
        print(self.__balance)


account = BankAccount(1000)

account.show_balance()


"""
Two underscores trigger name mangling.

The attribute is internally stored with a transformed name.

This makes accidental access from outside the class
more difficult.
"""


# ============================================================
# 7. Private Attributes Cannot Be Accessed Normally
# ============================================================

class User:

    def __init__(self, password):
        self.__password = password


user = User("secret")


# The following would raise an AttributeError:
#
# print(user.__password)


# ============================================================
# 8. Name Mangling
# ============================================================

class User:

    def __init__(self, password):
        self.__password = password


user = User("secret")

print(user.__dict__)


"""
Python internally transforms:

__password

into something similar to:

_User__password

This mechanism is called name mangling.

It is not intended to provide real security.
"""


# ============================================================
# 9. Accessing Private Data Through a Method
# ============================================================

class User:

    def __init__(self, password):
        self.__password = password

    def get_password(self):
        return self.__password


user = User("secret")

print(user.get_password())


"""
A method can provide controlled access to internal data.
"""


# ============================================================
# 10. Getter Method
# ============================================================

class User:

    def __init__(self, age):
        self.__age = age

    def get_age(self):
        return self.__age


user = User(24)

print(user.get_age())


"""
A getter is a method used to retrieve internal data.
"""


# ============================================================
# 11. Setter Method
# ============================================================

class User:

    def __init__(self, age):
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age < 0:
            raise ValueError(
                "Age cannot be negative."
            )

        self.__age = age


user = User(24)

print(user.get_age())

user.set_age(25)

print(user.get_age())


"""
A setter allows us to validate data before changing it.
"""


# ============================================================
# 12. Validation with a Setter
# ============================================================

class Product:

    def __init__(self, price):
        self.__price = price

    def get_price(self):
        return self.__price

    def set_price(self, price):
        if price < 0:
            raise ValueError(
                "Price cannot be negative."
            )

        self.__price = price


product = Product(100)

print(product.get_price())

product.set_price(150)

print(product.get_price())


# ============================================================
# 13. Why @property Is Useful
# ============================================================

"""
Using:

get_age()
set_age()

works, but Python provides a cleaner syntax with @property.

Instead of:

user.get_age()

we can write:

user.age

while still keeping control over how the value is accessed.
"""


# ============================================================
# 14. Basic @property
# ============================================================

class User:

    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age


user = User(24)

print(user.age)


"""
The age() method behaves like an attribute because
of @property.
"""


# ============================================================
# 15. @property with Setter
# ============================================================

class User:

    def __init__(self, age):
        self.age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError(
                "Age cannot be negative."
            )

        self._age = value


user = User(24)

print(user.age)

user.age = 25

print(user.age)


"""
The syntax looks like normal attribute access:

user.age = 25

But the setter runs behind the scenes.
"""


# ============================================================
# 16. Property Validation
# ============================================================

class Product:

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


product = Product(100)

print(product.price)

product.price = 200

print(product.price)


# ============================================================
# 17. Preventing Invalid Values
# ============================================================

class Student:

    def __init__(self, grade):
        self.grade = grade

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, value):
        if not 0 <= value <= 20:
            raise ValueError(
                "Grade must be between 0 and 20."
            )

        self._grade = value


student = Student(18)

print(student.grade)

student.grade = 19

print(student.grade)


# ============================================================
# 18. Read-Only Property
# ============================================================

class Circle:

    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return self.radius * 2


circle = Circle(5)

print(circle.diameter)


"""
There is no setter for diameter.

So diameter can be read but cannot normally be assigned.
"""


# ============================================================
# 19. Computed Property
# ============================================================

class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height


rectangle = Rectangle(10, 5)

print(rectangle.area)


"""
area is calculated from width and height.

There is no need to store area separately.
"""


# ============================================================
# 20. Practical Example: Bank Account
# ============================================================

class BankAccount:

    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError(
                "Deposit amount must be positive."
            )

        self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError(
                "Withdrawal amount must be positive."
            )

        if amount > self._balance:
            raise ValueError(
                "Insufficient balance."
            )

        self._balance -= amount


account = BankAccount(
    "Mohsen",
    1000
)

print(account.balance)

account.deposit(500)

print(account.balance)

account.withdraw(200)

print(account.balance)


"""
The balance can be read through:

account.balance

but changes happen through:

deposit()
withdraw()

This gives the class control over its internal state.
"""


# ============================================================
# 21. Practical Example: User Account
# ============================================================

class User:

    def __init__(self, username, password):
        self.username = username
        self._password = password

    def change_password(
        self,
        old_password,
        new_password
    ):
        if old_password != self._password:
            raise ValueError(
                "Old password is incorrect."
            )

        if len(new_password) < 8:
            raise ValueError(
                "Password must contain at least 8 characters."
            )

        self._password = new_password

    def check_password(self, password):
        return password == self._password


user = User(
    "mohsen",
    "oldpassword"
)

print(
    user.check_password("oldpassword")
)

user.change_password(
    "oldpassword",
    "newpassword"
)

print(
    user.check_password("newpassword")
)


# ============================================================
# 22. Practical Example: Product
# ============================================================

class Product:

    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def increase_stock(self, amount):
        if amount <= 0:
            raise ValueError(
                "Amount must be positive."
            )

        self.stock += amount

    def decrease_stock(self, amount):
        if amount <= 0:
            raise ValueError(
                "Amount must be positive."
            )

        if amount > self.stock:
            raise ValueError(
                "Not enough stock."
            )

        self.stock -= amount


product = Product(
    "Keyboard",
    50,
    10
)

product.increase_stock(5)
product.decrease_stock(3)

print(product.stock)


# ============================================================
# 23. Encapsulation and Internal State
# ============================================================

class Counter:

    def __init__(self):
        self._count = 0

    def increment(self):
        self._count += 1

    def decrement(self):
        if self._count > 0:
            self._count -= 1

    @property
    def count(self):
        return self._count


counter = Counter()

counter.increment()
counter.increment()
counter.increment()

print(counter.count)

counter.decrement()

print(counter.count)


"""
The counter controls how its internal state changes.
"""


# ============================================================
# 24. Read-Only Data
# ============================================================

class User:

    def __init__(self, username):
        self._username = username

    @property
    def username(self):
        return self._username


user = User("mohsen")

print(user.username)


"""
There is no setter for username.

The property is therefore effectively read-only
through the normal interface.
"""


# ============================================================
# 25. Protecting Calculated Data
# ============================================================

class Order:

    def __init__(self, price, quantity):
        self.price = price
        self.quantity = quantity

    @property
    def total(self):
        return self.price * self.quantity


order = Order(100, 3)

print(order.total)


"""
total is calculated automatically.

We don't need to manually store:

self.total

because it can be derived from existing data.
"""


# ============================================================
# 26. Encapsulation with Internal Helper Methods
# ============================================================

class Order:

    def __init__(self, price):
        self.price = price

    def calculate_tax(self):
        return self._calculate_tax()

    def _calculate_tax(self):
        return self.price * 0.09


order = Order(1000)

print(order.calculate_tax())


"""
A leading underscore can also be used for internal methods.

It signals that the method is intended to be used
inside the class or by closely related code.
"""


# ============================================================
# 27. Encapsulation Does Not Mean Complete Hiding
# ============================================================

"""
Python does not enforce strict private fields in the same way
some other programming languages do.

Instead, Python relies heavily on:

- conventions
- properties
- validation
- clear interfaces
- name mangling

The goal is usually controlled access rather than
absolute secrecy.
"""


# ============================================================
# 28. Public vs Protected vs Private
# ============================================================

class Example:

    def __init__(self):
        self.public = "Public"
        self._protected = "Protected convention"
        self.__private = "Private with name mangling"


example = Example()

print(example.public)
print(example._protected)

# Direct access to __private is not normally available:
#
# print(example.__private)


# ============================================================
# 29. When to Use @property
# ============================================================

"""
@property is especially useful when:

1. A value needs validation.
2. A value should be read-only.
3. A value is calculated from other attributes.
4. You want attribute-like syntax with controlled behavior.
5. You want to change internal implementation later
   without changing the public interface.
"""


# ============================================================
# 30. Best Practices
# ============================================================

"""
Best practices:

1. Keep internal state inside the class.
2. Validate important data before changing it.
3. Use properties when controlled attribute access is useful.
4. Use a single underscore for internal conventions.
5. Use double underscores only when name mangling is useful.
6. Avoid exposing unnecessary internal details.
7. Keep public interfaces simple.
8. Prefer meaningful methods such as deposit() and withdraw()
   over allowing unrestricted state changes.
9. Don't use private attributes everywhere without a reason.
10. Remember that encapsulation is about design and control,
    not just underscores.
"""


# ============================================================
# 31. Summary
# ============================================================

"""
Important concepts:

Encapsulation
    Keeping data and related behavior together
    and controlling access to internal state.

Public attribute
    Normal attribute accessible directly.

Protected attribute
    Attribute beginning with _.
    Mainly a developer convention.

Private attribute
    Attribute beginning with __.
    Python applies name mangling.

Getter
    Method used to retrieve data.

Setter
    Method used to change data with optional validation.

@property
    Provides attribute-style access to methods.

@<property>.setter
    Allows controlled assignment.

Read-only property
    Property with no setter.

The main idea:

Instead of allowing unrestricted access:

account.balance = -5000

we can control changes through:

account.deposit(...)
account.withdraw(...)

This keeps the object's state valid and makes the code
easier to maintain.
"""