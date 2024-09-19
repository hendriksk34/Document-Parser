import faiss
import numpy as np
from langchain.vectorstores.faiss import FAISS
from langchain.embeddings import OpenAIEmbeddings

class VectorDB:
    def __init__(self, api_key: str):
        self.embeddings = OpenAIEmbeddings(openai_api_key=api_key)
        self.index = FAISS(embedding_function=self.embeddings)

    def add_document(self, text: str):
        """
        Add text document to the vector database.
        Args:
            text (str): Document content to add.
        """
        embedding = self.embeddings.embed_query(text)
        self.index.add_texts([text], embedding)

    def search(self, query: str, top_k: int = 5):
        """
        Search the vector database for the top-k nearest neighbors to the query.
        Args:
            query (str): The query text.
            top_k (int): Number of neighbors to return.
        Returns:
            List of documents and distances.
        """
        return self.index.similarity_search(query, top_k=top_k)