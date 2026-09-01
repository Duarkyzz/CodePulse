from pathlib import Path


def find_project(path):
    path = Path(path)

    file_path = Path(path)

    for item in path.iterdir():
        if item.is_file():
            print(f"File: {item.name}")
        else:
            print(f"Directory: {item.name}")

find_project("C:\\users\\Dudz\\Desktop\\CodePulse");