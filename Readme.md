# Document Parser with RAG for Q&A

## Overview
This project allows users to upload PDF documents, parse their content, and ask questions using a Retrieval-Augmented Generation (RAG) approach with Langchain and OpenAI’s ADA model for embedding generation.

## Features
- Parse text from PDF documents.
- Generate vector embeddings using OpenAI ADA (`text-embedding-ada-002`) and store them in FAISS.
- Retrieve relevant documents and generate answers using Langchain's RetrievalQA with OpenAI GPT-4.

## Setup

### Prerequisites
- Python 3.9+
- OpenAI API Key

### Installation

1. Clone the repository:
    ```bash
    git clone <repository-url>
    cd document-parser-rag
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Set your OpenAI API Key in the config file.

### Running the App
Run the following command to start the app:
```bash
streamlit run app.py

### Running the tests

python -m unittest discover tests