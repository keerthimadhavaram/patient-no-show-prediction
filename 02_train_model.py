"""Train Logistic Regression and Random Forest classifiers to predict
patient no-shows.
Requires scikit-learn: pip install -r requirements.txt
"""
import pandas as pd
import joblib
import os
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler

FEATURES_NUMERIC = ["age", "days_until_appointment", "prior_no_shows",
                     "wait_time_minutes", "appointment_month"]
FEATURES_CATEGORICAL = ["gender", "city", "department", "insurance_type", "diagnosis"]
TARGET = "no_show"

def build_feature_matrix(df: pd.DataFrame):
    X = pd.get_dummies(df[FEATURES_NUMERIC + FEATURES_CATEGORICAL],
                        columns=FEATURES_CATEGORICAL, drop_first=True)
    y = df[TARGET]
    return X, y

def train():
    df = pd.read_csv("data/patient_appointments.csv")
    X, y = build_feature_matrix(df)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y)

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    log_reg = LogisticRegression(max_iter=1000, random_state=42)
    log_reg.fit(X_train_scaled, y_train)

    rf = RandomForestClassifier(n_estimators=200, max_depth=8, random_state=42)
    rf.fit(X_train, y_train)

    os.makedirs("models", exist_ok=True)
    joblib.dump({"model": log_reg, "scaler": scaler, "columns": list(X.columns)},
                "models/logistic_regression.joblib")
    joblib.dump({"model": rf, "columns": list(X.columns)},
                "models/random_forest.joblib")

    return log_reg, rf, scaler, X_train, X_test, y_train, y_test

if __name__ == "__main__":
    train()
    print("Models trained and saved to models/")
