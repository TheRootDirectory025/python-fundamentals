"""
Python Fundamentals
09 - Files
Topic: Text Files

This file covers:
- Opening files
- Reading files
- Writing files
- Appending to files
- File modes
- with statement
- Reading lines
- Writing multiple lines
- File existence
- Encoding
- Practical file handling examples
"""


# ============================================================
# 1. Opening a File
# ============================================================

"""
The open() function is used to open a file.

Basic syntax:

open(filename, mode)

Common modes:

"r" -> read
"w" -> write
"a" -> append
"x" -> create a new file

It is recommended to use the with statement
when working with files.
"""


# ============================================================
# 2. Reading a File
# ============================================================

"""
Assume that "example.txt" contains:

Hello Python
Welcome to programming
"""

try:
    with open("example.txt", "r") as file:
        content = file.read()

    print(content)

except FileNotFoundError:
    print("File not found.")


# ============================================================
# 3. Reading with the Default Mode
# ============================================================

"""
"r" is the default mode.

So this:

open("example.txt", "r")

is equivalent to:

open("example.txt")
"""

try:
    with open("example.txt") as file:
        content = file.read()

    print(content)

except FileNotFoundError:
    print("File not found.")


# ============================================================
# 4. read()
# ============================================================

try:
    with open("example.txt", "r") as file:
        content = file.read()

    print(content)

except FileNotFoundError:
    print("File not found.")


# read() returns the entire file as a string.


# ============================================================
# 5. Reading a Limited Number of Characters
# ============================================================

try:
    with open("example.txt", "r") as file:
        content = file.read(10)

    print(content)

except FileNotFoundError:
    print("File not found.")


# ============================================================
# 6. readline()
# ============================================================

try:
    with open("example.txt", "r") as file:
        first_line = file.readline()

    print(first_line)

except FileNotFoundError:
    print("File not found.")


# ============================================================
# 7. Reading Multiple Lines
# ============================================================

try:
    with open("example.txt", "r") as file:
        first_line = file.readline()
        second_line = file.readline()

    print(first_line)
    print(second_line)

except FileNotFoundError:
    print("File not found.")


# ============================================================
# 8. readlines()
# ============================================================

try:
    with open("example.txt", "r") as file:
        lines = file.readlines()

    print(lines)

except FileNotFoundError:
    print("File not found.")


# readlines() returns a list containing the lines.


# ============================================================
# 9. Looping Through a File
# ============================================================

try:
    with open("example.txt", "r") as file:
        for line in file:
            print(line.strip())

except FileNotFoundError:
    print("File not found.")


# ============================================================
# 10. Writing to a File
# ============================================================

"""
The "w" mode writes data to a file.

Important:
If the file already exists, "w" replaces its contents.
"""

with open("output.txt", "w") as file:
    file.write("Hello Python!")


# ============================================================
# 11. Writing Multiple Lines
# ============================================================

with open("output.txt", "w") as file:
    file.write("Python\n")
    file.write("Django\n")
    file.write("PostgreSQL\n")


# ============================================================
# 12. Writing a List of Lines
# ============================================================

lines = [
    "Python\n",
    "Django\n",
    "PostgreSQL\n"
]

with open("technologies.txt", "w") as file:
    file.writelines(lines)


# ============================================================
# 13. Appending to a File
# ============================================================

"""
The "a" mode adds new content to the end of a file
without deleting its existing content.
"""

with open("output.txt", "a") as file:
    file.write("Docker\n")


# ============================================================
# 14. Writing Without a New Line
# ============================================================

with open("output.txt", "w") as file:
    file.write("Python")
    file.write("Django")

print("Content written without automatic new lines.")


# ============================================================
# 15. Creating a New File with x
# ============================================================

"""
The "x" mode creates a new file.

If the file already exists, FileExistsError is raised.
"""

try:
    with open("new_file.txt", "x") as file:
        file.write("New file created.")

except FileExistsError:
    print("File already exists.")


# ============================================================
# 16. File Encoding
# ============================================================

"""
UTF-8 is a common encoding and is recommended when working
with text files, especially when the content may contain
non-English characters.
"""

with open(
    "unicode.txt",
    "w",
    encoding="utf-8"
) as file:
    file.write("Hello Python")


# ============================================================
# 17. Reading UTF-8 Text
# ============================================================

