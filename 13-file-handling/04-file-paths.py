"""
Python Fundamentals
13 - File Handling
Topic: File Paths with pathlib

This file covers:
- File paths
- pathlib.Path
- Relative paths
- Absolute paths
- Current working directory
- Path components
- Creating directories
- Creating files
- Joining paths
- Checking files and directories
- File extensions
- File names
- Parent directories
- glob()
- rglob()
- Renaming files
- Moving files
- Deleting files and directories
- Practical project structures
- Best practices
"""


# ============================================================
# 1. What Is a File Path?
# ============================================================

"""
A file path tells the operating system where a file
or directory is located.

Example:

documents/report.txt


A path can contain:

- Drive
- Directory
- Subdirectory
- File name
- File extension
"""


# ============================================================
# 2. Importing Path
# ============================================================

from pathlib import Path


# ============================================================
# 3. Creating a Path Object
# ============================================================

path = Path("example.txt")

print(path)


"""
Path objects represent filesystem paths.

Using pathlib is generally more convenient and readable
than manually building paths with strings.
"""


# ============================================================
# 4. Relative Paths
# ============================================================

path = Path("data/users.json")

print(path)


"""
This is a relative path.

It is interpreted relative to the current
working directory.
"""


# ============================================================
# 5. Current Working Directory
# ============================================================

current_directory = Path.cwd()

print(current_directory)


"""
cwd() means:

Current Working Directory
"""


# ============================================================
# 6. Absolute Path
# ============================================================

path = Path("data/users.json")

absolute_path = path.absolute()

print(absolute_path)


"""
absolute() returns an absolute representation
of the path.
"""


# ============================================================
# 7. Path Parts
# ============================================================

path = Path(
    "projects/python/data/users.json"
)

print(path.parts)


"""
parts returns the individual components of a path.
"""


# ============================================================
# 8. File Name
# ============================================================

path = Path(
    "projects/python/data/users.json"
)

print(path.name)


"""
name returns the final part of the path.

Result:

users.json
"""


# ============================================================
# 9. File Stem
# ============================================================

path = Path(
    "projects/python/data/users.json"
)

print(path.stem)


"""
stem returns the file name without its extension.

Result:

users
"""


# ============================================================
# 10. File Suffix
# ============================================================

path = Path(
    "projects/python/data/users.json"
)

print(path.suffix)


"""
suffix returns the file extension.

Result:

.json
"""


# ============================================================
# 11. Multiple Suffixes
# ============================================================

path = Path(
    "archive.tar.gz"
)

print(path.name)
print(path.stem)
print(path.suffix)
print(path.suffixes)


"""
suffixes returns all suffixes.

Example:

archive.tar.gz

suffixes:

[".tar", ".gz"]
"""


# ============================================================
# 12. Parent Directory
# ============================================================

path = Path(
    "projects/python/data/users.json"
)

print(path.parent)


"""
parent returns the directory containing the path.
"""


# ============================================================
# 13. Parent's Parent
# ============================================================

path = Path(
    "projects/python/data/users.json"
)

print(path.parent.parent)


"""
parent can be used repeatedly to move upward
through the directory structure.
"""


# ============================================================
# 14. Joining Paths
# ============================================================

base_path = Path("projects")

file_path = base_path / "python" / "data" / "users.json"

print(file_path)


"""
The / operator can be used to combine Path objects.

This is one of the most useful pathlib features.
"""


# ============================================================
# 15. joinpath()
# ============================================================

base_path = Path("projects")

file_path = base_path.joinpath(
    "python",
    "data",
    "users.json"
)

print(file_path)


"""
joinpath() provides another way to combine paths.
"""


# ============================================================
# 16. Checking Whether a Path Exists
# ============================================================

path = Path("example.txt")

if path.exists():
    print("Path exists.")
else:
    print("Path does not exist.")


# ============================================================
# 17. Checking Whether It Is a File
# ============================================================

path = Path("example.txt")

if path.is_file():
    print("This is a file.")


# ============================================================
# 18. Checking Whether It Is a Directory
# ============================================================

path = Path("data")

if path.is_dir():
    print("This is a directory.")


# ============================================================
# 19. Creating a Directory
# ============================================================

directory = Path("data")

directory.mkdir(
    exist_ok=True
)


