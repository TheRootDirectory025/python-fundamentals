"""
Python Fundamentals
04 - Loops
Topic: Loop Control Statements

This file covers:
- break
- continue
- pass
- break with for loops
- break with while loops
- continue with for loops
- continue with while loops
- Nested loops
- Real-world examples
"""


# ============================================================
# 1. break with a For Loop
# ============================================================

# break immediately stops the loop.

for number in range(1, 11):
    if number == 6:
        break

    print(number)


# ============================================================
# 2. break with a While Loop
# ============================================================

counter = 1

while counter <= 10:
    if counter == 6:
        break

    print(counter)
    counter += 1


# ============================================================
# 3. continue with a For Loop
# ============================================================

# continue skips the current iteration
# and moves to the next iteration.

for number in range(1, 11):
    if number % 2 == 0:
        continue

    print("Odd number:", number)


# ============================================================
# 4. continue with a While Loop
# ============================================================

counter = 0

while counter < 10:
    counter += 1

    if counter % 2 == 0:
        continue

    print("Odd number:", counter)


# ============================================================
# 5. Using break to Search for a Value
# ============================================================

numbers = [10, 25, 30, 45, 50]

target = 30

for number in numbers:
    if number == target:
        print("Target found:", number)
        break


# ============================================================
# 6. Using continue to Skip Values
# ============================================================

numbers = [1, 2, 3, 4, 5, 6, 7]

for number in numbers:
    if number == 4:
        continue

    print(number)


# ============================================================
# 7. pass Statement
# ============================================================

# pass does nothing.
# It is useful when a block of code is required syntactically
# but the implementation will be added later.

for number in range(5):
    if number == 3:
        pass

    print(number)


# Example:

def future_function():
    pass


# ============================================================
# 8. break vs continue
# ============================================================

"""
break:
    Stops the entire loop.

continue:
    Skips the current iteration.

pass:
    Does nothing and allows execution to continue.
"""


# ============================================================
# 9. break in Nested Loops
# ============================================================

for row in range(1, 4):
    for column in range(1, 6):
        if column == 3:
            break

        print(f"Row: {row}, Column: {column}")


# ============================================================
# 10. continue in Nested Loops
# ============================================================

for row in range(1, 4):
    for column in range(1, 6):
        if column == 3:
            continue

        print(f"Row: {row}, Column: {column}")


# ============================================================
# 11. Searching for the First Matching Value
# ============================================================

names = ["Ali", "Reza", "Sara", "Mohsen", "Nima"]

for name in names:
    if name == "Mohsen":
        print("Found:", name)
        break


# ============================================================
# 12. Skipping Invalid Values
# ============================================================

numbers = [10, -5, 20, -3, 30]

for number in numbers:
    if number < 0:
        continue

    print("Valid number:", number)


# ============================================================
# 13. Processing Data Until a Condition
# ============================================================

numbers = [5, 10, 15, 20, 25, 30]

total = 0

for number in numbers:
    total += number

    if total > 50:
        break

print("Total:", total)


# ============================================================
# 14. Real-World Example: Login Attempts
# ============================================================

correct_password = "python123"
max_attempts = 3

for attempt in range(1, max_attempts + 1):
    password = input("Enter password: ")

    if password == correct_password:
        print("Login successful.")
        break

    print("Incorrect password.")

else:
    print("Account temporarily locked.")


# ============================================================
# 15. Real-World Example: Processing Orders
# ============================================================

orders = [
    {"id": 1, "status": "completed"},
    {"id": 2, "status": "cancelled"},
    {"id": 3, "status": "completed"},
    {"id": 4, "status": "pending"},
]

for order in orders:
    if order["status"] == "cancelled":
        continue

    print("Processing order:", order["id"])


# ============================================================
# 16. Real-World Example: Finding an Available Product
# ============================================================

products = [
    {"name": "Keyboard", "stock": 0},
    {"name": "Mouse", "stock": 0},
    {"name": "Monitor", "stock": 5},
    {"name": "Headset", "stock": 10},
]

for product in products:
    if product["stock"] <= 0:
        continue

    print("Available product:", product["name"])
    break