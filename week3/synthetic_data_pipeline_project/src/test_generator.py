from data_generator import DataGenerator

def test_data_generator():
    """Test the DataGenerator class functionality."""
    print("🧪 Testing DataGenerator Class")
    
    # Create generator instance
    generator = DataGenerator(random_seed=123)
    
    # Generate dataset
    df = generator.generate_dataset(n_samples=300)
    
    # Display results
    print(f"\n📊 Dataset Overview:")
    print(f"Shape: {df.shape}")
    print(f"Columns: {list(df.columns)}")
    print(f"\nFirst 5 rows:")
    print(df.head())
    print(f"\nTarget distribution:")
    print(df['purchased'].value_counts())
    
    print("\n✅ OOP DataGenerator test completed!")

if __name__ == "__main__":
    test_data_generator()
