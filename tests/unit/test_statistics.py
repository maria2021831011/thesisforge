import pytest
from thesisforge.statistics.descriptive import mean, median, std, summary_stats

def test_mean():
    data = [1, 2, 3, 4, 5]
    assert mean(data) == 3.0

def test_median_odd():
    data = [5, 2, 1, 4, 3]
    assert median(data) == 3

def test_median_even():
    data = [1, 2, 3, 4]
    assert median(data) == 2.5

def test_std_sample():
    data = [2, 4, 4, 4, 5, 5, 7, 9]
    assert round(std(data, sample=True), 2) == 2.14

def test_std_population():
    data = [2, 4, 4, 4, 5, 5, 7, 9]
    assert round(std(data, sample=False), 2) == 2.0

def test_summary_stats():
    data = [1, 2, 3, 4, 5]
    stats = summary_stats(data)
    assert stats["mean"] == 3.0
    assert stats["median"] == 3
    assert round(stats["std"], 2) == 1.58
