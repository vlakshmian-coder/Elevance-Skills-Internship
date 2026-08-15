# Professor Arvind AI Research Assistant – Project Report

## 1. Project Title

**Professor Arvind AI Research Assistant**

## 2. Project Objective

The objective of this project was to develop an expert-domain chatbot capable of discussing scientific research topics using the arXiv dataset.

The selected domain is **Computer Science**.

The application combines research-paper retrieval, natural language processing, summarization, concept extraction, AI-generated explanations and follow-up conversations.

## 3. Elevance Skills Requirement

The project addresses the internship requirement to:

- Use the arXiv scientific-paper dataset.
- Train/build the chatbot around a selected subset of the dataset.
- Implement information extraction and summarization.
- Use an AI language model for explanation generation.
- Support follow-up questions on complex topics.
- Implement the solution using Streamlit.
- Provide paper searching and concept visualization.

## 4. Dataset

The project uses the arXiv metadata dataset.

A Computer Science subset was selected for the application.

For deployment, the required dataset was compressed and stored as:

`data/arxiv_cs_deployment.json.gz`

The application reads this local project-relative file during paper retrieval.

## 5. Research Paper Retrieval

The `arxiv_search.py` module performs the research-paper search.

The application:

1. Receives a natural-language research question.
2. Removes common stop words.
3. Extracts meaningful query terms.
4. Searches the paper title, abstract and category information.
5. Restricts results to Computer Science categories.
6. Returns up to five matching papers.

This provides the retrieval component of the research assistant.

## 6. Information Extraction

The application extracts important information from each retrieved paper, including:

- arXiv paper ID
- Title
- Authors
- Categories
- Abstract

The abstract is also processed for summarization and concept extraction.

## 7. Research Paper Summarization

The `summarize.py` module provides an extractive summarization function.

The abstract is divided into sentences and a concise summary is generated from the beginning of the abstract.

This provides users with a shorter version of the research content without displaying the complete abstract as the only source of information.

## 8. Concept Extraction

The application extracts meaningful words from research abstracts and calculates their frequency.

The most frequent concepts are collected from the retrieved papers.

These concepts are then used for the visualization component.

## 9. Concept Visualization

Professor Arvind presents the extracted concepts using a bar chart.

The visualization compares concept frequency across the retrieved research papers.

This helps users quickly identify recurring research concepts within the search results.

## 10. AI Explanation

The application generates a simplified explanation of the user's research question using the Nemotron 3.5 Lightning model through OpenRouter.

The system prompt instructs Professor Arvind to provide clear and accurate explanations in simple language.

The model is also instructed not to expose internal reasoning.

## 11. Conversational Context and Follow-up Questions

The application maintains conversation history using Streamlit session state.

The initial research question and the generated explanation are stored in the conversation history.

When a follow-up question is submitted, the previous conversation is supplied to the AI model so that the response can continue the discussion in context.

This allows users to move from an initial research question to related follow-up questions without starting a completely new conversation.

## 12. User Interface

The application is implemented using Streamlit.

The interface provides:

- Professor Arvind AI research assistant branding
- Research question input
- Search results
- AI explanation
- Research paper summaries
- Concept visualization
- Follow-up conversation

An AI-generated illustrative avatar is displayed as part of the educational project interface.

## 13. Technology Stack

- Python
- Streamlit
- arXiv metadata
- Natural Language Processing
- Extractive summarization
- Keyword extraction
- OpenRouter API
- NVIDIA Nemotron 3.5 Lightning
- Pandas
- JSON
- GZIP compression

## 14. Deployment

The application has been deployed using Streamlit Community Cloud.

### GitHub Repository

https://github.com/vlakshmian-coder/Prof-ARVIND-Research-AI-Assistant

### Live Application

https://prof-arvind-research-ai-assistant-6fzq87chneafhkfsicjqum.streamlit.app/

## 15. Testing and Demonstration

The application was tested with research questions and follow-up questions.

The final demonstration confirms that:

- Research questions return relevant Computer Science papers.
- Paper metadata and abstracts are displayed.
- Abstract summaries are generated.
- Concept frequencies are visualized.
- AI explanations are generated.
- Follow-up questions use the conversation history.

## 16. Project Outcome

Professor Arvind demonstrates a domain-specific AI research assistant capable of helping users explore Computer Science research.

The project combines traditional NLP techniques with an AI language model and a Streamlit interface to provide a complete research exploration workflow.

The final application supports research-paper retrieval, summarization, concept visualization, AI explanation and contextual follow-up conversations.

## 17. Conclusion

The completed Professor Arvind project demonstrates the practical application of NLP, information retrieval, summarization and conversational AI to scientific research.

It fulfills the Elevance Skills requirement for developing an expert-domain chatbot using the arXiv dataset and provides an interactive Streamlit interface for exploring and understanding Computer Science research topics.

## Author

**Vijayalakshmi Narayanan**