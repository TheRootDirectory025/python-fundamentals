"""
Python Fundamentals
04 - Loops
Topic: While Loop

This file covers:
- Basic while loops
- Conditions in while loops
- Incrementing and decrementing
- while with user input
- Infinite loops
- break and continue
- Nested while loops
- else with while
- Real-world examples
"""


# ============================================================
# 1. Basic While Loop
# ============================================================

counter = 1

while counter <= 5:
    print(counter)
    counter += 1


# ============================================================
# 2. Counting Backwards
# ============================================================

counter = 5

while counter > 0:
    print("Countdown:", counter)
    counter -= 1


# ============================================================
# 3. Using a Condition
# ============================================================

number = 1

while number <= 10:
    if number % 2 == 0:
        print("Even:", number)

    number += 1


# ============================================================
# 4. User Input with While
# ============================================================

"""
Keep asking the user for a password until the correct
password is entered.
"""

correct_password = "python123"
password = ""

while password != correct_password:
    password = input("Enter password: ")

print("Login successful.")


# ============================================================
# 5. Using break
# ============================================================

counter = 1

while counter <= 10:
    print(counter)

    if counter == 5:
        break

    counter += 1


# ============================================================
# 6. Using continue
# ============================================================

counter = 0

while counter < 10:
    counter += 1

    if counter % 2 == 0:
        continue

    print("Odd number:", counter)


# ============================================================
# 7. Avoiding an Infinite Loop
# ============================================================

"""
Always make sure the loop condition can eventually become False.

Example:

counter = 1

while counter <= 5:
    print(counter)
    counter += 1

If counter += 1 is removed, the loop would never end.
"""


# ============================================================
# 8. while with else
# ============================================================

counter = 1

while counter <= 3:
    print("Counter:", counter)
    counter += 1
else:
    print("Loop finished.")


# ============================================================
# 9. while with break and else
# ============================================================

number = 1

while number <= 5:
    if number == 10:
        break

    number += 1
else:
    print("Number 10 was not found.")


# ============================================================
# 10. Nested While Loops
# ============================================================

row = 1

while row <= 3:
    column = 1

    while column <= 3:
        print(f"Row: {row}, Column: {column}")
        column += 1

    row += 1


# ============================================================
# 11. Building a Simple Counter
# ============================================================

count = 0

while count < 5:
    count += 1
    print(f"Current count: {count}")


# ============================================================
# 12. Real-World Example: ATM Menu
# ============================================================

balance = 1000
choice = ""

while choice != "4":
    print("\nATM Menu")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        print("Balance:", balance)

    elif choice == "2":
        amount = float(input("Enter deposit amount: "))
        balance += amount
        print("Deposit successful.")

    elif choice == "3":
        amount = float(input("Enter withdrawal amount: "))

        if amount <= balance:
            balance -= amount
            print("Withdrawal successful.")
        else:
            print("Insufficient balance.")

    elif choice == "4":
        print("Goodbye.")

    else:
        print("Invalid option.")


# ============================================================
# 13. Real-World Example: Number Guessing
# ============================================================

secret_number = 7
guess = None

while guess != secret_number:
    guess = int(input("Guess the number: "))

    if guess < secret_number:
        print("Too low.")
    elif guess > secret_number:
        print("Too high.")

print("Correct!")

