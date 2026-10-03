"""
Python Iterators
================

This file covers:
- Iterable vs iterator
- iter()
- next()
- StopIteration
- for loops and iterators
- Creating custom iterators
- __iter__()
- __next__()
- Practical backend examples
"""


# ============================================================
# 1. Iterable vs Iterator
# ============================================================

# An iterable is an object that can be iterated over.

numbers = [10, 20, 30, 40]

for number in numbers:
    print(number)


# Lists are iterable objects.


# ============================================================
# 2. Creating An Iterator
# ============================================================

numbers = [10, 20, 30, 40]

iterator = iter(numbers)

print(iterator)


# iter() converts an iterable into an iterator.


# ============================================================
# 3. Using next()
# ============================================================

numbers = [10, 20, 30]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))


# Each call to next() returns the next item.


# ============================================================
# 4. StopIteration
# ============================================================

numbers = [10, 20]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))

# The next call raises StopIteration:
#
# print(next(iterator))


# StopIteration tells Python that
# the iterator has no more values.


# ============================================================
# 5. Handling StopIteration
# ============================================================

numbers = [10, 20]

iterator = iter(numbers)

try:
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))

except StopIteration:
    print("Iterator is exhausted")


# ============================================================
# 6. Iterator State
# ============================================================

numbers = [10, 20, 30]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))

# The iterator remembers its current position.

print(next(iterator))


# ============================================================
# 7. Iterators Are Stateful
# ============================================================

numbers = [1, 2, 3]

iterator = iter(numbers)

first = next(iterator)
second = next(iterator)

print("First:", first)
print("Second:", second)


# The iterator does not restart automatically.


# ============================================================
# 8. for Loop Internally Uses Iterators
# ============================================================

numbers = [10, 20, 30]

for number in numbers:
    print(number)


# Conceptually, Python does something similar to:
#
# iterator = iter(numbers)
#
# while True:
#     try:
#         number = next(iterator)
#         print(number)
#     except StopIteration:
#         break


# ============================================================
# 9. Manually Recreating A for Loop
# ============================================================

numbers = [10, 20, 30]

iterator = iter(numbers)

while True:
    try:
        number = next(iterator)
        print(number)

    except StopIteration:
        break


# ============================================================
# 10. Strings Are Iterable
# ============================================================

text = "Python"

iterator = iter(text)

print(next(iterator))
print(next(iterator))
print(next(iterator))


# ============================================================
# 11. Tuples Are Iterable
# ============================================================

values = (100, 200, 300)

iterator = iter(values)

print(next(iterator))
print(next(iterator))
print(next(iterator))


# ============================================================
# 12. Dictionaries Are Iterable
# ============================================================

user = {
    "id": 101,
    "name": "Mohsen",
    "role": "developer",
}

iterator = iter(user)

print(next(iterator))
print(next(iterator))
print(next(iterator))


# Iterating over a dictionary directly
# produces its keys.


# ============================================================
# 13. Dictionary Values
# ============================================================

user = {
    "id": 101,
    "name": "Mohsen",
    "role": "developer",
}

iterator = iter(user.values())

print(next(iterator))
print(next(iterator))
print(next(iterator))


# ============================================================
# 14. Dictionary Items
# ============================================================

user = {
    "id": 101,
    "name": "Mohsen",
}

iterator = iter(user.items())

print(next(iterator))
print(next(iterator))


# ============================================================
# 15. range() Is Iterable
# ============================================================

numbers = range(5)

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))


# ============================================================
# 16. Iterable Does Not Mean Iterator
# ============================================================

numbers = [1, 2, 3]

print(hasattr(numbers, "__iter__"))
print(hasattr(numbers, "__next__"))


# A list has __iter__()
# but does not have __next__().


# ============================================================
# 17. Iterator Has Both Methods
# ============================================================

numbers = [1, 2, 3]

iterator = iter(numbers)

print(hasattr(iterator, "__iter__"))
print(hasattr(iterator, "__next__"))


# An iterator implements both:
#
# __iter__()
# __next__()


# ============================================================
# 18. Iterator Protocol
# ============================================================

# Python's iterator protocol requires:
#
# __iter__()
# __next__()
#
# __iter__() returns the iterator itself.
#
# __next__() returns the next value.
#
# When there are no more values,
# __next__() raises StopIteration.


# ============================================================
# 19. Creating A Custom Iterator
# ============================================================

class CountUp:
    def __init__(self, maximum):
        self.current = 1
        self.maximum = maximum

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.maximum:
            value = self.current
            self.current += 1
            return value

        raise StopIteration


counter = CountUp(5)

print(next(counter))
print(next(counter))
print(next(counter))


# ============================================================
# 20. Using Custom Iterator With for
# ============================================================

counter = CountUp(5)

for number in counter:
    print(number)


# Python automatically calls:
#
# iter(counter)
# next(counter)
#
# until StopIteration is raised.


# ============================================================
# 21. Custom Iterator With Zero
# ============================================================

class CountFromZero:
    def __init__(self, maximum):
        self.current = 0
        self.maximum = maximum

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.maximum:
            value = self.current
            self.current += 1
            return value

        raise StopIteration


counter = CountFromZero(3)

for number in counter:
    print(number)


# ============================================================
# 22. Countdown Iterator
# ============================================================

class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > 0:
            value = self.current
            self.current -= 1
            return value

        raise StopIteration


