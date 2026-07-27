from pathlib import Path


def scan_repository(repository_path: str):
    """
    Scan a repository and return every file.
    """

    root = Path(repository_path)

    files = []

    for item in root.rglob("*"):
        # reads all folders and files within the root path
        if item.is_file():
            # filters out only the files
            files.append(item)

    return files