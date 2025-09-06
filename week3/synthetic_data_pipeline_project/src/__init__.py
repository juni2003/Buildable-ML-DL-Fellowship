"""
Synthetic Data Pipeline Package

A modular package for generating synthetic customer data with statistics and visualization.
"""

from .data_generator import DataGenerator
from .stats import calculate_mean, calculate_median, calculate_std, get_all_stats, print_stats
from .augment import augment_dataset, add_gaussian_noise, oversample_minority
from .visuals import plot_histogram, plot_scatterplot, quick_data_overview

__version__ = "1.0.0"
__all__ = ["DataGenerator", "calculate_mean", "calculate_median", "calculate_std", 
          "augment_dataset", "plot_histogram", "plot_scatterplot"]
