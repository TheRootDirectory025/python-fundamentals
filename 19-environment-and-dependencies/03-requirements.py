"""
Python Requirements Files

A requirements file records the Python packages and versions
required by a project.

The most common filename is:

    requirements.txt

It allows another developer or a deployment environment to
install the same project dependencies.

Common commands:

Create requirements.txt:
    python -m pip freeze > requirements.txt

Install dependencies:
    python -m pip install -r requirements.txt

Upgrade dependencies:
    python -m pip install --upgrade -r requirements.txt

Check installed packages:
    python -m pip list

Check dependency conflicts:
    python -m pip check

A requirements.txt file should normally be committed to Git,
while the .venv directory should not be committed.
"""


# ---------------------------------------------------------
# 1. What is requirements.txt?
# ---------------------------------------------------------

print("requirements.txt stores project dependencies.")

print(
    """
Example:

Django==5.2
djangorestframework==3.16.0
requests==2.32.5
"""
)


# ---------------------------------------------------------
# 2. Create requirements.txt
# ---------------------------------------------------------

create_command = "python -m pip freeze > requirements.txt"

print("\nCreate requirements.txt:")
print(create_command)


# ---------------------------------------------------------
# 3. Install requirements
# ---------------------------------------------------------

install_command = "python -m pip install -r requirements.txt"

print("\nInstall project dependencies:")
print(install_command)


# ---------------------------------------------------------
# 4. Upgrade requirements
# ---------------------------------------------------------

upgrade_command = "python -m pip install --upgrade -r requirements.txt"

print("\nUpgrade dependencies:")
print(upgrade_command)


# ---------------------------------------------------------
# 5. Exact versions
# ---------------------------------------------------------

exact_versions = """
Django==5.2
requests==2.32.5
"""

print("\nExact versions:")
print(exact_versions)


# ---------------------------------------------------------
# 6. Version ranges
# ---------------------------------------------------------

version_ranges = {
    "Minimum version": "Django>=5.2",
    "Maximum version": "Django<6.0",
    "Range": "Django>=5.2,<6.0",
    "Compatible release": "Django~=5.2",
}

print("Version ranges:")

for description, requirement in version_ranges.items():
    print(f"{description}: {requirement}")


# ---------------------------------------------------------
# 7. Direct dependencies
# ---------------------------------------------------------

direct_dependencies = [
    "Django",
    "djangorestframework",
    "psycopg",
    "redis",
    "celery",
]

print("\nExample direct dependencies:")

for dependency in direct_dependencies:
    print(f"- {dependency}")


# ---------------------------------------------------------
# 8. Transitive dependencies
# ---------------------------------------------------------

transitive_dependency_example = """
Your project
    |
    +-- Django
    |     |
    |     +-- asgiref
    |     +-- sqlparse
    |
    +-- requests
          |
          +-- urllib3
          +-- certifi
"""

print("\nExample dependency tree:")
print(transitive_dependency_example)


# ---------------------------------------------------------
# 9. requirements.txt and virtual environments
# ---------------------------------------------------------

workflow = [
    "Create a virtual environment.",
    "Activate the virtual environment.",
    "Install project dependencies.",
    "Run the project.",
    "Freeze dependencies into requirements.txt.",
]

print("Typical project workflow:")

for step_number, step in enumerate(workflow, start=1):
    print(f"{step_number}. {step}")


# ---------------------------------------------------------
# 10. Clone and setup workflow
# ---------------------------------------------------------

clone_workflow = [
    "Clone the repository.",
    "Create a new virtual environment.",
    "Activate the environment.",
    "Install requirements.txt.",
    "Run the project.",
]

print("\nSetup workflow after cloning:")

for step_number, step in enumerate(clone_workflow, start=1):
    print(f"{step_number}. {step}")


# ---------------------------------------------------------
# 11. requirements.txt example
# ---------------------------------------------------------

requirements_example = """
Django==5.2
djangorestframework==3.16.0
psycopg==3.2.9
redis==6.4.0
celery==5.5.3
"""

print("\nExample requirements.txt:")
print(requirements_example)


# ---------------------------------------------------------
# 12. Development dependencies
# ---------------------------------------------------------

development_dependencies = """
Development dependencies are packages used during development,
testing, linting, formatting, or debugging.

Examples:

pytest
ruff
black
mypy
"""

print("Development dependencies:")
print(development_dependencies)


# ---------------------------------------------------------
# 13. Separate requirements files
# ---------------------------------------------------------

separate_files = """
A larger project may use separate files:

requirements/
├── base.txt
├── development.txt
└── production.txt

development.txt can include base dependencies plus
development-only tools.
"""

print("Separate requirements files:")
print(separate_files)


# ---------------------------------------------------------
# 14. requirements files with -r
# ---------------------------------------------------------

include_command = "-r base.txt"

print("Include another requirements file:")
print(include_command)


# ---------------------------------------------------------
# 15. Git and requirements.txt
# ---------------------------------------------------------

git_rules = {
    "requirements.txt": "Commit to Git",
    ".venv/": "Do not commit",
    "__pycache__/": "Do not commit",
}

print("\nRecommended Git rules:")

for path, rule in git_rules.items():
    print(f"{path}: {rule}")


# ---------------------------------------------------------
# 16. Dependency reproducibility
# ---------------------------------------------------------

reproducibility_note = """
A requirements file helps make the environment reproducible.

The goal is to make sure that developers, CI systems, and
deployment environments install compatible dependencies.
"""

print("Dependency reproducibility:")
print(reproducibility_note)


# ---------------------------------------------------------
# 17. Dependency verification
# ---------------------------------------------------------

verification_commands = [
    "python -m pip list",
    "python -m pip freeze",
    "python -m pip check",
]

print("Dependency verification commands:")

for command in verification_commands:
    print(f"- {command}")


# ---------------------------------------------------------
# 18. Security and maintenance
# ---------------------------------------------------------

maintenance_rules = [
    "Keep dependencies reasonably up to date.",
    "Review major version upgrades carefully.",
    "Test the project after dependency upgrades.",
    "Remove unused dependencies.",
    "Avoid blindly installing packages you do not need.",
]

print("\nDependency maintenance:")

for rule in maintenance_rules:
    print(f"- {rule}")


# ---------------------------------------------------------
# 19. Backend project example
# ---------------------------------------------------------

backend_setup = """
Backend project:

python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
"""

print("Example backend setup:")
print(backend_setup)


# ---------------------------------------------------------
# 20. Best practices
# ---------------------------------------------------------

best_practices = [
    "Keep requirements files in version control.",
    "Use a virtual environment for local development.",
    "Use explicit versions when reproducibility matters.",
    "Separate development and production dependencies when useful.",
    "Review dependency changes before committing.",
    "Do not commit .venv.",
]

print("Best practices:")

for practice in best_practices:
    print(f"- {practice}")