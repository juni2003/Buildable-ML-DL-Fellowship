import os
import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score

class ModelTrainer:
    def __init__(self,
                 data_path=None,
                 target_col='purchased',
                 test_size=0.2,
                 random_state=42):
        # Prefer augmented dataset if it exists
        if data_path is None:
            aug_path = 'data/processed/augmented_data.csv'
            clean_path = 'data/processed/cleaned_data.csv'
            data_path = aug_path if os.path.isfile(aug_path) else clean_path
        self.data_path = data_path
        self.target_col = target_col
        self.test_size = test_size
        self.random_state = random_state
        self.models = {}
        self.metrics = []

    def load_data(self):
        df = pd.read_csv(self.data_path)
        if self.target_col not in df.columns:
            raise ValueError(f"Target column '{self.target_col}' not found.")
        X = df.drop(columns=[self.target_col])
        y = df[self.target_col]
        return X, y

    def split(self, X, y):
        return train_test_split(
            X, y,
            test_size=self.test_size,
            random_state=self.random_state,
            stratify=y
        )

    def build_models(self):
        # Logistic Regression with scaling
        logreg = Pipeline([
            ("scaler", StandardScaler()),
            ("clf", LogisticRegression(max_iter=1000, random_state=self.random_state))
        ])
        rf = RandomForestClassifier(
            n_estimators=200,
            random_state=self.random_state,
            n_jobs=-1
        )
        self.models = {
            "logistic_regression": logreg,
            "random_forest": rf
        }

    def evaluate(self, name, model, X_test, y_test):
        y_pred = model.predict(X_test)
        # Some models use predict_proba, others decision_function
        if hasattr(model, "predict_proba"):
            y_prob = model.predict_proba(X_test)[:, 1]
        else:
            # Fallback (not expected here)
            y_prob = y_pred
        m = {
            "model": name,
            "accuracy": accuracy_score(y_test, y_pred),
            "precision": precision_score(y_test, y_pred, zero_division=0),
            "recall": recall_score(y_test, y_pred, zero_division=0),
            "f1": f1_score(y_test, y_pred, zero_division=0),
            "roc_auc": roc_auc_score(y_test, y_prob)
        }
        self.metrics.append(m)
        print(f"{name}: acc={m['accuracy']:.4f} prec={m['precision']:.4f} "
              f"rec={m['recall']:.4f} f1={m['f1']:.4f} auc={m['roc_auc']:.4f}")

    def save_models(self):
        os.makedirs("models", exist_ok=True)
        for name, model in self.models.items():
            path = f"models/{name}.joblib"
            joblib.dump(model, path)
            print(f"Saved model: {path}")

    def save_metrics(self):
        os.makedirs("results", exist_ok=True)
        df_metrics = pd.DataFrame(self.metrics)
        df_metrics.to_csv("results/metrics.csv", index=False)
        print("Saved metrics: results/metrics.csv")

    def run(self):
        print(f"Loading data from: {self.data_path}")
        X, y = self.load_data()
        X_train, X_test, y_train, y_test = self.split(X, y)
        self.build_models()
        for name, model in self.models.items():
            model.fit(X_train, y_train)
            self.evaluate(name, model, X_test, y_test)
        self.save_models()
        self.save_metrics()
        # Return best model name by F1 (can adjust if preferred)
        best = max(self.metrics, key=lambda d: d["f1"])
        print(f"Best model by F1: {best['model']}")
        return best

if __name__ == "__main__":
    trainer = ModelTrainer()
    trainer.run()