"""
mkdir() creates a directory.

exist_ok=True prevents an error if the directory
already exists.
"""


# ============================================================
# 20. Creating Nested Directories
# ============================================================

directory = Path(
    "project/data/users"
)

directory.mkdir(
    parents=True,
    exist_ok=True
)


"""
parents=True creates missing parent directories.

Without parents=True, Python may fail if
the parent directory does not exist.
"""


# ============================================================
# 21. Creating an Empty File
# ============================================================

file_path = Path(
    "data/example.txt"
)

file_path.touch()


"""
touch() creates an empty file if it does not exist.
"""


# ============================================================
# 22. Writing Text with pathlib
# ============================================================

file_path = Path(
    "data/message.txt"
)

file_path.write_text(
    "Hello from pathlib!",
    encoding="utf-8"
)


# ============================================================
# 23. Reading Text with pathlib
# ============================================================

file_path = Path(
    "data/message.txt"
)

content = file_path.read_text(
    encoding="utf-8"
)

print(content)


# ============================================================
# 24. Writing Multiple Lines
# ============================================================

file_path = Path(
    "data/skills.txt"
)

content = (
    "Python\n"
    "Django\n"
    "PostgreSQL\n"
    "Docker\n"
)

file_path.write_text(
    content,
    encoding="utf-8"
)


# ============================================================
# 25. Reading Multiple Lines
# ============================================================

file_path = Path(
    "data/skills.txt"
)

content = file_path.read_text(
    encoding="utf-8"
)

lines = content.splitlines()

for line in lines:
    print(line)


# ============================================================
# 26. Listing Directory Contents
# ============================================================

directory = Path("data")

if directory.exists():

    for item in directory.iterdir():
        print(item)


"""
iterdir() returns the direct contents
of a directory.
"""


# ============================================================
# 27. Checking Items While Iterating
# ============================================================

directory = Path("data")

if directory.exists():

    for item in directory.iterdir():

        if item.is_file():
            print(
                f"File: {item}"
            )

        elif item.is_dir():
            print(
                f"Directory: {item}"
            )


# ============================================================
# 28. Finding Python Files with glob()
# ============================================================

directory = Path(".")

for file_path in directory.glob("*.py"):
    print(file_path)


"""
glob() searches according to a pattern.

*.py

means:

all files ending with .py
"""


# ============================================================
# 29. Finding JSON Files
# ============================================================

directory = Path(".")

for file_path in directory.glob("*.json"):
    print(file_path)


# ============================================================
# 30. Searching a Specific Directory
# ============================================================

directory = Path("data")

for file_path in directory.glob("*.txt"):
    print(file_path)


# ============================================================
# 31. Recursive Search with rglob()
# ============================================================

project = Path("project")

for file_path in project.rglob("*.py"):
    print(file_path)


"""
rglob() searches recursively through subdirectories.

Example:

project/
├── main.py
├── api/
│   └── users.py
└── services/
    └── auth.py

rglob("*.py") can find all three Python files.
"""


# ============================================================
# 32. Recursive Search for JSON Files
# ============================================================

project = Path("project")

for file_path in project.rglob("*.json"):
    print(file_path)


# ============================================================
# 33. Getting File Size
# ============================================================

file_path = Path(
    "data/message.txt"
)

if file_path.exists():

    size = file_path.stat().st_size

    print(
        f"File size: {size} bytes"
    )


"""
stat().st_size returns the file size in bytes.
"""


# ============================================================
# 34. File Metadata
# ============================================================

file_path = Path(
    "data/message.txt"
)

if file_path.exists():

    information = file_path.stat()

    print(
        information
    )


"""
stat() provides filesystem metadata.

It can contain information such as:

- File size
- Modification time
- Access time
- Creation-related information
"""


# ============================================================
# 35. Renaming a File
# ============================================================

old_path = Path(
    "data/old-name.txt"
)

new_path = Path(
    "data/new-name.txt"
)

if old_path.exists():

    old_path.rename(
        new_path
    )


"""
rename() changes the name or location of a path.
"""


# ============================================================
# 36. Moving a File
# ============================================================

source = Path(
    "data/message.txt"
)

destination = Path(
    "data/archive/message.txt"
)

