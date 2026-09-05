"""
Python Fundamentals
05 - Data Structures
Topic: Tuples

This file covers:
- Creating tuples
- Accessing tuple elements
- Indexing
- Negative indexing
- Slicing
- Tuple immutability
- Tuple methods
- Tuple unpacking
- Nested tuples
- Looping through tuples
- Converting between lists and tuples
- Real-world examples
"""


# ============================================================
# 1. Creating a Tuple
# ============================================================

coordinates = (10, 20)

print(coordinates)


# A tuple can contain different data types.

person = ("Ali", 22, "Computer Engineering")

print(person)


# A tuple can also contain duplicate values.

numbers = (1, 2, 2, 3, 4)

print(numbers)


# ============================================================
# 2. Creating a Single-Element Tuple
# ============================================================

# A comma is required for a single-element tuple.

single_item = ("Python",)

print(single_item)
print(type(single_item))


# Without the comma, this is just a string.

not_a_tuple = ("Python")

print(type(not_a_tuple))


# ============================================================
# 3. Accessing Tuple Elements
# ============================================================

languages = ("Python", "Kotlin", "Java")

print(languages[0])
print(languages[1])
print(languages[2])


# ============================================================
# 4. Negative Indexing
# ============================================================

print(languages[-1])
print(languages[-2])
print(languages[-3])


# ============================================================
# 5. Tuple Slicing
# ============================================================

numbers = (0, 1, 2, 3, 4, 5)

print(numbers[1:4])
print(numbers[:3])
print(numbers[3:])
print(numbers[:])
print(numbers[::2])


# ============================================================
# 6. Tuple Immutability
# ============================================================

"""
Tuples are immutable.

Once a tuple is created, its elements cannot be changed.

Example:

numbers = (10, 20, 30)

numbers[0] = 100

This would raise a TypeError.
"""


# ============================================================
# 7. Tuple Length
# ============================================================

fruits = ("apple", "banana", "orange")

print("Number of fruits:", len(fruits))


# ============================================================
# 8. Checking if an Element Exists
# ============================================================

fruits = ("apple", "banana", "orange")

print("apple" in fruits)
print("mango" in fruits)


# ============================================================
# 9. count()
# ============================================================

numbers = (1, 2, 2, 3, 2, 4)

print("Number of 2s:", numbers.count(2))


# ============================================================
# 10. index()
# ============================================================

fruits = ("apple", "banana", "orange")

print("Banana index:", fruits.index("banana"))


# ============================================================
# 11. Tuple Unpacking
# ============================================================

person = ("Ali", 22, "Computer Engineering")

name, age, major = person

print("Name:", name)
print("Age:", age)
print("Major:", major)


# ============================================================
# 12. Extended Unpacking
# ============================================================

numbers = (1, 2, 3, 4, 5)

first, *middle, last = numbers

print("First:", first)
print("Middle:", middle)
print("Last:", last)


# ============================================================
# 13. Nested Tuples
# ============================================================

students = (
    ("Ali", 18),
    ("Sara", 19),
    ("Reza", 16)
)

print(students[0])
print(students[1][0])
print(students[2][1])


# ============================================================
# 14. Looping Through a Tuple
# ============================================================

languages = ("Python", "Kotlin", "Java")

for language in languages:
    print(language)


# ============================================================
# 15. Looping with enumerate()
# ============================================================

languages = ("Python", "Kotlin", "Java")

for index, language in enumerate(languages, start=1):
    print(index, language)


# ============================================================
# 16. Converting List to Tuple
# ============================================================

languages_list = ["Python", "Kotlin", "Java"]

languages_tuple = tuple(languages_list)

print(languages_tuple)
print(type(languages_tuple))


# ============================================================
# 17. Converting Tuple to List
# ============================================================

languages_tuple = ("Python", "Kotlin", "Java")

languages_list = list(languages_tuple)

languages_list.append("C++")

print(languages_list)


# ============================================================
# 18. Tuple Concatenation
# ============================================================

first = (1, 2, 3)
second = (4, 5, 6)

combined = first + second

print(combined)


# ============================================================
# 19. Tuple Repetition
# ============================================================

numbers = (1, 2)

repeated = numbers * 3

print(repeated)


# ============================================================
# 20. Built-in Functions with Tuples
# ============================================================

numbers = (10, 20, 5, 40, 15)

print("Length:", len(numbers))
print("Minimum:", min(numbers))
print("Maximum:", max(numbers))
print("Sum:", sum(numbers))


# ============================================================
# 21. Real-World Example: Coordinates
# ============================================================

location = (35.6892, 51.3890)

latitude, longitude = location

print("Latitude:", latitude)
print("Longitude:", longitude)


# ============================================================
# 22. Real-World Example: User Information
# ============================================================

user = ("Mohsen", 24, "Backend Developer")

name, age, job = user

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Job: {job}")


# ============================================================
# 23. Real-World Example: Database Record
# ============================================================

user_record = (101, "Ali", "ali@example.com")

user_id, username, email = user_record

print("User ID:", user_id)
print("Username:", username)
print("Email:", email)


# ============================================================
# Important Notes
# ============================================================

"""
Tuples are:

- Ordered
- Immutable
- Indexed
- Allow duplicate values
- Can contain different data types

Common tuple operations:

len()
count()
index()
in
not in
slicing
unpacking

Use tuples when the collection should not be modified
after creation.
"""