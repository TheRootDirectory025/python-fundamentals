"""
Python Fundamentals
13 - File Handling
Topic: Reading and Writing Files

This file covers:
- What file handling is
- Opening files
- Reading files
- Writing files
- Appending to files
- File modes
- Encoding
- with statement
- Reading line by line
- Writing multiple lines
- pathlib basics
- Practical file handling examples
"""


# ============================================================
# 1. What Is File Handling?
# ============================================================

"""
File handling means reading data from files and writing data
to files.

Python can work with many types of files:

- TXT
- CSV
- JSON
- Logs
- Configuration files
- Images and binary files

In this file we focus mainly on text files.
"""


# ============================================================
# 2. Opening a File
# ============================================================

"""
The open() function is used to open a file.

Basic syntax:

open(
    filename,
    mode
)

Example:

file = open("example.txt", "r")

Always remember to close a file when you are finished
with it.
"""


# ============================================================
# 3. Reading a File
# ============================================================

file = open(
    "example.txt",
    "r",
    encoding="utf-8"
)

content = file.read()

print(content)

file.close()


"""
read() reads the entire file as a string.
"""


# ============================================================
# 4. Writing a File
# ============================================================

file = open(
    "output.txt",
    "w",
    encoding="utf-8"
)

file.write("Hello, Python!")

file.close()


"""
w means write mode.

Important:

If the file already exists, write mode replaces
its existing content.
"""


# ============================================================
# 5. Writing Multiple Lines
# ============================================================

file = open(
    "users.txt",
    "w",
    encoding="utf-8"
)

file.write("Mohsen\n")
file.write("Ali\n")
file.write("Sara\n")

file.close()


# ============================================================
# 6. Appending to a File
# ============================================================

file = open(
    "users.txt",
    "a",
    encoding="utf-8"
)

file.write("Reza\n")

file.close()


"""
a means append mode.

Existing content remains unchanged and new content
is added to the end of the file.
"""


# ============================================================
# 7. File Modes
# ============================================================

"""
Common file modes:

r
    Read

w
    Write and replace existing content

a
    Append

x
    Create a new file

r+
    Read and write

w+
    Write and read, replacing existing content

a+
    Append and read

b
    Binary mode
"""


# ============================================================
# 8. Reading a Specific Number of Characters
# ============================================================

file = open(
    "example.txt",
    "r",
    encoding="utf-8"
)

content = file.read(10)

print(content)

file.close()


"""
read(10) reads up to 10 characters.
"""


# ============================================================
# 9. readline()
# ============================================================

file = open(
    "users.txt",
    "r",
    encoding="utf-8"
)

first_line = file.readline()

print(first_line)

file.close()


"""
readline() reads one line at a time.
"""


# ============================================================
# 10. Reading Multiple Lines
# ============================================================

file = open(
    "users.txt",
    "r",
    encoding="utf-8"
)

first_line = file.readline()
second_line = file.readline()

print(first_line)
print(second_line)

file.close()


# ============================================================
# 11. readlines()
# ============================================================

file = open(
    "users.txt",
    "r",
    encoding="utf-8"
)

lines = file.readlines()

print(lines)

file.close()


"""
readlines() returns a list containing the lines.
"""


# ============================================================
# 12. Iterating Over a File
# ============================================================

file = open(
    "users.txt",
    "r",
    encoding="utf-8"
)

for line in file:
    print(line.strip())

file.close()


"""
Iterating directly over a file is useful when processing
large files line by line.
"""


# ============================================================
# 13. Why strip() Is Often Used
# ============================================================

file = open(
    "users.txt",
    "r",
    encoding="utf-8"
)

for line in file:
    print(line.strip())

file.close()


"""
Lines read from a text file often contain a newline character:

"User 1\n"

strip() removes surrounding whitespace,
including the newline.
"""


# ============================================================
# 14. Using with
# ============================================================

with open(
    "example.txt",
    "r",
    encoding="utf-8"
) as file:

    content = file.read()

    print(content)


"""
with automatically closes the file when the block finishes.

This is the recommended approach for normal file handling.
"""


# ============================================================
# 15. Writing with with
# ============================================================

with open(
    "message.txt",
    "w",
    encoding="utf-8"
) as file:

    file.write(
        "Welcome to Python!"
    )


# ============================================================
# 16. Appending with with
# ============================================================

with open(
    "message.txt",
    "a",
    encoding="utf-8"
) as file:

    file.write(
        "\nThis line was appended."
    )


# ============================================================
# 17. Writing Multiple Lines
# ============================================================

users = [
    "Mohsen",
    "Ali",
    "Sara",
    "Reza"
]

