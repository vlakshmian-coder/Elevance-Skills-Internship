# ==========================================================
# Project: Dynamic Knowledge Base Chatbot
# File: update_knowledge_base.py
# Author: Vijayalakshmi Narayanan
# Description:
# Automatically updates the knowledge base with new documents.
# ==========================================================

import os
import shutil

source_folder = "Project-2/new_documents"
destination_folder = "Project-2/knowledge_base"

for filename in os.listdir(source_folder):

    if filename.endswith(".txt"):

        source = os.path.join(source_folder, filename)
        destination = os.path.join(destination_folder, filename)

        shutil.move(source, destination)

        print(f"Moved: {filename}")

print("\nKnowledge Base Updated Successfully!")