import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path: str) -> str:
    """
    Extract text from a PDF document.
    Args:
        pdf_path (str): Path to the PDF file.
    Returns:
        str: Extracted text content from the PDF.
    """
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text("text")
    doc.close()
    return text