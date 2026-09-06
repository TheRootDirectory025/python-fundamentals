"""
Python Fundamentals
05 - Data Structures
Topic: Sets

This file covers:
- Creating sets
- Set properties
- Adding elements
- Removing elements
- Checking membership
- Set operations
- Union
- Intersection
- Difference
- Symmetric difference
- Subsets and supersets
- Looping through sets
- Converting between lists and sets
- Removing duplicates
- Real-world examples
"""


# ============================================================
# 1. Creating a Set
# ============================================================

numbers = {1, 2, 3, 4, 5}

print(numbers)


# Sets automatically remove duplicate values.

numbers = {1, 2, 2, 3, 3, 4}

print(numbers)


# ============================================================
# 2. Set Properties
# ============================================================

"""
Sets are:

- Unordered
- Mutable
- Do not allow duplicate values
- Not indexed
- Useful for membership testing and set operations
"""


# ============================================================
# 3. Creating an Empty Set
# ============================================================

# {} creates an empty dictionary, not a set.

empty_set = set()

print(empty_set)
print(type(empty_set))


# ============================================================
# 4. Adding Elements
# ============================================================

languages = {"Python", "Kotlin"}

languages.add("Java")

print(languages)


# ============================================================
# 5. Adding Multiple Elements
# ============================================================

languages = {"Python", "Kotlin"}

languages.update(["Java", "C++"])

print(languages)


# ============================================================
# 6. Removing Elements with remove()
# ============================================================

languages = {"Python", "Kotlin", "Java"}

languages.remove("Java")

print(languages)


# remove() raises an error if the element does not exist.


# ============================================================
# 7. Removing Elements with discard()
# ============================================================

languages = {"Python", "Kotlin", "Java"}

languages.discard("Java")
languages.discard("C++")

print(languages)


# discard() does not raise an error if the element is missing.


# ============================================================
# 8. Removing an Arbitrary Element with pop()
# ============================================================

numbers = {10, 20, 30, 40}

removed_number = numbers.pop()

print("Removed:", removed_number)
print("Remaining:", numbers)


# ============================================================
# 9. Clearing a Set
# ============================================================

numbers = {1, 2, 3, 4}

numbers.clear()

print(numbers)


# ============================================================
# 10. Checking Membership
# ============================================================

languages = {"Python", "Kotlin", "Java"}

print("Python" in languages)
print("C++" in languages)


# ============================================================
# 11. Set Length
# ============================================================

numbers = {10, 20, 30, 40}

print("Number of elements:", len(numbers))


# ============================================================
# 12. Looping Through a Set
# ============================================================

languages = {"Python", "Kotlin", "Java"}

for language in languages:
    print(language)


# ============================================================
# 13. Union
# ============================================================

"""
Union combines all unique elements from two sets.

Operator: |
Method: union()
"""

backend_languages = {"Python", "Java", "Go"}
mobile_languages = {"Kotlin", "Swift", "Java"}

all_languages = backend_languages | mobile_languages

print("All languages:", all_languages)


# Using union()

all_languages = backend_languages.union(mobile_languages)

print("All languages:", all_languages)


# ============================================================
# 14. Intersection
# ============================================================

"""
Intersection returns elements that exist in both sets.

Operator: &
Method: intersection()
"""

common_languages = backend_languages & mobile_languages

print("Common languages:", common_languages)


# ============================================================
# 15. Difference
# ============================================================

"""
Difference returns elements that exist in the first set
but not in the second set.

Operator: -
Method: difference()
"""

only_backend = backend_languages - mobile_languages

print("Backend only:", only_backend)


# ============================================================
# 16. Symmetric Difference
# ============================================================

"""
Symmetric difference returns elements that exist in either
set, but not in both.

Operator: ^
Method: symmetric_difference()
"""

different_languages = backend_languages ^ mobile_languages

print("Different languages:", different_languages)


# ============================================================
# 17. Subset
# ============================================================

small_set = {1, 2}
large_set = {1, 2, 3, 4, 5}

print("Is subset:", small_set.issubset(large_set))


# ============================================================
# 18. Superset
# ============================================================

print("Is superset:", large_set.issuperset(small_set))


# ============================================================
# 19. Disjoint Sets
# ============================================================

first = {1, 2, 3}
second = {4, 5, 6}

print("Are disjoint:", first.isdisjoint(second))


# ============================================================
# 20. Converting a List to a Set
# ============================================================

numbers = [1, 2, 2, 3, 3, 4, 4, 5]

unique_numbers = set(numbers)

print("Original:", numbers)
print("Unique:", unique_numbers)


# ============================================================
# 21. Removing Duplicates from a List
# ============================================================

names = ["Ali", "Sara", "Ali", "Reza", "Sara"]

unique_names = list(set(names))

print("Original:", names)
print("Unique:", unique_names)


# Note:
# Converting a set back to a list does not preserve the
# original order.


# ============================================================
# 22. Set Operations with Numbers
# ============================================================

even_numbers = {2, 4, 6, 8, 10}
numbers = {1, 2, 3, 4, 5, 6}

common_numbers = even_numbers & numbers
only_even = even_numbers - numbers
all_numbers = even_numbers | numbers

print("Common:", common_numbers)
print("Only even:", only_even)
print("All:", all_numbers)


# ============================================================
# 23. Real-World Example: Common Skills
# ============================================================

developer_1_skills = {
    "Python",
    "Django",
    "SQL",
    "Git"
}

developer_2_skills = {
    "Python",
    "FastAPI",
    "SQL",
    "Docker"
}

common_skills = developer_1_skills & developer_2_skills

print("Common skills:", common_skills)


# ============================================================
# 24. Real-World Example: Course Registration
# ============================================================

all_students = {"Ali", "Sara", "Reza", "Nima", "Maryam"}

python_students = {"Ali", "Sara", "Nima"}
database_students = {"Sara", "Reza", "Nima"}

students_in_both_courses = python_students & database_students

print("Students in both courses:", students_in_both_courses)


# ============================================================
# 25. Real-World Example: Permission Checking
# ============================================================

required_permissions = {
    "read",
    "write"
}

user_permissions = {
    "read",
    "write",
    "delete"
}

has_required_permissions = required_permissions.issubset(user_permissions)

print("Has required permissions:", has_required_permissions)


# ============================================================
# Important Notes
# ============================================================

"""
Important set methods:

add()
update()
remove()
discard()
pop()
clear()

Set operations:

|   Union
&   Intersection
-   Difference
^   Symmetric difference

Relationship methods:

issubset()
issuperset()
isdisjoint()

Use sets when:
- You need unique values.
- You frequently check whether an item exists.
- You need mathematical set operations.
"""