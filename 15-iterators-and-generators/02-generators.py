"""
Python Generators
=================

This file covers:
- Generator functions
- yield
- next()
- Generator state
- Lazy evaluation
- Generator expressions
- yield from
- Sending values to generators
- Closing generators
- Practical backend examples
"""


# ============================================================
# 1. What Is A Generator?
# ============================================================

# A generator is a special type of iterator.
#
# Instead of returning all values at once,
# a generator produces values one at a time.


def numbers():
    yield 1
    yield 2
    yield 3


generator = numbers()

print(generator)


# ============================================================
# 2. Using next()
# ============================================================

generator = numbers()

print(next(generator))
print(next(generator))
print(next(generator))


# The next call raises StopIteration:
#
# print(next(generator))


# ============================================================
# 3. Generator Function
# ============================================================

def count_up():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5


for number in count_up():
    print(number)


# A function containing yield becomes
# a generator function.


# ============================================================
# 4. yield vs return
# ============================================================

def with_return():
    return 10


def with_yield():
    yield 10


print(with_return())

print(with_yield())


# return ends the function.
#
# yield pauses the function and allows it
# to continue later.


# ============================================================
# 5. Generator State
# ============================================================

def sequence():
    print("Start")

    yield 1

    print("Middle")

    yield 2

    print("End")

    yield 3


generator = sequence()

print(next(generator))
print(next(generator))
print(next(generator))


# The function pauses after every yield.


# ============================================================
# 6. Lazy Evaluation
# ============================================================

def generate_numbers():
    print("Generating 1")
    yield 1

    print("Generating 2")
    yield 2

    print("Generating 3")
    yield 3


generator = generate_numbers()

print("Generator created")

print(next(generator))
print(next(generator))
print(next(generator))


# Values are generated only when requested.


# ============================================================
# 7. Generator With range()
# ============================================================

def count_to(maximum):
    number = 1

    while number <= maximum:
        yield number
        number += 1


for number in count_to(5):
    print(number)


# ============================================================
# 8. Infinite Generator
# ============================================================

def infinite_numbers():
    number = 1

    while True:
        yield number
        number += 1


generator = infinite_numbers()

print(next(generator))
print(next(generator))
print(next(generator))


# The generator can continue indefinitely.


# ============================================================
# 9. Limiting An Infinite Generator
# ============================================================

generator = infinite_numbers()

for _ in range(5):
    print(next(generator))


# ============================================================
# 10. Generator With Condition
# ============================================================

def even_numbers(maximum):
    number = 0

    while number <= maximum:
        if number % 2 == 0:
            yield number

        number += 1


for number in even_numbers(10):
    print(number)


# ============================================================
# 11. Generator From A List
# ============================================================

def generate_users(users):
    for user in users:
        yield user


users = [
    {"id": 1, "name": "Ali"},
    {"id": 2, "name": "Sara"},
    {"id": 3, "name": "Mohsen"},
]

for user in generate_users(users):
    print(user)


# ============================================================
# 12. Generator for Active Users
# ============================================================

def active_users(users):
    for user in users:
        if user["active"]:
            yield user


users = [
    {"id": 1, "name": "Ali", "active": True},
    {"id": 2, "name": "Sara", "active": False},
    {"id": 3, "name": "Mohsen", "active": True},
]

for user in active_users(users):
    print(user)


# ============================================================
# 13. Generator for Orders
# ============================================================

def pending_orders(orders):
    for order in orders:
        if order["status"] == "pending":
            yield order


orders = [
    {"id": 101, "status": "completed"},
    {"id": 102, "status": "pending"},
    {"id": 103, "status": "pending"},
]

for order in pending_orders(orders):
    print(order)


# ============================================================
# 14. Generator and Memory
# ============================================================

# A list stores all values in memory.

numbers = [number for number in range(1_000_000)]

print(type(numbers))


# A generator produces values when needed.

numbers_generator = (
    number for number in range(1_000_000)
)

print(type(numbers_generator))


# The generator does not need to create
# all one million values immediately.


# ============================================================
# 15. Generator Expression
# ============================================================

numbers = (
    number * 2
    for number in range(5)
)

for number in numbers:
    print(number)


# Generator expressions are similar to
# list comprehensions but use parentheses.


