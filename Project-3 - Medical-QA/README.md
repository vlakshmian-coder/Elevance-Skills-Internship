# Medical AIRA – Medical Q&A Chatbot

## Project Overview

Medical AIRA is a conversational medical question-answering assistant developed using the MedQuAD dataset.

The project was implemented as a Streamlit application that allows users to ask medical questions and retrieve relevant information from a curated medical question-answering knowledge base.

The project follows the Elevance Skills internship requirement to develop a specialized Medical Q&A chatbot using the MedQuAD dataset and a retrieval mechanism.

## Internship Requirement

The project implements:

- Medical Q&A using the MedQuAD dataset
- Retrieval of relevant medical information
- Natural-language question answering
- Basic medical information retrieval
- A simple Streamlit user interface

## Key Features

### 1. MedQuAD Dataset

Medical AIRA uses the **MedQuAD (Medical Question Answer Dataset)** as its primary knowledge source.

The dataset contains medical questions and corresponding answers collected from trusted medical information sources.

The processed MedQuAD knowledge base is stored in compressed JSON format for efficient use by the application.

### 2. Retrieval-Based Question Answering

When a user enters a medical question, the application searches the medical knowledge base for relevant information.

The retrieval process helps the assistant provide answers based on the available medical source material rather than relying only on unrestricted model generation.

### 3. Conversational Interface

Medical AIRA provides a simple Streamlit interface where users can enter medical questions and view the retrieved answer.

### 4. Medical Information Support

The assistant is designed to help users explore general medical information, including questions related to health conditions, symptoms, treatments and other medical topics represented in the MedQuAD knowledge base.

### 5. Testing

The project includes test files for checking important components of the application and its supporting functionality.

## Project Structure

```text
Medical-AIRA-App/
│
├── images/
│
├── app.py
├── aira_gui.py
├── bag_of_words.py
├── conversation_memory.py
├── image_processor.py
├── load_medquad.py
├── medquad_processed.json.gz
├── preprocess.py
├── read_documents.py
├── requirements.txt
├── search_documents.py
├── sentiment_analyzer.py
├── test.py
├── test_image_processor.py
├── test_memory.py
├── test_sentiment.py
├── test_vision_assistant.py
├── tfidf.py
├── update_knowledge_base.py
├── vectorize_documents.py
└── vision_assistant.py
```

## Technologies Used

- Python
- Streamlit
- Natural Language Processing (NLP)
- Information retrieval
- TF-IDF
- Bag of Words
- MedQuAD dataset
- JSON / compressed JSON data
- Python-based testing

## Dataset

The project uses the MedQuAD dataset:

**MedQuAD – Medical Question Answering Dataset**

Source:

https://github.com/abachaa/MedQuAD

The original dataset is processed into a compressed JSON knowledge base used by the application.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/vlakshmian-coder/Medical-AIRA-App.git
```

### 2. Open the project directory

```bash
cd Medical-AIRA-App
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## Running the Application

Start the Streamlit application with:

```bash
streamlit run app.py
```

Streamlit will provide a local URL through which the Medical AIRA interface can be accessed.

## Live Application

**Medical AIRA – Streamlit**

https://medical-aira-app-gcjguhiyxlwpzm3hlui9dc.streamlit.app/

## Example Usage

1. Open the Medical AIRA application.
2. Enter a medical question.
3. Submit the question.
4. The application searches the medical knowledge base.
5. Relevant medical information is presented to the user.

## Project Outcome

Medical AIRA demonstrates the implementation of a specialized medical question-answering chatbot using a real medical Q&A dataset and a retrieval mechanism.

The project provides a simple interface for accessing general medical information while keeping the knowledge source and retrieval process central to the application.

## Medical Safety Disclaimer

Medical AIRA is an educational and informational AI project.

It is **not a substitute for professional medical advice, diagnosis or treatment**.

Users should consult a qualified healthcare professional for medical decisions. For urgent or emergency symptoms, appropriate emergency medical services should be contacted.

## Author

**Vijayalakshmi Narayanan**

AI / Generative AI Learner