destination.parent.mkdir(
    parents=True,
    exist_ok=True
)

if source.exists():

    source.rename(
        destination
    )


"""
rename() can also be used to move a file
to another directory.
"""


# ============================================================
# 37. Deleting a File
# ============================================================

file_path = Path(
    "data/temporary.txt"
)

if file_path.exists():

    file_path.unlink()


"""
unlink() deletes a file.

Be careful when using it because deletion
can be permanent.
"""


# ============================================================
# 38. Removing an Empty Directory
# ============================================================

directory = Path(
    "data/empty-directory"
)

if directory.exists():

    directory.rmdir()


"""
rmdir() removes an empty directory.

It will fail if the directory contains files
or other directories.
"""


# ============================================================
# 39. Path Comparison
# ============================================================

path_1 = Path("data/users.json")
path_2 = Path("data/users.json")

if path_1 == path_2:
    print("Paths are equal.")


# ============================================================
# 40. Changing File Extension
# ============================================================

path = Path(
    "data/report.txt"
)

new_path = path.with_suffix(
    ".json"
)

print(new_path)


"""
with_suffix() creates a new Path object
with a different extension.

It does not rename the actual file by itself.
"""


# ============================================================
# 41. Changing File Name
# ============================================================

path = Path(
    "data/report.txt"
)

new_path = path.with_name(
    "final-report.txt"
)

print(new_path)


"""
with_name() creates a new path with another file name.
"""


# ============================================================
# 42. Building a Project Structure
# ============================================================

project_root = Path(
    "my-project"
)

directories = [
    project_root / "src",
    project_root / "tests",
    project_root / "data",
    project_root / "config"
]

for directory in directories:

    directory.mkdir(
        parents=True,
        exist_ok=True
    )


# ============================================================
# 43. Creating Project Files
# ============================================================

project_root = Path(
    "my-project"
)

files = [
    project_root / "README.md",
    project_root / "src" / "main.py",
    project_root / "tests" / "test_main.py",
    project_root / "config" / "settings.json"
]

for file_path in files:

    file_path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    file_path.touch(
        exist_ok=True
    )


# ============================================================
# 44. Practical Example: Find All Python Files
# ============================================================

project = Path("my-project")

python_files = list(
    project.rglob("*.py")
)

for file_path in python_files:
    print(file_path)


# ============================================================
# 45. Practical Example: Count Python Files
# ============================================================

project = Path("my-project")

python_files = list(
    project.rglob("*.py")
)

print(
    f"Python files: {len(python_files)}"
)


# ============================================================
# 46. Practical Example: Find All JSON Files
# ============================================================

project = Path("my-project")

json_files = list(
    project.rglob("*.json")
)

for file_path in json_files:
    print(file_path)


# ============================================================
# 47. Practical Example: Find Files by Extension
# ============================================================

project = Path("my-project")

extensions = {
    ".py",
    ".json",
    ".md"
}

for file_path in project.rglob("*"):

    if (
        file_path.is_file()
        and file_path.suffix in extensions
    ):
        print(file_path)


# ============================================================
# 48. Practical Example: List Only Directories
# ============================================================

project = Path("my-project")

for item in project.iterdir():

    if item.is_dir():
        print(item)


# ============================================================
# 49. Practical Example: List Only Files
# ============================================================

project = Path("my-project")

for item in project.iterdir():

    if item.is_file():
        print(item)


# ============================================================
# 50. Practical Example: File Extension Statistics
# ============================================================

project = Path("my-project")

extension_counts = {}

for file_path in project.rglob("*"):

    if file_path.is_file():

        extension = file_path.suffix

        if extension:
            extension_counts[extension] = (
                extension_counts.get(extension, 0) + 1
            )


for extension, count in extension_counts.items():

    print(
        f"{extension}: {count}"
    )


# ============================================================
# 51. Practical Example: Find Large Files
# ============================================================

project = Path("my-project")

for file_path in project.rglob("*"):

    if file_path.is_file():

        size = file_path.stat().st_size

        if size > 1024 * 1024:

            print(
                f"Large file: {file_path}"
            )


"""
1024 * 1024 bytes = approximately 1 MB.
"""


# ============================================================
# 52. Relative Path
# ============================================================

project = Path(
    "my-project/src/main.py"
)

