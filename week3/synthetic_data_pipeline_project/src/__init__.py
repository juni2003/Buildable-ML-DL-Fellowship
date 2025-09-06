"""
Synthetic Data Pipeline Package

A modular package for generating synthetic customer data and training ML models.
"""

from .data_generator import DataGenerator
from .data_preprocessor import DataPreprocessor
from .model_trainer import ModelTrainer

__version__ = "1.0.0"
__all__ = ["DataGenerator", "DataPreprocessor", "ModelTrainer"]
