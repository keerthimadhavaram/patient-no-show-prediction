# Business Problem

Patient no-shows create scheduling inefficiencies, reduce provider
productivity, increase operational costs, and delay care for other
patients who could have filled that slot.

This project builds a classification model to flag appointments at
elevated risk of a no-show **before** the appointment date, so clinic
staff can prioritize reminder calls, SMS reminders, or overbooking
decisions for the highest-risk slots rather than treating every
appointment the same.

## Target Variable

`no_show`: 1 if the patient did not attend, 0 if they attended.

Base rate in this dataset: **19.7%** of appointments end in a no-show
— consistent with published no-show rates in outpatient healthcare
settings (commonly cited in the 15-30% range).
