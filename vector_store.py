class VectorStore:
    def __init__(self, index):
        self.index = index

    def query(self, embedding, top_k=5):
        D, I = self.index.search(embedding, top_k)
        return I
