import numpy as np
import pandas as pd
import faiss
from datasets import load_dataset
from sentence_transformers import SentenceTransformer

def build_ledgar_index(output_index_path="ledgar_index.faiss", output_embeddings_path="ledgar_embeddings.npy", output_csv_path="ledgar_clauses.csv"):
    # Load LEDGAR dataset
    dataset = load_dataset("lex_glue", "ledgar", split="train")
    clauses = dataset["text"]
    labels = [dataset.features["label"].int2str(l) for l in dataset["label"]]

    # Save metadata (optional)
    df = pd.DataFrame({
        "id": [i for i in range(len(clauses))],
        "clause_text": clauses,
        "label": labels
    })
    df.to_csv(output_csv_path, index=False)

    # Encode using Sentence-Transformer
    model = SentenceTransformer("all-MiniLM-L6-v2")
    print("Encoding LEDGAR clauses...")
    embeddings = model.encode(clauses, convert_to_numpy=True, show_progress_bar=True)

    # Save embeddings for later use
    np.save(output_embeddings_path, embeddings)

    # Build FAISS index
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings.astype('float32'))

    # Save index
    faiss.write_index(index, output_index_path)
    print("FAISS index and embeddings saved.")

if __name__ == "__main__":
    build_ledgar_index()
