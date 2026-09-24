"""
Python Fundamentals
11 - Object-Oriented Programming
Topic: Classes

This file covers:
- What classes are
- What objects are
- Attributes
- Methods
- __init__
- self
- Creating objects
- Updating attributes
- Instance methods
- Class attributes
- Basic encapsulation
- Practical examples
"""


# ============================================================
# 1. What Is a Class?
# ============================================================

"""
A class is a blueprint for creating objects.

For example, a User class can describe what every user has:

- name
- age
- email

and what every user can do:

- login
- logout
- display information

The class defines the structure and behavior.

An object is an actual instance created from that class.
"""


# ============================================================
# 2. Creating a Simple Class
# ============================================================

class User:
    pass


# User is now a class.


# ============================================================
# 3. Creating an Object
# ============================================================

user = User()

print(user)


"""
user is an object created from the User class.

We can create multiple objects from the same class.
"""


user1 = User()
user2 = User()

print(user1)
print(user2)


# ============================================================
# 4. Instance Attributes
# ============================================================

class User:
    pass


user = User()

user.name = "Mohsen"
user.age = 24

print(user.name)
print(user.age)


"""
Attributes are pieces of data associated with an object.
"""


# ============================================================
# 5. __init__
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

It is commonly used to initialize object attributes.
"""


# ============================================================
# 6. Understanding self
# ============================================================

class User:

    def __init__(self, name, age):
        self.name = name
        self.age = age


"""
self refers to the current object.

When we write:

user = User("Mohsen", 24)

Python internally associates:

self -> user

So:

self.name

means:

the name belonging to this object.
"""


# ============================================================
# 7. Multiple Objects
# ============================================================

class User:

    def __init__(self, name, age):
        self.name = name
        self.age = age


user1 = User("Ali", 22)
user2 = User("Sara", 25)
user3 = User("Mohsen", 24)

print(user1.name)
print(user2.name)
print(user3.name)


# Each object has its own attributes.


# ============================================================
# 8. Instance Methods
# ============================================================

class User:

    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, {self.name}!")


user = User("Mohsen")

user.greet()


"""
A method is a function defined inside a class.

Methods usually operate on the object using self.
"""


# ============================================================
# 9. Method with Parameters
# ============================================================

class Calculator:

    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b


calculator = Calculator()

print(calculator.add(10, 5))
print(calculator.multiply(10, 5))


# ============================================================
# 10. Methods Using Object Attributes
# ============================================================

class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


rectangle = Rectangle(10, 5)

print(rectangle.area())
print(rectangle.perimeter())


# ============================================================
# 11. Updating Attributes
# ============================================================

class User:

    def __init__(self, name, age):
        self.name = name
        self.age = age


user = User("Mohsen", 24)

print(user.age)

user.age = 25

print(user.age)


# ============================================================
# 12. Method for Updating Attributes
# ============================================================

class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount


account = BankAccount("Mohsen", 1000)

account.deposit(500)

print(account.balance)


# ============================================================
# 13. Multiple Methods
# ============================================================

class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount

    def show_balance(self):
        print(f"Balance: {self.balance}")


account = BankAccount("Mohsen", 1000)

account.deposit(500)
account.withdraw(200)
account.show_balance()


# ============================================================
# 14. Returning Values from Methods
# ============================================================

class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


rectangle = Rectangle(10, 20)

area = rectangle.area()

print(f"Area: {area}")


# ============================================================
# 15. Class Attributes
# ============================================================

class User:

    species = "Human"

    def __init__(self, name):
        self.name = name


user1 = User("Ali")
user2 = User("Mohsen")

print(user1.species)
print(user2.species)


"""
species is a class attribute.

It belongs to the class rather than a specific object.
"""


# ============================================================
# 16. Instance vs Class Attributes
# ============================================================

class User:

    platform = "Website"

    def __init__(self, name):
        self.name = name


user1 = User("Ali")
user2 = User("Mohsen")

print(user1.name)
print(user2.name)

print(user1.platform)
print(user2.platform)


"""
name
    Instance attribute.

platform
    Class attribute.
"""


# ============================================================
# 17. Changing a Class Attribute
# ============================================================

class User:

    platform = "Website"

    def __init__(self, name):
        self.name = name


print(User.platform)

User.platform = "Mobile App"

print(User.platform)


# ============================================================
# 18. Object Representation
# ============================================================

class User:

    def __init__(self, name, age):
        self.name = name
        self.age = age


user = User("Mohsen", 24)

print(user)


"""
By default, printing an object does not give a very useful
representation.

We can improve this with __str__.
"""


# ============================================================
# 19. __str__
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
__str__ controls the human-readable representation
of an object.
"""


# ============================================================
# 20. __repr__
# ============================================================

class User:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"User(name='{self.name}', age={self.age})"


user = User("Mohsen", 24)

print(repr(user))


"""
__repr__ is intended to provide a more detailed
representation of an object, often useful for debugging.
"""


# ============================================================
# 21. Checking Object Type
# ============================================================

class User:
    pass


user = User()

print(type(user))
print(isinstance(user, User))


# ============================================================
# 22. Comparing Objects
# ============================================================

class User:

    def __init__(self, name):
        self.name = name


user1 = User("Mohsen")
user2 = User("Mohsen")

print(user1 == user2)


"""
Two separate objects are not automatically considered equal
just because their attributes contain the same values.

Later, special methods can be used to define custom equality.
"""


# ============================================================
# 23. Practical Example: Product
# ============================================================