with open(
    "users.txt",
    "w",
    encoding="utf-8"
) as file:

    for user in users:
        file.write(
            user + "\n"
        )


# ============================================================
# 18. writelines()
# ============================================================

lines = [
    "Python\n",
    "Django\n",
    "SQL\n",
    "PostgreSQL\n"
]

with open(
    "skills.txt",
    "w",
    encoding="utf-8"
) as file:

    file.writelines(lines)


"""
writelines() writes multiple strings.

Important:

writelines() does not automatically add newline characters.

Therefore the strings above explicitly contain \n.
"""


# ============================================================
# 19. Checking Whether a File Exists
# ============================================================

from pathlib import Path


file_path = Path("example.txt")

if file_path.exists():
    print("File exists.")
else:
    print("File does not exist.")


# ============================================================
# 20. Checking Whether a Path Is a File
# ============================================================

path = Path("example.txt")

if path.is_file():
    print("This is a file.")


# ============================================================
# 21. Checking Whether a Path Is a Directory
# ============================================================

path = Path(".")

if path.is_dir():
    print("This is a directory.")


# ============================================================
# 22. Reading with pathlib
# ============================================================

from pathlib import Path


file_path = Path("example.txt")

if file_path.exists():
    content = file_path.read_text(
        encoding="utf-8"
    )

    print(content)


"""
pathlib provides a convenient alternative for simple
text file operations.
"""


# ============================================================
# 23. Writing with pathlib
# ============================================================

from pathlib import Path


file_path = Path("notes.txt")

file_path.write_text(
    "Python file handling.",
    encoding="utf-8"
)


# ============================================================
# 24. Encoding
# ============================================================

"""
Encoding determines how text is represented as bytes.

For modern applications, UTF-8 is a common choice.

Example:

open(
    "file.txt",
    "r",
    encoding="utf-8"
)
"""


# ============================================================
# 25. Working with Persian Text
# ============================================================

with open(
    "persian.txt",
    "w",
    encoding="utf-8"
) as file:

    file.write(
        "سلام، پایتون!"
    )


with open(
    "persian.txt",
    "r",
    encoding="utf-8"
) as file:

    content = file.read()

    print(content)


"""
Using UTF-8 allows Python to correctly handle
many languages and character sets.
"""


# ============================================================
# 26. File Position
# ============================================================

with open(
    "example.txt",
    "r",
    encoding="utf-8"
) as file:

    print(file.tell())

    content = file.read(5)

    print(content)

    print(file.tell())


"""
tell() returns the current position in the file.
"""


# ============================================================
# 27. seek()
# ============================================================

with open(
    "example.txt",
    "r",
    encoding="utf-8"
) as file:

    file.seek(0)

    content = file.read()

    print(content)


"""
seek() moves the file position.

seek(0)

moves the position back to the beginning.
"""


# ============================================================
# 28. Reading After seek()
# ============================================================

with open(
    "example.txt",
    "r",
    encoding="utf-8"
) as file:

    first_part = file.read(5)

    print(first_part)

    file.seek(0)

    complete_content = file.read()

    print(complete_content)


# ============================================================
# 29. FileNotFoundError
# ============================================================

try:

    with open(
        "missing.txt",
        "r",
        encoding="utf-8"
    ) as file:

        content = file.read()

except FileNotFoundError:

    print("File was not found.")


"""
Trying to open a non-existing file in read mode
raises FileNotFoundError.
"""


# ============================================================
# 30. PermissionError
# ============================================================

"""
A file operation can also fail because the program
does not have enough permissions.

Example:

try:
    with open(
        "protected.txt",
        "r",
        encoding="utf-8"
    ) as file:
        content = file.read()

except PermissionError:
    print("Permission denied.")
"""


# ============================================================
# 31. Practical Example: Save User Information
# ============================================================

name = "Mohsen"
age = 24
role = "Backend Developer"

with open(
    "user.txt",
    "w",
    encoding="utf-8"
) as file:

    file.write(
        f"Name: {name}\n"
    )

    file.write(
        f"Age: {age}\n"
    )

    file.write(
        f"Role: {role}\n"
    )


# ============================================================
# 32. Practical Example: Read User Information
# ============================================================

try:

    with open(
        "user.txt",
        "r",
        encoding="utf-8"
    ) as file:

        for line in file:
            print(line.strip())

except FileNotFoundError:

    print("User file does not exist.")


# ============================================================
# 33. Practical Example: Simple Log File
# ============================================================

from datetime import datetime


message = "User logged in"

timestamp = datetime.now()

with open(
    "application.log",
    "a",
    encoding="utf-8"
) as file:

    file.write(
        f"{timestamp} - {message}\n"
    )