try:
    with open(
        "unicode.txt",
        "r",
        encoding="utf-8"
    ) as file:
        content = file.read()

    print(content)

except FileNotFoundError:
    print("File not found.")


# ============================================================
# 18. The with Statement
# ============================================================

"""
The with statement automatically closes the file
after the block finishes.

Preferred:

with open("file.txt") as file:
    content = file.read()

Instead of manually managing:

file = open("file.txt")
content = file.read()
file.close()
"""


# ============================================================
# 19. Checking Whether a File Is Closed
# ============================================================

with open("output.txt", "r") as file:
    print(f"Inside block: {file.closed}")

print(f"Outside block: {file.closed}")


# ============================================================
# 20. File Mode
# ============================================================

with open("output.txt", "r") as file:
    print(f"Mode: {file.mode}")


# ============================================================
# 21. File Name
# ============================================================

with open("output.txt", "r") as file:
    print(f"Filename: {file.name}")


# ============================================================
# 22. Read and Process Lines
# ============================================================

with open("technologies.txt", "r") as file:
    for line in file:
        technology = line.strip()

        if technology:
            print(f"Technology: {technology}")


# ============================================================
# 23. Remove New Line Characters
# ============================================================

with open("technologies.txt", "r") as file:
    lines = file.readlines()

clean_lines = [
    line.strip()
    for line in lines
]

print(clean_lines)


# ============================================================
# 24. Count Lines
# ============================================================

with open("technologies.txt", "r") as file:
    line_count = sum(
        1
        for line in file
    )

print(f"Line count: {line_count}")


# ============================================================
# 25. Count Words
# ============================================================

try:
    with open("example.txt", "r") as file:
        content = file.read()

    words = content.split()

    print(f"Word count: {len(words)}")

except FileNotFoundError:
    print("File not found.")


# ============================================================
# 26. Count Characters
# ============================================================

try:
    with open("example.txt", "r") as file:
        content = file.read()

    print(f"Character count: {len(content)}")

except FileNotFoundError:
    print("File not found.")


# ============================================================
# 27. Search for Text in a File
# ============================================================

try:
    with open("example.txt", "r") as file:
        content = file.read()

    keyword = "Python"

    if keyword in content:
        print("Keyword found.")
    else:
        print("Keyword not found.")

except FileNotFoundError:
    print("File not found.")


# ============================================================
# 28. Count a Word in a File
# ============================================================

try:
    with open("example.txt", "r") as file:
        content = file.read()

    count = content.lower().count("python")

    print(f"Python appears {count} times.")

except FileNotFoundError:
    print("File not found.")


# ============================================================
# 29. Copy Text from One File to Another
# ============================================================

try:
    with open("example.txt", "r") as source:
        content = source.read()

    with open("copy.txt", "w") as destination:
        destination.write(content)

    print("File copied successfully.")

except FileNotFoundError:
    print("Source file not found.")


# ============================================================
# 30. Append User Data
# ============================================================

name = "Mohsen"
age = 24

with open("users.txt", "a", encoding="utf-8") as file:
    file.write(
        f"Name: {name}, Age: {age}\n"
    )


# ============================================================
# 31. Practical Example: Save Skills
# ============================================================

skills = [
    "Python",
    "Django",
    "SQL",
    "Git",
    "Docker",
    "Kotlin"
]

with open(
    "skills.txt",
    "w",
    encoding="utf-8"
) as file:
    for skill in skills:
        file.write(f"{skill}\n")


# ============================================================
# 32. Practical Example: Load Skills
# ============================================================

try:
    with open(
        "skills.txt",
        "r",
        encoding="utf-8"
    ) as file:
        skills = [
            line.strip()
            for line in file
            if line.strip()
        ]

    print(skills)

except FileNotFoundError:
    print("Skills file not found.")


# ============================================================
# 33. Practical Example: Simple Log File
# ============================================================

message = "User logged in successfully."

with open(
    "app.log",
    "a",
    encoding="utf-8"
) as file:
    file.write(f"{message}\n")


# ============================================================
# 34. Practical Example: Save Program Results
# ============================================================

numbers = [10, 20, 30, 40, 50]

total = sum(numbers)
average = total / len(numbers)

with open(
    "results.txt",
    "w",
    encoding="utf-8"
) as file:
    file.write(f"Total: {total}\n")
    file.write(f"Average: {average:.2f}\n")


