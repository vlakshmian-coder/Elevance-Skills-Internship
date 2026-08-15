# Professor Arvind AI Research Assistant

## Project Overview

Professor Arvind AI Research Assistant is a Streamlit-based research assistant designed to help users explore, summarize and understand scientific research papers.

The project uses a computer-science subset of the arXiv metadata dataset and combines information retrieval, extractive summarization, keyword extraction, AI-generated explanations and conversational follow-up questions.

The project was developed to satisfy the Elevance Skills internship requirement for an expert-domain chatbot using the arXiv dataset.

## Internship Requirement

The project implements the following required capabilities:

- Use the arXiv dataset for scientific papers.
- Focus the chatbot on a specific domain/subset — Computer Science.
- Search and retrieve relevant research papers.
- Extract and summarize information from research paper abstracts.
- Extract important concepts/keywords from research content.
- Generate explanations using an open AI language model.
- Maintain conversational context for follow-up questions.
- Provide a Streamlit interface.
- Provide concept visualization.

## Key Features

### 1. Computer Science Research Search

Professor Arvind searches a prepared arXiv metadata dataset and returns relevant computer-science papers.

The search considers:

- Paper title
- Abstract
- arXiv categories

Natural-language questions are processed into meaningful search terms before searching the dataset.

### 2. Research Paper Information

For each matching paper, the application displays:

- Paper title
- Paper ID
- Categories
- Authors
- Abstract

### 3. Extractive Summarization

The application generates a concise summary from each research paper abstract.

The summarization component uses an extractive approach that selects the first meaningful sentences from the abstract.

### 4. Concept Extraction and Visualization

Important keywords are extracted from paper abstracts using frequency-based keyword extraction.

The application combines the extracted concepts across the retrieved papers and displays their frequency through a bar-chart visualization.

### 5. AI Explanation

Professor Arvind provides an AI-generated explanation of the research topic in simple language.

The application uses the Nemotron 3.5 Lightning model through OpenRouter for conversational explanation generation.

### 6. Follow-up Questions

The application maintains conversation history using Streamlit session state.

After the initial research question, users can ask follow-up questions and Professor Arvind uses the previous conversation history when generating the response.

### 7. Streamlit Interface

The complete application is implemented using Streamlit and provides:

- Research question input
- Research paper retrieval
- AI explanation
- Paper summaries
- Concept visualization
- Follow-up conversation

## Project Structure

```text
Prof-ARVIND-Research-AI-Assistant/
│
├── data/
│   └── arxiv_cs_deployment.json.gz
│
├── images/
│   └── professor_arvind.png
│
├── 01_load_arxiv.ipynb
├── app.py
├── arxiv_search.py
├── bag_of_words.py
├── conversation_memory.py
├── image_processor.py
├── load_medquad.py
├── ollama_chat.py
├── preprocess.py
├── read_documents.py
├── search_documents.py
├── sentiment_analyzer.py
├── summarize.py
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
- arXiv metadata
- Natural Language Processing (NLP)
- Extractive summarization
- Keyword extraction
- OpenRouter API
- NVIDIA Nemotron 3.5 Lightning
- Pandas
- JSON / GZIP compressed data

## Dataset

The project uses the **arXiv scientific paper metadata dataset** and focuses on papers belonging to Computer Science categories.

For deployment, a compressed computer-science dataset is included in:

```text
data/arxiv_cs_deployment.json.gz
```

This allows the deployed Streamlit application to access the required research metadata without depending on a local Windows file path.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/vlakshmian-coder/Prof-ARVIND-Research-AI-Assistant.git
```

### 2. Open the project directory

```bash
cd Prof-ARVIND-Research-AI-Assistant
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the OpenRouter API key

The application requires an OpenRouter API key for AI-generated explanations and follow-up conversations.

For Streamlit deployment, the key is stored securely using Streamlit Secrets.

The API key should not be placed directly in the source code.

## Run the Application

Start the Streamlit application with:

```bash
streamlit run app.py
```

The application will open in a browser.

## How to Use

1. Enter a research question.
2. Click **Submit**.
3. Professor Arvind searches the computer-science arXiv dataset.
4. Relevant papers are displayed.
5. Each paper includes its abstract and an extractive summary.
6. An AI explanation of the research topic is generated.
7. Important concepts are visualized.
8. Ask a follow-up question to continue the conversation.

## Live Application

**Professor Arvind AI Research Assistant**

https://prof-arvind-research-ai-assistant-6fzq87chneafhkfsicjqum.streamlit.app/

## GitHub Repository

https://github.com/vlakshmian-coder/Prof-ARVIND-Research-AI-Assistant

## Project Outcome

Professor Arvind demonstrates a domain-specific research assistant that combines scientific-paper retrieval, NLP-based summarization, concept extraction, AI explanation generation and conversational follow-up.

The project provides an interactive Streamlit interface for exploring computer-science research topics and understanding them through simplified AI-generated explanations.

## Educational Disclaimer

Professor Arvind is an educational research assistant and should not be considered a replacement for academic peer review or expert research guidance.

## Author

**Vijayalakshmi Narayanan**

AI / Generative AI Learner