import pandas as pd

# Load data
df = pd.read_csv("data/raw/SCMS_Delivery_History_Dataset.csv")

print("\n========== BASIC INFO ==========")
print(df.info())

print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())

print("\n========== NUMERICAL SUMMARY ==========")
print(df.describe())

print("\n========== UNIQUE VALUES ==========")

categorical_cols = [
    "Country",
    "Shipment Mode",
    "Vendor",
    "Product Group",
    "Managed By",
    "Fulfill Via"
]

for col in categorical_cols:
    print(f"\n{col}:")
    print(df[col].nunique())