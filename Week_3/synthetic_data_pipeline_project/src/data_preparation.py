import pandas as pd

# Load CSV data

def load_data(file_path):
    return pd.read_csv(file_path)

# Handle missing values

def handle_missing_values(df):
    # Fill missing values with the mean for numerical columns
    for column in df.select_dtypes(include=['float64', 'int64']).columns:
        df[column].fillna(df[column].mean(), inplace=True)
    # Fill missing values with the mode for categorical columns
    for column in df.select_dtypes(include=['object']).columns:
        mode = df[column].mode()
        if not mode.empty:
            df[column].fillna(mode[0], inplace=True)
    return df

# Encode categorical variables

def encode_categorical_variables(df):
    return pd.get_dummies(df, drop_first=True)

# Save cleaned data

def save_cleaned_data(df, output_path):
    df.to_csv(output_path, index=False)

# Example usage:
# df = load_data('data/raw_data.csv')
# df = handle_missing_values(df)
# df = encode_categorical_variables(df)
# save_cleaned_data(df, 'data/cleaned_data.csv')