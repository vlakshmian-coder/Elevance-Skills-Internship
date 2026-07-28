# ==========================================================
# Project: Multi-Modal AI Assistant
# File: conversation_memory.py
# Author: Vijayalakshmi Narayanan
# Description:
# Stores conversation history so AIRA can remember
# previous questions and answers.
# ==========================================================

class ConversationMemory:

    def __init__(self):
        self.history = []

    # Save a conversation
    def add_message(self, user_message, assistant_reply):

        self.history.append({
            "user": user_message,
            "assistant": assistant_reply
        })

    # Show all previous conversations
    def get_history(self):
        return self.history

    # Clear memory
    def clear_memory(self):
        self.history = []