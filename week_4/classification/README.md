# Classification Task: Weather Prediction

## 🌦️ Dataset Overview

**File**: `weather_classification_data.csv`  
**Task**: Multi-class classification  
**Target Variable**: Weather Type (Rainy, Sunny, Cloudy, Snowy)

## 📊 Features Description

| Feature | Type | Description |
|---------|------|-------------|
| Temperature | Numeric | Temperature in Celsius |
| Humidity | Numeric | Humidity percentage |
| Wind Speed | Numeric | Wind speed in km/h |
| Precipitation (%) | Numeric | Precipitation percentage |
| Cloud Cover | Categorical | Cloud cover description |
| Atmospheric Pressure | Numeric | Pressure in hPa |
| UV Index | Numeric | UV radiation strength |
| Season | Categorical | Season when recorded |
| Visibility (km) | Numeric | Visibility distance |
| Location | Categorical | Location type |
| **Weather Type** | **Categorical** | **Target: Rainy/Sunny/Cloudy/Snowy** |

## 🎯 Task Requirements

### 1. Data Cleaning & Preparation
- [ ] Load and explore dataset structure
- [ ] Handle missing values (justify methods)
- [ ] Encode categorical variables (one-hot/label encoding)
- [ ] Normalize/standardize numerical features
- [ ] Split data (80% train, 20% test)

### 2. Exploratory Data Analysis
- [ ] Generate summary statistics
- [ ] Create visualizations:
  - Histograms for feature distributions
  - Scatter plots for feature relationships
  - Box plots for outlier detection
  - Correlation heatmap
- [ ] Identify patterns and anomalies

### 3. Machine Learning Models
Apply **minimum 3 algorithms**:

**Suggested Models & Rationale**:
1. **Logistic Regression**: Baseline linear model, interpretable
2. **Decision Tree**: Handles non-linear relationships, easy to visualize
3. **Random Forest**: Ensemble method, robust to overfitting
4. **Additional options**: SVM, KNN, Gradient Boosting

### 4. Model Evaluation
**Metrics to Calculate**:
- Accuracy
- Precision, Recall, F1-Score (per class)
- Confusion Matrix
- Classification Report

## 📁 File Structure

```
classification/
├── README.md                           # This file
├── weather_classification_analysis.ipynb  # Main analysis
├── data/
│   └── weather_classification_data.csv
└── reports/
    └── classification_report.md        # Final report
```

## 🎯 Expected Deliverables

1. **Jupyter Notebook** with complete analysis
2. **Classification Report** summarizing findings
3. **Model Comparison** table/visualization
4. **Best Model Selection** with justification

## 💡 Tips for Success

- Start with simple models before complex ones
- Pay attention to class imbalance
- Use cross-validation for robust evaluation
- Document your reasoning for each step
- Create clear, labeled visualizations
