
from pathlib import Path


def find_project(path, root):
    path = Path(path)
    files = []

    for item in path.iterdir():
        if item.is_file():
            item = item.relative_to(root)
            files.append(item)

        elif item.is_dir():
            files.extend(find_project(item, root))

    return files
 
root = Path("C:\\users\\Dudz\\Desktop\\CodePulse")

result = find_project(root, root)

print(result)