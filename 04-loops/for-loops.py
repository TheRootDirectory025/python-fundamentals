"""
Python Fundamentals
04 - Loops
Topic: For Loop

This file covers:
- Basic for loops
- range()
- Looping through strings
- Looping through lists
- start, stop, and step
- Nested for loops
- for loop with conditions
- enumerate()
- Practical examples
"""


# ============================================================
# 1. Basic For Loop
# ============================================================

for number in range(5):
    print(number)


# ============================================================
# 2. Using range()
# ============================================================

# range(5) generates numbers from 0 to 4.

for number in range(5):
    print("Number:", number)


# ============================================================
# 3. Specifying Start and Stop
# ============================================================

# range(start, stop)

for number in range(1, 6):
    print(number)


# ============================================================
# 4. Using Step
# ============================================================

# range(start, stop, step)

for number in range(0, 11, 2):
    print("Even number:", number)


# Counting backwards

for number in range(10, 0, -1):
    print("Countdown:", number)


# ============================================================
# 5. Looping Through a String
# ============================================================

name = "Python"

for character in name:
    print(character)


# ============================================================
# 6. Looping Through a List
# ============================================================

languages = ["Python", "Kotlin", "Java", "C++"]

for language in languages:
    print("Language:", language)


# ============================================================
# 7. Looping Through a Tuple
# ============================================================

numbers = (10, 20, 30, 40)

for number in numbers:
    print(number)


# ============================================================
# 8. Using a For Loop with Conditions
# ============================================================

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for number in numbers:
    if number % 2 == 0:
        print("Even:", number)


# ============================================================
# 9. Calculating a Total
# ============================================================

prices = [10, 20, 15, 30]

total = 0

for price in prices:
    total += price

print("Total:", total)


# ============================================================
# 10. Nested For Loops
# ============================================================

for row in range(3):
    for column in range(3):
        print("Row:", row, "Column:", column)


# ============================================================
# 11. Creating a Multiplication Table
# ============================================================

number = 5

for multiplier in range(1, 11):
    result = number * multiplier
    print(f"{number} x {multiplier} = {result}")


# ============================================================
# 12. enumerate()
# ============================================================

# enumerate() gives us both the index and the value.

languages = ["Python", "Kotlin", "Java"]

for index, language in enumerate(languages):
    print(index, language)


# Starting the index from 1

for index, language in enumerate(languages, start=1):
    print(index, language)


# ============================================================
# 13. Looping Through a Dictionary
# ============================================================

student = {
    "name": "Ali",
    "age": 22,
    "major": "Computer Engineering"
}

for key in student:
    print(key, ":", student[key])


# Using items()

for key, value in student.items():
    print(f"{key}: {value}")


# ============================================================
# 14. Finding the Maximum Value
# ============================================================

scores = [15, 18, 12, 20, 17]

highest_score = scores[0]

for score in scores:
    if score > highest_score:
        highest_score = score

print("Highest score:", highest_score)


# ============================================================
# 15. Counting Matching Values
# ============================================================

numbers = [1, 5, 3, 5, 8, 5, 2]

count = 0

for number in numbers:
    if number == 5:
        count += 1

print("Number of 5s:", count)


# ============================================================
# 16. Real-World Example: Shopping Cart
# ============================================================

cart = [
    {"name": "Keyboard", "price": 50},
    {"name": "Mouse", "price": 25},
    {"name": "Headset", "price": 75}
]

total_price = 0

for product in cart:
    total_price += product["price"]

print("Cart total:", total_price)


# ============================================================
# 17. Real-World Example: Student Scores
# ============================================================

scores = [18, 15, 20, 12, 17]

total_score = 0

for score in scores:
    total_score += score

average_score = total_score / len(scores)

print("Average score:", average_score)

