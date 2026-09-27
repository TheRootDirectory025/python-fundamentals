"""
Python Fundamentals
11 - Object-Oriented Programming
Topic: Inheritance

This file covers:
- What inheritance is
- Parent classes
- Child classes
- Inheriting attributes
- Inheriting methods
- Overriding methods
- super()
- Extending parent classes
- Multilevel inheritance
- Multiple inheritance
- isinstance()
- issubclass()
- Practical examples
"""


# ============================================================
# 1. What Is Inheritance?
# ============================================================

"""
Inheritance allows one class to reuse functionality
from another class.

The existing class is called:

Parent class
Base class
Superclass

The new class is called:

Child class
Derived class
Subclass

Example:

Animal
    ↓
Dog

Dog can inherit common behavior from Animal.
"""


# ============================================================
# 2. Basic Inheritance
# ============================================================

class Animal:

    def speak(self):
        print("Animal makes a sound.")


class Dog(Animal):
    pass


dog = Dog()

dog.speak()


"""
Dog inherits the speak() method from Animal.
"""


# ============================================================
# 3. Parent and Child Classes
# ============================================================

class Animal:

    def eat(self):
        print("Animal is eating.")


class Dog(Animal):
    def bark(self):
        print("Dog is barking.")


dog = Dog()

dog.eat()
dog.bark()


"""
Dog has:

- Its own method: bark()
- An inherited method: eat()
"""


# ============================================================
# 4. Inheriting __init__
# ============================================================

class Person:

    def __init__(self, name):
        self.name = name


class Student(Person):
    pass


student = Student("Mohsen")

print(student.name)


"""
Student inherits the __init__ method from Person.
"""


# ============================================================
# 5. Adding New Attributes
# ============================================================

class Person:

    def __init__(self, name):
        self.name = name


class Student(Person):

    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id


student = Student(
    "Mohsen",
    1001
)

print(student.name)
print(student.student_id)


# ============================================================
# 6. Reusing the Parent Constructor with super()
# ============================================================

class Person:

    def __init__(self, name):
        self.name = name


class Student(Person):

    def __init__(self, name, student_id):
        super().__init__(name)
        self.student_id = student_id


student = Student(
    "Mohsen",
    1001
)

print(student.name)
print(student.student_id)


"""
super() allows us to access functionality from the parent class.

Instead of repeating:

self.name = name

we use:

super().__init__(name)
"""


# ============================================================
# 7. Overriding a Method
# ============================================================

class Animal:

    def speak(self):
        print("Animal makes a sound.")


class Dog(Animal):

    def speak(self):
        print("Dog says: Woof!")


animal = Animal()
dog = Dog()

animal.speak()
dog.speak()


"""
Dog replaces the inherited speak() behavior
with its own implementation.

This is called method overriding.
"""


# ============================================================
# 8. Calling the Parent Method with super()
# ============================================================

class Animal:

    def speak(self):
        print("Animal makes a sound.")


class Dog(Animal):

    def speak(self):
        super().speak()
        print("Dog says: Woof!")


dog = Dog()

dog.speak()


"""
super() can call the parent implementation
before adding child-specific behavior.
"""


# ============================================================
# 9. Extending a Parent Method
# ============================================================

class User:

    def display(self):
        print("User information")


class Admin(User):

    def display(self):
        super().display()
        print("Admin permissions")


admin = Admin()

admin.display()


# ============================================================
# 10. Practical Example: Employees
# ============================================================

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print(
            f"Name: {self.name}\n"
            f"Salary: {self.salary}"
        )


class Developer(Employee):

    def write_code(self):
        print(f"{self.name} is writing code.")


developer = Developer(
    "Mohsen",
    3000
)

developer.display()
developer.write_code()


# ============================================================
# 11. Adding Developer-Specific Attributes
# ============================================================

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class Developer(Employee):

    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self.language = language

    def write_code(self):
        print(
            f"{self.name} is writing "
            f"{self.language} code."
        )


developer = Developer(
    "Mohsen",
    3000,
    "Python"
)

print(developer.name)
print(developer.salary)
print(developer.language)

developer.write_code()


# ============================================================
# 12. Another Child Class
# ============================================================

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print(
            f"{self.name} - "
            f"${self.salary}"
        )


class Developer(Employee):

    def write_code(self):
        print("Writing code...")