relative_path = project.relative_to(
    "my-project"
)

print(relative_path)


"""
Result:

src/main.py
"""


# ============================================================
# 53. Resolving a Path
# ============================================================

path = Path(
    "my-project/src/main.py"
)

resolved_path = path.resolve()

print(resolved_path)


"""
resolve() produces an absolute, normalized path.
"""


# ============================================================
# 54. Checking Whether One Path Is Inside Another
# ============================================================

project = Path("my-project").resolve()

file_path = Path(
    "my-project/src/main.py"
).resolve()


try:

    file_path.relative_to(project)

    print(
        "File is inside the project."
    )

except ValueError:

    print(
        "File is outside the project."
    )


# ============================================================
# 55. Paths in Backend Projects
# ============================================================

"""
Backend applications frequently need paths for:

- Static files
- Media files
- Templates
- Configuration
- Logs
- Uploaded files
- Database files
- Test data

Example Django-like structure:

project/
├── manage.py
├── config/
├── users/
├── products/
├── static/
├── media/
└── templates/

Pathlib makes working with these locations easier.
"""


# ============================================================
# 56. Pathlib and Configuration
# ============================================================

BASE_DIR = Path(__file__).resolve().parent

print(BASE_DIR)


"""
__file__ represents the current Python file.

resolve() converts it into an absolute path.

parent gets the directory containing the file.

This pattern is very common in Python projects.
"""


# ============================================================
# 57. Building Paths from BASE_DIR
# ============================================================

BASE_DIR = Path(__file__).resolve().parent

data_directory = BASE_DIR / "data"

data_directory.mkdir(
    exist_ok=True
)

data_file = data_directory / "users.json"

print(data_file)


"""
Instead of hard-coding an absolute path, we can
build paths relative to the project location.
"""


# ============================================================
# 58. Pathlib vs String Paths
# ============================================================

"""
Traditional string-based path:

"data/users/profile.json"


Pathlib:

Path("data") / "users" / "profile.json"


Pathlib is usually easier to read, compose,
and maintain.
"""


# ============================================================
# 59. Cross-Platform Paths
# ============================================================

"""
Different operating systems use different path separators.

Windows:

C:\\Users\\Mohsen\\project\\data


Linux/macOS:

/home/mohsen/project/data


Pathlib handles platform-specific path construction.

Example:

path = Path("project") / "data" / "users.json"

This works naturally across operating systems.
"""


# ============================================================
# 60. Best Practices
# ============================================================

"""
Best practices:

1. Prefer pathlib.Path for filesystem paths.
2. Avoid manually concatenating paths with strings.
3. Use / to combine Path objects.
4. Use exists() before operations when appropriate.
5. Use is_file() and is_dir() when type matters.
6. Use mkdir(parents=True, exist_ok=True) for nested
   directory creation.
7. Be careful with unlink() and rmdir().
8. Use glob() for direct pattern matching.
9. Use rglob() for recursive searches.
10. Build project paths from a known base directory.
11. Avoid hard-coded operating-system-specific paths.
12. Use UTF-8 when working with text files.
13. Validate paths that come from external users.
14. Do not blindly delete files based on user input.
"""


# ============================================================
# 61. Summary
# ============================================================

"""
Important pathlib features:

Path()
    Creates a Path object.

Path.cwd()
    Returns the current working directory.

absolute()
    Returns an absolute path.

resolve()
    Resolves a path into an absolute normalized path.

name
    File or directory name.

stem
    File name without extension.

suffix
    File extension.

suffixes
    All file extensions.

parent
    Parent directory.

exists()
    Checks whether a path exists.

is_file()
    Checks whether the path is a file.

is_dir()
    Checks whether the path is a directory.

mkdir()
    Creates a directory.

touch()
    Creates an empty file.

iterdir()
    Lists direct directory contents.

glob()
    Searches using a pattern.

rglob()
    Recursively searches using a pattern.

read_text()
    Reads text.

write_text()
    Writes text.

rename()
    Renames or moves a path.

unlink()
    Deletes a file.

rmdir()
    Removes an empty directory

with_suffix()
    Changes a file suffix in a new Path object.

with_name()
    Changes a file name in a new Path object.

Pathlib is one of the most useful standard-library tools
for real Python projects.
"""