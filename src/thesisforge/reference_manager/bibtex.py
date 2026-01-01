"""
bibtex_manager.py
-----------------
Simple BibTeX manager for adding, reading, and searching references.
"""

from typing import List, Dict, Optional
import bibtexparser
from bibtexparser.bparser import BibTexParser
from bibtexparser.customization import homogenize_latex_encoding

class BibManager:
    def __init__(self, bib_file: Optional[str] = None):
        self.bib_file = bib_file
        self.entries: List[Dict] = []
        if bib_file:
            self.load_bib(bib_file)

    def load_bib(self, bib_file: str):
        """Load BibTeX file."""
        with open(bib_file, "r", encoding="utf-8") as bf:
            parser = BibTexParser(common_strings=True)
            parser.customization = homogenize_latex_encoding
            bib_database = bibtexparser.load(bf, parser=parser)
            self.entries = bib_database.entries

    def search_by_author(self, author_name: str) -> List[Dict]:
        """Return list of entries matching the author name."""
        return [e for e in self.entries if author_name.lower() in e.get("author", "").lower()]

    def add_entry(self, entry: Dict):
        """Add a new BibTeX entry."""
        self.entries.append(entry)

    def save(self, path: Optional[str] = None):
        """Save entries back to a BibTeX file."""
        bib_db = bibtexparser.bibdatabase.BibDatabase()
        bib_db.entries = self.entries
        output_file = path or self.bib_file
        if not output_file:
            raise ValueError("No file specified to save BibTeX data.")
        with open(output_file, "w", encoding="utf-8") as bf:
            bibtexparser.dump(bib_db, bf)