class Product:

    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def display(self):
        print(
            f"{self.name} - "
            f"${self.price} - "
            f"Stock: {self.stock}"
        )

    def is_available(self):
        return self.stock > 0


product = Product(
    "Keyboard",
    50,
    10
)

product.display()

print(product.is_available())


# ============================================================
# 24. Practical Example: Student
# ============================================================

class Student:

    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average(self):
        return sum(self.grades) / len(self.grades)

    def passed(self):
        return self.average() >= 10


student = Student(
    "Mohsen",
    [18, 17, 19]
)

print(student.average())
print(student.passed())


# ============================================================
# 25. Practical Example: Car
# ============================================================

class Car:

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start(self):
        print(
            f"{self.brand} {self.model} has started."
        )

    def display_info(self):
        print(
            f"{self.brand} "
            f"{self.model} "
            f"({self.year})"
        )


car = Car(
    "Toyota",
    "Camry",
    2024
)

car.display_info()
car.start()


# ============================================================
# 26. Practical Example: User
# ============================================================

class User:

    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.is_active = True

    def deactivate(self):
        self.is_active = False

    def activate(self):
        self.is_active = True

    def display(self):
        print(
            f"Username: {self.username}\n"
            f"Email: {self.email}\n"
            f"Active: {self.is_active}"
        )


user = User(
    "mohsen",
    "mohsen@example.com"
)

user.display()

user.deactivate()

user.display()


# ============================================================
# 27. Basic Encapsulation
# ============================================================

"""
Encapsulation means keeping data and the operations
that work with that data together.

For example:

BankAccount

contains:
- balance
- owner

and methods such as:
- deposit()
- withdraw()

Instead of manipulating everything independently,
the object controls how its data changes.
"""


# ============================================================
# 28. Protected Convention
# ============================================================

class User:

    def __init__(self, name):
        self._name = name


user = User("Mohsen")

print(user._name)


"""
A single underscore is a convention meaning:

"This attribute is intended for internal use."

Python does not strictly prevent access to it.
"""


# ============================================================
# 29. Private Attributes
# ============================================================

class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance


account = BankAccount(1000)

print(account.get_balance())


"""
A double underscore triggers name mangling.

It makes accidental access from outside the class
more difficult.

It is not absolute security.
"""


# ============================================================
# 30. Property
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
@property allows a method to be accessed like an attribute.
"""


# ============================================================
# 31. Property with Setter
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


# ============================================================
# 32. Practical Example: Product Price Validation
# ============================================================

class Product:

    def __init__(self, name, price):
        self.name = name
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


product = Product(
    "Keyboard",
    50
)

print(product.price)

product.price = 60

print(product.price)


# ============================================================
# 33. Objects Containing Other Objects
# ============================================================

class Engine:

    def start(self):
        print("Engine started.")


class Car:

    def __init__(self):
        self.engine = Engine()

    def start(self):
        self.engine.start()
        print("Car started.")


car = Car()

car.start()


"""
An object can contain another object.

This relationship is very common in real applications.
"""


# ============================================================
# 34. Class Method
# ============================================================

class User:

    platform = "Website"

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_platform(cls, platform):
        cls.platform = platform


print(User.platform)

User.change_platform("Mobile App")

print(User.platform)


"""
A class method receives cls instead of self.

It works with the class rather than a specific instance.
"""


# ============================================================
# 35. Static Method
# ============================================================

class Calculator:

    @staticmethod
    def add(a, b):
        return a + b


result = Calculator.add(10, 20)

print(result)


"""
A static method does not need access to self or cls.

It is useful when a function logically belongs to a class
but does not need object or class state.
"""


# ============================================================
# 36. Instance vs Class vs Static Method
# ============================================================

class Example:

    class_value = 10

    def instance_method(self):
        return "Uses self."

    @classmethod
    def class_method(cls):
        return cls.class_value

    @staticmethod
    def static_method():
        return "Does not use self or cls."


example = Example()

print(example.instance_method())
print(example.class_method())
print(example.static_method())


# ============================================================
# 37. Practical Example: E-commerce Product
# ============================================================

class Product:

    tax_rate = 0.09

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def price_with_tax(self):
        return self.price * (1 + Product.tax_rate)

    @classmethod
    def change_tax_rate(cls, new_rate):
        cls.tax_rate = new_rate

    @staticmethod
    def is_valid_price(price):
        return price >= 0


product = Product(
    "Laptop",
    1000
)

print(product.price_with_tax())

Product.change_tax_rate(0.10)

print(product.price_with_tax())

print(Product.is_valid_price(500))


# ============================================================
# 38. Best Practices
# ============================================================

"""
Best practices:

1. Give classes meaningful names.
2. Use PascalCase for class names.
3. Keep each class focused on a clear responsibility.
4. Use self for instance data and behavior.
5. Use class attributes only for shared class-level data.
6. Validate important data when appropriate.
7. Keep methods reasonably small.
8. Avoid putting unrelated functionality into one class.
9. Use properties when controlled access to attributes is useful.
10. Use class methods and static methods only when they
    actually fit the problem.
"""


# ============================================================
# 39. Summary
# ============================================================

"""
Important concepts:

Class
    Blueprint for creating objects.

Object
    An instance of a class.

Attribute
    Data associated with an object or class.

Method
    Function defined inside a class.

__init__
    Initializes a new object.

self
    Refers to the current object.

@property
    Allows controlled attribute access.

@classmethod
    Method that works with the class.

@staticmethod
    Method that does not need instance or class state.

The basic pattern:

class User:

    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello {self.name}")


user = User("Mohsen")

user.greet()
"""