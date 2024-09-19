from langchain.chains import RetrievalQA
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import OpenAI

class RAGAgent:
    def __init__(self, api_key: str, vector_db: FAISS):
        self.vector_db = vector_db
        self.llm = OpenAI(api_key=api_key, model="gpt-4")  # Or gpt-3.5-turbo

    def answer_question(self, question: str):
        """
        Answer a question using Langchain's RetrievalQA with the vector database.
        Args:
            question (str): The question to be answered.
        Returns:
            str: Generated answer.
        """
        qa_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            retriever=self.vector_db.as_retriever(),
            return_source_documents=True
        )
        result = qa_chain.run(question)
        return result
