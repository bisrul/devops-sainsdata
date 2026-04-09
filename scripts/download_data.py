import pandas as pd
import os
import zipfile
import kaggle

# ✅ Automatically download from Kaggle
print("⬇️ Downloading dataset from Kaggle...")

kaggle.api.authenticate()

kaggle.api.dataset_download_files(
    "vivek468/superstore-dataset-final",  # dataset name
    path="data/raw/",                      # where to save
    unzip=True                             # auto unzip
)

print("✅ Download complete!")

# ✅ Load the dataset
df = pd.read_csv("data/raw/Sample - Superstore.csv", encoding="latin1")

# ✅ Save to standard name
df.to_csv("data/raw/sales.csv", index=False)

print(f"✅ Loaded {len(df)} rows of sales data")
print(df.head())  # preview first 5 rows