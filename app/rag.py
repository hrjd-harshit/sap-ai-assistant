from dotenv import load_dotenv
load_dotenv()

import json
import pickle
import numpy as np
import os
from langchain_groq import ChatGroq

def get_answer(question: str) -> str:
    print(f"🔍 Searching knowledge base for: {question}")

    # Debug — check API key
    groq_key = os.getenv("GROQ_API_KEY")
    print(f"🔑 Groq API Key loaded: {bool(groq_key)}")
    if not groq_key:
        return "ERROR: GROQ_API_KEY not found in .env file!"

    # Load chunks and vectorizer
    with open("search_db/chunks.json", "r") as f:
        chunks = json.load(f)
    with open("search_db/vectorizer.pkl", "rb") as f:
        vectorizer = pickle.load(f)

    # Find most relevant chunks
    question_vec = vectorizer.transform([question])
    chunk_vecs = vectorizer.transform(chunks)
    scores = (chunk_vecs * question_vec.T).toarray().flatten()
    top_indices = np.argsort(scores)[::-1][:3]
    context = "\n\n".join([chunks[i] for i in top_indices])

    # Ask Groq
    llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        api_key=groq_key,
        temperature=0
    )

    prompt = f"""You are an SAP Security expert assistant.
Use the following SAP knowledge to answer the question.
If you don't know the answer, say "I don't have information on that."

Context:
{context}

Question: {question}

Answer:"""

    response = llm.invoke(prompt)
    return response.content

if __name__ == "__main__":
    print(get_answer("What is SU53?"))