# ============================================================
# 16. List Comprehension vs Generator
# ============================================================

numbers_list = [
    number * 2
    for number in range(5)
]

numbers_generator = (
    number * 2
    for number in range(5)
)

print(numbers_list)

for number in numbers_generator:
    print(number)


# List comprehension:
# Creates the values immediately.
#
# Generator expression:
# Produces values lazily.


# ============================================================
# 17. Generator With Filtering
# ============================================================

numbers = (
    number
    for number in range(20)
    if number % 2 == 0
)

for number in numbers:
    print(number)


# ============================================================
# 18. Generator for File Reading
# ============================================================

def read_lines(filename):
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            yield line.strip()


# Example:
#
# for line in read_lines("data.txt"):
#     print(line)


# This approach can process a large file
# without loading the entire file into memory.


# ============================================================
# 19. Generator for CSV-Like Records
# ============================================================

import csv


def read_csv_rows(filename):
    with open(
        filename,
        "r",
        encoding="utf-8",
        newline="",
    ) as file:
        reader = csv.DictReader(file)

        for row in reader:
            yield row


# Example:
#
# for row in read_csv_rows("users.csv"):
#     print(row)


# ============================================================
# 20. Generator for Database-Like Records
# ============================================================

def process_records(records):
    for record in records:
        yield record


records = [
    {"id": 1, "name": "Ali"},
    {"id": 2, "name": "Sara"},
    {"id": 3, "name": "Reza"},
]

for record in process_records(records):
    print(record)


# ============================================================
# 21. Transforming Data With A Generator
# ============================================================

def usernames(users):
    for user in users:
        yield user["username"]


users = [
    {"username": "ali"},
    {"username": "sara"},
    {"username": "mohsen"},
]

for username in usernames(users):
    print(username)


# ============================================================
# 22. Filtering and Transforming
# ============================================================

def active_usernames(users):
    for user in users:
        if user["active"]:
            yield user["username"]


users = [
    {"username": "ali", "active": True},
    {"username": "sara", "active": False},
    {"username": "mohsen", "active": True},
]

for username in active_usernames(users):
    print(username)


# ============================================================
# 23. Chaining Generators
# ============================================================

def numbers(maximum):
    for number in range(maximum):
        yield number


def even_numbers(numbers):
    for number in numbers:
        if number % 2 == 0:
            yield number


def squared(numbers):
    for number in numbers:
        yield number ** 2


result = squared(
    even_numbers(
        numbers(10)
    )
)

for number in result:
    print(number)


# Generators can be combined into processing pipelines.


# ============================================================
# 24. yield from
# ============================================================

def first_numbers():
    yield 1
    yield 2
    yield 3


def more_numbers():
    yield 4
    yield 5
    yield 6


def all_numbers():
    yield from first_numbers()
    yield from more_numbers()


for number in all_numbers():
    print(number)


# yield from delegates iteration
# to another iterable or generator.


# ============================================================
# 25. yield from A List
# ============================================================

def generate_items():
    items = ["Python", "Django", "PostgreSQL"]

    yield from items


for item in generate_items():
    print(item)


# ============================================================
# 26. Generator Returning A Value
# ============================================================

def calculate_total(numbers):
    total = 0

    for number in numbers:
        total += number
        yield number

    return total


generator = calculate_total([10, 20, 30])

try:
    while True:
        print(next(generator))

except StopIteration as error:
    print("Total:", error.value)


# The return value of a generator
# becomes the value of StopIteration.


# ============================================================
# 27. Sending Values Into A Generator
# ============================================================

def receiver():
    value = yield
    print("Received:", value)


generator = receiver()

next(generator)

generator.send("Hello")


# send() resumes the generator and
# provides a value to yield.


# ============================================================
# 28. Generator With send()
# ============================================================

def calculator():
    total = 0

    while True:
        value = yield total

        if value is None:
            break

        total += value


generator = calculator()

print(next(generator))
print(generator.send(10))
print(generator.send(20))
print(generator.send(30))

generator.close()


# ============================================================
# 29. Closing A Generator
# ============================================================

def simple_generator():
    try:
        yield 1
        yield 2
        yield 3

    finally:
        print("Generator closed")


generator = simple_generator()

print(next(generator))

generator.close()


# ============================================================
# 30. Generator With try/finally
# ============================================================

