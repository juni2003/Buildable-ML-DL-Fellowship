"""
Demonstration of modular programming approach.
Shows how to use all modules together.
"""

from data_generator import DataGenerator
from data_preprocessor import DataPreprocessor  
from model_trainer import ModelTrainer

def run_complete_pipeline():
    """Demonstrate the complete modular pipeline."""
    print(" MODULAR PROGRAMMING DEMONSTRATION")
    print("=" * 50)
    
    # Step 1: Generate Data
    print("\n 1 DATA GENERATION MODULE")
    generator = DataGenerator(random_seed=42)
    data = generator.generate_dataset(n_samples=400)
    print(f"Generated data shape: {data.shape}")
    
    # Step 2: Preprocess Data
    print("\n 2 DATA PREPROCESSING MODULE")
    preprocessor = DataPreprocessor()
    categorical_cols = ['gender', 'product_type']
    X, y = preprocessor.prepare_data(data, 'purchased', categorical_cols)
    print(f"Features shape: {X.shape}")
    print(f"Target shape: {y.shape}")
    
    # Step 3: Train Models
    print("\n 3 MODEL TRAINING MODULE")
    trainer = ModelTrainer(test_size=0.2, random_state=42)
    results = trainer.train_and_evaluate(X, y)
    
    # Step 4: Results Summary
    print("\n PIPELINE RESULTS SUMMARY")
    print("-" * 30)
    for model_name, metrics in results.items():
        print(f"{model_name}: {metrics['accuracy']:.4f}")
    
    best_model_name, best_model = trainer.get_best_model()
    print(f"\n Best Model: {best_model_name}")
    
    print("\n MODULAR PIPELINE COMPLETED SUCCESSFULLY!")

if __name__ == "__main__":
    run_complete_pipeline()
