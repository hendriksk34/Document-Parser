import unittest
from components.document_parser import extract_text_from_pdf

class TestDocumentParser(unittest.TestCase):
    def test_pdf_parsing(self):
        text = extract_text_from_pdf("tests/sample.pdf")
        self.assertIsInstance(text, str)
        self.assertGreater(len(text), 0)

if __name__ == '__main__':
    unittest.main()