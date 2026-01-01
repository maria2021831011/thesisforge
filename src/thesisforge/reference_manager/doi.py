"""
doi_manager.py
---------------
Simple DOI fetcher using CrossRef API
"""

from typing import Optional, Dict
import requests

class DOIManager:
    CROSSREF_API = "https://api.crossref.org/works/"

    @staticmethod
    def fetch_metadata(doi: str) -> Optional[Dict]:
        """Fetch DOI metadata from CrossRef API."""
        url = f"{DOIManager.CROSSREF_API}{doi}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data.get("message", {})
        return None
