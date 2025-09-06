import pandas as pd
import numpy as np
import os

class DataGenerator:
    """Generates synthetic customer data for classification."""
    
    def __init__(self, random_seed=42):
        np.random.seed(random_seed)
    
    def generate_dataset(self, n_samples=500):
        """Generate synthetic dataset with required features."""
        
        # 5 Numerical features
        age = np.random.randint(18, 80, n_samples)
        income = np.random.randint(20000, 100000, n_samples)
        purchase_amount = np.random.randint(10, 500, n_samples)
        monthly_visits = np.random.randint(1, 20, n_samples)
        satisfaction_score = np.random.randint(1, 11, n_samples)
        
        # 2 Categorical features
        gender = np.random.choice(['Male', 'Female'], n_samples)
        product_type = np.random.choice(['Electronics', 'Clothing', 'Books'], n_samples)
        
        # Binary target (based on income and satisfaction)
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
    
    def save_dataset(self, df, filename='generated_data.csv'):
        """Save dataset to data/raw folder."""
        
        filepath = f'../data/raw/{filename}'
        df.to_csv(filepath, index=False)
        print(f"Dataset saved to: {filepath}")
        return filepath

# Test the generator
if __name__ == "__main__":
    generator = DataGenerator()
    data = generator.generate_dataset(500)
    print(f"Generated dataset shape: {data.shape}")
    print(data.head())
    print("✅ DataGenerator working successfully!")