class Designer(Employee):

    def design(self):
        print("Designing...")


developer = Developer(
    "Mohsen",
    3000
)

designer = Designer(
    "Sara",
    2800
)

developer.display()
developer.write_code()

designer.display()
designer.design()


"""
Both Developer and Designer inherit from Employee.

This creates a hierarchy:

             Employee
              /    \
             /      \
       Developer   Designer
"""


# ============================================================
# 13. Multiple Levels of Inheritance
# ============================================================

class Animal:

    def eat(self):
        print("Eating...")


class Mammal(Animal):

    def breathe(self):
        print("Breathing...")


class Dog(Mammal):

    def bark(self):
        print("Barking...")


dog = Dog()

dog.eat()
dog.breathe()
dog.bark()


"""
The inheritance chain is:

Animal
   ↓
Mammal
   ↓
Dog

Dog receives functionality from both parent levels.
"""


# ============================================================
# 14. Multilevel Practical Example
# ============================================================

class Person:

    def introduce(self):
        print("I am a person.")


class Employee(Person):

    def work(self):
        print("I am working.")


class Developer(Employee):

    def write_code(self):
        print("I am writing code.")


developer = Developer()

developer.introduce()
developer.work()
developer.write_code()


# ============================================================
# 15. Multiple Inheritance
# ============================================================

"""
Python allows a class to inherit from more than one class.

Example:

class Child(ParentA, ParentB):
    pass
"""


class Flyer:

    def fly(self):
        print("Flying...")


class Swimmer:

    def swim(self):
        print("Swimming...")


class Duck(Flyer, Swimmer):
    pass


duck = Duck()

duck.fly()
duck.swim()


"""
Duck inherits from both Flyer and Swimmer.
"""


# ============================================================
# 16. Multiple Inheritance Example
# ============================================================

class Logger:

    def log(self, message):
        print(f"LOG: {message}")


class Serializer:

    def serialize(self, data):
        return str(data)


class Service(Logger, Serializer):
    pass


service = Service()

service.log("Processing data")

result = service.serialize(
    {"name": "Mohsen"}
)

print(result)


# ============================================================
# 17. Method Resolution Order
# ============================================================

"""
When multiple inheritance is used, Python needs to determine
which implementation should be used first.

Python uses Method Resolution Order (MRO).

We can inspect it with:

ClassName.mro()
"""


class A:

    def show(self):
        print("A")


class B(A):

    def show(self):
        print("B")


class C(A):

    def show(self):
        print("C")


class D(B, C):
    pass


print(D.mro())

d = D()

d.show()


"""
Python follows the MRO to decide which show() method
should be called.
"""


# ============================================================
# 18. isinstance()
# ============================================================

class Animal:
    pass


class Dog(Animal):
    pass


dog = Dog()

print(isinstance(dog, Dog))
print(isinstance(dog, Animal))


"""
A Dog object is also considered an Animal because
Dog inherits from Animal.
"""


# ============================================================
# 19. issubclass()
# ============================================================

class Animal:
    pass


class Dog(Animal):
    pass


print(issubclass(Dog, Animal))
print(issubclass(Animal, Dog))


"""
issubclass() checks whether one class inherits from another.
"""


# ============================================================
# 20. Polymorphism Through Inheritance
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
Different objects respond to the same method
in different ways.

This is one example of polymorphism.
"""


# ============================================================
# 21. Practical Example: Payment Methods
# ============================================================

class Payment:

    def pay(self, amount):
        print(
            f"Processing payment of ${amount}"
        )


class CreditCardPayment(Payment):

    def pay(self, amount):
        print(
            f"Paid ${amount} using credit card."
        )


class PayPalPayment(Payment):

    def pay(self, amount):
        print(
            f"Paid ${amount} using PayPal."
        )


payments = [
    CreditCardPayment(),
    PayPalPayment()
]

for payment in payments:
    payment.pay(100)


"""
The application can work with Payment objects
without needing to know the exact child class.
"""


# ============================================================
# 22. Abstract Idea of a Parent Class
# ============================================================

"""
Sometimes a parent class exists mainly to define
a common interface.

For example:

Payment
    ↓
CreditCardPayment
PayPalPayment
BankTransferPayment

Every payment type should implement:

pay()

