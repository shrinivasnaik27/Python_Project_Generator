
from pathlib import Path
import keyword
import re
import textwrap


def normalize_project_name(name: str) -> str:
    """Convert a project name into a safe Python-friendly folder name."""
    name = name.strip().lower()
    name = re.sub(r"[\s-]+", "_", name)
    return name


def validate_project_name(name: str) -> bool:
    """Allow simple folder names that are also valid Python identifiers."""
    return (
        bool(name)
        and name.isidentifier()
        and not keyword.iskeyword(name)
    )


def build_files(project_name: str) -> dict[str, str]:
    """Return the starter files for a new Python project."""
    return {
        "main.py": textwrap.dedent('''\
            def main():
                """Run the application."""
                print("Hello from your new Python project!")


            if __name__ == "__main__":
                main()
        '''),
        "requirements.txt": (
            "# Add third-party packages here, one per line.\\n"
        ),
        ".gitignore": textwrap.dedent('''\
            __pycache__/
            *.py[cod]
            .venv/
            venv/
            env/
            .env
            .pytest_cache/
            .coverage
            htmlcov/
            .idea/
            .vscode/
            .DS_Store
            Thumbs.db
        '''),
        "README.md": textwrap.dedent(f'''\
            # {project_name}

            A Python project generated with Python Project Generator.

            ## Features

            - Simple Python entry point
            - Organized project structure
            - Dependency file
            - Git ignore rules
            - Starter unit test

            ## Requirements

            - Python 3.10 or later

            ## Run the application

            ```bash
            python main.py
            ```

            ## Run tests

            ```bash
            python -m unittest discover -s tests -v
            ```

            ## Dependencies

            Add any third-party packages your application needs to
            `requirements.txt`, then install them with:

            ```bash
            python -m pip install -r requirements.txt
            ```

            ## License

            Add a license before distributing this project if needed.
        '''),
        "tests/__init__.py": "",
        "tests/test_main.py": textwrap.dedent('''\
            import unittest
            from main import main


            class TestMain(unittest.TestCase):
                def test_main_runs_without_error(self):
                    # Calling main should complete successfully.
                    self.assertIsNone(main())


            if __name__ == "__main__":
                unittest.main()
        '''),
    }


def generate_project(name: str, parent: Path | None = None) -> Path:
    """Create a project directory without overwriting existing files."""
    project_name = normalize_project_name(name)

    if not validate_project_name(project_name):
        raise ValueError(
            "Use letters, numbers, and underscores; "
            "the name must not start with a number or be a Python keyword."
        )

    base = (parent or Path.cwd()).resolve()
    target = base / project_name

    # Ensure the project stays inside the selected parent directory.
    if target.parent != base:
        raise ValueError("Invalid project path.")

    if target.exists():
        raise FileExistsError(
            f"'{target}' already exists. Choose another name."
        )

    files = build_files(project_name)

    target.mkdir(parents=True)

    try:
        for relative_path, content in files.items():
            file_path = target / relative_path
            file_path.parent.mkdir(parents=True, exist_ok=True)
            file_path.write_text(content, encoding="utf-8")
    except OSError:
        # Clean up a partially generated project if file creation fails.
        import shutil
        shutil.rmtree(target, ignore_errors=True)
        raise

    return target


def main():
    print("=" * 42)
    print("       PYTHON PROJECT GENERATOR")
    print("=" * 42)
    print("Create a ready-to-use Python project.\\n")

    name = input("Enter project name (e.g. weather_app): ").strip()

    if not name:
        print("Error: Project name cannot be empty.")
        return

    try:
        project_path = generate_project(name)
        print("\\nProject created successfully!")
        print(f"Location: {project_path}")
        print("\\nGenerated files:")

        for path in sorted(project_path.rglob("*")):
            if path.is_file():
                print(f"  - {path.relative_to(project_path)}")

        print("\\nNext steps:")
        print(f"  1. cd {project_path.name}")
        print("  2. python main.py")
        print("  3. python -m unittest discover -s tests -v")

    except (ValueError, FileExistsError, OSError) as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
