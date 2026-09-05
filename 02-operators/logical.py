"""
Python Fundamentals
02 - Operators
Topic: Logical Operators

This file covers:
- and operator
- or operator
- not operator
- Combining comparison operators
- Boolean expressions
- Operator precedence
- Real-world examples
"""


# ============================================================
# 1. The "and" Operator
# ============================================================

# "and" returns True only when both conditions are True.

age = 25
has_id = True

can_enter = age >= 18 and has_id

print("Can enter:", can_enter)


# Example

temperature = 25
is_sunny = True

good_weather = temperature > 20 and is_sunny

print("Good weather:", good_weather)


# ============================================================
# 2. The "or" Operator
# ============================================================

# "or" returns True when at least one condition is True.

has_ticket = True
is_vip = False

can_enter = has_ticket or is_vip

print("Can enter:", can_enter)


# Example

is_weekend = False
is_holiday = True

day_off = is_weekend or is_holiday

print("Day off:", day_off)


# ============================================================
# 3. The "not" Operator
# ============================================================

# "not" reverses a Boolean value.

is_logged_in = True

print("Is logged in:", is_logged_in)
print("Is not logged in:", not is_logged_in)


# Example

is_blocked = False

can_access = not is_blocked

print("Can access:", can_access)


# ============================================================
# 4. Combining Comparison and Logical Operators
# ============================================================

age = 22
has_permission = True

can_access = age >= 18 and has_permission

print("Can access:", can_access)


# Another example

score = 17

passed_exam = score >= 10
excellent_score = score >= 18

print("Passed exam:", passed_exam)
print("Excellent score:", excellent_score)


# ============================================================
# 5. Using Multiple Logical Operators
# ============================================================

age = 25
has_id = True
has_ticket = True

can_enter = age >= 18 and has_id and has_ticket

print("Can enter:", can_enter)


# ============================================================
# 6. Using "and" with Different Conditions
# ============================================================

username = "admin"
password_correct = True

is_admin = username == "admin" and password_correct

print("Is admin:", is_admin)


# ============================================================
# 7. Using "or" with Different Conditions
# ============================================================

payment_method = "card"

can_pay = payment_method == "card" or payment_method == "cash"

print("Can pay:", can_pay)


# ============================================================
# 8. Using "not" with a Condition
# ============================================================

age = 16

is_adult = age >= 18
is_minor = not is_adult

print("Is adult:", is_adult)
print("Is minor:", is_minor)


# ============================================================
# 9. Combining "and", "or", and "not"
# ============================================================

age = 25
has_ticket = True
is_banned = False

can_enter = age >= 18 and has_ticket and not is_banned

print("Can enter:", can_enter)


# ============================================================
# 10. Logical Operator Precedence
# ============================================================

# Python evaluates "not" before "and",
# and "and" before "or".

result = True or False and False

print("Result:", result)


# Parentheses can make the intended logic clearer.

result = (True or False) and False

print("Result with parentheses:", result)


# ============================================================
# 11. Truth Table Examples
# ============================================================

# AND

print("True and True:", True and True)
print("True and False:", True and False)
print("False and True:", False and True)
print("False and False:", False and False)


# OR

print("True or True:", True or True)
print("True or False:", True or False)
print("False or True:", False or True)
print("False or False:", False or False)


# NOT

print("not True:", not True)
print("not False:", not False)


# ============================================================
# 12. Real-World Example: Login System
# ============================================================

username = "admin"
password = "1234"

correct_username = username == "admin"
correct_password = password == "1234"

login_successful = correct_username and correct_password

print("Login successful:", login_successful)


# ============================================================
# 13. Real-World Example: Shopping Discount
# ============================================================

total_price = 150
is_member = True

eligible_for_discount = total_price >= 100 and is_member

print("Eligible for discount:", eligible_for_discount)


# ============================================================
# 14. Real-World Example: Access Control
# ============================================================

age = 20
is_banned = False
has_permission = True

can_access = age >= 18 and not is_banned and has_permission

print("Access granted:", can_access)


# ============================================================
# Mini Challenge
# ============================================================
