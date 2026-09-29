"""
Python Fundamentals
13 - File Handling
Topic: CSV Files

This file covers:
- What CSV files are
- Reading CSV files
- csv.reader
- csv.DictReader
- Writing CSV files
- csv.writer
- csv.DictWriter
- Headers
- Rows and columns
- Appending rows
- Practical data-processing examples
- Best practices
"""


# ============================================================
# 1. What Is a CSV File?
# ============================================================

"""
CSV stands for Comma-Separated Values.

A CSV file stores tabular data using rows and columns.

Example:

name,age,role
Mohsen,24,Backend Developer
Ali,25,Android Developer
Sara,23,Frontend Developer

Each line represents a row.

Each comma separates columns.
"""


# ============================================================
# 2. Importing the csv Module
# ============================================================

import csv


"""
The csv module is part of Python's standard library.

No external package is required.
"""


# ============================================================
# 3. Creating a CSV File
# ============================================================

with open(
    "users.csv",
    "w",
    newline="",
    encoding="utf-8"
) as file:

    writer = csv.writer(file)

    writer.writerow(
        ["name", "age", "role"]
    )

    writer.writerow(
        ["Mohsen", 24, "Backend Developer"]
    )

    writer.writerow(
        ["Ali", 25, "Android Developer"]
    )

    writer.writerow(
        ["Sara", 23, "Frontend Developer"]
    )


"""
newline=""

is recommended when working with the csv module.

It helps avoid unwanted blank lines on some platforms.
"""


# ============================================================
# 4. Reading a CSV File with csv.reader
# ============================================================

with open(
    "users.csv",
    "r",
    newline="",
    encoding="utf-8"
) as file:

    reader = csv.reader(file)

    for row in reader:
        print(row)


"""
Each row is returned as a list.

Example:

[
    "Mohsen",
    "24",
    "Backend Developer"
]
"""


# ============================================================
# 5. Reading the Header Separately
# ============================================================

with open(
    "users.csv",
    "r",
    newline="",
    encoding="utf-8"
) as file:

    reader = csv.reader(file)

    header = next(reader)

    print("Header:", header)

    for row in reader:
        print("Row:", row)


"""
next(reader)

moves the reader to the next row.

Here it is used to read the header first.
"""


# ============================================================
# 6. Accessing CSV Columns by Index
# ============================================================

with open(
    "users.csv",
    "r",
    newline="",
    encoding="utf-8"
) as file:

    reader = csv.reader(file)

    next(reader)

    for row in reader:

        name = row[0]
        age = row[1]
        role = row[2]

        print(
            f"{name} - {age} - {role}"
        )


"""
CSV data read by csv.reader is represented as strings.

Therefore:

age = row[1]

returns "24", not integer 24.
"""


# ============================================================
# 7. Converting CSV Values
# ============================================================

with open(
    "users.csv",
    "r",
    newline="",
    encoding="utf-8"
) as file:

    reader = csv.reader(file)

    next(reader)

    for row in reader:

        name = row[0]
        age = int(row[1])
        role = row[2]

        print(
            f"{name} is {age} years old."
        )


"""
CSV files do not automatically preserve Python data types.

If a value represents a number, you may need to convert it.
"""


# ============================================================
# 8. csv.DictReader
# ============================================================

"""
DictReader reads each row as a dictionary.

Example:

{
    "name": "Mohsen",
    "age": "24",
    "role": "Backend Developer"
}
"""


with open(
    "users.csv",
    "r",
    newline="",
    encoding="utf-8"
) as file:

    reader = csv.DictReader(file)

    for row in reader:

        print(row)


# ============================================================
# 9. Accessing DictReader Values
# ============================================================

with open(
    "users.csv",
    "r",
    newline="",
    encoding="utf-8"
) as file:

    reader = csv.DictReader(file)

    for row in reader:

        name = row["name"]
        age = int(row["age"])
        role = row["role"]

        print(
            f"{name} - {age} - {role}"
        )


"""
DictReader is often easier to understand than
using column indexes.
"""


# ============================================================
# 10. Creating CSV with DictWriter
# ============================================================

users = [
    {
        "name": "Mohsen",
        "age": 24,
        "role": "Backend Developer"
    },
    {
        "name": "Ali",
        "age": 25,
        "role": "Android Developer"
    },
    {
        "name": "Sara",
        "age": 23,
        "role": "Frontend Developer"
    }
]


with open(
    "users-dict.csv",
    "w",
    newline="",
    encoding="utf-8"
) as file:

    fieldnames = [
        "name",
        "age",
        "role"
    ]

    writer = csv.DictWriter(
        file,
        fieldnames=fieldnames
    )

    writer.writeheader()

    for user in users:
        writer.writerow(user)


"""
writeheader()

writes:

name,age,role
"""


# ============================================================
# 11. Writing Multiple Dictionary Rows
# ============================================================

