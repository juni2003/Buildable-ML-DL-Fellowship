"""
Data augmentation module for enhancing datasets.
"""
import numpy as np
import pandas as pd

def add_gaussian_noise(df, columns, noise_factor=0.1):
    """Add Gaussian noise to numerical columns."""
    df_augmented = df.copy()
    
    for col in columns:
        if col in df.columns:
            noise = np.random.normal(0, df[col].std() * noise_factor, len(df))
            df_augmented[col] = df_augmented[col] + noise
    
    print(f" Added Gaussian noise to {len(columns)} columns")
    return df_augmented

def oversample_minority(df, target_column, ratio=0.5):
    """Oversample minority class to balance dataset."""
    # Find minority class
    class_counts = df[target_column].value_counts()
    minority_class = class_counts.idxmin()
    majority_class = class_counts.idxmax()
    
    minority_data = df[df[target_column] == minority_class]
    majority_count = class_counts[majority_class]
    minority_count = class_counts[minority_class]
    
    # Calculate how many samples to add
    target_minority_count = int(majority_count * ratio)
    samples_to_add = max(0, target_minority_count - minority_count)
    
    if samples_to_add > 0:
        # Randomly sample from minority class with replacement
        oversampled = minority_data.sample(n=samples_to_add, replace=True, random_state=42)
        df_augmented = pd.concat([df, oversampled], ignore_index=True)
        print(f"Added {samples_to_add} samples to minority class")
    else:
        df_augmented = df.copy()
        print(" No oversampling needed")
    
    return df_augmented

def create_synthetic_combinations(df, numerical_cols, n_combinations=50):
    """Create synthetic data by combining existing samples."""
    synthetic_samples = []
    
    for _ in range(n_combinations):
        # Pick two random rows
        idx1, idx2 = np.random.choice(len(df), 2, replace=False)
        row1 = df.iloc[idx1]
        row2 = df.iloc[idx2]
        
        # Create synthetic row by averaging numerical features
        synthetic_row = row1.copy()
        for col in numerical_cols:
            if col in df.columns:
                synthetic_row[col] = (row1[col] + row2[col]) / 2
        
        synthetic_samples.append(synthetic_row)
    
    synthetic_df = pd.DataFrame(synthetic_samples)
    df_augmented = pd.concat([df, synthetic_df], ignore_index=True)
    
    print(f" Created {n_combinations} synthetic combinations")
    return df_augmented

def augment_dataset(df, target_column, numerical_cols, method='noise'):
    """Main augmentation function with multiple methods."""
    print(f"🔄 Augmenting dataset using method: {method}")
    
    if method == 'noise':
        return add_gaussian_noise(df, numerical_cols)
    elif method == 'oversample':
        return oversample_minority(df, target_column)
    elif method == 'synthetic':
        return create_synthetic_combinations(df, numerical_cols)
    elif method == 'all':
        # Apply all methods
        df_noise = add_gaussian_noise(df, numerical_cols, noise_factor=0.05)
        df_oversampled = oversample_minority(df_noise, target_column)
        df_final = create_synthetic_combinations(df_oversampled, numerical_cols, n_combinations=25)
        return df_final
    else:
        print(" Unknown method. Using 'noise' as default.")
        return add_gaussian_noise(df, numerical_cols)
