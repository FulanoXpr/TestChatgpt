import os

def load_documents(data_dir):
    """Loads documents from a directory."""
    docs = []
    for filename in os.listdir(data_dir):
        if filename.endswith('.txt'):
            with open(os.path.join(data_dir, filename), 'r', encoding='utf-8') as f:
                docs.append(f.read())
    return docs
