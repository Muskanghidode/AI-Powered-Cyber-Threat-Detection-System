import pandas as pd

# Load Dataset
data = pd.read_csv("data/raw/cicids2017_cleaned.csv")

# Success Message
print("========== DATASET LOADED SUCCESSFULLY ==========")

# Display First 5 Rows
print("\nFirst 5 Rows:")
print(data.head())

# Display Dataset Shape
print("\nDataset Shape:")
print(data.shape)

# Display Column Names
print("\nColumn Names:")
print(data.columns)

# Display Dataset Information
print("\nDataset Information:")
print(data.info())