import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder

class DataPreprocessor:
    """Module for data cleaning and preprocessing operations."""
    
    def __init__(self):
        self.scaler = StandardScaler()
        self.label_encoders = {}
        self.is_fitted = False
    
    def clean_data(self, df):
        """Clean the dataset by handling missing values and duplicates."""
        print("🧹 Cleaning data...")
        
        # Remove duplicates
        initial_rows = len(df)
        df_clean = df.drop_duplicates()
        removed_duplicates = initial_rows - len(df_clean)
        
        # Handle missing values (fill with median for numerical, mode for categorical)
        numerical_cols = df_clean.select_dtypes(include=[np.number]).columns
        categorical_cols = df_clean.select_dtypes(exclude=[np.number]).columns
        
        for col in numerical_cols:
            df_clean[col] = df_clean[col].fillna(df_clean[col].median())
        
        for col in categorical_cols:
            df_clean[col] = df_clean[col].fillna(df_clean[col].mode()[0])
        
        print(f" Removed {removed_duplicates} duplicates")
        print(f" Cleaned dataset shape: {df_clean.shape}")
        
        return df_clean
    
    def encode_categorical(self, df, categorical_columns):
        """Encode categorical variables using Label Encoding."""
        print("🏷️ Encoding categorical variables...")
        
        df_encoded = df.copy()
        
        for col in categorical_columns:
            if col in df_encoded.columns:
                if col not in self.label_encoders:
                    self.label_encoders[col] = LabelEncoder()
                    df_encoded[col] = self.label_encoders[col].fit_transform(df_encoded[col])
                else:
                    df_encoded[col] = self.label_encoders[col].transform(df_encoded[col])
        
        print(f" Encoded {len(categorical_columns)} categorical columns")
        return df_encoded
    
    def scale_features(self, X_train, X_test=None):
        """Scale numerical features using StandardScaler."""
        print("📏 Scaling features...")
        
        if not self.is_fitted:
            X_train_scaled = self.scaler.fit_transform(X_train)
            self.is_fitted = True
        else:
            X_train_scaled = self.scaler.transform(X_train)
        
        if X_test is not None:
            X_test_scaled = self.scaler.transform(X_test)
            print(" Training and test sets scaled")
            return X_train_scaled, X_test_scaled
        
        print("Training set scaled")
        return X_train_scaled
    
    def prepare_data(self, df, target_column, categorical_columns):
        """Complete data preparation pipeline."""
        print(" Starting data preparation pipeline...")
        
        # Step 1: Clean data
        df_clean = self.clean_data(df)
        
        # Step 2: Encode categorical variables
        df_encoded = self.encode_categorical(df_clean, categorical_columns)
        
        # Step 3: Separate features and target
        X = df_encoded.drop(columns=[target_column])
        y = df_encoded[target_column]
        
        print(" Data preparation completed")
        return X, y
