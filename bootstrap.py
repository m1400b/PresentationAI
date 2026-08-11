"""
PresentationAI Bootstrap

Initializes the PresentationAI project structure.

Author: ChatGPT & User
Version: 0.1.0
"""

from pathlib import Path
import json

# ----------------------------------------------------------------------
# Project Information
# ----------------------------------------------------------------------

PROJECT_NAME = "PresentationAI"

ROOT = Path(__file__).parent.resolve()

# ----------------------------------------------------------------------
# Folder Structure
# ----------------------------------------------------------------------

DIRECTORIES = [

    "src",

    "src/ai",
    "src/assets",
    "src/config",
    "src/core",
    "src/data",
    "src/database",
    "src/models",
    "src/presentation",
    "src/services",
    "src/ui",
    "src/utils",

    "assets",
    "assets/fonts",
    "assets/icons",
    "assets/images",
    "assets/logos",

    "database",

    "logs",

    "output",

    "plugins",

    "projects",

    "templates",

    "themes",

    "tests"

]

# ----------------------------------------------------------------------
# Files
# ----------------------------------------------------------------------

FILES = {

    "README.md": f"# {PROJECT_NAME}\n",

    ".gitignore":
"""__pycache__/
*.pyc
*.pyo
*.pyd
*.db
*.log
.venv/
.idea/
.vscode/
output/
""",

    "launcher.py":
'''"""
Application Entry Point
"""

def main():

    print("PresentationAI Started")

if __name__ == "__main__":
    main()
''',

    "src/config/settings.json":
json.dumps(
{
    "language": "fa",
    "theme": "Corporate",
    "database": "database/app.db",
    "output": "output",
    "default_ai": "ollama",
    "autosave": True,
    "version": "0.1.0"
},
indent=4,
ensure_ascii=False
),

}

# ----------------------------------------------------------------------
# Helper Functions
# ----------------------------------------------------------------------

def create_directories():

    print("Creating folders...")

    for folder in DIRECTORIES:

        path = ROOT / folder

        path.mkdir(parents=True, exist_ok=True)

        print(f"  ✓ {folder}")


def create_init_files():

    print("\nCreating __init__.py files...")

    for folder in DIRECTORIES:

        if folder.startswith("src"):

            init_file = ROOT / folder / "__init__.py"

            if not init_file.exists():

                init_file.write_text(
                    '"""Package"""\n',
                    encoding="utf-8"
                )

                print(f"  ✓ {init_file.relative_to(ROOT)}")


def create_files():

    print("\nCreating files...")

    for filename, content in FILES.items():

        path = ROOT / filename

        if not path.exists():

            path.parent.mkdir(parents=True, exist_ok=True)

            path.write_text(content, encoding="utf-8")

            print(f"  ✓ {filename}")


def create_database():

    db = ROOT / "database" / "app.db"

    if not db.exists():

        db.touch()

        print("\n✓ SQLite database created")


# ----------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------

def main():

    print("=" * 60)
    print(PROJECT_NAME)
    print("Bootstrap v0.1")
    print("=" * 60)

    create_directories()

    create_init_files()

    create_files()

    create_database()

    print("\nProject initialized successfully.")


if __name__ == "__main__":

    main()