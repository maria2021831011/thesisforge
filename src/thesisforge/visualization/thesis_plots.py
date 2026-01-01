"""
thesis_plots.py
----------------
Provides functions to create common thesis-ready plots using matplotlib and seaborn.

Functions:
- line_plot
- bar_plot
- histogram
- scatter_plot
"""

from typing import List, Optional, Union
import matplotlib.pyplot as plt
import seaborn as sns

Number = Union[int, float]

# Set a clean default style
sns.set_theme(style="whitegrid", palette="pastel")

def line_plot(
    x: List[Number],
    y: List[Number],
    title: Optional[str] = None,
    xlabel: Optional[str] = None,
    ylabel: Optional[str] = None,
    save_path: Optional[str] = None
) -> None:
    """Create a simple line plot."""
    plt.figure(figsize=(8, 5))
    sns.lineplot(x=x, y=y, marker="o")
    if title:
        plt.title(title, fontsize=14)
    if xlabel:
        plt.xlabel(xlabel)
    if ylabel:
        plt.ylabel(ylabel)
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=300)
    plt.show()

def bar_plot(
    x: List[str],
    y: List[Number],
    title: Optional[str] = None,
    xlabel: Optional[str] = None,
    ylabel: Optional[str] = None,
    save_path: Optional[str] = None
) -> None:
    """Create a simple bar plot."""
    plt.figure(figsize=(8, 5))
    sns.barplot(x=x, y=y)
    if title:
        plt.title(title, fontsize=14)
    if xlabel:
        plt.xlabel(xlabel)
    if ylabel:
        plt.ylabel(ylabel)
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=300)
    plt.show()

def histogram(
    data: List[Number],
    bins: int = 10,
    title: Optional[str] = None,
    xlabel: Optional[str] = None,
    ylabel: Optional[str] = "Frequency",
    save_path: Optional[str] = None
) -> None:
    """Create a histogram."""
    plt.figure(figsize=(8, 5))
    sns.histplot(data, bins=bins, kde=True)
    if title:
        plt.title(title, fontsize=14)
    if xlabel:
        plt.xlabel(xlabel)
    if ylabel:
        plt.ylabel(ylabel)
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=300)
    plt.show()

def scatter_plot(
    x: List[Number],
    y: List[Number],
    title: Optional[str] = None,
    xlabel: Optional[str] = None,
    ylabel: Optional[str] = None,
    save_path: Optional[str] = None
) -> None:
    """Create a scatter plot."""
    plt.figure(figsize=(8, 5))
    sns.scatterplot(x=x, y=y, s=80)
    if title:
        plt.title(title, fontsize=14)
    if xlabel:
        plt.xlabel(xlabel)
    if ylabel:
        plt.ylabel(ylabel)
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=300)
    plt.show()
