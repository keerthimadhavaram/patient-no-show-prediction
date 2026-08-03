"""Explore the target distribution and feature landscape before modeling."""
import pandas as pd

if __name__ == "__main__":
    df = pd.read_csv("data/patient_appointments.csv")
    print("Shape:", df.shape)
    print("\nTarget distribution:")
    print(df["no_show"].value_counts(normalize=True).round(3))
    print("\nNo-show rate by insurance type:")
    print(df.groupby("insurance_type")["no_show"].mean().round(3).sort_values(ascending=False))
    print("\nNo-show rate by prior_no_shows:")
    print(df.groupby("prior_no_shows")["no_show"].mean().round(3))
    print("\nMissing values:")
    print(df.isna().sum())
