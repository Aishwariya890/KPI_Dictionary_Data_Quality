import pandas as pd

# KPI Dictionary
kpis = [
    {
        "KPI Name": "Total Revenue",
        "Business Definition": "Total revenue after discount",
        "Formula": "SUM(quantity × unit_price × (1 - discount_pct/100))",
        "Grain": "Order",
        "Filter": "Valid orders with valid discount",
        "Decision Owner": "Sales Manager",
        "Refresh Cadence": "Daily"
    },
    {
        "KPI Name": "Gross Sales",
        "Business Definition": "Total sales value before discount",
        "Formula": "SUM(quantity × unit_price)",
        "Grain": "Order",
        "Filter": "Valid quantity and unit price",
        "Decision Owner": "Sales Manager",
        "Refresh Cadence": "Daily"
    },
    {
        "KPI Name": "Total Orders",
        "Business Definition": "Number of unique orders",
        "Formula": "COUNT(DISTINCT order_id)",
        "Grain": "Order",
        "Filter": "Valid unique order IDs",
        "Decision Owner": "Operations Manager",
        "Refresh Cadence": "Daily"
    },
    {
        "KPI Name": "Total Quantity",
        "Business Definition": "Total number of items ordered",
        "Formula": "SUM(quantity)",
        "Grain": "Order",
        "Filter": "Valid quantity",
        "Decision Owner": "Operations Manager",
        "Refresh Cadence": "Daily"
    },
    {
        "KPI Name": "Average Order Value",
        "Business Definition": "Average revenue generated per order",
        "Formula": "Total Revenue / Total Orders",
        "Grain": "Order",
        "Filter": "Valid orders",
        "Decision Owner": "Sales Manager",
        "Refresh Cadence": "Daily"
    },
    {
        "KPI Name": "Average Unit Price",
        "Business Definition": "Average selling price per item",
        "Formula": "Gross Sales / Total Quantity",
        "Grain": "Order",
        "Filter": "Valid numeric values",
        "Decision Owner": "Finance Manager",
        "Refresh Cadence": "Daily"
    },
    {
        "KPI Name": "Discount Rate",
        "Business Definition": "Percentage of gross sales given as discount",
        "Formula": "Total Discount / Gross Sales × 100",
        "Grain": "Order",
        "Filter": "Valid discount values",
        "Decision Owner": "Sales Manager",
        "Refresh Cadence": "Daily"
    },
    {
        "KPI Name": "Paid Order Rate",
        "Business Definition": "Percentage of orders marked as paid",
        "Formula": "Paid Orders / Total Orders × 100",
        "Grain": "Order",
        "Filter": "Valid payment status",
        "Decision Owner": "Finance Manager",
        "Refresh Cadence": "Daily"
    },
    {
        "KPI Name": "Pending Order Rate",
        "Business Definition": "Percentage of orders with pending payment",
        "Formula": "Pending Orders / Total Orders × 100",
        "Grain": "Order",
        "Filter": "Valid payment status",
        "Decision Owner": "Finance Manager",
        "Refresh Cadence": "Daily"
    },
    {
        "KPI Name": "Revenue per Quantity",
        "Business Definition": "Average net revenue per item",
        "Formula": "Total Revenue / Total Quantity",
        "Grain": "Order",
        "Filter": "Valid orders",
        "Decision Owner": "Finance Manager",
        "Refresh Cadence": "Daily"
    }
]

# Convert to DataFrame
kpi_df = pd.DataFrame(kpis)

# Save Excel file
kpi_df.to_excel("KPI_Dictionary.xlsx", index=False)

print("=" * 60)
print("KPI DICTIONARY CREATED SUCCESSFULLY")
print("=" * 60)

print("Total KPIs:", len(kpi_df))
print("File: KPI_Dictionary.xlsx")

print("\nKPI Dictionary:")
print(kpi_df.to_string(index=False))