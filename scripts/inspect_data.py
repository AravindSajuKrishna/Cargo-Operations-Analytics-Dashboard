import pandas as pd

df = pd.read_csv("data/raw/SCMS_Delivery_History_Dataset.csv")

print("\nDataset Shape:")
print(df.shape)

print("\nColumns:")
for col in df.columns:
    print(col)

print("\nFirst 5 Rows:")
print(df.head())
