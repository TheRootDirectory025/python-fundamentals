"""
Python Fundamentals
03 - Conditionals
Topic: Match-Case

This file covers:
- match statement
- case statement
- Matching exact values
- Multiple cases
- Default case (_)
- Matching strings
- Matching numbers
- Combining match-case with conditions
- Real-world examples
"""


# ============================================================
# 1. Basic Match-Case
# ============================================================

day = 1

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")


# ============================================================
# 2. Default Case
# ============================================================

day = 10

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case _:
        print("Invalid day")


# ============================================================
# 3. Matching Strings
# ============================================================

role = "admin"

match role:
    case "admin":
        print("Administrator")
    case "user":
        print("Regular user")
    case "guest":
        print("Guest user")
    case _:
        print("Unknown role")


# ============================================================
# 4. Multiple Values in One Case
# ============================================================

day = "Saturday"

match day:
    case "Saturday" | "Sunday":
        print("Weekend")
    case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
        print("Weekday")
    case _:
        print("Invalid day")


# ============================================================
# 5. Matching Numbers
# ============================================================

command = 2

match command:
    case 1:
        print("Start")
    case 2:
        print("Pause")
    case 3:
        print("Stop")
    case _:
        print("Unknown command")


# ============================================================
# 6. Match-Case with Conditions
# ============================================================

score = 17

match score:
    case score if score >= 18:
        print("Excellent")
    case score if score >= 10:
        print("Passed")
    case _:
        print("Failed")


# ============================================================
# 7. Match-Case with User Input
# ============================================================

choice = "yes"

match choice:
    case "yes":
        print("User selected Yes")
    case "no":
        print("User selected No")
    case _:
        print("Invalid choice")


# ============================================================
# 8. Comparing Match-Case with if-elif
# ============================================================

"""
For simple value matching, match-case can be cleaner than
a long chain of if-elif statements.

Example:

if role == "admin":
    ...
elif role == "user":
    ...
else:
    ...

Can be written as:

match role:
    case "admin":
        ...
    case "user":
        ...
    case _:
        ...
"""


# ============================================================
# 9. Real-World Example: HTTP Status Code
# ============================================================

status_code = 404

match status_code:
    case 200:
        message = "Success"
    case 201:
        message = "Created"
    case 400:
        message = "Bad Request"
    case 401:
        message = "Unauthorized"
    case 403:
        message = "Forbidden"
    case 404:
        message = "Not Found"
    case 500:
        message = "Internal Server Error"
    case _:
        message = "Unknown Status Code"

print("Status:", message)


# ============================================================
# 10. Real-World Example: Simple Calculator
# ============================================================

operator = "+"
a = 10
b = 5

match operator:
    case "+":
        result = a + b
    case "-":
        result = a - b
    case "*":
        result = a * b
    case "/":
        result = a / b
    case _:
        result = None
        print("Invalid operator")

print("Result:", result)


# ============================================================
# 11. Real-World Example: User Role
# ============================================================

user_role = "editor"

match user_role:
    case "admin":
        permission = "Full access"
    case "editor":
        permission = "Can edit content"
    case "viewer":
        permission = "Read-only access"
    case _:
        permission = "No access"

print("Permission:", permission)

