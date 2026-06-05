import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv("data/raw/SCMS_Delivery_History_Dataset.csv")

# -----------------------------
# Convert Date Columns
# -----------------------------

date_columns = [
    "PQ First Sent to Client Date",
    "PO Sent to Vendor Date",
    "Scheduled Delivery Date",
    "Delivered to Client Date",
    "Delivery Recorded Date"
]

for col in date_columns:
    df[col] = pd.to_datetime(
        df[col],
        errors="coerce",
        dayfirst=True
    )
# -----------------------------
# Handle Missing Shipment Mode
# -----------------------------

df["Shipment Mode"] = df["Shipment Mode"].fillna("Unknown")

# -----------------------------
# Insurance Null Values
# -----------------------------

df["Line Item Insurance (USD)"] = (
    df["Line Item Insurance (USD)"]
    .fillna(0)
)

# -----------------------------
# Convert Freight Cost
# -----------------------------

df["Freight Cost (USD)"] = pd.to_numeric(
    df["Freight Cost (USD)"],
    errors="coerce"
)

# -----------------------------
# Convert Weight
# -----------------------------

df["Weight (Kilograms)"] = pd.to_numeric(
    df["Weight (Kilograms)"],
    errors="coerce"
)

# -----------------------------
# Feature Engineering
# -----------------------------

df["Delivery Days"] = (
    df["Delivered to Client Date"]
    - df["PO Sent to Vendor Date"]
).dt.days

df["Cost Per KG"] = np.where(
    df["Weight (Kilograms)"] > 0,
    df["Freight Cost (USD)"] / df["Weight (Kilograms)"],
    np.nan
)

df["Freight Percentage"] = (
    df["Freight Cost (USD)"]
    / df["Line Item Value"]
) * 100

df["Weight Category"] = pd.cut(
    df["Weight (Kilograms)"],
    bins=[0, 100, 1000, 10000, float("inf")],
    labels=[
        "Light",
        "Medium",
        "Heavy",
        "Very Heavy"
    ]
)
# -----------------------------
# Save Cleaned Dataset
# -----------------------------

df.to_csv(
    "data/processed/cleaned_shipments.csv",
    index=False
)

print("Data cleaned successfully!")
print(df.head())