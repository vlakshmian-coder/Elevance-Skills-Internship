import tkinter as tk

# Create main window
window = tk.Tk()

# Window title
window.title("AIRA - AI Knowledge Assistant")

# Window size
window.geometry("900x600")

# Background colour
window.configure(bg="#EAF4FF")

# Heading
title = tk.Label(
    window,
    text="🤖 AIRA - AI Knowledge Assistant",
    font=("Arial", 20, "bold"),
    bg="#EAF4FF",
    fg="#0B5394"
)

title.pack(pady=20)
from PIL import Image, ImageTk
from search_documents import search_knowledge_base
from conversation_memory import ConversationMemory

memory = ConversationMemory()

# Load AIRA avatar

import os

# Get the folder where this Python file is located
current_dir = os.path.dirname(os.path.abspath(__file__))

# Build the correct path to the image
image_path = os.path.join(current_dir, "..", "images", "aira.png")

image = Image.open(image_path)
image = image.resize((220, 220))

photo = ImageTk.PhotoImage(image)

avatar = tk.Label(window, image=photo, bg="#EAF4FF")
avatar.image = photo
avatar.pack(pady=10)
# Chat display
chat_box = tk.Text(
    window,
    height=12,
    width=60,
    font=("Arial", 11),
    wrap="word"
)

chat_box.pack(pady=10)

chat_box.insert(
    tk.END,
    "👩 AIRA:\nWelcome! I’m AIRA, your AI Knowledge Assistant.\nAsk me about AI, Python, Machine Learning, Deep Learning, or any topic in the knowledge base.\n\n"
)

chat_box.config(state="disabled")
# Function when Send button is clicked
def send_message():

    question = question_entry.get()

    if question.strip() == "":
        return

    chat_box.config(state="normal")

    chat_box.insert(tk.END, f"\nYou: {question}\n")

    try:
        source, answer, score = search_knowledge_base(question)

        chat_box.insert(
            tk.END,
            f"AIRA:\n"
            f"📄 Source: {source}\n"
            f"🎯 Confidence: {score:.2f}\n\n"
            f"{answer}\n\n"
        )

        # Save conversation in memory
        memory.add_message(question, answer)
        
        print(memory.get_history())

    except Exception as e:
        chat_box.insert(
            tk.END,
            f"AIRA:\nError: {e}\n\n"
        )

    chat_box.config(state="disabled")

    chat_box.see(tk.END)

    question_entry.delete(0, tk.END)

# Question label
question_label = tk.Label(
    window,
    text="Ask AIRA:",
    font=("Arial", 11, "bold"),
    bg="#EAF4FF"
)

question_label.pack()

# Question entry
question_entry = tk.Entry(
    window,
    width=55,
    font=("Arial", 11)
)

question_entry.pack(pady=5)

# Send button
send_button = tk.Button(
    window,
    text="📨 Send",
    font=("Arial", 11, "bold"),
    bg="#0B5394",
    fg="white",
    activebackground="#1565C0",
    activeforeground="white",
    width=15,
    height=2,
    command=send_message
)

send_button.pack(pady=10)

window.mainloop()