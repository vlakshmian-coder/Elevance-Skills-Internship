import streamlit as st
from pathlib import Path

# Page Configuration
st.set_page_config(
    page_title="Professor Arvind AI Research Assistant",
    page_icon="📚",
    layout="wide"
)

# Title
st.markdown(
    """
    <h3 style='text-align:center; margin-bottom:5px;'>
    👨‍🏫 Professor Arvind AI Research Assistant
    </h3>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <h4 style='text-align:center; color:#6C757D;'>
    Helping researchers explore, summarize and understand scientific literature using Artificial Intelligence.
    </h4>
    """,
    unsafe_allow_html=True
)
st.divider()

# Professor Image
image_path = Path(__file__).parent / "images" / "professor_arvind.png"

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.image(image_path, width=250)
    st.caption(
    "🛈 The profile image shown above is an AI-generated illustrative avatar created for this educational project and does not represent an actual photograph of Professor Arvind."
)



# Welcome Message
st.subheader("Welcome!")

st.write("""
This AI Research Assistant helps users:

- 📚 Explore research publications
- 📝 Summarize research papers
- 💬 Ask questions about research topics
- 🤖 Learn through AI-powered conversations
""")

st.info(
    "🚀 This project is currently under development."
)

# Input Box
question = st.text_input(
    "Ask a research question:"
)

# Button
if st.button("Submit"):

    if question.strip() == "":
        st.warning("Please enter a question.")

    else:
        st.success("Research Assistant is under development.")
        st.write("Your Question:")
        st.write(question)

st.divider()

st.markdown("---")

st.caption(
    "© 2026 Professor Arvind AI Research Assistant | "
    "Developed by Vijayalakshmi Narayanan | "
    "Educational Research Project"
)