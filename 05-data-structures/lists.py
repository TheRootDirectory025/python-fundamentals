"""
Python Fundamentals
05 - Data Structures
Topic: Lists

This file covers:
- Creating lists
- Accessing elements
- Indexing
- Negative indexing
- Slicing
- Updating elements
- Adding elements
- Removing elements
- List length
- Searching in lists
- Sorting and reversing
- Copying lists
- Nested lists
- Looping through lists
- Real-world examples
"""


# ============================================================
# 1. Creating a List
# ============================================================

fruits = ["apple", "banana", "orange"]

print(fruits)


# A list can contain different data types.

mixed_list = ["Python", 25, True, 3.14]

print(mixed_list)


# ============================================================
# 2. Accessing List Elements
# ============================================================

fruits = ["apple", "banana", "orange"]

print(fruits[0])
print(fruits[1])
print(fruits[2])


# ============================================================
# 3. Negative Indexing
# ============================================================

# Negative indexes start from the end of the list.

print(fruits[-1])
print(fruits[-2])
print(fruits[-3])


# ============================================================
# 4. List Slicing
# ============================================================

numbers = [0, 1, 2, 3, 4, 5]

print(numbers[1:4])
print(numbers[:3])
print(numbers[3:])
print(numbers[:])
print(numbers[::2])


# ============================================================
# 5. Updating List Elements
# ============================================================

fruits = ["apple", "banana", "orange"]

fruits[1] = "mango"

print(fruits)


# ============================================================
# 6. Adding Elements with append()
# ============================================================

fruits = ["apple", "banana"]

fruits.append("orange")

print(fruits)


# ============================================================
# 7. Adding Elements with insert()
# ============================================================

fruits = ["apple", "orange"]

fruits.insert(1, "banana")

print(fruits)


# ============================================================
# 8. Adding Multiple Elements with extend()
# ============================================================

fruits = ["apple", "banana"]

fruits.extend(["orange", "mango"])

print(fruits)


# ============================================================
# 9. Removing Elements with remove()
# ============================================================

fruits = ["apple", "banana", "orange"]

fruits.remove("banana")

print(fruits)


# ============================================================
# 10. Removing Elements with pop()
# ============================================================

numbers = [10, 20, 30, 40]

removed_number = numbers.pop()

print("Removed:", removed_number)
print("List:", numbers)


# Remove an element by index.

numbers = [10, 20, 30, 40]

removed_number = numbers.pop(1)

print("Removed:", removed_number)
print("List:", numbers)


# ============================================================
# 11. Removing Elements with del
# ============================================================

numbers = [10, 20, 30, 40]

del numbers[1]

print(numbers)


# ============================================================
# 12. Clearing a List
# ============================================================

numbers = [1, 2, 3, 4, 5]

numbers.clear()

print(numbers)


# ============================================================
# 13. Finding the Length
# ============================================================

fruits = ["apple", "banana", "orange"]

print("Number of fruits:", len(fruits))


# ============================================================
# 14. Checking if an Element Exists
# ============================================================

fruits = ["apple", "banana", "orange"]

print("apple" in fruits)
print("mango" in fruits)


# ============================================================
# 15. Finding an Element's Position
# ============================================================

fruits = ["apple", "banana", "orange"]

index = fruits.index("banana")

print("Banana index:", index)


# ============================================================
# 16. Counting Elements
# ============================================================

numbers = [1, 2, 2, 3, 2, 4]

count = numbers.count(2)

print("Number of 2s:", count)


# ============================================================
# 17. Sorting a List
# ============================================================

numbers = [5, 2, 8, 1, 3]

numbers.sort()

print("Ascending:", numbers)


# Sort in descending order.

numbers.sort(reverse=True)

print("Descending:", numbers)


# ============================================================
# 18. sorted() Function
# ============================================================

numbers = [5, 2, 8, 1, 3]

sorted_numbers = sorted(numbers)

print("Original:", numbers)
print("Sorted:", sorted_numbers)


# sorted() creates a new list.


# ============================================================
# 19. Reversing a List
# ============================================================

numbers = [1, 2, 3, 4, 5]

numbers.reverse()

print(numbers)


# ============================================================
# 20. Copying a List
# ============================================================

original = [1, 2, 3]

copied = original.copy()

copied.append(4)

print("Original:", original)
print("Copied:", copied)


# ============================================================
# 21. Looping Through a List
# ============================================================

languages = ["Python", "Kotlin", "Java"]

for language in languages:
    print(language)


# ============================================================
# 22. List with Conditions
# ============================================================

numbers = [1, 2, 3, 4, 5, 6]

for number in numbers:
    if number % 2 == 0:
        print("Even:", number)


# ============================================================
# 23. Nested Lists
# ============================================================

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[0])
print(matrix[1][2])


# ============================================================
# 24. List Unpacking
# ============================================================

person = ["Ali", 22, "Computer Engineering"]

name, age, major = person

print("Name:", name)
print("Age:", age)
print("Major:", major)


# ============================================================
# 25. Useful Built-in Functions
# ============================================================

numbers = [10, 20, 5, 40, 15]

print("Length:", len(numbers))
print("Minimum:", min(numbers))
print("Maximum:", max(numbers))
print("Sum:", sum(numbers))


# ============================================================
# 26. Real-World Example: Shopping Cart
# ============================================================

cart = ["Keyboard", "Mouse", "Headset"]

cart.append("Mouse Pad")

print("Cart:", cart)

cart.remove("Mouse")

print("Updated cart:", cart)


# ============================================================
# 27. Real-World Example: Student Scores
# ============================================================

scores = [18, 15, 20, 12, 17]

average = sum(scores) / len(scores)

print("Scores:", scores)
print("Average:", average)


# ============================================================
# 28. Real-World Example: Filtering Data
# ============================================================

ages = [12, 18, 25, 16, 30, 14]

adults = []

for age in ages:
    if age >= 18:
        adults.append(age)

print("Adult ages:", adults)


# ============================================================
# Important Notes
# ============================================================

"""
Lists are:

- Ordered
- Mutable
- Indexed
- Allow duplicate values
- Can contain different data types

Common methods:

append()
insert()
extend()
remove()
pop()
clear()
index()
count()
sort()
reverse()
copy()
"""