with open(
    "users-bulk.csv",
    "w",
    newline="",
    encoding="utf-8"
) as file:

    fieldnames = [
        "name",
        "age",
        "role"
    ]

    writer = csv.DictWriter(
        file,
        fieldnames=fieldnames
    )

    writer.writeheader()

    writer.writerows(users)


"""
writerows() writes multiple dictionary rows at once.
"""


# ============================================================
# 12. Appending a Row to CSV
# ============================================================

new_user = {
    "name": "Reza",
    "age": 26,
    "role": "Python Developer"
}


with open(
    "users-dict.csv",
    "a",
    newline="",
    encoding="utf-8"
) as file:

    fieldnames = [
        "name",
        "age",
        "role"
    ]

    writer = csv.DictWriter(
        file,
        fieldnames=fieldnames
    )

    writer.writerow(new_user)


"""
Append mode keeps existing rows and adds the new row
at the end.
"""


# ============================================================
# 13. CSV with Different Delimiter
# ============================================================

"""
CSV does not always have to use a comma.

For example, some files use:

;

or:

|

The delimiter can be specified manually.
"""


with open(
    "semicolon-data.csv",
    "w",
    newline="",
    encoding="utf-8"
) as file:

    writer = csv.writer(
        file,
        delimiter=";"
    )

    writer.writerow(
        ["name", "age", "role"]
    )

    writer.writerow(
        ["Mohsen", 24, "Backend Developer"]
    )


# ============================================================
# 14. Reading a Different Delimiter
# ============================================================

with open(
    "semicolon-data.csv",
    "r",
    newline="",
    encoding="utf-8"
) as file:

    reader = csv.reader(
        file,
        delimiter=";"
    )

    for row in reader:
        print(row)


# ============================================================
# 15. CSV Quoting
# ============================================================

"""
CSV fields can contain commas.

Example:

name,description
Mohsen,"Python, Django and PostgreSQL"

The csv module handles quoting automatically.
"""


with open(
    "products.csv",
    "w",
    newline="",
    encoding="utf-8"
) as file:

    writer = csv.writer(file)

    writer.writerow(
        ["name", "description"]
    )

    writer.writerow(
        [
            "Backend Course",
            "Python, Django and PostgreSQL"
        ]
    )


# ============================================================
# 16. Reading Quoted Values
# ============================================================

with open(
    "products.csv",
    "r",
    newline="",
    encoding="utf-8"
) as file:

    reader = csv.reader(file)

    for row in reader:
        print(row)


"""
The csv module correctly handles the comma inside
the description field.
"""


# ============================================================
# 17. Filtering CSV Data
# ============================================================

with open(
    "users.csv",
    "r",
    newline="",
    encoding="utf-8"
) as file:

    reader = csv.DictReader(file)

    for row in reader:

        if row["role"] == "Backend Developer":
            print(row)


# ============================================================
# 18. Finding Users by Age
# ============================================================

with open(
    "users.csv",
    "r",
    newline="",
    encoding="utf-8"
) as file:

    reader = csv.DictReader(file)

    for row in reader:

        age = int(row["age"])

        if age >= 25:
            print(row["name"])


# ============================================================
# 19. Counting CSV Rows
# ============================================================

with open(
    "users.csv",
    "r",
    newline="",
    encoding="utf-8"
) as file:

    reader = csv.DictReader(file)

    count = 0

    for row in reader:
        count += 1

    print(
        f"Number of users: {count}"
    )


# ============================================================
# 20. Calculating an Average
# ============================================================

with open(
    "users.csv",
    "r",
    newline="",
    encoding="utf-8"
) as file:

    reader = csv.DictReader(file)

    ages = []

    for row in reader:
        ages.append(
            int(row["age"])
        )

    if ages:
        average_age = sum(ages) / len(ages)

        print(
            f"Average age: {average_age:.2f}"
        )


# ============================================================
# 21. Creating a Student CSV
# ============================================================

students = [
    {
        "name": "Mohsen",
        "score": 18.5,
        "major": "Computer Engineering"
    },
    {
        "name": "Ali",
        "score": 16.75,
        "major": "Computer Engineering"
    },
    {
        "name": "Sara",
        "score": 19.25,
        "major": "Computer Engineering"
    }
]


with open(
    "students.csv",
    "w",
    newline="",
    encoding="utf-8"
) as file:

    fieldnames = [
        "name",
        "score",
        "major"
    ]

    writer = csv.DictWriter(
        file,
        fieldnames=fieldnames
    )

    writer.writeheader()
    writer.writerows(students)


# ============================================================
# 22. Processing Student Scores
# ============================================================

with open(
    "students.csv",
    "r",
    newline="",
    encoding="utf-8"
) as file:

    reader = csv.DictReader(file)

    for student in reader:

        score = float(
            student["score"]
        )

        if score >= 18:
            status = "Excellent"
        elif score >= 12:
            status = "Passed"
        else:
            status = "Failed"

        print(
            f"{student['name']}: {status}"
        )


