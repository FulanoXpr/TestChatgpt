def retrieve(query, embedding_model, vector_store, docs, top_k=5):
    query_emb = embedding_model.encode([query])
    indices = vector_store.query(query_emb, top_k)
    return [docs[i] for i in indices[0]]