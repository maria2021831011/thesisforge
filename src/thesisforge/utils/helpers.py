from typing import List

def flatten_list(nested_list: List[List]):
    """Flatten a nested list into a single list."""
    return [item for sublist in nested_list for item in sublist]
