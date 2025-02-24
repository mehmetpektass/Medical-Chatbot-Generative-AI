# Medical Chatbot Generative AI Project👩‍⚕

## Description
This project is a robust question-answering system designed to process PDF documents, extract meaningful data, and provide concise and accurate responses. The system uses LangChain for document processing and splitting, and HuggingFace embeddings for text representation. Additionally, a chat interface is implemented using Flask for user interaction.

<br>

## Features

* **PDF Loading:** Extract data from PDF files located in a specified directory.
* **Text Splitting:** Split large chunks of text into manageable pieces for efficient processing.
*  **HuggingFace Embeddings:** Generate embeddings for textual data using pre-trained HuggingFace models. 
* **Vector Store Creation:** Creates a Pinecone vector store to store and retrieve relevant information from the chunked text.
* **Retrieval Augmented Generation (RAG):** Utilizes a Retrieval Augmented Generation (RAG) chain to retrieve relevant information from the vector store and use it to generate responses to user queries.
* **Prompt System:**  An advanced prompt system ensures clear and professional responses to user queries.
* **Chat Interface:** A simple and clean HTML-CSS based a **Flask** user interface for interacting with the system.




<br>

## Tech Stack
### Tools and Libraries
* **LangChain:** A powerful library for developing and deploying language models.
* **Sentence-Transformers:** A HuggingFace model used to generate embeddings for text chunks. 
* **Pinecone:** A vector database service used to store and retrieve embeddings for efficient information retrieval.
* **OpenAI:** Provides access to powerful language models like GPT-3.5-turbo for generating human-like text.
* **Flask:** A lightweight Python web framework for building the chat interface.


<br>

<br>


## Installation & Setup
```bash
git clone https://github.com/mehmetpektass/Medical-Chatbot-Generative-AI.git
cd Medical_Chatbot_Generative_AI

```
```
pip install -r requirements.txt

```


## Contribution Guidelines  🚀
 Pull requests are welcome. If you'd like to contribute, please:

* Fork the repository.
* Create a feature branch.
* Submit a pull request with a clear description of changes.



