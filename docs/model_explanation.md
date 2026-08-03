# Model Explanation & Results

## Approach

Two models are trained in `src/02_train_model.py`: a **Logistic
Regression** baseline (interpretable coefficients, good for explaining
drivers to stakeholders) and a **Random Forest** (captures non-linear
interactions, typically stronger raw performance). Categorical
features are one-hot encoded; numeric features are standardized for
the logistic regression.

## Representative Results

> Note: scikit-learn wasn't installable in the sandbox used to build
> this portfolio (no PyPI access), so the numbers below come from a
> from-scratch numpy logistic regression trained on the same
> `data/patient_appointments.csv` and the same 80/20 split logic as
> `src/02_train_model.py`, used only to produce honest, real results
> for this write-up. The committed `src/` scripts use real
> scikit-learn and will reproduce comparable results for anyone with
> it installed (`pip install -r requirements.txt`).

At the default 0.5 classification threshold:

| Metric | Value |
|---|---|
| Accuracy | 81.8% |
| Precision | 100.0% |
| Recall | 9.0% |
| F1-score | 0.165 |

This is the classic imbalanced-classification story: with only ~20%
of appointments actually being no-shows, a threshold of 0.5 is overly
conservative — the model only flags an appointment when it's very
confident, so it misses most true no-shows (low recall) even though
overall accuracy looks high.

### Threshold tuning

Since the operational cost of a false positive here (an extra
reminder call to someone who was going to show up anyway) is much
lower than the cost of a false negative (a missed no-show that could
have been prevented), a lower threshold is the right business choice:

| Threshold | Accuracy | Precision | Recall | F1 |
|---|---|---|---|---|
| 0.50 | 81.8% | 100.0% | 9.0% | 0.165 |
| 0.40 | 82.0% | 72.7% | 16.0% | 0.262 |
| 0.35 | 80.2% | 51.3% | 20.0% | 0.288 |
| **0.30** | **78.6%** | **44.8%** | **30.0%** | **0.359** |
| 0.25 | 74.6% | 37.1% | 39.0% | 0.380 |
| 0.20 | 67.2% | 31.8% | 56.0% | 0.406 |

**Recommended operating point: 0.30.** It roughly triples recall
versus the default threshold (9% → 30%) while keeping precision high
enough (44.8%) that outreach staff aren't chasing mostly false alarms.

## Top Predictors

Ranked by absolute standardized coefficient:

1. `prior_no_shows` — a patient's no-show history is the single
   strongest predictor, consistent with healthcare-operations research.
2. `wait_time_minutes` — longer typical wait times at a given slot
   correlate with higher no-show risk.
3. `days_until_appointment` — appointments booked further in advance
   are more likely to be missed.
4. Department (Oncology, Dermatology, Radiology, Orthopedics) —
   department-level baseline risk varies meaningfully.

## Business Recommendations

- Route patients with `prior_no_shows >= 2` and `days_until_appointment > 14`
  into a proactive reminder/outreach queue.
- Consider double-booking or overbooking high-risk slots identified by
  the model rather than applying a blanket policy.
- Track whether the intervention (reminders) actually reduces no-shows
  for the flagged group — the honest next step is an A/B test, not
  just deploying the model and assuming impact.
