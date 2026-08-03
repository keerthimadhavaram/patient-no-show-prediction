# Interview Prep — Questions This Project Answers

1. **Walk me through your modeling approach for this problem.**
   Two models (Logistic Regression for interpretability, Random Forest
   for raw performance), one-hot encoded categoricals, standardized
   numerics for the logistic model, 80/20 stratified split — see
   `src/02_train_model.py`.

2. **Your accuracy is 82% but recall is only 9% — is that a good model?**
   No, and that's the point: with a ~20% base rate, a model that
   predicts "no-show" only when very confident gets high accuracy by
   mostly predicting the majority class. Accuracy alone is misleading
   on imbalanced data — see `docs/model_explanation.md`'s threshold
   discussion.

3. **How would you decide what classification threshold to use?**
   Base it on the relative cost of false positives vs. false
   negatives. Here, a missed no-show is costlier than an unnecessary
   reminder call, so I'd lower the threshold to trade some precision
   for meaningfully higher recall (0.30 in this project's analysis).

4. **What features mattered most, and does that make business sense?**
   Prior no-show count, wait time, and days-until-appointment ranked
   highest — all align with how healthcare operations research
   describes no-show risk, which is a good sanity check on the model.

5. **How would you validate this model actually helps before rolling
   it out fully?**
   An A/B test: apply the outreach intervention to model-flagged
   high-risk patients in a treatment group vs. a control group, and
   measure the actual no-show rate difference — not just trust the
   offline metrics.
