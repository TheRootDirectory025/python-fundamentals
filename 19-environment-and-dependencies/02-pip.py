"""
Python pip

pip is Python's package installer.

It is used to:
- Install packages.
- Upgrade packages.
- Remove packages.
- Inspect installed packages.
- Install specific package versions.
- Install packages from requirements files.

Common commands:

Install a package:
    python -m pip install requests

Install a specific version:
    python -m pip install requests==2.32.5

Upgrade a package:
    python -m pip install --upgrade requests

Uninstall a package:
    python -m pip uninstall requests

Show package information:
    python -m pip show requests

List installed packages:
    python -m pip list

Show packages in freeze format:
    python -m pip freeze

Check whether pip is available:
    python -m pip --version

Using "python -m pip" is generally preferred over simply "pip"
because it makes it explicit which Python interpreter is being used.
"""

import subprocess
import sys


# ---------------------------------------------------------
# 1. Check pip version
# ---------------------------------------------------------

print("Checking pip version:")

result = subprocess.run(
    [sys.executable, "-m", "pip", "--version"],
    capture_output=True,
    text=True,
)

print(result.stdout.strip())


# ---------------------------------------------------------
# 2. Understand python -m pip
# ---------------------------------------------------------

print("\nCurrent Python executable:")
print(sys.executable)

print("\nRecommended pip command:")
print(f"{sys.executable} -m pip")


# ---------------------------------------------------------
# 3. Common pip commands
# ---------------------------------------------------------

pip_commands = {
    "Install package": "python -m pip install requests",
    "Install specific version": "python -m pip install requests==2.32.5",
    "Upgrade package": "python -m pip install --upgrade requests",
    "Uninstall package": "python -m pip uninstall requests",
    "Show package": "python -m pip show requests",
    "List packages": "python -m pip list",
    "Freeze packages": "python -m pip freeze",
}

print("\nCommon pip commands:")

for description, command in pip_commands.items():
    print(f"{description}:")
    print(f"  {command}")


# ---------------------------------------------------------
# 4. Install packages into a virtual environment
# ---------------------------------------------------------

print("\nRecommended workflow:")

workflow = [
    "Create a virtual environment.",
    "Activate the virtual environment.",
    "Upgrade pip.",
    "Install project dependencies.",
    "Verify installed packages.",
]

for step_number, step in enumerate(workflow, start=1):
    print(f"{step_number}. {step}")


# ---------------------------------------------------------
# 5. Upgrade pip
# ---------------------------------------------------------

upgrade_command = "python -m pip install --upgrade pip"

print("\nUpgrade pip:")
print(upgrade_command)


# ---------------------------------------------------------
# 6. Install a package
# ---------------------------------------------------------

install_command = "python -m pip install requests"

print("\nInstall a package:")
print(install_command)


# ---------------------------------------------------------
# 7. Install a specific package version
# ---------------------------------------------------------

version_command = "python -m pip install Django==5.2"

print("\nInstall a specific package version:")
print(version_command)


# ---------------------------------------------------------
# 8. Version constraints
# ---------------------------------------------------------

version_constraints = {
    "Exact version": "Django==5.2",
    "Minimum version": "Django>=5.2",
    "Maximum version": "Django<6.0",
    "Compatible release": "Django~=5.2",
}

print("\nVersion constraints:")

for description, requirement in version_constraints.items():
    print(f"{description}: {requirement}")


# ---------------------------------------------------------
# 9. Upgrade a package
# ---------------------------------------------------------

upgrade_package_command = "python -m pip install --upgrade requests"

print("\nUpgrade a package:")
print(upgrade_package_command)


# ---------------------------------------------------------
# 10. Uninstall a package
# ---------------------------------------------------------

uninstall_command = "python -m pip uninstall requests"

print("\nUninstall a package:")
print(uninstall_command)


# ---------------------------------------------------------
# 11. Inspect an installed package
# ---------------------------------------------------------

show_command = "python -m pip show requests"

print("\nShow package information:")
print(show_command)


# ---------------------------------------------------------
# 12. List installed packages
# ---------------------------------------------------------

list_command = "python -m pip list"

print("\nList installed packages:")
print(list_command)


# ---------------------------------------------------------
# 13. Freeze installed packages
# ---------------------------------------------------------

freeze_command = "python -m pip freeze"

print("\nFreeze installed packages:")
print(freeze_command)


# ---------------------------------------------------------
# 14. pip freeze output
# ---------------------------------------------------------

example_freeze_output = """
Django==5.2
requests==2.32.5
urllib3==2.5.0
"""

print("Example pip freeze output:")
print(example_freeze_output)


# ---------------------------------------------------------
# 15. Package dependencies
# ---------------------------------------------------------

dependency_example = """
Django
├── asgiref
└── sqlparse
"""

print("Example dependency relationship:")
print(dependency_example)


# ---------------------------------------------------------
# 16. Direct vs transitive dependencies
# ---------------------------------------------------------

dependency_types = {
    "Direct dependency": "A package your project explicitly installs.",
    "Transitive dependency": "A package installed because another package needs it.",
}

print("Dependency types:")

for dependency_type, description in dependency_types.items():
    print(f"{dependency_type}: {description}")


# ---------------------------------------------------------
# 17. Verify an installed package
# ---------------------------------------------------------

check_command = "python -m pip check"

print("\nCheck installed package dependencies:")
print(check_command)


# ---------------------------------------------------------
# 18. Upgrade all packages
# ---------------------------------------------------------

upgrade_all_note = """
pip does not provide a simple built-in command that should blindly
upgrade every package in a production project.

Dependency upgrades should be intentional and tested.
"""

print("Package upgrade note:")
print(upgrade_all_note)


# ---------------------------------------------------------
# 19. pip and virtual environments
# ---------------------------------------------------------

environment_note = """
When a virtual environment is active, pip installs packages into
that environment instead of the global Python environment.

Always verify the active interpreter before installing packages.
"""

print("pip and virtual environments:")
print(environment_note)


# ---------------------------------------------------------
# 20. Practical backend example
# ---------------------------------------------------------

backend_dependencies = [
    "Django",
    "djangorestframework",
    "psycopg",
    "redis",
    "celery",
]

print("\nExample backend dependencies:")

for dependency in backend_dependencies:
    print(f"- {dependency}")


# ---------------------------------------------------------
# 21. Recommended backend installation
# ---------------------------------------------------------

backend_install_command = (
    "python -m pip install "
    "Django "
    "djangorestframework "
    "psycopg "
    "redis "
    "celery"
)

print("\nExample backend installation command:")
print(backend_install_command)


# ---------------------------------------------------------
# 22. Best practices
# ---------------------------------------------------------

best_practices = [
    "Use a virtual environment for each project.",
    "Prefer python -m pip over plain pip.",
    "Pin important production dependencies.",
    "Review dependency upgrades before applying them.",
    "Use requirements files for reproducible installations.",
    "Do not commit the .venv directory to Git.",
    "Run pip check when debugging dependency conflicts.",
]

print("\nBest practices:")

for practice in best_practices:
    print(f"- {practice}")