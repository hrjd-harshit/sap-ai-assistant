from dotenv import load_dotenv
load_dotenv()

import json
import os
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle

def ingest_docs():
    print("📄 Loading SAP knowledge base...")
    with open("docs/sap_security.txt", "r") as f:
        text = f.read()

    # Split into chunks
    chunks = [chunk.strip() for chunk in text.split("\n\n") if chunk.strip()]

    print("🔢 Creating TF-IDF index...")
    vectorizer = TfidfVectorizer()
    vectorizer.fit(chunks)

    # Save chunks and vectorizer
    os.makedirs("search_db", exist_ok=True)
    with open("search_db/chunks.json", "w") as f:
        json.dump(chunks, f)
    with open("search_db/vectorizer.pkl", "wb") as f:
        pickle.dump(vectorizer, f)

    print("✅ Knowledge base ingested successfully!")
    print(f"📊 Total chunks stored: {len(chunks)}")

if __name__ == "__main__":
    ingest_docs()