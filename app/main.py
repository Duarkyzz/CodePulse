IGNORED_DIRS = {
    ".git",
    "__pycache__",
    "venv",
    ".venv",
    "node_modules"
}

from pathlib import Path


def find_project(path):
    path = Path(path)

    for ignored_dir in IGNORED_DIRS:
        ignored_path = path / ignored_dir
        if ignored_path.exists() and ignored_path.is_dir():
            print(f"Ignored Directory: {ignored_dir}")

        else:
            print(f"Searching in: {path}")

    for item in path.iterdir():
        if item.is_file():
            print(f"File: {item.name}")

        elif item.is_dir():
            print(f"Directory: {item.name}")
            find_project(item)  # Recursively search in subdirectories
 
find_project("C:\\users\\Dudz\\Desktop\\CodePulse");