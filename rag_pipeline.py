def rag_pipeline(query, data_dir, embedding_model, vector_store, docs, openai_key):
    # Retrieve relevant docs
    retrieved_docs = retrieve(query, embedding_model, vector_store, docs)
    # Generate answer
    answer = generate_answer(query, " ".join(retrieved_docs), openai_key)
    return answer
