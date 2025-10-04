# Regression Task: Car Price Analysis (Preprocessing Only)

## 🚗 Dataset Overview

**File**: `pakwheels_used_cars.csv`  
**Source**: PakWheels (Pakistan's largest car marketplace)  
**Size**: ~78,000 cars with 13 features  
**Task**: Data preprocessing and EDA only (no model building required)

## 📊 Features Description

| Feature | Type | Description |
|---------|------|-------------|
| ad_ref | Identifier | Unique advertisement reference |
| city | Categorical | City where car is sold |
| assembly | Categorical | Local vs Imported |
| body | Categorical | Body type (sedan, hatchback, etc.) |
| make | Categorical | Car manufacturer |
| model | Categorical | Car model variant |
| year | Numeric | Year of production |
| engine_cc | Numeric | Engine volume |
| transmission | Categorical | Auto/Manual |
| fuel_type | Categorical | Petrol/Diesel/Hybrid |
| color | Categorical | Car color |
| registered | Categorical | Registration city/province |
| mileage | Numeric | Mileage in kilometers |
| **price** | **Numeric** | **Target: Car price in PKR** |

## 🎯 Task Requirements

### 1. Data Cleaning & Preparation
- [ ] Load and explore dataset structure
- [ ] Handle missing values (justify methods)
- [ ] Identify and handle outliers
- [ ] Data type corrections
- [ ] Feature engineering opportunities
- [ ] Encode categorical variables
- [ ] Normalize/standardize numerical features

### 2. Exploratory Data Analysis
- [ ] Dataset shape and basic info
- [ ] Missing value analysis
- [ ] Summary statistics
- [ ] Price distribution analysis
- [ ] Feature relationships with price
- [ ] Categorical feature analysis

### 3. Visualizations Required
- [ ] **Histograms**: Price distribution, mileage, year
- [ ] **Scatter plots**: Price vs mileage, year, engine_cc
- [ ] **Box plots**: Price by make, transmission, fuel_type
- [ ] **Correlation heatmap**: Numerical features
- [ ] **Bar charts**: Count by categorical features

### 4. Data Quality Assessment
- [ ] Missing value patterns
- [ ] Outlier identification
- [ ] Data consistency checks
- [ ] Feature correlation analysis

## 📁 File Structure

```
regression/
├── README.md                    # This file
├── car_price_analysis.ipynb     # Main preprocessing notebook
├── data/
│   └── pakwheels_used_cars.csv
└── reports/
    └── regression_report.md     # EDA findings
```

## 🎯 Expected Deliverables

1. **Jupyter Notebook** with complete preprocessing
2. **EDA Report** with key insights
3. **Data Quality Assessment**
4. **Recommendations** for future modeling

## 💡 Focus Areas

- **Price Analysis**: What factors most influence car prices?
- **Market Insights**: Popular makes, models, cities
- **Data Quality**: Missing values, outliers, inconsistencies
- **Feature Engineering**: Create new meaningful features

## ⚠️ Important Notes

- **No model building required** for this dataset
- Focus on thorough preprocessing and EDA
- Document all data cleaning decisions
- Provide business insights from analysis
