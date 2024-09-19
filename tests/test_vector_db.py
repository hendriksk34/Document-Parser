import unittest
from components.vector_db import VectorDB

class TestVectorDB(unittest.TestCase):
    def setUp(self):
        self.vector_db = VectorDB(api_key="test-api-key")

    def test_add_and_search_document(self):
        self.vector_db.add_document("This is a test document.")
        results = self.vector_db.search("test", top_k=1)
        self.assertGreater(len(results), 0)

if __name__ == '__main__':
    unittest.main()