countdown = Countdown(5)

for number in countdown:
    print(number)


# ============================================================
# 23. Even Number Iterator
# ============================================================

class EvenNumbers:
    def __init__(self, maximum):
        self.current = 0
        self.maximum = maximum

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.maximum:
            value = self.current
            self.current += 2
            return value

        raise StopIteration


numbers = EvenNumbers(10)

for number in numbers:
    print(number)


# ============================================================
# 24. Paginated Data Iterator
# ============================================================

class PageIterator:
    def __init__(self, pages):
        self.pages = pages
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.pages):
            page = self.pages[self.index]
            self.index += 1
            return page

        raise StopIteration


pages = [
    ["user1", "user2"],
    ["user3", "user4"],
    ["user5", "user6"],
]

page_iterator = PageIterator(pages)

for page in page_iterator:
    print("Page:", page)


# ============================================================
# 25. Processing Records
# ============================================================

class RecordIterator:
    def __init__(self, records):
        self.records = records
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.records):
            record = self.records[self.index]
            self.index += 1
            return record

        raise StopIteration


records = [
    {"id": 1, "name": "Ali"},
    {"id": 2, "name": "Sara"},
    {"id": 3, "name": "Reza"},
]

for record in RecordIterator(records):
    print(record)


# ============================================================
# 26. Database-Like Iterator
# ============================================================

class UserIterator:
    def __init__(self, users):
        self.users = users
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.users):
            raise StopIteration

        user = self.users[self.index]
        self.index += 1

        return user


users = [
    {"id": 1, "username": "ali"},
    {"id": 2, "username": "sara"},
    {"id": 3, "username": "mohsen"},
]

user_iterator = UserIterator(users)

for user in user_iterator:
    print(user["username"])


# ============================================================
# 27. Iterator Is Consumed
# ============================================================

numbers = [1, 2, 3]

iterator = iter(numbers)

for number in iterator:
    print(number)

# The iterator is now exhausted.

for number in iterator:
    print(number)


# Nothing is printed the second time.


# ============================================================
# 28. Creating A New Iterator
# ============================================================

numbers = [1, 2, 3]

first_iterator = iter(numbers)
second_iterator = iter(numbers)

print(next(first_iterator))
print(next(first_iterator))

print(next(second_iterator))


# Each iterator has its own state.


# ============================================================
# 29. iter() With A Sentinel
# ============================================================

# iter() can also accept a callable and a sentinel value.

def get_number():
    return 1


iterator = iter(get_number, 1)

# The iterator stops when the callable
# returns the sentinel value.


# ============================================================
# 30. Practical Input Iterator
# ============================================================

def get_command():
    return input("Enter command: ")


# Example:
#
# for command in iter(get_command, "exit"):
#     print("Command:", command)
#
# The loop stops when the user enters "exit".


# ============================================================
# 31. Iterator vs List
# ============================================================

numbers = [1, 2, 3, 4, 5]

iterator = iter(numbers)

print(type(numbers))
print(type(iterator))


# A list stores its elements.
# An iterator keeps track of where it currently is.


# ============================================================
# 32. Why Iterators Matter
# ============================================================

# Iterators are useful when:
#
# - Processing sequences
# - Reading large amounts of data
# - Streaming data
# - Processing database records
# - Handling paginated results
# - Avoiding unnecessary work
# - Building generators


# ============================================================
# 33. Large Data Example
# ============================================================

# A list creates and stores all values.

numbers = [number for number in range(1000)]

print(len(numbers))


# An iterator can produce values one by one.

iterator = iter(range(1000))

print(next(iterator))
print(next(iterator))
print(next(iterator))


# ============================================================
# 34. Backend Example
# ============================================================

class OrderIterator:
    def __init__(self, orders):
        self.orders = orders
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.orders):
            raise StopIteration

        order = self.orders[self.index]
        self.index += 1

        return order


orders = [
    {"id": 101, "total": 250},
    {"id": 102, "total": 500},
    {"id": 103, "total": 150},
]

for order in OrderIterator(orders):
    print(
        f"Order {order['id']}: "
        f"{order['total']}"
    )


# ============================================================
# 35. Iterator With Filtering
# ============================================================

class ActiveUserIterator:
    def __init__(self, users):
        self.users = users
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.users):
            user = self.users[self.index]
            self.index += 1

            if user["active"]:
                return user

        raise StopIteration


users = [
    {"id": 1, "active": True},
    {"id": 2, "active": False},
    {"id": 3, "active": True},
]

for user in ActiveUserIterator(users):
    print(user)


# ============================================================
# 36. Important Difference
# ============================================================

# Iterable:
#
# Can produce an iterator.
#
# Example:
#
# list
# tuple
# string
# dictionary
# set
# range


# Iterator:
#
# Produces values one at a time.
#
# Uses:
#
# __iter__()
# __next__()


# ============================================================
# 37. Key Rules
# ============================================================

# Rule 1:
# Use iter() to obtain an iterator.

# Rule 2:
# Use next() to retrieve the next value.

# Rule 3:
# StopIteration signals the end.

# Rule 4:
# for loops use the iterator protocol internally.

# Rule 5:
# An iterator keeps state.

# Rule 6:
# Iterators can help process data incrementally.

# Rule 7:
# Generators provide a simpler way
# to create many kinds of iterators.