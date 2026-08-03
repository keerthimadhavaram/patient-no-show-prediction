# Data Dictionary — patient_appointments.csv

| Column | Description |
|---|---|
| patient_id | Patient identifier |
| age | Patient age |
| gender | Female / Male / Other |
| city | Patient city |
| department | Hospital department for this appointment |
| insurance_type | Private / Medicare / Medicaid / Self-Pay / HMO / PPO |
| diagnosis | Visit reason / diagnosis |
| days_until_appointment | Days between scheduling and the appointment date |
| prior_no_shows | Count of this patient's previous no-shows |
| wait_time_minutes | Typical wait time for this appointment slot |
| appointment_month | Calendar month of the appointment (1-12) |
| no_show | Target: 1 = no-show, 0 = attended |
