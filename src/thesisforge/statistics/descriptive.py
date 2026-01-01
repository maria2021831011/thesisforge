"""
descriptive.py
---------------

Provides functions for basic descriptive statistics for thesis data analysis.

Functions:
- mean
- median
- std
- summary_stats
"""

from typing import List, Dict, Union
import math

Number = Union[int, float]

def mean(data: List[Number]) -> float:
    """Calculate mean (average) of a numeric list."""
    if not data:
        raise ValueError("Data list is empty")
    return sum(data) / len(data)

def median(data: List[Number]) -> float:
    """Calculate median of a numeric list."""
    if not data:
        raise ValueError("Data list is empty")
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2
    else:
        return sorted_data[mid]

def std(data: List[Number], sample: bool = True) -> float:
    """Calculate standard deviation.
    sample=True calculates sample std, sample=False calculates population std
    """
    if not data:
        raise ValueError("Data list is empty")
    n = len(data)
    if n == 1 and sample:
        raise ValueError("Sample standard deviation requires at least two data points")
    avg = mean(data)
    variance = sum((x - avg) ** 2 for x in data) / (n - 1 if sample else n)
    return math.sqrt(variance)

def summary_stats(data: List[Number]) -> Dict[str, float]:
    """Return a dictionary with mean, median, and standard deviation."""
    return {
        "mean": mean(data),
        "median": median(data),
        "std": std(data)
    }
