"""
Python Fundamentals
07 - Strings
Topic: String Methods

This file covers:
- Creating and accessing strings
- Changing string case
- Removing whitespace
- Searching inside strings
- Replacing text
- Splitting and joining strings
- Checking string content
- Counting characters and substrings
- Practical string manipulation
"""


# ============================================================
# 1. Creating Strings
# ============================================================

name = "Mohsen"
language = 'Python'

print(name)
print(language)


# ============================================================
# 2. Accessing Characters
# ============================================================

text = "Python"

print(text[0])
print(text[1])
print(text[-1])
print(text[-2])


# ============================================================
# 3. String Length
# ============================================================

text = "Python"

print(len(text))


# ============================================================
# 4. Changing Case
# ============================================================

text = "Python Programming"

print(text.upper())
print(text.lower())
print(text.capitalize())
print(text.title())


# ============================================================
# 5. swapcase()
# ============================================================

text = "Python Programming"

print(text.swapcase())


# ============================================================
# 6. strip()
# ============================================================

text = "   Python   "

print(text)
print(text.strip())


# ============================================================
# 7. lstrip() and rstrip()
# ============================================================

text = "   Python   "

print(text.lstrip())
print(text.rstrip())


# ============================================================
# 8. Removing Specific Characters
# ============================================================

text = "...Python..."

print(text.strip("."))


# ============================================================
# 9. startswith()
# ============================================================

filename = "report.pdf"

print(filename.startswith("report"))
print(filename.startswith("image"))


# ============================================================
# 10. endswith()
# ============================================================

filename = "report.pdf"

print(filename.endswith(".pdf"))
print(filename.endswith(".jpg"))


# ============================================================
# 11. find()
# ============================================================

text = "Python is a powerful language."

position = text.find("powerful")

print(position)


# If the text does not exist, find() returns -1.

print(text.find("Java"))


# ============================================================
# 12. rfind()
# ============================================================

text = "Python Python Python"

print(text.rfind("Python"))


# rfind() returns the position of the last occurrence.


# ============================================================
# 13. index()
# ============================================================

text = "Python programming"

print(text.index("programming"))


# index() is similar to find(),
# but raises an error if the substring does not exist.

# print(text.index("Java"))


# ============================================================
# 14. count()
# ============================================================

text = "Python Python Python"

print(text.count("Python"))
print(text.count("Java"))


# ============================================================
# 15. replace()
# ============================================================

text = "I like Java."

new_text = text.replace(
    "Java",
    "Python"
)

print(new_text)


# ============================================================
# 16. Replace Multiple Occurrences
# ============================================================

text = "Python is easy. Python is powerful."

new_text = text.replace(
    "Python",
    "Django"
)

print(new_text)


# ============================================================
# 17. Limiting replace()
# ============================================================

text = "Python Python Python"

new_text = text.replace(
    "Python",
    "Django",
    1
)

print(new_text)


# ============================================================
# 18. split()
# ============================================================

text = "Python Django FastAPI"

words = text.split()

print(words)


# ============================================================
# 19. split() with a Separator
# ============================================================

text = "Python,Django,FastAPI"

technologies = text.split(",")

print(technologies)


# ============================================================
# 20. split() with Multiple Spaces
# ============================================================

text = "Python   Django   FastAPI"

words = text.split()

print(words)


# ============================================================
# 21. splitlines()
# ============================================================

text = """Python
Django
FastAPI"""

lines = text.splitlines()

print(lines)


# ============================================================
# 22. join()
# ============================================================

words = [
    "Python",
    "Django",
    "FastAPI"
]

result = " ".join(words)

print(result)


# ============================================================
# 23. join() with Comma
# ============================================================

words = [
    "Python",
    "Django",
    "FastAPI"
]

result = ", ".join(words)

print(result)


# ============================================================
# 24. join() with New Line
# ============================================================

items = [
    "Python",
    "Django",
    "PostgreSQL"
]

result = "\n".join(items)

print(result)


# ============================================================
# 25. Checking String Content
# ============================================================

text = "Python123"

print(text.isalpha())
print(text.isdigit())
print(text.isalnum())


# ============================================================
# 26. isalpha()
# ============================================================

print("Python".isalpha())
print("Python123".isalpha())
print("123".isalpha())


# ============================================================
# 27. isdigit()
# ============================================================

print("12345".isdigit())
print("Python".isdigit())
print("123abc".isdigit())


# ============================================================
# 28. isalnum()
# ============================================================

print("Python123".isalnum())
print("Python".isalnum())
print("Python 123".isalnum())


# Spaces and special characters make isalnum() return False.


# ============================================================
# 29. isspace()
# ============================================================

print("   ".isspace())
print("Python".isspace())
print("Python ".isspace())


# ============================================================
# 30. islower() and isupper()
# ============================================================

print("python".islower())
print("Python".islower())

print("PYTHON".isupper())
print("Python".isupper())


