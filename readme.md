# Python Project Generator 🐍

A lightweight command-line tool that automatically creates a clean, ready-to-use Python project structure with essential files and a starter unit test.

## ✨ Features

- Generate a new Python project in seconds.
- Automatically create `main.py`.
- Generate a project-specific `README.md`.
- Include `requirements.txt` and `.gitignore`.
- Create a `tests/` directory with a starter unit test.
- Validate project names.
- Prevent overwriting existing project directories.
- Use Python's standard library without external dependencies.

## 🛠️ Technologies

- Python 3.10+
- pathlib
- re
- unittest
- Python standard library

## 📁 Project Structure

```text
python-project-generator/
├── generator.py
├── README.md
├── requirements.txt
└── .gitignore
```

## ⚙️ Getting Started

### Prerequisites

Install Python 3.10 or later.

### Run the generator

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/python-project-generator.git
cd python-project-generator
```

Run the script:

```bash
python generator.py
```

Enter a project name when prompted, for example:

```text
weather_app
```

The generator creates a new `weather_app/` directory containing the starter files.

### Run the generated project

```bash
cd weather_app
python main.py
```

Expected output:

```text
Hello from your new Python project!
```

### Run the generated test

```bash
python -m unittest discover -s tests -v
```

## 📦 Dependencies

No third-party dependencies are required. The project uses Python's built-in libraries.

## 🔐 Safety

The generator refuses to create a project if the destination directory already exists. Choose a different name if the directory is already present.

## 🎯 Purpose

This project demonstrates Python automation, filesystem operations, input validation, reusable functions, and automated testing.

## 🚀 Future Improvements

- Optional Flask or Streamlit project templates
- Automatic virtual environment setup
- Git initialization option
- Customizable starter files
- Interactive project templates

## 👨‍💻 Author

Shrinivas Naik

GitHub: [@shrinivasnaik25](https://github.com/shrinivasnaik25)

---

If you find this tool useful, consider giving the repository a ⭐.