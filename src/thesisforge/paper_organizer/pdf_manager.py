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
        self.pdf_path: Optional[str] = pdf_path
        self.reader: Optional[PyPDF2.PdfReader] = None
        if pdf_path:
            self.load_pdf(pdf_path)

    def load_pdf(self, pdf_path: str) -> None:
        if not os.path.exists(pdf_path):
            raise FileNotFoundError(f"{pdf_path} does not exist.")
        self.pdf_path = pdf_path
        self.reader = PyPDF2.PdfReader(pdf_path)

    def get_metadata(self) -> Dict[str, str]:
        if self.reader is None:
            raise ValueError("PDF not loaded.")
        if self.reader.metadata is None:
            return {}
        return {k[1:]: str(v) for k, v in self.reader.metadata.items()}


    def extract_text(self, page_numbers: Optional[List[int]] = None) -> str:
        """Extract text from PDF. If page_numbers is None, extract all pages."""
        if not self.pdf_path:
            raise ValueError("PDF not loaded.")
        text: str = ""
        with pdfplumber.open(self.pdf_path) as pdf:
            pages: List[int] = page_numbers or list(range(len(pdf.pages)))
            for i in pages:
                page_text: Optional[str] = pdf.pages[i].extract_text()
                if page_text:
                    text += page_text + "\n"
        return text

    def search_text(self, query: str) -> Dict[int, str]:
        """
        Search for a query string in the PDF.
        Returns a dict of page number -> text snippet.
        """
        if not self.pdf_path:
            raise ValueError("PDF not loaded.")
        results: Dict[int, str] = {}
        with pdfplumber.open(self.pdf_path) as pdf:
            for i, page in enumerate(pdf.pages):
                page_text: Optional[str] = page.extract_text()
                if page_text and query.lower() in page_text.lower():
                    idx: int = page_text.lower().find(query.lower())
                    snippet: str = page_text[max(0, idx-30): idx+30]
                    results[i+1] = snippet
        return results