# ============================================================
# 23. Creating a Report CSV
# ============================================================

with open(
    "student-report.csv",
    "w",
    newline="",
    encoding="utf-8"
) as file:

    fieldnames = [
        "name",
        "score",
        "status"
    ]

    writer = csv.DictWriter(
        file,
        fieldnames=fieldnames
    )

    writer.writeheader()

    with open(
        "students.csv",
        "r",
        newline="",
        encoding="utf-8"
    ) as student_file:

        reader = csv.DictReader(
            student_file
        )

        for student in reader:

            score = float(
                student["score"]
            )

            if score >= 18:
                status = "Excellent"
            elif score >= 12:
                status = "Passed"
            else:
                status = "Failed"

            writer.writerow(
                {
                    "name": student["name"],
                    "score": score,
                    "status": status
                }
            )


# ============================================================
# 24. Handling Missing Files
# ============================================================

try:

    with open(
        "missing.csv",
        "r",
        newline="",
        encoding="utf-8"
    ) as file:

        reader = csv.DictReader(file)

        for row in reader:
            print(row)

except FileNotFoundError:

    print("CSV file was not found.")


# ============================================================
# 25. Handling Invalid Numeric Data
# ============================================================

with open(
    "students.csv",
    "r",
    newline="",
    encoding="utf-8"
) as file:

    reader = csv.DictReader(file)

    for student in reader:

        try:

            score = float(
                student["score"]
            )

            print(
                f"{student['name']}: {score}"
            )

        except ValueError:

            print(
                f"Invalid score for "
                f"{student['name']}"
            )


# ============================================================
# 26. CSV and Unicode
# ============================================================

persian_users = [
    {
        "name": "محسن",
        "role": "مهندس نرم افزار"
    },
    {
        "name": "علی",
        "role": "برنامه نویس اندروید"
    }
]


with open(
    "persian-users.csv",
    "w",
    newline="",
    encoding="utf-8"
) as file:

    fieldnames = [
        "name",
        "role"
    ]

    writer = csv.DictWriter(
        file,
        fieldnames=fieldnames
    )

    writer.writeheader()
    writer.writerows(persian_users)


# ============================================================
# 27. Reading Persian CSV
# ============================================================

with open(
    "persian-users.csv",
    "r",
    newline="",
    encoding="utf-8"
) as file:

    reader = csv.DictReader(file)

    for row in reader:
        print(
            f"{row['name']} - {row['role']}"
        )


# ============================================================
# 28. Using restkey with DictReader
# ============================================================

"""
DictReader normally expects each row to have the expected
number of columns.

restkey can store extra values when a row contains
more columns than expected.
"""


# ============================================================
# 29. Using restval with DictReader
# ============================================================

"""
restval can provide a value when a row contains
fewer columns than expected.

These options are useful when processing CSV files
from external systems that may not always have
perfectly consistent data.
"""


# ============================================================
# 30. CSV in Backend Development
# ============================================================

"""
CSV files are commonly used for:

- Data import
- Data export
- Reports
- User lists
- Product catalogs
- Financial data
- Administrative tools
- Bulk database operations

For example, a backend application may allow an administrator
to upload a CSV file containing hundreds of users.

The application can then:

1. Read the CSV.
2. Validate each row.
3. Convert values to appropriate types.
4. Save valid records to a database.
5. Report invalid rows.
"""


# ============================================================
# 31. CSV vs Database
# ============================================================

"""
CSV is useful for exchanging or processing data.

A database is usually more appropriate for:

- Large applications
- Concurrent users
- Relationships
- Transactions
- Searching
- Indexing
- Authentication data
- Complex queries

CSV should not automatically replace a database.
"""


# ============================================================
# 32. CSV Best Practices
# ============================================================

"""
Best practices:

1. Use the csv module instead of manually splitting strings.
2. Use newline="" when opening CSV files.
3. Specify encoding="utf-8".
4. Use DictReader when column names improve readability.
5. Use DictWriter when writing dictionary-based data.
6. Validate external CSV data.
7. Convert numeric values explicitly.
8. Handle missing files.
9. Handle invalid data.
10. Avoid loading extremely large datasets into memory
    unnecessarily.
11. Keep CSV processing separate from business logic.
12. Use databases for application data that requires
    relationships and reliable concurrent access.
"""


# ============================================================
# 33. Summary
# ============================================================

"""
Important tools:

csv.reader
    Reads rows as lists.

csv.DictReader
    Reads rows as dictionaries.

csv.writer
    Writes rows as lists.

csv.DictWriter
    Writes rows as dictionaries.

writerow()
    Writes one row.

writerows()
    Writes multiple rows.

writeheader()
    Writes dictionary field names as a header.

Common pattern:

with open(
    "data.csv",
    "r",
    newline="",
    encoding="utf-8"
) as file:

    reader = csv.DictReader(file)

    for row in reader:
        print(row)

The csv module is the standard Python solution
for working with CSV data.
"""