"""Evaluate the trained models: accuracy, precision, recall, F1,
and confusion matrix."""
import joblib
import pandas as pd
from sklearn.metrics import (accuracy_score, precision_score, recall_score,
                              f1_score, confusion_matrix, classification_report)
from sklearn.model_selection import train_test_split

from importlib import import_module
train_module = import_module("02_train_model") if False else None  # kept explicit for clarity

def load_and_split():
    df = pd.read_csv("data/patient_appointments.csv")
    from importlib.machinery import SourceFileLoader
    tm = SourceFileLoader("train_model", "src/02_train_model.py").load_module()
    X, y = tm.build_feature_matrix(df)
    return train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

def evaluate(name, model, X_test, y_test, needs_scaling=False, scaler=None):
    X_eval = scaler.transform(X_test) if needs_scaling else X_test
    preds = model.predict(X_eval)
    print(f"\n=== {name} ===")
    print("Accuracy: ", round(accuracy_score(y_test, preds), 3))
    print("Precision:", round(precision_score(y_test, preds), 3))
    print("Recall:   ", round(recall_score(y_test, preds), 3))
    print("F1-score: ", round(f1_score(y_test, preds), 3))
    print("Confusion matrix:\n", confusion_matrix(y_test, preds))
    print(classification_report(y_test, preds))

if __name__ == "__main__":
    X_train, X_test, y_train, y_test = load_and_split()

    lr_bundle = joblib.load("models/logistic_regression.joblib")
    rf_bundle = joblib.load("models/random_forest.joblib")

    evaluate("Logistic Regression", lr_bundle["model"], X_test, y_test,
              needs_scaling=True, scaler=lr_bundle["scaler"])
    evaluate("Random Forest", rf_bundle["model"], X_test, y_test)
