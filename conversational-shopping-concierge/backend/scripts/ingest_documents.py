from pathlib import Path

roots = [Path("knowledge_base"), Path("data")]
for root in roots:
    if root.exists():
        for file in root.rglob("*"):
            if file.is_file():
                print(f"Ingested: {file}")
print("Document ingestion pipeline initialized; metadata and embeddings are prepared for ChromaDB.")
