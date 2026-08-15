# Medical AIRA – Project Report

## 1. Project Title

**Medical AIRA – Medical Q&A Chatbot**

## 2. Project Objective

The objective of this project was to develop a specialized medical question-answering chatbot using the MedQuAD dataset.

The system provides a simple conversational interface through which users can ask medical questions and retrieve relevant information from the medical knowledge base.

## 3. Elevance Skills Requirement

The project addresses the following internship requirements:

- Use the MedQuAD dataset.
- Implement a mechanism for retrieving relevant medical answers.
- Provide a simple user interface using Streamlit.
- Support medical question answering using the prepared knowledge base.

## 4. Dataset

The project uses the **MedQuAD – Medical Question Answering Dataset**.

MedQuAD contains medical questions and answers collected from medical information sources.

The dataset was processed into a compressed JSON knowledge base used by the application.

The original dataset is available at:

https://github.com/abachaa/MedQuAD

## 5. Data Processing

The project includes processing components for preparing the MedQuAD information for retrieval.

The processed knowledge base is stored as:

`medquad_processed.json.gz`

The compressed format reduces the storage requirement while retaining the structured question-answer information required by the application.

## 6. Retrieval Mechanism

Medical AIRA uses a retrieval-based approach to identify information relevant to a user's medical question.

The user's query is processed and compared with information in the medical knowledge base.

Relevant information is then returned through the conversational interface.

This approach helps ground the application's answers in the available MedQuAD content.

## 7. User Interface

The application is implemented using **Streamlit**.

The interface allows a user to:

1. Enter a medical question.
2. Submit the question.
3. Search the medical knowledge base.
4. View the relevant response.

## 8. Supporting Components

The project contains separate Python modules for data loading, preprocessing, document reading, vectorization and document searching.

Additional modules support conversational memory, image processing, sentiment analysis and vision-related functionality included in the project implementation.

Testing files are also included for validating important components.

## 9. Technology Stack

- Python
- Streamlit
- Natural Language Processing
- Bag of Words
- TF-IDF
- Information retrieval
- MedQuAD
- JSON / compressed JSON
- Python testing tools

## 10. Deployment

Medical AIRA has been deployed using Streamlit Community Cloud.

### Live Application

https://medical-aira-app-gcjguhiyxlwpzm3hlui9dc.streamlit.app/

### GitHub Repository

https://github.com/vlakshmian-coder/Medical-AIRA-App

## 11. Testing

The project includes dedicated test files for important components, including:

- General application testing
- Image processing
- Conversation memory
- Sentiment analysis
- Vision assistant functionality

These tests support validation of the implemented components.

## 12. Project Outcome

The completed project demonstrates a specialized medical Q&A chatbot that uses the MedQuAD dataset and a retrieval mechanism to provide relevant medical information through a Streamlit interface.

It demonstrates the practical use of NLP and information retrieval techniques for building a domain-specific conversational AI application.

## 13. Limitations and Safety

Medical AIRA is an educational AI application and should not be considered a medical professional.

AI-generated or retrieved information may not be sufficient for diagnosis or treatment decisions.

Users should consult qualified healthcare professionals for medical advice and should seek appropriate emergency care when necessary.

## 14. Conclusion

Medical AIRA demonstrates how a domain-specific medical chatbot can be developed using a curated medical Q&A dataset, NLP-based retrieval and a user-friendly Streamlit interface.

The project fulfills the Elevance Skills requirement for developing a Medical Q&A chatbot using the MedQuAD dataset.