def resource_generator():
    try:
        yield "Resource is active"

    finally:
        print("Cleaning up resource")


generator = resource_generator()

print(next(generator))

generator.close()


# ============================================================
# 31. Practical Pagination
# ============================================================

def paginate(items, page_size):
    for start in range(0, len(items), page_size):
        yield items[
            start:start + page_size
        ]


products = [
    "Laptop",
    "Phone",
    "Tablet",
    "Monitor",
    "Keyboard",
    "Mouse",
]

for page in paginate(products, 2):
    print("Page:", page)


# ============================================================
# 32. Batch Processing
# ============================================================

def batches(items, batch_size):
    batch = []

    for item in items:
        batch.append(item)

        if len(batch) == batch_size:
            yield batch
            batch = []

    if batch:
        yield batch


items = list(range(1, 11))

for batch in batches(items, 3):
    print("Batch:", batch)


# This pattern can be useful when processing
# large amounts of records.


# ============================================================
# 33. API-Like Data Stream
# ============================================================

def api_records(records):
    for record in records:
        yield {
            "id": record["id"],
            "name": record["name"],
        }


records = [
    {"id": 1, "name": "Ali", "password": "secret"},
    {"id": 2, "name": "Sara", "password": "secret"},
]

for record in api_records(records):
    print(record)


# The generator can transform internal data
# before sending it somewhere else.


# ============================================================
# 34. Large Number Stream
# ============================================================

def number_stream():
    number = 1

    while True:
        yield number
        number += 1


stream = number_stream()

for _ in range(5):
    print(next(stream))


# ============================================================
# 35. Generator Pipeline
# ============================================================

def read_numbers(numbers):
    for number in numbers:
        yield number


def only_positive(numbers):
    for number in numbers:
        if number > 0:
            yield number


def double(numbers):
    for number in numbers:
        yield number * 2


data = [-5, 2, -1, 4, 6, -3]

pipeline = double(
    only_positive(
        read_numbers(data)
    )
)

for number in pipeline:
    print(number)


# ============================================================
# 36. When To Use Generators
# ============================================================

# Generators are useful when:
#
# - Data is large.
# - Data should be processed incrementally.
# - You do not need all values at once.
# - You are reading large files.
# - You are processing streams.
# - You are creating pipelines.
# - You are working with paginated data.
# - You want lazy evaluation.


# ============================================================
# 37. When Not To Use Generators
# ============================================================

# A normal list can be better when:
#
# - You need random access.
# - You need to iterate multiple times.
# - The dataset is small.
# - You need the complete collection immediately.
# - You need list-specific operations.


# ============================================================
# 38. Important Difference
# ============================================================

# List:
#
# numbers = [1, 2, 3, 4]
#
# Values are stored immediately.


# Generator:
#
# numbers = (number for number in range(4))
#
# Values are produced when requested.


# ============================================================
# 39. Generator vs Custom Iterator
# ============================================================

# Custom iterator:

class Counter:
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


# Generator version:

def counter(maximum):
    current = 1

    while current <= maximum:
        yield current
        current += 1


for number in Counter(3):
    print(number)

for number in counter(3):
    print(number)


# Generators are often much simpler to write.


# ============================================================
# 40. Final Practical Example
# ============================================================

def process_orders(orders):
    for order in orders:
        if order["status"] != "cancelled":
            yield {
                "id": order["id"],
                "total": order["total"],
            }


orders = [
    {
        "id": 101,
        "status": "completed",
        "total": 250,
    },
    {
        "id": 102,
        "status": "cancelled",
        "total": 150,
    },
    {
        "id": 103,
        "status": "pending",
        "total": 500,
    },
]

for order in process_orders(orders):
    print(order)


# ============================================================
# 41. Key Rules
# ============================================================

# Rule 1:
# yield turns a function into a generator.

# Rule 2:
# Generators are iterators.

# Rule 3:
# Generators produce values lazily.

# Rule 4:
# next() requests the next value.

# Rule 5:
# StopIteration signals the end.

# Rule 6:
# yield from delegates iteration.

# Rule 7:
# Generator expressions use parentheses.

# Rule 8:
# Generators are useful for large or streaming data.

# Rule 9:
# Generators can be chained into processing pipelines.

# Rule 10:
# A generator is consumed as you iterate over it.