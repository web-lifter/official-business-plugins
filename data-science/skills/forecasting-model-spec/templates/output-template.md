# Forecasting Model Spec — {{series_name}}

**Cadence:** {{cadence}}
**Horizon:** {{h}} periods
**History:** {{n}} periods
**Owner:** {{name}}

---

## Series Snapshot

| Metric | Value |
|--------|-------|
| Mean | {{val}} |
| StDev | {{val}} |
| % zeros | {{pct}} |
| Trend | {{linear/multiplicative/break}} |
| Seasonality | {{daily/weekly/yearly}} |
| Known regressors | {{list}} |

---

## Diagnostic Findings

- Stationarity (ADF p-value): {{p}}
- Autocorrelation profile: {{describe}}
- Outliers identified: {{count}} (treatment: {{action}})
- Structural breaks: {{none/dates}}
- AU public-holiday effect: {{magnitude}}

---

## Recommended Model

**Family:** {{model}}
**Spec:** {{hyperparameters}}
**Why this model:** {{rationale}}

---

## Feature Engineering / Regressors

| Regressor | Source | Known at forecast time? | Notes |
|-----------|--------|------------------------|-------|

---

## Validation Plan

- **Method:** Walk-forward backtest, {{n}} origins, train/test gap {{p}} periods
- **Baseline 1:** Naive (last observed)
- **Baseline 2:** Seasonal-naive (same period last year/week)
- **Primary metric:** {{MAPE/sMAPE/RMSE}}
- **Secondary:** Directional accuracy; % within 10%

| Origin | MAPE | sMAPE | RMSE | Beats baseline 1? | Beats baseline 2? |
|--------|------|-------|------|------------------|------------------|

---

## Monitoring + Retraining

**Daily:** Log forecast vs actual; alert if absolute error > {{threshold}}
**Weekly:** Rolling 4-week MAPE chart; alert if > 1.5× backtest MAPE
**Monthly:** Full re-validation with newest data

**Retraining triggers:**
- Weekly scheduled retrain
- MAPE breach
- Known intervention (pricing / marketing / supply)
- Seasonality shift (e.g. school-holiday calendar change)

---

## Accuracy Targets

| Metric | Target | Justification |
|--------|--------|---------------|
| MAPE | < {{n}}% | Cost of being wrong; downstream-team consumer needs |
| Directional | > {{n}}% | Decisions are direction-sensitive |