# ============================================================
# 35. Practical Example: Read Program Results
# ============================================================

try:
    with open(
        "results.txt",
        "r",
        encoding="utf-8"
    ) as file:
        results = file.read()

    print(results)

except FileNotFoundError:
    print("Results file not found.")


# ============================================================
# 36. Practical Example: Filter Lines
# ============================================================

try:
    with open(
        "technologies.txt",
        "r",
        encoding="utf-8"
    ) as file:
        django_lines = [
            line.strip()
            for line in file
            if "Django" in line
        ]

    print(django_lines)

except FileNotFoundError:
    print("File not found.")


# ============================================================
# 37. Practical Example: Replace Text in a File
# ============================================================

try:
    with open(
        "example.txt",
        "r",
        encoding="utf-8"
    ) as file:
        content = file.read()

    updated_content = content.replace(
        "Python",
        "Django"
    )

    with open(
        "updated.txt",
        "w",
        encoding="utf-8"
    ) as file:
        file.write(updated_content)

    print("File updated successfully.")

except FileNotFoundError:
    print("File not found.")


# ============================================================
# 38. Handling File Errors
# ============================================================

filename = "missing.txt"

try:
    with open(
        filename,
        "r",
        encoding="utf-8"
    ) as file:
        content = file.read()

except FileNotFoundError:
    print(
        f"File '{filename}' does not exist."
    )

except PermissionError:
    print(
        f"Permission denied for '{filename}'."
    )


# ============================================================
# 39. File Processing Function
# ============================================================

def read_file(filename):
    try:
        with open(
            filename,
            "r",
            encoding="utf-8"
        ) as file:
            return file.read()

    except FileNotFoundError:
        print(f"File '{filename}' not found.")

        return None


content = read_file("example.txt")

if content is not None:
    print(content)


# ============================================================
# 40. File Writing Function
# ============================================================

def write_file(filename, content):
    with open(
        filename,
        "w",
        encoding="utf-8"
    ) as file:
        file.write(content)


write_file(
    "message.txt",
    "Hello from Python!"
)


# ============================================================
# 41. File Appending Function
# ============================================================

def append_to_file(filename, content):
    with open(
        filename,
        "a",
        encoding="utf-8"
    ) as file:
        file.write(content)


append_to_file(
    "message.txt",
    "\nThis line was appended."
)


# ============================================================
# 42. Practical Example: Simple User Database
# ============================================================

users = [
    "ali",
    "sara",
    "mohsen",
]

with open(
    "users.txt",
    "w",
    encoding="utf-8"
) as file:
    for username in users:
        file.write(f"{username}\n")


def load_users(filename):
    try:
        with open(
            filename,
            "r",
            encoding="utf-8"
        ) as file:
            return [
                line.strip()
                for line in file
                if line.strip()
            ]

    except FileNotFoundError:
        return []


loaded_users = load_users("users.txt")

print(loaded_users)


# ============================================================
# 43. Important Difference Between Modes
# ============================================================

"""
"r"
    Read existing file.
    Raises FileNotFoundError if it does not exist.

"w"
    Write to a file.
    Creates the file if it does not exist.
    Replaces existing content.

"a"
    Append to a file.
    Creates the file if it does not exist.
    Keeps existing content.

"x"
    Create a new file.
    Raises FileExistsError if it already exists.
"""


# ============================================================
# 44. Best Practices
# ============================================================

"""
Best practices:

1. Prefer the with statement.
2. Specify encoding="utf-8" for text files.
3. Handle FileNotFoundError when appropriate.
4. Do not use "w" when you want to preserve old content.
5. Use "a" when adding content to an existing file.
6. Keep file operations inside functions when possible.
7. Avoid loading very large files entirely with read().
8. Process large files line by line when appropriate.
"""


# ============================================================
# 45. Summary
# ============================================================

"""
Important methods:

open()
    Open a file.

read()
    Read the entire file or a specific number of characters.

readline()
    Read one line.

readlines()
    Read all lines into a list.

write()
    Write text to a file.

writelines()
    Write multiple strings.

close()
    Close a file.

Common modes:

r -> read
w -> write
a -> append
x -> create

Preferred pattern:

with open(
    "file.txt",
    "r",
    encoding="utf-8"
) as file:
    content = file.read()
"""