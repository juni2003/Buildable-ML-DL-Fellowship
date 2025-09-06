import pandas as pd
import numpy as np
import os
from datetime import datetime

# Custom Exception Classes
class InvalidFilePathError(Exception):
    """Custom exception for invalid file paths."""
    pass

class DataGenerationError(Exception):
    """Custom exception for data generation failures."""
    pass

class DataGenerator:
    """Generates synthetic customer data for classification."""
    
    def __init__(self, random_seed=42):
        np.random.seed(random_seed)
    
    def log_error(self, error_message):
        """Save error messages to logs/errors.txt"""
        try:
            # Create logs directory if it doesn't exist
            if not os.path.exists('../logs'):
                os.makedirs('../logs')
            
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_message = f"[{timestamp}] ERROR: {error_message}\n"
            
            with open('../logs/errors.txt', 'a') as f:
                f.write(log_message)
            print(f"Error logged to ../logs/errors.txt")
        except Exception as e:
            print(f"Failed to write to log file: {e}")
    
    def generate_dataset(self, n_samples=500):
        """Generate synthetic dataset with error handling."""
        
        # Parameter validation with custom exceptions
        if not isinstance(n_samples, int):
            error_msg = f"n_samples must be integer, got {type(n_samples).__name__}"
            self.log_error(error_msg)
            raise DataGenerationError(error_msg)
        
        if n_samples <= 0:
            error_msg = f"n_samples must be positive, got {n_samples}"
            self.log_error(error_msg)
            raise DataGenerationError(error_msg)
        
        try:
            # 5 Numerical features
            age = np.random.randint(18, 80, n_samples)
            income = np.random.randint(20000, 100000, n_samples)
            purchase_amount = np.random.randint(10, 500, n_samples)
            monthly_visits = np.random.randint(1, 20, n_samples)
            satisfaction_score = np.random.randint(1, 11, n_samples)
            
            # 2 Categorical features
            gender = np.random.choice(['Male', 'Female'], n_samples)
            product_type = np.random.choice(['Electronics', 'Clothing', 'Books'], n_samples)
            
            # Binary target
            purchase_prob = (income / 100000) * 0.5 + (satisfaction_score / 10) * 0.3 + 0.2
            purchased = np.random.binomial(1, purchase_prob, n_samples)
            
            # Create DataFrame
            data = {
                'age': age,
                'income': income,
                'purchase_amount': purchase_amount,
                'monthly_visits': monthly_visits,
                'satisfaction_score': satisfaction_score,
                'gender': gender,
                'product_type': product_type,
                'purchased': purchased
            }
            
            return pd.DataFrame(data)
            
        except Exception as e:
            error_msg = f"Data generation failed: {str(e)}"
            self.log_error(error_msg)
            raise DataGenerationError(error_msg)
    
    def save_dataset(self, df, filename='generated_data.csv'):
        """Save dataset with file path validation."""
        
        # File path validation
        if not isinstance(filename, str):
            error_msg = f"Filename must be string, got {type(filename).__name__}"
            self.log_error(error_msg)
            raise InvalidFilePathError(error_msg)
        
        if not filename.endswith('.csv'):
            error_msg = f"File must have .csv extension, got {filename}"
            self.log_error(error_msg)
            raise InvalidFilePathError(error_msg)
        
        # Check for invalid characters
        invalid_chars = '<>:"|?*'
        if any(char in filename for char in invalid_chars):
            error_msg = f"Filename contains invalid characters: {filename}"
            self.log_error(error_msg)
            raise InvalidFilePathError(error_msg)
        
        try:
            filepath = f'../data/raw/{filename}'
            df.to_csv(filepath, index=False)
            print(f"Dataset saved to: {filepath}")
            return filepath
            
        except Exception as e:
            error_msg = f"Failed to save file {filename}: {str(e)}"
            self.log_error(error_msg)
            raise InvalidFilePathError(error_msg)

# Test error handling
if __name__ == "__main__":
    generator = DataGenerator()
    
    print("Testing Exception Handling:\n")
    
    # Test 1: Valid case
    try:
        data = generator.generate_dataset(100)
        print("✅ Valid data generation successful")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
    
    # Test 2: Invalid n_samples (negative)
    try:
        data = generator.generate_dataset(-5)
    except DataGenerationError as e:
        print(f"✅ Caught DataGenerationError: {e}")
    
    # Test 3: Invalid filename
    try:
        data = generator.generate_dataset(50)
        generator.save_dataset(data, 'bad<file>.txt')
    except InvalidFilePathError as e:
        print(f"✅ Caught InvalidFilePathError: {e}")
    
    print("\n🔍 Check logs/errors.txt for error logs!")
