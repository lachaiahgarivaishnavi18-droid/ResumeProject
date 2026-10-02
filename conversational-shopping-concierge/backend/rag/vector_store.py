class VectorStore:
    def __init__(self):
        self.documents = []

    def add_documents(self, documents: list[dict]) -> None:
        self.documents.extend(documents)

    def similarity_search(self, query: str, k: int = 3) -> list[dict]:
        return [{"content": query, "metadata": {"source": "mock-document"}} for _ in range(min(k, len(self.documents) or 1))]
