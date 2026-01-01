"""
notes.py
--------
Placeholder for managing notes on research papers.
"""

class NoteManager:
    def __init__(self):
        self.notes = []

    def add_note(self, note: str):
        self.notes.append(note)

    def get_notes(self):
        return self.notes
