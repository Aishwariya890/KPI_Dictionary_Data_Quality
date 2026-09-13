# KPI Dictionary & Data Quality Contract

## 📌 Project Overview

This project translates an ambiguous business request into measurable KPIs and a testable data-quality agreement.

The project uses a retail orders dataset to define business KPIs, identify data-quality problems, and establish clear rules for trustworthy reporting.

---

## 🎯 Objectives

- Define measurable business KPIs
- Create a KPI Dictionary
- Profile the quality of retail order data
- Check completeness, uniqueness, validity, consistency, and freshness
- Define data-quality thresholds
- Create escalation actions for quality failures
- Identify whether the dataset is trusted for KPI reporting

---

## 📊 Dataset

The project uses a retail orders dataset containing information about:

- Order ID
- Order Date
- Customer Segment
- City
- Category
- Quantity
- Unit Price
- Discount Percentage
- Payment Status

Total records in the raw dataset: **12**

---

## 📈 KPI Dictionary

The project defines 10 KPIs:

1. Total Revenue
2. Gross Sales
3. Total Orders
4. Total Quantity
5. Average Order Value
6. Average Unit Price
7. Discount Rate
8. Paid Order Rate
9. Pending Order Rate
10. Revenue per Quantity

Each KPI includes:

- KPI Name
- Formula
- Grain
- Filters
- Owner
- Refresh Cadence

---

## 🔍 Data Quality Checks

The executable notebook checks:

### 1. Completeness
Checks missing values in required fields.

### 2. Uniqueness
Checks whether Order IDs are unique.

### 3. Validity
Checks:

- Order date format
- Quantity
- Unit price
- Discount percentage

### 4. Consistency
Checks approved values for:

- Customer Segment
- Payment Status

### 5. Freshness
Checks whether the dataset has been refreshed within the required time limit.

---

## 🚨 Data Quality Contract

The contract defines three quality statuses:

### PASS
The dataset is trusted for KPI reporting.

### WARNING
The dataset can be used with documented limitations.

### FAIL
The dataset must not be used for trusted KPI reporting until critical issues are corrected.

---

## ⚠️ Current Dataset Status

The raw dataset contains data-quality issues such as:

- Duplicate Order IDs
- Invalid or missing dates
- Invalid quantities
- Missing values

Therefore, the executable quality checks identify the dataset as:

**FAIL**

The raw data is not modified or silently cleaned before profiling.

---

## 👥 Data Ownership

- Data Owner: Operations Manager
- KPI Owner: Sales Manager
- Financial KPI Owner: Finance Manager
- Data Quality Monitoring: Data Analyst
- Refresh Cadence: Daily

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- OpenPyXL
- Jupyter Notebook
- Microsoft Excel
- Markdown

---

## 📁 Project Structure

```text
KPI_Dictionary_Data_Quality
│
├── Data
│   ├── retail-orders-raw.csv
│   └── retail-data-dictionary.csv
│
├── Notebook
│   └── data_quality_profile.ipynb
│
├── Output
│   └── data_quality_summary.csv
│
├── create_kpi_dictionary.py
├── KPI_Dictionary.xlsx
├── Data_Quality_Contract.md
├── README.md
└── requirements.txt