"""
Append mode is useful for log files because we usually
don't want to delete previous log entries.
"""


# ============================================================
# 34. Practical Example: Search in a File
# ============================================================

keyword = "Python"

try:

    with open(
        "skills.txt",
        "r",
        encoding="utf-8"
    ) as file:

        for line in file:

            if keyword.lower() in line.lower():
                print(
                    f"Found: {line.strip()}"
                )

except FileNotFoundError:

    print("Skills file not found.")


# ============================================================
# 35. Practical Example: Count Lines
# ============================================================

try:

    with open(
        "users.txt",
        "r",
        encoding="utf-8"
    ) as file:

        line_count = 0

        for line in file:
            line_count += 1

        print(
            f"Number of lines: {line_count}"
        )

except FileNotFoundError:

    print("Users file not found.")


# ============================================================
# 36. Practical Example: Count Non-Empty Lines
# ============================================================

try:

    with open(
        "users.txt",
        "r",
        encoding="utf-8"
    ) as file:

        count = 0

        for line in file:

            if line.strip():
                count += 1

        print(
            f"Non-empty lines: {count}"
        )

except FileNotFoundError:

    print("Users file not found.")


# ============================================================
# 37. Practical Example: Copy Text Content
# ============================================================

source = "source.txt"
destination = "destination.txt"

try:

    with open(
        source,
        "r",
        encoding="utf-8"
    ) as source_file:

        content = source_file.read()

    with open(
        destination,
        "w",
        encoding="utf-8"
    ) as destination_file:

        destination_file.write(content)

    print("File copied successfully.")

except FileNotFoundError:

    print("Source file was not found.")


# ============================================================
# 38. Practical Example: Process File Line by Line
# ============================================================

try:

    with open(
        "users.txt",
        "r",
        encoding="utf-8"
    ) as file:

        for line_number, line in enumerate(
            file,
            start=1
        ):

            username = line.strip()

            if username:
                print(
                    f"{line_number}: {username}"
                )

except FileNotFoundError:

    print("Users file not found.")


# ============================================================
# 39. File Mode Summary
# ============================================================

"""
Mode:

r
    Read existing file.

w
    Write and replace existing content.

a
    Append to the end.

x
    Create a new file.
    Fails if the file already exists.

r+
    Read and write.

w+
    Write and read.
    Existing content is replaced.

a+
    Append and read.

b
    Binary mode.

Examples:

rb
    Read binary.

wb
    Write binary.
"""


# ============================================================
# 40. Text vs Binary Files
# ============================================================

"""
Text files:

- .txt
- .csv
- .json
- .log

Usually handled using:

encoding="utf-8"


Binary files:

- images
- videos
- audio
- executable files

Use binary mode:

rb
wb


Example:

with open(
    "image.jpg",
    "rb"
) as file:

    data = file.read()
"""


# ============================================================
# 41. Why with Is Recommended
# ============================================================

"""
Instead of:

file = open(...)
content = file.read()
file.close()


Prefer:

with open(...) as file:
    content = file.read()


The with statement makes resource management safer
and ensures the file is closed after the block.
"""


# ============================================================
# 42. Avoid Reading Huge Files at Once
# ============================================================

"""
For a small file:

content = file.read()

is usually fine.

For a very large file, prefer:

for line in file:
    process(line)

This avoids loading the entire file into memory at once.
"""


# ============================================================
# 43. File Handling in Backend Development
# ============================================================

"""
File handling is useful for:

- application logs
- configuration files
- reports
- imports and exports
- uploaded files
- data processing
- temporary files
- backups

Backend applications often need to work with files
even when the main data is stored in a database.
"""


# ============================================================
# 44. Best Practices
# ============================================================

"""
Best practices:

1. Prefer the with statement.
2. Specify encoding for text files.
3. Use UTF-8 for general text data.
4. Handle FileNotFoundError when appropriate.
5. Use append mode for logs.
6. Be careful with write mode because it replaces content.
7. Process large files line by line.
8. Use pathlib for modern path handling.
9. Use binary mode for binary files.
10. Keep file operations small and focused.
"""


# ============================================================
# 45. Summary
# ============================================================

"""
Important concepts:

open()
    Opens a file.

read()
    Reads content.

readline()
    Reads one line.

readlines()
    Reads lines into a list.

write()
    Writes content.

writelines()
    Writes multiple strings.

with
    Safely manages the file resource.

seek()
    Moves the file position.

tell()
    Returns the current file position.

pathlib
    Provides convenient filesystem operations.

The main idea:

Open the file,
perform the required operation,
and let with safely handle closing it.
"""