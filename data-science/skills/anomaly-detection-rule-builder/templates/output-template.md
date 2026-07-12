## Anomaly Detection System — [Business Name]

### 1. Detection Rule Summary

| Rule ID | Metric | Type | Severity | Status |
|---------|--------|------|----------|--------|
| {{rule_id}} | {{metric_name}} | Static / Statistical | Critical / Warning / Info | Active / Tuning |

<!-- Provide a summary table of all detection rules before diving into detail. -->

---

### 2. Metric Profiles

For each monitored metric:

- **Metric:** {{metric_name}}
- **Source:** {{table.column or API endpoint}}
- **Normal Range:** {{lower_bound}} to {{upper_bound}}
- **Granularity:** Hourly / Daily / Weekly
- **Seasonality:** {{day-of-week pattern, monthly pattern, annual events}}
- **Baseline Period:** {{rolling window, e.g. 30 days}}

<!-- Repeat for each metric. Include expected patterns and known seasonal effects. -->

---

### 3. Static Threshold Rules

For each static rule:

- **Rule ID:** {{rule_id}}
- **Metric:** {{metric_name}}
- **Condition:** `{{metric}} {{operator}} {{threshold}}`
- **Severity:** Critical / Warning / Info
- **SQL:**
```sql
-- {{Rule description}}
SELECT ...
FROM ...
WHERE ...
```
- **Rationale:** {{Why this threshold was chosen}}

<!-- Static thresholds are appropriate for hard limits: revenue > $0, error rate < 5%, etc. -->

---

### 4. Statistical Detection Rules

For each statistical rule:

- **Rule ID:** {{rule_id}}
- **Metric:** {{metric_name}}
- **Method:** Z-score / Percentage deviation / IQR
- **Lookback Window:** {{e.g. 30 days rolling}}
- **Threshold:** {{e.g. Z > 3.0 or deviation > 25%}}
- **Day-of-Week Adjustment:** Yes / No
- **SQL:**
```sql
-- {{Rule description with statistical method}}
WITH baseline AS (
  SELECT ...
),
current_value AS (
  SELECT ...
)
SELECT ...
```
- **Sensitivity Notes:** {{Expected false positive rate, tuning guidance}}

<!-- Statistical rules adapt to changing baselines. Always include day-of-week adjustment for daily metrics. -->

---

### 5. Alerting Configuration

**Severity Levels:**

| Level | Response Time | Notification Channel | Escalation |
|-------|--------------|---------------------|------------|
| Critical | {{e.g. 15 min}} | {{e.g. SMS + Slack}} | {{escalation path}} |
| Warning | {{e.g. 4 hours}} | {{e.g. Slack}} | {{escalation path}} |
| Info | {{e.g. next business day}} | {{e.g. email digest}} | None |

**Alert Message Template:**
```
[{{severity}}] {{rule_name}}: {{metric}} is {{current_value}} (expected {{expected_range}}).
Investigation: {{playbook_link}}
```

<!-- Define routing, deduplication, and suppression rules for known events. -->

---

### 6. Investigation Playbook

For each rule, provide 2-3 investigation steps:

**Rule: {{rule_id}} — {{rule_name}}**
1. Check {{first thing to verify — e.g. data source freshness}}
2. Compare {{second check — e.g. same metric from alternative source}}
3. Review {{third check — e.g. recent deployments or known events calendar}}
4. **If confirmed:** {{action to take}}
5. **If false positive:** {{how to suppress and log}}

<!-- Every alert must tell the responder what to check first. An alert without a playbook is noise. -->

---

### 7. Tuning Schedule

**Week 1-2:** Deploy rules with alerting in observation mode (log only, no notifications).
- Review all triggered alerts daily
- Classify each as true positive, false positive, or inconclusive
- Adjust thresholds for rules with >20% false positive rate

**Week 3-4:** Enable notifications for rules with <10% false positive rate.
- Continue observation for remaining rules
- Add entries to known-events calendar as patterns emerge

**Ongoing (Monthly):**
- Review false positive log
- Adjust thresholds and lookback windows
- Update known-events calendar for upcoming seasonal events
- Assess whether new metrics need monitoring

<!-- Log every alert, suppression, and classification. This data drives threshold tuning. -->
