"""
Statistics module using NumPy for calculating basic statistical measures.
"""
import numpy as np
import pandas as pd

def calculate_mean(data):
    """Calculate mean using NumPy."""
    if isinstance(data, pd.Series):
        data = data.values
    return np.mean(data)

def calculate_median(data):
    """Calculate median using NumPy."""
    if isinstance(data, pd.Series):
        data = data.values
    return np.median(data)

def calculate_std(data):
    """Calculate standard deviation using NumPy."""
    if isinstance(data, pd.Series):
        data = data.values
    return np.std(data)

def get_all_stats(data):
    """Get mean, median, and std in one function."""
    stats_dict = {
        'mean': calculate_mean(data),
        'median': calculate_median(data), 
        'std': calculate_std(data)
    }
    return stats_dict

def print_stats(data, column_name="Data"):
    """Print formatted statistics."""
    stats = get_all_stats(data)
    print(f"\n📊 Statistics for {column_name}:")
    print(f"Mean: {stats['mean']:.2f}")
    print(f"Median: {stats['median']:.2f}")
    print(f"Standard Deviation: {stats['std']:.2f}")
