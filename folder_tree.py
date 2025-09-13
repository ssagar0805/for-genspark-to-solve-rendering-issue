import os

# Folders or files we usually don't care about
IGNORE_DIRS = {
    '__pycache__', '.git', '.idea', '.vscode', 'node_modules',
    '.venv', 'venv', 'env', '.mypy_cache', '.pytest_cache'
}
IGNORE_FILES = {
    '.DS_Store', 'Thumbs.db'
}

def print_tree(start_path, prefix="", file=None):
    items = sorted(os.listdir(start_path))
    items = [i for i in items if i not in IGNORE_FILES and not i.startswith('.')]

    for index, item in enumerate(items):
        path = os.path.join(start_path, item)
        connector = "├── " if index < len(items) - 1 else "└── "
        line = prefix + connector + item
        print(line)
        if file:
            file.write(line + "\n")

        if os.path.isdir(path) and item not in IGNORE_DIRS:
            extension = "│   " if index < len(items) - 1 else "    "
            print_tree(path, prefix + extension, file)

if __name__ == "__main__":
    ROOT = "."  # current folder
    out_file = "folder_structure.txt"
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(os.path.basename(os.path.abspath(ROOT)) + "\n")
        print(os.path.basename(os.path.abspath(ROOT)))
        print_tree(ROOT, file=f)

    print(f"\nSaved to {out_file}")
