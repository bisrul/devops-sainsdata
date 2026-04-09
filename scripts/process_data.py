# scripts/process_data.py
import pandas as pd

df = pd.read_csv("data/raw/sales.csv")

print("Columns:", df.columns.tolist())
print(df.head())

import pandas as pd

df = pd.read_csv("data/raw/sales.csv", encoding="latin1")

# Clean column names
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# Convert date column (Superstore uses 'order_date')
df["order_date"] = pd.to_datetime(df["order_date"])

# Add useful columns
df["month"] = df["order_date"].dt.month_name()
df["year"] = df["order_date"].dt.year
df["revenue"] = df["sales"] * df["quantity"]

# Save cleaned data
df.to_csv("data/processed/sales_clean.csv", index=False)

print(f"✅ Processed {len(df)} rows of sales data")
print(f"✅ Columns: {df.columns.tolist()}")
print(df.head())