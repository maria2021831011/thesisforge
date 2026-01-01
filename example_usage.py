"""
example_usage.py
----------------
Demo script to test thesisforge modules.
Run from project root: python example_usage.py
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from thesisforge.statistics.descriptive import mean, median, std, summary_stats
from thesisforge.visualization.thesis_plots import line_plot, bar_plot
from thesisforge.reference_manager.bibtex import BibManager
from thesisforge.paper_organizer.pdf_manager import PDFManager
from thesisforge.utils.logger import logger

# -----------------------
# 1️⃣ Statistics
data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
logger.info("=== Statistics Demo ===")
print("Data:", data)
print("Mean:", mean(data))
print("Median:", median(data))
print("Std:", round(std(data), 2))
print("Summary:", summary_stats(data))
print("\n")

# -----------------------
# 2️⃣ Visualization
logger.info("=== Visualization Demo ===")
line_plot(data, data, title="Line Plot Example", xlabel="X-axis", ylabel="Y-axis")
bar_plot(["A","B","C"], [5,3,8], title="Bar Plot Example", xlabel="Category", ylabel="Value")
print("Check plots in your GUI or Jupyter notebook.\n")

# -----------------------
# 3️⃣ Reference Manager
logger.info("=== Reference Manager Demo ===")
bib_manager = BibManager()
bib_manager.add_entry({
    "ENTRYTYPE": "article",
    "ID": "smith2026",
    "author": "John Smith",
    "title": "Research in Python",
    "journal": "Journal of AI",
    "year": "2026"
})
print("Bib entries:", bib_manager.entries)
print("\n")

# -----------------------
# 4️⃣ Paper Organizer
logger.info("=== Paper Organizer Demo ===")
try:
    pdf_file = "sample_paper.pdf"  # replace with a local PDF path
    pdf_manager = PDFManager(pdf_file)
    metadata = pdf_manager.get_metadata()
    text_preview = pdf_manager.extract_text(page_numbers=[0])[:200]
    print("PDF Metadata:", metadata)
    print("Text Preview (first 200 chars):", text_preview)
except FileNotFoundError:
    print(f"PDF file '{pdf_file}' not found. Skipping Paper Organizer demo.")

logger.info("Example usage script finished successfully.")