The exact implementation can be different.
"""


# ============================================================
# 23. Practical Example: Vehicles
# ============================================================

class Vehicle:

    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print("Vehicle started.")


class Car(Vehicle):

    def start(self):
        print(
            f"{self.brand} car started."
        )


class Motorcycle(Vehicle):

    def start(self):
        print(
            f"{self.brand} motorcycle started."
        )


vehicles = [
    Car("Toyota"),
    Motorcycle("Honda")
]

for vehicle in vehicles:
    vehicle.start()


# ============================================================
# 24. Parent Attributes and Child Methods
# ============================================================

class User:

    def __init__(self, username):
        self.username = username


class Admin(User):

    def delete_user(self, username):
        print(
            f"{self.username} deleted "
            f"user {username}."
        )


admin = Admin("admin")

print(admin.username)

admin.delete_user("mohsen")


# ============================================================
# 25. Parent Method + Child Method
# ============================================================

class User:

    def login(self):
        print("User logged in.")


class Admin(User):

    def manage_users(self):
        print("Managing users.")


admin = Admin()

admin.login()
admin.manage_users()


# ============================================================
# 26. Practical Example: E-commerce
# ============================================================

class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display(self):
        print(
            f"{self.name}: ${self.price}"
        )


class PhysicalProduct(Product):

    def __init__(
        self,
        name,
        price,
        weight
    ):
        super().__init__(name, price)
        self.weight = weight

    def shipping_cost(self):
        return self.weight * 2


class DigitalProduct(Product):

    def __init__(
        self,
        name,
        price,
        file_size
    ):
        super().__init__(name, price)
        self.file_size = file_size


physical = PhysicalProduct(
    "Keyboard",
    50,
    2
)

digital = DigitalProduct(
    "Python Course",
    30,
    500
)

physical.display()
print(physical.shipping_cost())

digital.display()


# ============================================================
# 27. When to Use Inheritance
# ============================================================

"""
Inheritance is useful when there is a genuine
"IS-A" relationship.

Examples:

Dog IS-A Animal

Developer IS-A Employee

Car IS-A Vehicle

CreditCardPayment IS-A Payment


Inheritance is usually not appropriate simply because
two classes share some code.

Sometimes composition is a better solution.
"""


# ============================================================
# 28. Inheritance vs Composition
# ============================================================

"""
Inheritance:

Car IS-A Vehicle


Composition:

Car HAS-A Engine


Example:

class Engine:

    def start(self):
        print("Engine started.")


class Car:

    def __init__(self):
        self.engine = Engine()


Here Car does not inherit from Engine.

Instead, Car contains an Engine object.
"""


# ============================================================
# 29. Common Mistake
# ============================================================

class Person:

    def __init__(self, name):
        self.name = name


class Student(Person):

    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id


"""
This works, but it duplicates the parent's initialization.

A cleaner approach is usually:

"""


class Student(Person):

    def __init__(self, name, student_id):
        super().__init__(name)
        self.student_id = student_id


# ============================================================
# 30. Best Practices
# ============================================================

"""
Best practices:

1. Use inheritance when there is a meaningful IS-A relationship.
2. Use super() when extending parent initialization or behavior.
3. Keep inheritance hierarchies reasonably simple.
4. Avoid inheritance just to reuse a few lines of code.
5. Consider composition when the relationship is HAS-A.
6. Override methods only when the child genuinely needs
   different behavior.
7. Keep parent classes focused.
8. Avoid unnecessarily deep inheritance chains.
9. Understand MRO when using multiple inheritance.
10. Prefer readable class hierarchies over clever designs.
"""


# ============================================================
# 31. Summary
# ============================================================

"""
Important concepts:

Inheritance
    Allows a class to reuse functionality from another class.

Parent class
    The class being inherited from.

Child class
    The class that inherits.

super()
    Accesses functionality from the parent class.

Method overriding
    Replacing a parent's method with a child implementation.

Multilevel inheritance
    A class inherits through multiple levels.

Multiple inheritance
    A class inherits from multiple parent classes.

MRO
    Method Resolution Order.

isinstance()
    Checks whether an object is an instance of a class.

issubclass()
    Checks whether a class inherits from another class.

Polymorphism
    Different objects can provide different implementations
    of the same interface.

The basic pattern:

class Parent:
    def method(self):
        pass


class Child(Parent):
    def method(self):
        super().method()
        pass
"""