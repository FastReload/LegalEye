import faiss
from sentence_transformers import SentenceTransformer
import numpy as np
import pandas as pd

class ClauseMatcher:
    def __init__(self, index_path, embeddings_path, csv_path='ledgar_clauses.csv', model_name='all-MiniLM-L6-v2'):
        # Load the Sentence-Transformer model
        self.model = SentenceTransformer(model_name)

        # Load FAISS index
        self.index = faiss.read_index(index_path)

        # Load LEDGAR embeddings (not directly used, but available)
        self.embeddings = np.load(embeddings_path)

        # Load LEDGAR clause texts and metadata from CSV
        self.ledgar_df = pd.read_csv(csv_path)

    def match(self, clause, top_k=5):
        # Encode the input clause
        embedding = self.model.encode([clause])

        # Search the FAISS index for top_k matches
        distances, indices = self.index.search(embedding, top_k)

        # Return a list of dictionaries with match info
        matches = []
        for idx, dist in zip(indices[0], distances[0]):
            clause_text = self.ledgar_df.loc[idx, "clause_text"]
            matches.append({
                "id": idx,
                "text": clause_text,
                "distance": dist
            })

        return matches
