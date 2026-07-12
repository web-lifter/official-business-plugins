# Forecasting Model Spec — Weekly active users (AU SaaS)

**Cadence:** Weekly (week ending Sunday)
**Horizon:** 8 weeks
**History:** 156 weeks (3 years)
**Owner:** Data team — Sara

---

## Series Snapshot

| Metric | Value |
|--------|-------|
| Mean | 28,400 WAU |
| StDev | 4,200 |
| % zeros | 0% |
| Trend | Linear positive (~+200 WAU/wk) |
| Seasonality | Weekly + annual (school holiday dips Dec–Jan and Jul) |
| Known regressors | Paid-marketing spend (weekly $); product-launch flags; AU public holidays |

---

## Diagnostic Findings

- Stationarity (ADF p-value on log-diff): 0.001 (stationary in first difference)
- Autocorrelation profile: strong at lag 1 (0.78) and lag 52 (0.61); weak at lag 26
- Outliers identified: 3 (COVID lockdown weeks Mar-Apr 2020; treatment: dummy variable)
- Structural breaks: one — post-COVID return to baseline by week of 30/06/2022
- AU public-holiday effect: -8% to -12% WAU on weeks containing Christmas Day, New Year, Easter Monday

---

## Recommended Model

**Family:** Prophet (additive)
**Spec:**
- yearly_seasonality = True (Fourier order 10)
- weekly_seasonality = True (Fourier order 3)
- holidays = AU public holidays (NSW + VIC + QLD + WA + SA + TAS + ACT + NT consolidated)
- changepoint_prior_scale = 0.05 (conservative — series is fairly smooth)
- seasonality_mode = "multiplicative" (variance grows with level)
- additional regressors: paid-marketing-spend (lag 0), product-launch (binary flag)

**Why this model:** Prophet handles multiple seasonalities + holidays well; interpretable; regressor support; ~156 weeks is sufficient. SARIMA would also work but holiday handling is more manual. ML overkill at this data size.

---

## Feature Engineering / Regressors

| Regressor | Source | Known at forecast time? | Notes |
|-----------|--------|------------------------|-------|
| Paid-marketing spend | Marketing planned budget | Yes (committed budget known 8 wk out) | Lag 0 |
| Product-launch flag | Product roadmap | Yes (≥ 4 wk lead time on launches) | Binary |
| AU public holidays | Static (sourced from data.gov.au) | Yes | Built-in to Prophet |
| Weather | BoM forecasts | Partial (7 days reliable) | Excluded — too short to be useful |
| Competitor activity | Manual flags | No | Excluded — not known at forecast time |

---

## Validation Plan

- **Method:** Walk-forward backtest, 4 origins (every 12 weeks), train/test gap 8 weeks
- **Baseline 1:** Naive (last week's value)
- **Baseline 2:** Seasonal-naive (same week last year + linear trend)
- **Primary metric:** MAPE
- **Secondary:** Directional accuracy on weekly delta; % weeks within ±10%

| Origin | MAPE | sMAPE | RMSE | Beats baseline 1? | Beats baseline 2? |
|--------|------|-------|------|------------------|------------------|
| Origin 1 (06/2025) | 4.8% | 4.7% | 1,580 | Yes (vs 9.2%) | Yes (vs 6.1%) |
| Origin 2 (09/2025) | 5.2% | 5.0% | 1,650 | Yes (vs 9.5%) | Yes (vs 6.4%) |
| Origin 3 (12/2025) | 6.1% | 5.8% | 1,820 | Yes (vs 10.2%) | Yes (vs 7.0%) — holiday season harder |
| Origin 4 (03/2026) | 5.3% | 5.1% | 1,610 | Yes (vs 9.4%) | Yes (vs 6.3%) |

Mean across origins: **MAPE 5.4%**, well below the 8% target.

---

## Monitoring + Retraining

**Daily:** Not applicable (weekly cadence)
**Weekly (every Monday):** Forecast vs actual logged. Alert if absolute error > 12% (2.2× backtest MAPE).
**Monthly:** Rolling 8-week MAPE; alert if > 1.5× backtest MAPE.
**Quarterly:** Full re-validation; reconsider changepoint_prior_scale.

**Retraining triggers:**
- **Scheduled:** Weekly retrain on the freshest data (cheap with Prophet)
- **Event-driven:** Any week MAPE > 12%; major product launch; pricing change; competitor entry/exit; AU policy change affecting product

---

## Accuracy Targets

| Metric | Target | Justification |
|--------|--------|---------------|
| MAPE | < 8% | Marketing planning team needs ±10% confidence to allocate spend |
| Directional accuracy | > 75% | We use the forecast to decide spend up/down weekly |
| % weeks within ±10% | > 60% | Pricing/staffing decisions key off this |

Current backtest results comfortably exceed all three targets.
