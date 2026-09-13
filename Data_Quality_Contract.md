# Data Quality Contract

## 1. Purpose

This Data Quality Contract defines the minimum quality standards required for the retail orders dataset to be trusted for KPI reporting and business decisions.

## 2. Data Owner

- Data Owner: Operations Manager
- KPI Owner: Sales Manager
- Financial KPI Owner: Finance Manager
- Data Quality Monitoring: Data Analyst
- Refresh Cadence: Daily

## 3. Data Quality Rules

| Quality Dimension | Rule | Threshold | Severity |
|---|---|---:|---|
| Completeness | Required fields must not be missing | >= 98% | High |
| Uniqueness | Order IDs must be unique | 0 duplicates | Critical |
| Validity | Order dates must use valid ISO format | 0 invalid | Critical |
| Validity | Quantity must be greater than 0 | 0 invalid | Critical |
| Validity | Unit price must be greater than 0 | 0 invalid | Critical |
| Validity | Discount must be between 0 and 100 | 0 invalid | High |
| Consistency | Customer segment must use approved values | <= 1% violations | High |
| Consistency | Payment status must use approved values | <= 1% violations | High |
| Freshness | Data must be refreshed within 24 hours | <= 24 hours | High |

## 4. Approved Values

### Customer Segment

Allowed values:

- Student
- Fresher
- Professional

### Payment Status

Allowed values:

- Paid
- Pending

## 5. Pass / Warning / Fail Rules

### PASS

The dataset can be used for KPI reporting when all Critical rules pass and no high-severity rule exceeds its threshold.

### WARNING

A non-critical quality issue exceeds its threshold.

The Data Analyst must notify the responsible owner and create a remediation task.

### FAIL

Any Critical quality rule fails.

The dataset must be marked as NOT TRUSTED for KPI reporting until the issue is corrected and the quality checks are successfully rerun.

## 6. Escalation Actions

### Critical Failure

1. Stop publishing KPI results.
2. Mark the dataset as NOT TRUSTED.
3. Notify the Operations Manager.
4. Create a data remediation ticket.
5. Correct or reload the affected data.
6. Rerun all data quality checks.
7. Publish KPI results only after the critical issue passes.

### High-Severity Failure

1. Notify the responsible KPI/data owner.
2. Record the issue.
3. Investigate the source of the problem.
4. Correct the data where required.
5. Rerun the relevant quality check.

## 7. Data Quality Status

The dataset will receive one of the following statuses:

- PASS — Data is trusted for reporting.
- WARNING — Data can be used with documented limitations.
- FAIL — Data must not be used for trusted KPI reporting.

## 8. Contract Review

The Data Quality Contract should be reviewed whenever:

- A new column is added.
- A KPI definition changes.
- Business rules change.
- Data source changes.
- Reporting requirements change.