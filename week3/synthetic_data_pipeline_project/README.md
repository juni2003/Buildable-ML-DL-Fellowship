# Synthetic Data Pipeline Project

A lightweight, end‑to‑end machine learning mini‑pipeline built on a synthetic customer dataset.  
It demonstrates: data preparation, exploratory analysis, statistical summarization, data augmentation, visualization, model training (Logistic Regression vs Random Forest), evaluation, and artifact saving.

---

## 1. Key Features

- Reproducible directory layout (`data/`, `plots/`, `models/`, `results/`).
- Clean / augmented datasets (`cleaned_data.csv`, `augmented_data.csv`).
- Exploratory visualizations (age distribution, gender distribution, correlation heatmap, age vs income scatter).
- Simple statistics module (mean, median, std for selected numeric columns).
- Data augmentation (row duplication + small Gaussian noise on numeric predictors; target preserved).
- Binary classification task (`purchased`).
- Metrics captured: Accuracy, Precision, Recall, F1, ROC‑AUC.
- Model artifacts saved with `joblib`.

---

## 2. Dataset (Synthetic)

Columns (representative):
| Column | Type | Description |
|--------|------|-------------|
| age | int/float | Customer age |
| income | float | Annual income (synthetic currency units) |
| purchase_amount | float | Recent purchase monetary value |
| monthly_visits | int | Approx. monthly site visits |
| satisfaction_score | float | User feedback score (e.g. 1–5 or scaled) |
| gender | int | 0 = Female, 1 = Male |
| product_type | int | Encoded product/category type |
| purchased | int (target) | 0 = No purchase, 1 = Purchased |

Notes:
- Entirely synthetic; safe for open demonstration.
- Class balance may be moderately skewed depending on generation parameters.
- Augmentation doubles row count with mild feature jitter; target is NOT altered.

---

## 3. Repository Structure

```
project_root/
├─ data/
│  ├─ raw/                  # (Optional) original synthetic generation outputs
│  └─ processed/
│     ├─ cleaned_data.csv
│     └─ augmented_data.csv
├─ plots/
│  ├─ age_histogram.png
│  ├─ gender_barplot.png
│  ├─ correlation_heatmap.png
│  └─ age_income_scatter.png
├─ models/
│  ├─ logistic_regression.joblib
│  └─ random_forest.joblib
├─ results/
│  └─ metrics.csv
├─ stats.py
├─ augment.py
├─ visualizer.py
├─ model_trainer.py
├─ q7_run.py                # (Optional helper: stats + augmentation demo)
└─ README.md
```

---

## 4. Installation

```bash
# (Optional) create environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

pip install -r requirements.txt
```

If you do not have a `requirements.txt`, install essentials:
```bash
pip install pandas numpy seaborn matplotlib scikit-learn joblib
```

---

## 5. Pipeline Overview

1. (Data Generation – external / not included explicitly)  
2. Cleaning (remove/repair NaNs except target, encode categorical fields).  
3. Exploratory Data Analysis (EDA) & visualization (`visualizer.py`).  
4. Statistics summary (`stats.py` via `q7_run.py`).  
5. Augmentation (`augment.py`) to expand dataset size and encourage model robustness.  
6. Train & evaluate models (`model_trainer.py`).  
7. Persist artifacts (models + metrics + plots).  
8. Review performance & iterate.

---

## 6. Scripts

### visualizer.py
- Loads `data/processed/cleaned_data.csv`.
- Generates four plots into `plots/`.
- Quick visual sanity check for distributions and relationships.

### stats.py
- Functions: `compute_mean`, `compute_median`, `compute_std`, `describe_columns`.
- Used to report basic descriptive statistics for selected numeric features.

### augment.py
- Function: `augment_dataset(df, noise_frac=0.02, target_col='purchased')`
- Duplicates the dataset, adds light Gaussian noise to numeric predictors (excludes target), concatenates & shuffles.

### q7_run.py (optional helper)
- Loads cleaned data.
- Computes stats for first two numeric columns (excluding target).
- Runs augmentation and saves `augmented_data.csv`.

### model_trainer.py
- Selects augmented dataset if present; otherwise uses cleaned.
- Splits (stratified, test_size=0.2).
- Builds Logistic Regression (with scaling) and Random Forest.
- Evaluates: accuracy, precision, recall, F1, ROC‑AUC.
- Saves models to `models/` and metrics to `results/metrics.csv`.
- Reports best model (by F1).

---

## 7. Usage Walkthrough

### A. Ensure processed data exists
Place `cleaned_data.csv` in `data/processed/`.

