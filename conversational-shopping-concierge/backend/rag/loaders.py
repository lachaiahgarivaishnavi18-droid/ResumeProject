from pathlib import Path


def load_documents(folder: str) -> list[str]:
    docs = []
    root = Path(folder)
    if root.exists():
        for file in sorted(root.rglob('*')):
            if file.is_file():
                docs.append(file.read_text(errors='ignore'))
    return docs
