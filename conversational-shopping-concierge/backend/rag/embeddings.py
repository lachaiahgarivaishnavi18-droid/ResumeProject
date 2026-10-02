class EmbeddingProvider:
    def __init__(self, model: str = 'text-embedding-3-small'):
        self.model = model

    def embed(self, text: str) -> list[float]:
        return [0.0] * 1536