### B. (Optional) Run statistics + augmentation
```bash
python q7_run.py
```
Outputs:
- Updated `data/processed/augmented_data.csv`.
- Console stats for selected numeric columns.

### C. Generate plots
```bash
python visualizer.py
```

### D. Train models
```bash
python model_trainer.py
```
Artifacts:
- `models/logistic_regression.joblib`
- `models/random_forest.joblib`
- `results/metrics.csv`

### E. Inspect metrics
Open `results/metrics.csv` or read in Python:
```python
import pandas as pd
print(pd.read_csv("results/metrics.csv"))
```

---

## 8. Example Evaluation Results (Sample Run)

| Model                | Accuracy | Precision | Recall | F1     | ROC-AUC |
|----------------------|----------|-----------|--------|--------|---------|
| logistic_regression  | 0.5900   | 0.6337    | 0.8516 | 0.7267 | 0.5697  |
| random_forest        | 0.8400   | 0.8117    | 0.9766 | 0.8865 | 0.8989  |

Interpretation:
- Random Forest generalizes better on nonlinear patterns (higher F1 & ROC‑AUC).
- Logistic Regression still achieves high recall but lower precision and ranking ability.

---

## 9. Common Issues & Fixes

| Issue | Cause | Fix |
|-------|-------|-----|
| ValueError: Unknown label type: continuous | Target (`purchased`) became non-binary after imputation or noise | Exclude target from augmentation & imputation; threshold or cast back to int |
| Poor performance on Logistic Regression | Nonlinear feature interactions | Add polynomial/interaction terms or use tree ensembles |
| All metrics low | Noise too high / data leakage / wrong target | Re-check augmentation noise fraction & target integrity |
| ROC-AUC error | Only one class in test split | Ensure stratified split & sufficient class balance |

Sanity check snippet:
```python
df = pd.read_csv('data/processed/augmented_data.csv')
assert set(df['purchased'].unique()) <= {0,1}
```

---

## 10. Extensibility (Future Roadmap)

Potential enhancements:
- Config file (YAML/JSON) for paths & hyperparameters.
- Automated data validation (target binary, no forbidden NaNs) before training.
- Class imbalance handling (SMOTE, class weights).
- Additional models: Gradient Boosting / XGBoost / LightGBM.
- Hyperparameter tuning (Grid / Random / Bayesian).
- Experiment tracking (MLflow) and structured logging.
- Dockerization & scheduled retraining.
- FastAPI microservice + drift monitoring.

---

## 11. Reproducibility Tips

- Fix random seeds (already using `random_state=42`).
- Save environment: `pip freeze > requirements.txt`.
- Version control data schema changes (add a `SCHEMA.md` if columns evolve).
- Store metrics with timestamps if running multiple experiments.

---

## 12. Sample Code Snippets

Load and predict with best model:
```python
import joblib, pandas as pd
model = joblib.load("models/random_forest.joblib")
X_new = pd.read_csv("data/processed/cleaned_data.csv").drop(columns=["purchased"])
preds = model.predict(X_new.head(5))
print(preds)
```

Quick ROC-AUC recalculation (if needed):
```python
from sklearn.metrics import roc_auc_score
probs = model.predict_proba(X_new)[:,1]
# (Assuming you have the true labels y_true)
# roc_auc_score(y_true, probs)
```

---

## 13. Limitations

- Synthetic dataset may not reflect real-world noise, seasonality, or rare events.
- Simple augmentation (noise + duplication) may not introduce genuine new behavior.
- No feature engineering beyond basic encodings.
- No formal hyperparameter tuning performed yet.

---

## 14. License

(Insert license of choice, e.g. MIT. Example:)

```
MIT License – See LICENSE file if added.
```

---

## 15. Acknowledgments

- Built with: [pandas](https://pandas.pydata.org/), [NumPy](https://numpy.org/), [scikit-learn](https://scikit-learn.org/), [Seaborn](https://seaborn.pydata.org/), [Matplotlib](https://matplotlib.org/).
- Educational synthetic project for demonstrating a minimal ML workflow.

---

## 16. Quick Start Summary

```bash
# 1. Install deps
pip install pandas numpy seaborn matplotlib scikit-learn joblib

# 2. (Ensure cleaned_data.csv exists)
# 3. Augment (optional)
python q7_run.py

# 4. Visualize
python visualizer.py

# 5. Train models
python model_trainer.py

# 6. Review metrics
cat results/metrics.csv
```

---

Feel free to adapt, extend, or integrate with more advanced MLOps tooling as next steps. Enjoy experimenting!
