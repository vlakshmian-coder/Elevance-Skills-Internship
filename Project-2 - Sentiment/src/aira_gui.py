"""AIRA desktop GUI with knowledge-base, vision, memory, and sentiment support."""

import os
import tkinter as tk
from tkinter import filedialog

from PIL import Image, ImageTk

from conversation_memory import ConversationMemory

from language_support import (
    detect_language,
    translate_to_english,
    translate_from_english,
)

from search_documents import search_knowledge_base
from sentiment_analyzer import detect_sentiment
from vision_assistant import analyse_image


memory = ConversationMemory()
last_uploaded_image = None


def append_to_chat(text):
    """Add text to the read-only conversation panel."""
    chat_box.config(state="normal")
    chat_box.insert(tk.END, text)
    chat_box.config(state="disabled")
    chat_box.see(tk.END)


def sentiment_reply(question):
    """Return a short empathetic response for the user's detected sentiment."""
    # Keep the existing analyzer as the source of truth, while accepting a
    # common informal spelling that is not in its original word list.
    normalized_question = question.lower().replace("thank u", "thank you")
    sentiment = detect_sentiment(normalized_question)

    if sentiment == "Positive":
        return "😊 That's wonderful to hear! I'm happy I could help.\n\n"
    if sentiment == "Negative":
        return "💙 I'm sorry this feels frustrating. Let's work through it together.\n\n"
    return ""


def image_response(question):
    """Answer a question about the most recently uploaded image, if applicable."""
    if last_uploaded_image is None:
        return None

    image_question = question.lower()
    image_terms = (
        "image", "photo", "picture", "size", "width", "height", "format", "mode",
    )
    if not any(term in image_question for term in image_terms):
        return None

    if any(term in image_question for term in ("size", "width", "height", "dimension")):
        return (
            "The uploaded image is "
            f"{last_uploaded_image['width']} × {last_uploaded_image['height']} pixels."
        )
    if "format" in image_question or "file type" in image_question:
        return f"The uploaded image is in {last_uploaded_image['format']} format."
    if "mode" in image_question or "colour" in image_question or "color" in image_question:
        return f"The uploaded image uses {last_uploaded_image['mode']} colour mode."

    return last_uploaded_image["report"]


def send_message(event=None):
    """Process a typed question and show AIRA's response."""
    question = question_entry.get().strip()
    if not question:
        return

    if question.lower() == "show history":
        history = memory.get_history().strip()
        if not history:
            history = "No conversation history available."
        append_to_chat(f"\n📜 Conversation History\n\n{history}\n\n")
        question_entry.delete(0, tk.END)
        return

    append_to_chat(f"\nYou: {question}\n")

    uploaded_image_answer = image_response(question)
    if uploaded_image_answer is not None:
        append_to_chat(f"AIRA:\n{uploaded_image_answer}\n\n")
        memory.add_message(question, uploaded_image_answer)
        question_entry.delete(0, tk.END)
        return

    try:
        user_language = detect_language(question)

        english_question = translate_to_english(question)

        source, answer, score = search_knowledge_base(english_question)

        answer = translate_from_english(answer, user_language)

        reply = sentiment_reply(question)
        append_to_chat(
            "AIRA:\n"
            f"{reply}"
            f"📄 Source: {source}\n"
            f"🎯 Confidence: {score:.2f}\n\n"
            f"{answer}\n\n"
        )
        memory.add_message(question, answer)
    except Exception as error:
        append_to_chat(f"AIRA:\nError: {error}\n\n")

    question_entry.delete(0, tk.END)


def upload_image():
    """Select, analyse, and remember an image for later image-aware questions."""
    file_path = filedialog.askopenfilename(
        title="Select an Image",
        filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp *.gif *.webp")],
    )
    if not file_path:
        return

    try:
        image_name = os.path.basename(file_path)
        report = analyse_image(image_name)

        with Image.open(file_path) as selected_image:
            width, height = selected_image.size
            image_format = selected_image.format or "Unknown"
            image_mode = selected_image.mode

        global last_uploaded_image
        last_uploaded_image = {
            "report": report,
            "width": width,
            "height": height,
            "format": image_format,
            "mode": image_mode,
        }

        append_to_chat(f"\n🖼 Vision Assistant\n\n{report}\n\n")
    except Exception as error:
        append_to_chat(f"\nVision Assistant Error:\n{error}\n\n")


window = tk.Tk()
window.title("AIRA - AI Knowledge Assistant")
window.geometry("900x700")
window.configure(bg="#EAF4FF")

title = tk.Label(
    window,
    text="🤖 AIRA - AI Knowledge Assistant",
    font=("Arial", 20, "bold"),
    bg="#EAF4FF",
    fg="#0B5394",
)
title.pack(pady=15)

current_dir = os.path.dirname(os.path.abspath(__file__))
avatar_path = os.path.join(current_dir, "..", "images", "aira.png")
try:
    avatar_image = Image.open(avatar_path).resize((160, 160))
    avatar_photo = ImageTk.PhotoImage(avatar_image)
    avatar = tk.Label(window, image=avatar_photo, bg="#EAF4FF")
    avatar.image = avatar_photo
    avatar.pack(pady=5)
except (FileNotFoundError, OSError):
    pass

chat_box = tk.Text(window, width=88, height=18, font=("Arial", 11), wrap=tk.WORD)
chat_box.pack(padx=20, pady=10)

# Welcome message
chat_box.insert(
    tk.END,
    "🤖 AIRA: Hello! I am AIRA, your AI Knowledge Assistant.\n\n"
    "I can answer your questions, analyze images, and help you learn.\n"
    "Please type your question below and press Send.\n\n"
)

chat_box.config(state="disabled")

question_label = tk.Label(
    window,
    text="Ask AIRA:",
    font=("Arial", 11, "bold"),
    bg="#EAF4FF",
)
question_label.pack()

question_entry = tk.Entry(window, width=60, font=("Arial", 11))
question_entry.pack(pady=5)
question_entry.bind("<Return>", send_message)

button_frame = tk.Frame(window, bg="#EAF4FF")
button_frame.pack(pady=10)

send_button = tk.Button(
    button_frame,
    text="📨 Send",
    font=("Arial", 11, "bold"),
    bg="#0B5394",
    fg="white",
    activebackground="#1565C0",
    activeforeground="white",
    width=15,
    height=2,
    command=send_message,
)
send_button.pack(side=tk.LEFT, padx=5)

upload_button = tk.Button(
    button_frame,
    text="🖼 Upload Image",
    font=("Arial", 11, "bold"),
    bg="#2E8B57",
    fg="white",
    activebackground="#3CB371",
    activeforeground="white",
    width=15,
    height=2,
    command=upload_image,
)
upload_button.pack(side=tk.LEFT, padx=5)

question_entry.focus_set()
window.mainloop()
