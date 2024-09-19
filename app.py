import streamlit as st
from components.document_parser import extract_text_from_pdf
from components.embeddings import AdaEmbeddingGenerator
from components.vector_db import VectorDB
from components.rag_agent import RAGAgent

# OpenAI API key from config
OPENAI_API_KEY = "your-openai-api-key"

# Initialize components
embedding_gen = AdaEmbeddingGenerator(api_key=OPENAI_API_KEY)
vector_db = VectorDB(api_key=OPENAI_API_KEY)
rag_agent = RAGAgent(api_key=OPENAI_API_KEY, vector_db=vector_db)

# Streamlit UI
st.title("Document Parser with RAG for Q&A")
st.write("Upload a PDF document and ask questions based on its content.")

# File uploader
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file:
    # Extract text from the uploaded PDF
    text_content = extract_text_from_pdf(uploaded_file)
    
    # Generate embeddings for the document and store in vector DB
    vector_db.add_document(text_content)
    
    # Display the extracted text
    st.write("Extracted Text from PDF:", text_content[:500])  # Show first 500 characters

    # Question asking interface
    question = st.text_input("Ask a question based on the document:")
    if question:
        answer = rag_agent.answer_question(question)
        st.write("Answer:", answer)