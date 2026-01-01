"""
pdf_manager.py
---------------
Manage PDFs for research papers:
- extract text
- get metadata
- search within PDFs
"""

from typing import Optional, List, Dict
import PyPDF2
import pdfplumber
import os

class PDFManager:
    def __init__(self, pdf_path: Optional[str] = None):
        self.pdf_path = pdf_path
        self.reader = None
        if pdf_path:
            self.load_pdf(pdf_path)

    def load_pdf(self, pdf_path: str):
        """Load PDF file."""
        if not os.path.exists(pdf_path):
            raise FileNotFoundError(f"{pdf_path} does not exist.")
        self.pdf_path = pdf_path
        self.reader = PyPDF2.PdfReader(pdf_path)

    def get_metadata(self) -> Dict[str, str]:
        """Return PDF metadata as dictionary."""
        if not self.reader:
            raise ValueError("PDF not loaded.")
        return {k[1:]: v for k, v in self.reader.metadata.items()}

    def extract_text(self, page_numbers: Optional[List[int]] = None) -> str:
        """Extract text from PDF. If page_numbers is None, extract all pages."""
        if not self.pdf_path:
            raise ValueError("PDF not loaded.")
        text = ""
        with pdfplumber.open(self.pdf_path) as pdf:
            pages = page_numbers or list(range(len(pdf.pages)))
            for i in pages:
                text += pdf.pages[i].extract_text() + "\n"
        return text

    def search_text(self, query: str) -> Dict[int, str]:
        """
        Search for a query string in the PDF.
        Returns a dict of page number -> text snippet.
        """
        if not self.pdf_path:
            raise ValueError("PDF not loaded.")
        results = {}
        with pdfplumber.open(self.pdf_path) as pdf:
            for i, page in enumerate(pdf.pages):
                page_text = page.extract_text()
                if page_text and query.lower() in page_text.lower():
                    # Return snippet around query
                    idx = page_text.lower().find(query.lower())
                    snippet = page_text[max(0, idx-30): idx+30]
                    results[i+1] = snippet
        return results
