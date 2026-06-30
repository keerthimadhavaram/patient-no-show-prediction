# Patient No-Show Prediction

## Project Overview

This project uses machine learning to predict whether a patient is likely to miss a scheduled appointment. It is designed for Data Analyst, Healthcare Data Analyst, Data Science, and Healthcare Analytics roles.

The project demonstrates a complete classification workflow using Python, Pandas, Scikit-learn, feature engineering, model training, and model evaluation.

## Business Problem

Patient no-shows create scheduling inefficiencies, reduce provider productivity, increase operational costs, and delay patient care. Healthcare organizations can use predictive analytics to identify high-risk appointments and take proactive actions such as reminders, outreach, or schedule optimization.

## Objective

Build a classification model that predicts whether an appointment will result in a no-show.

Target variable:

```text
no_show
```

- `1` = Patient did not attend appointment
- `0` = Patient attended appointment

## Tools Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Logistic Regression
- Random Forest
- Classification Metrics
- Feature Engineering
- Healthcare Analytics

## Repository Structure

```text
patient-no-show-prediction/
├── README.md
├── requirements.txt
├── UPLOAD_STEPS.md
├── data/
│   └── patient_appointments.csv
├── src/
│   ├── 01_data_overview.py
│   ├── 02_train_model.py
│   ├── 03_evaluate_model.py
│   └── 04_predict_sample.py
├── models/
│   └── add_trained_model_here.md
├── docs/
│   ├── business_problem.md
│   ├── data_dictionary.md
│   ├── model_explanation.md
│   └── interview_questions.md
└── screenshots/
    └── add_model_output_screenshots_here.md
```

## Machine Learning Workflow

1. Load appointment dataset
2. Explore target distribution
3. Prepare features and target variable
4. One-hot encode categorical features
5. Split data into training and testing sets
6. Train Logistic Regression and Random Forest models
7. Evaluate using accuracy, precision, recall, F1-score, and confusion matrix
8. Explain business use case and recommendations

## Features Used

- Age
- Gender
- City
- Department
- Insurance Type
- Diagnosis
- Days Until Appointment
- Prior No-Shows
- Wait Time Minutes
- Appointment Month

## Evaluation Metrics

- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix

## Business Recommendations

Healthcare teams can use this model to:

- Identify high-risk no-show appointments
- Send reminder calls or SMS messages
- Prioritize outreach for patients with prior no-shows
- Improve scheduling efficiency
- Reduce lost appointment slots
- Support proactive care management

## Resume Alignment

This project supports Python, Pandas, NumPy, Scikit-learn, predictive analytics, classification, healthcare analytics, data preprocessing, feature engineering, and model evaluation.

## Author

**Keerthi Madhavaram**  
Data Analyst | Healthcare Analytics | Business Intelligence
