import pandas as pd

df = pd.read_csv("data/processed/cleaned_shipments.csv")

print("\n========== EXECUTIVE KPIs ==========")

print("Total Shipments:", len(df))

print(
    "Total Shipment Value (USD):",
    round(df["Line Item Value"].sum(), 2)
)

print(
    "Total Freight Cost (USD):",
    round(df["Freight Cost (USD)"].sum(), 2)
)

print(
    "Total Weight (KG):",
    round(df["Weight (Kilograms)"].sum(), 2)
)

print(
    "Countries Served:",
    df["Country"].nunique()
)

print(
    "Vendors:",
    df["Vendor"].nunique()
)

print(
    "Average Delivery Days:",
    round(df["Delivery Days"].mean(), 2)
)

print(
    "Average Cost Per KG:",
    round(df["Cost Per KG"].mean(), 2)
)