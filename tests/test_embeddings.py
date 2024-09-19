import unittest
from components.embeddings import AdaEmbeddingGenerator

class TestAdaEmbeddingGenerator(unittest.TestCase):
    def setUp(self):
        self.embedder = AdaEmbeddingGenerator(api_key="test-api-key")

    def test_generate_embedding(self):
        embedding = self.embedder.generate_embedding("This is a test sentence.")
        self.assertIsInstance(embedding, list)
        self.assertGreater(len(embedding), 0)

if __name__ == '__main__':
    unittest.main()