# ============================================================
# 31. istitle()
# ============================================================

print("Python Programming".istitle())
print("python programming".istitle())


# ============================================================
# 32. Practical Example: Username Validation
# ============================================================

username = "mohsen123"

is_valid = (
    username.isalnum()
    and len(username) >= 5
)

print(is_valid)


# ============================================================
# 33. Practical Example: Cleaning User Input
# ============================================================

user_input = "   Mohsen Bagheri   "

cleaned_input = user_input.strip()

print(cleaned_input)


# ============================================================
# 34. Practical Example: Email Normalization
# ============================================================

email = "  MOHSEN@EXAMPLE.COM  "

normalized_email = email.strip().lower()

print(normalized_email)


# ============================================================
# 35. Practical Example: Search in Text
# ============================================================

description = "Python is a popular programming language."

keyword = "Python"

if keyword.lower() in description.lower():
    print("Keyword found.")
else:
    print("Keyword not found.")


# ============================================================
# 36. Practical Example: Extract File Extension
# ============================================================

filename = "profile_picture.jpg"

parts = filename.split(".")

extension = parts[-1]

print(extension)


# ============================================================
# 37. Practical Example: File Validation
# ============================================================

filename = "profile_picture.jpg"

if filename.lower().endswith((".jpg", ".jpeg", ".png")):
    print("Valid image file.")
else:
    print("Invalid image file.")


# ============================================================
# 38. Practical Example: Convert CSV-like Text
# ============================================================

data = "Ali,18,Tehran"

parts = data.split(",")

name = parts[0]
age = parts[1]
city = parts[2]

print(name)
print(age)
print(city)


# ============================================================
# 39. Practical Example: Create a URL Slug
# ============================================================

title = "Python Programming Fundamentals"

slug = title.lower().replace(" ", "-")

print(slug)


# ============================================================
# 40. Practical Example: Remove Extra Spaces
# ============================================================

text = "Python    is    easy    to    learn"

words = text.split()

clean_text = " ".join(words)

print(clean_text)


# ============================================================
# 41. Practical Example: Count Words
# ============================================================

text = "Python is easy to learn"

words = text.split()

word_count = len(words)

print(f"Word count: {word_count}")


# ============================================================
# 42. Practical Example: Count a Character
# ============================================================

email = "mohsen@example.com"

at_count = email.count("@")

print(f"@ count: {at_count}")


# ============================================================
# 43. Practical Example: Basic Email Check
# ============================================================

email = "mohsen@example.com"

is_valid = (
    "@" in email
    and "." in email
    and not email.startswith("@")
    and not email.endswith("@")
)

print(is_valid)


# ============================================================
# 44. Practical Example: Mask Sensitive Data
# ============================================================

phone = "09123456789"

masked_phone = phone[:3] + "****" + phone[-3:]

print(masked_phone)


# ============================================================
# 45. Practical Example: Format Tags
# ============================================================

tags = "python,django,backend,api"

tag_list = tags.split(",")

formatted_tags = [
    f"#{tag.strip().lower()}"
    for tag in tag_list
]

print(formatted_tags)


# ============================================================
# 46. String Methods Are Immutable
# ============================================================

text = "python"

text.upper()

print(text)


# The original string did not change.
# String methods return a new string.


# ============================================================
# 47. Saving the Result
# ============================================================

text = "python"

text = text.upper()

print(text)


# ============================================================
# 48. Chaining String Methods
# ============================================================

text = "   PYTHON PROGRAMMING   "

result = text.strip().lower().replace(
    " ",
    "-"
)

print(result)


# ============================================================
# 49. Practical Example: Normalize a Product Name
# ============================================================

product_name = "   GAMING KEYBOARD   "

normalized_name = (
    product_name
    .strip()
    .lower()
    .replace(" ", "-")
)

print(normalized_name)


# ============================================================
# 50. Summary
# ============================================================

"""
Common string methods:

upper()
    Convert characters to uppercase.

lower()
    Convert characters to lowercase.

capitalize()
    Capitalize the first character.

title()
    Capitalize the first character of each word.

strip()
    Remove whitespace from both sides.

lstrip()
    Remove whitespace from the left side.

rstrip()
    Remove whitespace from the right side.

startswith()
    Check how a string starts.

endswith()
    Check how a string ends.

find()
    Find the first occurrence.

rfind()
    Find the last occurrence.

count()
    Count occurrences.

replace()
    Replace part of a string.

split()
    Split a string into a list.

join()
    Combine strings into one string.

isalpha()
    Check whether all characters are alphabetic.

isdigit()
    Check whether all characters are digits.

isalnum()
    Check whether all characters are letters or digits.

isspace()
    Check whether all characters are whitespace.

islower()
    Check whether characters are lowercase.

isupper()
    Check whether characters are uppercase.

String methods do not modify the original string.
They return a new string because strings are immutable.
"""