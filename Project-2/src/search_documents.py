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

folder_path = "Project-1/knowledge_base"

documents = []
filenames = []

# Read documents
for filename in os.listdir(folder_path):
    if filename.endswith(".txt"):
        with open(os.path.join(folder_path, filename), "r", encoding="utf-8") as file:
            documents.append(file.read())
            filenames.append(filename)

# Create TF-IDF vectors
vectorizer = TfidfVectorizer()

document_vectors = vectorizer.fit_transform(documents)

# User query
while True:

    query = input("\nAsk a question (or type exit): ")

    if query.lower() == "exit":
        print("Goodbye!")
        break

    query_vector = vectorizer.transform([query])

    similarity = cosine_similarity(query_vector, document_vectors)

    best_match = similarity.argmax()

    print("\nMost Relevant Document:")
    print(filenames[best_match])

    print("\nSimilarity Score:")
    print(f"{similarity[0][best_match]:.2f}")

    print("\nContent:\n")
    print(documents[best_match])


