"""Score a handful of sample appointments with the trained model, the
way an outreach/scheduling tool would call this in production."""
import joblib
import pandas as pd

SAMPLE_APPOINTMENTS = pd.DataFrame([
    {"age": 24, "gender": "Male", "city": "Chicago", "department": "Primary Care",
     "insurance_type": "Medicaid", "diagnosis": "Annual Checkup",
     "days_until_appointment": 21, "prior_no_shows": 3, "wait_time_minutes": 35,
     "appointment_month": 8},
    {"age": 68, "gender": "Female", "city": "Naperville", "department": "Cardiology",
     "insurance_type": "Medicare", "diagnosis": "Hypertension",
     "days_until_appointment": 2, "prior_no_shows": 0, "wait_time_minutes": 15,
     "appointment_month": 8},
])

if __name__ == "__main__":
    bundle = joblib.load("models/random_forest.joblib")
    model, columns = bundle["model"], bundle["columns"]

    X_sample = pd.get_dummies(SAMPLE_APPOINTMENTS,
        columns=["gender","city","department","insurance_type","diagnosis"], drop_first=True)
    X_sample = X_sample.reindex(columns=columns, fill_value=0)

    probs = model.predict_proba(X_sample)[:, 1]
    preds = model.predict(X_sample)

    for i, (p, pred) in enumerate(zip(probs, preds)):
        risk = "HIGH RISK" if p > 0.5 else "low risk"
        print(f"Appointment {i+1}: no-show probability = {p:.2f} ({risk}, predicted={pred})")
