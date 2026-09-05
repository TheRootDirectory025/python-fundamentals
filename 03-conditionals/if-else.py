"""
Python Fundamentals
03 - Conditionals
Topic: If, Elif, and Else

This file covers:
- if statements
- else statements
- elif statements
- Comparison in conditions
- Logical operators in conditions
- Nested conditions
- Multiple conditions
- Conditional expressions
- Real-world examples
"""


# ============================================================
# 1. Basic if Statement
# ============================================================

age = 20

if age >= 18:
    print("You are an adult.")


# ============================================================
# 2. The else Statement
# ============================================================

age = 16

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")


# ============================================================
# 3. The elif Statement
# ============================================================

score = 17

if score >= 18:
    print("Excellent")
elif score >= 10:
    print("Passed")
else:
    print("Failed")


# ============================================================
# 4. Multiple Conditions
# ============================================================

temperature = 30

if temperature > 35:
    print("It is very hot.")
elif temperature >= 25:
    print("It is warm.")
elif temperature >= 15:
    print("The weather is mild.")
else:
    print("It is cold.")


# ============================================================
# 5. Using Logical Operators in Conditions
# ============================================================

age = 22
has_id = True

if age >= 18 and has_id:
    print("Access granted.")
else:
    print("Access denied.")


# ============================================================
# 6. Using "or" in Conditions
# ============================================================

is_weekend = False
is_holiday = True

if is_weekend or is_holiday:
    print("You do not have to work.")
else:
    print("It is a working day.")


# ============================================================
# 7. Using "not" in Conditions
# ============================================================

is_banned = False

if not is_banned:
    print("User can access the system.")
else:
    print("User is banned.")


# ============================================================
# 8. Nested if Statements
# ============================================================

age = 25
has_ticket = True

if age >= 18:
    print("Age requirement passed.")

    if has_ticket:
        print("You can enter.")
    else:
        print("You need a ticket.")
else:
    print("You are not old enough.")


# ============================================================
# 9. Checking Ranges
# ============================================================

score = 15

if 0 <= score <= 20:
    print("Valid score.")
else:
    print("Invalid score.")


# ============================================================
# 10. Multiple elif Conditions
# ============================================================

score = 14

if score >= 18:
    grade = "A"
elif score >= 16:
    grade = "B"
elif score >= 14:
    grade = "C"
elif score >= 10:
    grade = "D"
else:
    grade = "F"

print("Grade:", grade)


# ============================================================
# 11. String Conditions
# ============================================================

role = "admin"

if role == "admin":
    print("Welcome, administrator.")
elif role == "user":
    print("Welcome, user.")
else:
    print("Unknown role.")


# ============================================================
# 12. Checking Empty Strings
# ============================================================

username = ""

if username:
    print("Username is provided.")
else:
    print("Username is empty.")


# ============================================================
# 13. Conditional Expression
# ============================================================

age = 20

status = "Adult" if age >= 18 else "Minor"

print("Status:", status)


# ============================================================
# 14. Real-World Example: Login System
# ============================================================

username = "admin"
password = "1234"

if username == "admin" and password == "1234":
    print("Login successful.")
else:
    print("Invalid username or password.")


# ============================================================
# 15. Real-World Example: Exam Result
# ============================================================

score = 16
attendance = 85

if score >= 10 and attendance >= 70:
    print("Student passed the course.")
else:
    print("Student failed the course.")


# ============================================================
# 16. Real-World Example: Shipping Cost
# ============================================================

order_total = 120

if order_total >= 100:
    shipping_cost = 0
elif order_total >= 50:
    shipping_cost = 5
else:
    shipping_cost = 10

print("Shipping cost:", shipping_cost)

