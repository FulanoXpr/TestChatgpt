import openai

def generate_answer(query, retrieved_docs, openai_key):
    openai.api_key = openai_key
    prompt = f"Context:\n{retrieved_docs}\n\nQuestion: {query}\nAnswer:"
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()