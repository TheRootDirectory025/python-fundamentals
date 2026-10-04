"""
Python Virtual Environments

A virtual environment creates an isolated Python environment for a project.

Why use virtual environments?
- Keep project dependencies isolated.
- Avoid conflicts between different projects.
- Use different package versions for different projects.
- Make projects easier to reproduce.
- Keep the global Python installation clean.

Common commands:

Linux / macOS:
    python3 -m venv .venv
    source .venv/bin/activate
    deactivate

Windows PowerShell:
    python -m venv .venv
    .venv\Scripts\Activate.ps1
    deactivate

Windows CMD:
    python -m venv .venv
    .venv\Scripts\activate.bat
    deactivate

The .venv directory is usually added to .gitignore because it
contains a local copy of the Python environment and installed packages.
"""

import platform
import sys
from pathlib import Path


# ---------------------------------------------------------
# 1. Check the Python interpreter
# ---------------------------------------------------------

print("Python executable:")
print(sys.executable)

print("\nPython version:")
print(platform.python_version())


# ---------------------------------------------------------
# 2. Detect whether a virtual environment is active
# ---------------------------------------------------------

def is_virtual_environment() -> bool:
    """
    Return True when Python is running inside a virtual environment.
    """

    return sys.prefix != sys.base_prefix


print("\nVirtual environment active:")
print(is_virtual_environment())


# ---------------------------------------------------------
# 3. Inspect Python prefixes
# ---------------------------------------------------------

print("\nCurrent Python prefix:")
print(sys.prefix)

print("\nBase Python prefix:")
print(sys.base_prefix)


# ---------------------------------------------------------
# 4. Check the expected .venv directory
# ---------------------------------------------------------

venv_path = Path(".venv")

print("\nExpected virtual environment path:")
print(venv_path)

print("\nDoes .venv exist?")
print(venv_path.exists())


# ---------------------------------------------------------
# 5. Understand the typical project structure
# ---------------------------------------------------------

project_structure = """
my-project/
├── .venv/
├── src/
├── tests/
├── requirements.txt
├── .gitignore
└── README.md
"""

print("\nTypical project structure:")
print(project_structure)


# ---------------------------------------------------------
# 6. Create a virtual environment
# ---------------------------------------------------------

creation_command = "python -m venv .venv"

print("Command to create a virtual environment:")
print(creation_command)


# ---------------------------------------------------------
# 7. Activate the virtual environment
# ---------------------------------------------------------

activation_commands = {
    "Linux / macOS": "source .venv/bin/activate",
    "Windows PowerShell": ".venv\\Scripts\\Activate.ps1",
    "Windows CMD": ".venv\\Scripts\\activate.bat",
}

print("\nActivation commands:")

for operating_system, command in activation_commands.items():
    print(f"{operating_system}: {command}")


# ---------------------------------------------------------
# 8. Deactivate the virtual environment
# ---------------------------------------------------------

print("\nDeactivate command:")
print("deactivate")


# ---------------------------------------------------------
# 9. Why one environment per project?
# ---------------------------------------------------------

projects = {
    "project-a": "Django 5.x",
    "project-b": "Django 4.x",
    "project-c": "FastAPI",
}

print("\nExample of isolated project dependencies:")

for project, dependency in projects.items():
    print(f"{project}: {dependency}")


# ---------------------------------------------------------
# 10. Python executable inside a virtual environment
# ---------------------------------------------------------

print("\nCurrent interpreter information:")

if is_virtual_environment():
    print("Python is running inside a virtual environment.")
else:
    print("Python is running outside a virtual environment.")


# ---------------------------------------------------------
# 11. Recreating an environment
# ---------------------------------------------------------

recreate_steps = [
    "Create a new virtual environment.",
    "Activate the environment.",
    "Install project dependencies.",
]

print("\nTypical environment recreation steps:")

for step_number, step in enumerate(recreate_steps, start=1):
    print(f"{step_number}. {step}")


# ---------------------------------------------------------
# 12. Virtual environments and Git
# ---------------------------------------------------------

gitignore_entry = ".venv/"

print("\nRecommended .gitignore entry:")
print(gitignore_entry)


# ---------------------------------------------------------
# 13. IDE interpreter
# ---------------------------------------------------------

ide_note = """
When using an IDE such as PyCharm or VS Code:

1. Create the virtual environment.
2. Select the Python interpreter inside .venv.
3. Install project dependencies into that environment.
4. Run and test the project using that interpreter.
"""

print("\nIDE setup:")
print(ide_note)


# ---------------------------------------------------------
# 14. Important concept
# ---------------------------------------------------------

concept = """
A virtual environment does not create a completely different Python
language or operating system.

It provides an isolated Python environment where packages installed
for one project do not interfere with packages installed for another.
"""

print("Important concept:")
print(concept)