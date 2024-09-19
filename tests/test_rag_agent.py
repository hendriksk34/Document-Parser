import unittest
from components.rag_agent import RAGAgent
from components.vector_db import VectorDB

class TestRAGAgent(unittest.TestCase):
    def setUp(self):
        self.vector_db = VectorDB(api_key="test-key")
        self.rag_agent = RAGAgent(api_key="test-key", vector_db=self.vector_db)

    def test_answer_question(self):
        self.vector_db.add_document("This is a test document about machine learning.")
        answer = self.rag_agent.answer_question("What is this document about?")
        self.assertIn("machine learning", answer)

if __name__ == '__main__':
    unittest.main()