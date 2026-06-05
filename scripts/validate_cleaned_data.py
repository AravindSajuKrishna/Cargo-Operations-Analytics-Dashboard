import pandas as pd

df = pd.read_csv("data/processed/cleaned_shipments.csv")

print("\nDelivered Date Missing:")
print(df["Delivered to Client Date"].isnull().sum())

print("\nPO Sent Date Missing:")
print(df["PO Sent to Vendor Date"].isnull().sum())

print("\nDelivery Days Missing:")
print(df["Delivery Days"].isnull().sum())

print("\nWeight Zero Count:")
print((df["Weight (Kilograms)"] == 0).sum())

print("\nFreight Cost Missing:")
print(df["Freight Cost (USD)"].isnull().sum())