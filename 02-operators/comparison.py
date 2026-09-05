"""
Python Fundamentals
02 - Operators
Topic: Comparison Operators

This file covers:
- Equal to
- Not equal to
- Greater than
- Less than
- Greater than or equal to
- Less than or equal to
- Comparing variables
- Comparing strings
- Comparing multiple values
- Chained comparisons
- Real-world examples
"""


# ============================================================
# 1. Equal To
# ============================================================

a = 10
b = 10

print("a == b:", a == b)


# ============================================================
# 2. Not Equal To
# ============================================================

a = 10
b = 5

print("a != b:", a != b)


# ============================================================
# 3. Greater Than
# ============================================================

print("a > b:", a > b)


# ============================================================
# 4. Less Than
# ============================================================

print("a < b:", a < b)


# ============================================================
# 5. Greater Than or Equal To
# ============================================================

age = 18

print("age >= 18:", age >= 18)


# ============================================================
# 6. Less Than or Equal To
# ============================================================

score = 20

print("score <= 20:", score <= 20)


# ============================================================
# 7. Comparison Operators Summary
# ============================================================

x = 15
y = 10

print("x == y:", x == y)
print("x != y:", x != y)
print("x > y:", x > y)
print("x < y:", x < y)
print("x >= y:", x >= y)
print("x <= y:", x <= y)


# ============================================================
# 8. Comparing Variables
# ============================================================

user_age = 22
minimum_age = 18

is_old_enough = user_age >= minimum_age

print("Old enough:", is_old_enough)


# ============================================================
# 9. Comparing Strings
# ============================================================

first_name = "Ali"
second_name = "Reza"

print("Names are equal:", first_name == second_name)
print("Names are different:", first_name != second_name)


# String comparisons are case-sensitive.

username_1 = "Mohsen"
username_2 = "mohsen"

print("Usernames are equal:", username_1 == username_2)


# ============================================================
# 10. Comparing Numbers
# ============================================================

temperature = 35

print("Temperature is above 30:", temperature > 30)
print("Temperature is below or equal to 40:", temperature <= 40)


# ============================================================
# 11. Chained Comparisons
# ============================================================

age = 25

# This checks whether age is between 18 and 30.

is_in_range = 18 <= age <= 30

print("Age is between 18 and 30:", is_in_range)


# Another example

score = 17

is_valid_score = 0 <= score <= 20

print("Valid score:", is_valid_score)


# ============================================================
# 12. Comparing Multiple Values
# ============================================================

a = 10
b = 20
c = 30

print("a < b:", a < b)
print("b < c:", b < c)

print("a < b < c:", a < b < c)


# ============================================================
# 13. Comparison Results are Boolean
# ============================================================

number = 50

result = number > 25

print("Result:", result)
print("Result type:", type(result))


# ============================================================
# 14. Real-World Example: Exam Result
# ============================================================

student_score = 16
passing_score = 10

passed = student_score >= passing_score

print("Student passed:", passed)


# ============================================================
# 15. Real-World Example: Product Price
# ============================================================

product_price = 850
budget = 1000

within_budget = product_price <= budget

print("Product is within budget:", within_budget)


# ============================================================
# Mini Challenge
# ============================================================
