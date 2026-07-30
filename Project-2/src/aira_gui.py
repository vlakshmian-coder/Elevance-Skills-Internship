from tkinter import filedialog
from vision_assistant import analyse_image

import tkinter as tk
from PIL import Image, ImageTk
from search_documents import search_knowledge_base
from conversation_memory import ConversationMemory
import os

memory = ConversationMemory()

window = tk.Tk()
window.title("AIRA - AI Knowledge Assistant")
window.geometry("900x600")
window.configure(bg="#EAF4FF")

title = tk.Label(window,text="🤖 AIRA - AI Knowledge Assistant",
                 font=("Arial",20,"bold"),bg="#EAF4FF",fg="#0B5394")
title.pack(pady=20)

current_dir=os.path.dirname(os.path.abspath(__file__))
image_path=os.path.join(current_dir,"..","images","aira.png")
image=Image.open(image_path).resize((220,220))
photo=ImageTk.PhotoImage(image)
avatar=tk.Label(window,image=photo,bg="#EAF4FF")
avatar.image=photo
avatar.pack(pady=10)

chat_box=tk.Text(window,height=12,width=60,font=("Arial",11),wrap="word")
chat_box.pack(pady=10)
chat_box.insert(tk.END,"👩 AIRA:\nWelcome! I'm AIRA, your AI Knowledge Assistant.\nAsk me about AI, Python, Machine Learning, Deep Learning, or any topic in the knowledge base.\n\n")
chat_box.config(state="disabled")

def send_message():
    question=question_entry.get().strip()
    if not question:
        return
    chat_box.config(state="normal")
    if question.lower()=="show history":
        history=memory.get_history().strip()
        if not history:
            history="No conversation history available."
        chat_box.insert(tk.END,"\n📜 Conversation History\n\n"+history+"\n\n")
        chat_box.config(state="disabled")
        chat_box.see(tk.END)
        question_entry.delete(0,tk.END)
        return
    chat_box.insert(tk.END,f"\nYou: {question}\n")
    try:
        source,answer,score=search_knowledge_base(question)
        chat_box.insert(tk.END,f"AIRA:\n📄 Source: {source}\n🎯 Confidence: {score:.2f}\n\n{answer}\n\n")
        memory.add_message(question,answer)
    except Exception as e:
        chat_box.insert(tk.END,f"AIRA:\nError: {e}\n\n")
    chat_box.config(state="disabled")
    chat_box.see(tk.END)
    question_entry.delete(0,tk.END)

def upload_image():

    file_path = filedialog.askopenfilename(

        title="Select an Image",

        filetypes=[
            ("Image Files", "*.png *.jpg *.jpeg *.bmp")
        ]
    )

    if not file_path:
        return

    import os

    image_name = os.path.basename(file_path)

    try:

        result = analyse_image(image_name)

        chat_box.config(state="normal")

        chat_box.insert(

            tk.END,

            "\n🖼 Vision Assistant\n\n"

            + result

            + "\n\n"

        )

        chat_box.config(state="disabled")

        chat_box.see(tk.END)

    except Exception as e:

        chat_box.config(state="normal")

        chat_box.insert(

            tk.END,

            f"\nVision Assistant Error:\n{e}\n\n"

        )

        chat_box.config(state="disabled")

# Question label
question_label=tk.Label(window,text="Ask AIRA:",font=("Arial",11,"bold"),bg="#EAF4FF")
question_label.pack()
question_entry=tk.Entry(window,width=55,font=("Arial",11))
question_entry.pack(pady=5)
send_button=tk.Button(window,text="📨 Send",font=("Arial",11,"bold"),
bg="#0B5394",fg="white",activebackground="#1565C0",activeforeground="white",
width=15,height=2,command=send_message)
send_button.pack(pady=10)

upload_button = tk.Button(

    window,

    text="🖼 Upload Image",

    font=("Arial", 11, "bold"),

    bg="#2E8B57",

    fg="white",

    activebackground="#3CB371",

    activeforeground="white",

    width=15,

    height=2,

    command=upload_image

)

upload_button.pack(pady=5)

window.mainloop()
