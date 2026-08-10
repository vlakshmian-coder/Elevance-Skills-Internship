import os
import sys
import streamlit as st
from PIL import Image

# ----------------------------------------------------
# Configure Streamlit page
# ----------------------------------------------------

st.set_page_config(
    page_title="Medical AIRA",
    page_icon="🩺",
    layout="centered"
)

# ----------------------------------------------------
# Add src folder to Python path
# ----------------------------------------------------

current_dir = os.path.dirname(os.path.abspath(__file__))
src_path = os.path.join(current_dir, "src")
sys.path.append(src_path)

from search_documents import search_knowledge_base

# ----------------------------------------------------
# Initialize Chat History
# ----------------------------------------------------

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ----------------------------------------------------
# Load Avatar
# ----------------------------------------------------

image_path = os.path.join(
    current_dir,
    "images",
    "aira.png"
)

avatar = Image.open(image_path)

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.image(avatar, width=180)

# ----------------------------------------------------
# Header
# ----------------------------------------------------

st.markdown(
    "🩺 Medical AIRA",
    unsafe_allow_html=True
)

st.markdown(
    "Your AI Medical Assistant",
    unsafe_allow_html=True
)

st.markdown("""
Welcome to **Medical AIRA**!

📚 Powered by the **MedQuAD Medical Knowledge Base**

You can ask about:

- 🩺 Diseases
- 🤒 Symptoms
- 🔬 Diagnosis
- 💊 Treatments
- 💉 Medications
- ❤️ General Health
""")

st.divider()

# ----------------------------------------------------
# User Question
# ----------------------------------------------------

question = st.text_input(
    "Ask your medical question"
)

# ----------------------------------------------------
# Ask Button
# ----------------------------------------------------

if st.button("🔍 Ask Medical AIRA"):

    if question.strip() == "":
        st.warning("Please enter a medical question.")

    else:

        with st.spinner(
            "Searching the MedQuAD medical knowledge base..."
        ):

            source, answer, score = search_knowledge_base(question)

        # Save conversation to session state
        st.session_state.chat_history.append({
            "question": question,
            "source": source,
            "answer": answer,
            "score": score
        })

# ----------------------------------------------------
# Display Conversation History
# ----------------------------------------------------

if st.session_state.chat_history:

    st.divider()

    st.subheader("💬 Medical AIRA Conversation")

    for chat in st.session_state.chat_history:

        st.markdown("### 🧑 Your Question")

        st.write(chat["question"])

        st.markdown("### 🩺 Medical AIRA's Response")

        with st.container(border=True):

            st.markdown(
                f"**📄 Source:** {chat['source']}"
            )

            st.markdown(
                f"**🎯 Confidence:** {chat['score']:.2f}"
            )

            st.write(chat["answer"])

# ----------------------------------------------------
# Disclaimer
# ----------------------------------------------------

st.divider()

st.caption(
    "⚠️ This AI assistant is for educational purposes only. "
    "It should not replace professional medical advice, diagnosis, or treatment."
)
