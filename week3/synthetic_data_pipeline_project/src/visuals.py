"""
Visualization helper functions using matplotlib.
"""
import matplotlib.pyplot as plt
import numpy as np

def plot_histogram(data, column_name="Data", bins=20, title=None):
    """Create histogram for numerical data."""
    plt.figure(figsize=(8, 6))
    plt.hist(data, bins=bins, alpha=0.7, edgecolor='black')
    
    if title is None:
        title = f"Histogram of {column_name}"
    
    plt.title(title)
    plt.xlabel(column_name)
    plt.ylabel('Frequency')
    plt.grid(True, alpha=0.3)
    plt.show()
    print(f"✅ Histogram plotted for {column_name}")

def plot_scatterplot(x_data, y_data, x_label="X", y_label="Y", title=None):
    """Create scatter plot for two variables."""
    plt.figure(figsize=(8, 6))
    plt.scatter(x_data, y_data, alpha=0.6)
    
    if title is None:
        title = f"Scatter Plot: {x_label} vs {y_label}"
    
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.grid(True, alpha=0.3)
    plt.show()
    print(f"✅ Scatter plot created: {x_label} vs {y_label}")

def plot_multiple_histograms(df, columns, figsize=(12, 8)):
    """Plot multiple histograms in subplots."""
    n_cols = len(columns)
    n_rows = (n_cols + 1) // 2
    
    fig, axes = plt.subplots(n_rows, 2, figsize=figsize)
    axes = axes.flatten() if n_rows > 1 else [axes] if n_rows == 1 else axes
    
    for i, col in enumerate(columns):
        if i < len(axes):
            axes[i].hist(df[col], bins=20, alpha=0.7, edgecolor='black')
            axes[i].set_title(f'Histogram of {col}')
            axes[i].set_xlabel(col)
            axes[i].set_ylabel('Frequency')
            axes[i].grid(True, alpha=0.3)
    
    # Hide empty subplots
    for j in range(i + 1, len(axes)):
        axes[j].set_visible(False)
    
    plt.tight_layout()
    plt.show()
    print(f"✅ Multiple histograms plotted for {len(columns)} columns")

def quick_data_overview(df, numerical_cols):
    """Quick visual overview of numerical data."""
    print("📊 Creating quick data overview...")
    
    # Plot histograms for all numerical columns
    plot_multiple_histograms(df, numerical_cols)
    
    # Create scatter plot matrix for first 3 numerical columns
    if len(numerical_cols) >= 2:
        col1, col2 = numerical_cols[0], numerical_cols[1]
        plot_scatterplot(df[col1], df[col2], col1, col2)
    
    print("✅ Quick overview completed")
