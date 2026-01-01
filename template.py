import os
from pathlib import Path
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# FIXED & UNIQUE PROJECT NAME (PyPI + GitHub safe)
PROJECT_NAME = "thesisforge"

logging.info(f"Creating project: {PROJECT_NAME}")

list_of_files = [
    # GitHub
    ".github/workflows/.gitkeep",

    # Source package
    f"src/{PROJECT_NAME}/__init__.py",

    # Paper Organizer
    f"src/{PROJECT_NAME}/paper_organizer/__init__.py",
    f"src/{PROJECT_NAME}/paper_organizer/pdf_manager.py",
    f"src/{PROJECT_NAME}/paper_organizer/metadata_extractor.py",
    f"src/{PROJECT_NAME}/paper_organizer/notes.py",

    # Reference Manager
    f"src/{PROJECT_NAME}/reference_manager/__init__.py",
    f"src/{PROJECT_NAME}/reference_manager/citation.py",
    f"src/{PROJECT_NAME}/reference_manager/bibtex.py",
    f"src/{PROJECT_NAME}/reference_manager/doi.py",

    # Visualization
    f"src/{PROJECT_NAME}/visualization/__init__.py",
    f"src/{PROJECT_NAME}/visualization/thesis_plots.py",
    f"src/{PROJECT_NAME}/visualization/styles.py",

    # Statistics
    f"src/{PROJECT_NAME}/statistics/__init__.py",
    f"src/{PROJECT_NAME}/statistics/descriptive.py",
    f"src/{PROJECT_NAME}/statistics/hypothesis.py",
    f"src/{PROJECT_NAME}/statistics/regression.py",

    # Utils
    f"src/{PROJECT_NAME}/utils/__init__.py",
    f"src/{PROJECT_NAME}/utils/logger.py",
    f"src/{PROJECT_NAME}/utils/helpers.py",

    # Tests
    "tests/__init__.py",
    "tests/unit/__init__.py",
    "tests/integration/__init__.py",
    "tests/unit/test_statistics.py",
    "tests/unit/test_visualization.py",
    "tests/unit/test_reference.py",

    # Config files
    "requirements.txt",
    "requirements_dev.txt",
    "pyproject.toml",
    "setup.cfg",
    "setup.py",
    "tox.ini",
    "README.md",
    "init_setup.sh",
]

for filepath in list_of_files:
    path = Path(filepath)
    os.makedirs(path.parent, exist_ok=True)

    if not path.exists():
        path.touch()
        logging.info(f"Created file: {path}")
    else:
        logging.info(f"File already exists: {path}")
