# ==========================================================
# Project: Dynamic Knowledge Base Chatbot
# File: search_documents.py
# Author: Vijayalakshmi Narayanan
# Description:
# Searches the knowledge base using TF-IDF and cosine
# similarity to find the most relevant document.
# ==========================================================

import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

current_dir = os.path.dirname(os.path.abspath(__file__))
folder_path = os.path.join(current_dir, "..", "knowledge_base")

print("Knowledge Base Folder:", folder_path)
print("Files found:", os.listdir(folder_path))

documents = []
filenames = []

# Read documents
for filename in os.listdir(folder_path):
    if filename.endswith(".txt"):
        with open(os.path.join(folder_path, filename), "r", encoding="utf-8") as file:
            documents.append(file.read())
            filenames.append(filename)

# Create TF-IDF vectors
vectorizer = TfidfVectorizer(
    stop_words="english",
    lowercase=True
)

document_vectors = vectorizer.fit_transform(documents)

# Function to search the knowledge base
def search_knowledge_base(query):

    query_vector = vectorizer.transform([query])

    similarity = cosine_similarity(query_vector, document_vectors)

    # Print similarity score for every document
    print("\nSimilarity Scores:")
    for i, filename in enumerate(filenames):
        print(f"{filename}: {similarity[0][i]:.4f}")

    best_match = similarity.argmax()

    best_score = similarity[0][best_match]

    print(f"\nBest Match: {filenames[best_match]}")
    print(f"Best Score: {best_score:.4f}")

    # Minimum similarity required
    if best_score < 0.20:
        return (
            "No matching document",
            "Sorry, I couldn't find an answer in my knowledge base.\n"
            "Please try asking about AI, Python, Machine Learning, "
            "Deep Learning, or another topic available in the knowledge base.",
            best_score
        )

    return (
        filenames[best_match],
        documents[best_match],
        best_score
    )


