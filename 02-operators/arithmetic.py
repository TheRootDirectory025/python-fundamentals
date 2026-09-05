"""
Python Fundamentals
02 - Operators
Topic: Arithmetic Operators

This file covers:
- Addition
- Subtraction
- Multiplication
- Division
- Floor division
- Modulus
- Exponentiation
- Operator precedence
- Arithmetic with variables
- Real-world examples
"""


# ============================================================
# 1. Addition
# ============================================================

a = 10
b = 3

result = a + b

print("Addition:", result)


# ============================================================
# 2. Subtraction
# ============================================================

result = a - b

print("Subtraction:", result)


# ============================================================
# 3. Multiplication
# ============================================================

result = a * b

print("Multiplication:", result)


# ============================================================
# 4. Division
# ============================================================

# Division always returns a float in Python.

result = a / b

print("Division:", result)


# ============================================================
# 5. Floor Division
# ============================================================

# Floor division returns the integer part of the division.

result = a // b

print("Floor division:", result)


# ============================================================
# 6. Modulus
# ============================================================

# Modulus returns the remainder of a division.

result = a % b

print("Remainder:", result)


# Example:
# 10 divided by 3 has a remainder of 1.

print("10 % 3 =", 10 % 3)


# ============================================================
# 7. Exponentiation
# ============================================================

# The ** operator is used to raise a number to a power.

result = a ** b

print("Exponentiation:", result)

# 10 ** 3 = 1000


# ============================================================
# 8. Arithmetic Operators Summary
# ============================================================

x = 20
y = 6

print("x + y =", x + y)
print("x - y =", x - y)
print("x * y =", x * y)
print("x / y =", x / y)
print("x // y =", x // y)
print("x % y =", x % y)
print("x ** y =", x ** y)


# ============================================================
# 9. Operator Precedence
# ============================================================

# Python follows a specific order when evaluating expressions.
#
# 1. Parentheses
# 2. Exponentiation
# 3. Multiplication, division, floor division, modulus
# 4. Addition and subtraction

result = 2 + 3 * 4

print("Without parentheses:", result)

result = (2 + 3) * 4

print("With parentheses:", result)


# Example with multiple operators

result = 10 + 5 * 2 - 3

print("Mixed arithmetic:", result)


# ============================================================
# 10. Arithmetic with Variables
# ============================================================

price = 100
quantity = 3

total_price = price * quantity

print("Total price:", total_price)


# ============================================================
# 11. Incrementing and Decrementing
# ============================================================

score = 10

score = score + 5

print("Score after adding 5:", score)

score = score - 2

print("Score after subtracting 2:", score)


# ============================================================
# 12. Arithmetic Assignment Operators
# ============================================================

number = 10

number += 5
print("After += 5:", number)

number -= 3
print("After -= 3:", number)

number *= 2
print("After *= 2:", number)

number /= 4
print("After /= 4:", number)


# ============================================================
# 13. Checking Even and Odd Numbers
# ============================================================

number = 17

# If the remainder is 0, the number is even.
# Otherwise, it is odd.

print("Remainder:", number % 2)


# ============================================================
# 14. Real-World Example: Shopping Calculator
# ============================================================

product_price = 25.50
quantity = 4

subtotal = product_price * quantity
discount = 10

final_price = subtotal - discount

print("Subtotal:", subtotal)
print("Discount:", discount)
print("Final price:", final_price)


# ============================================================
# 15. Real-World Example: Average Score
# ============================================================

score_1 = 18
score_2 = 16
score_3 = 20

average = (score_1 + score_2 + score_3) / 3

print("Average score:", average)


