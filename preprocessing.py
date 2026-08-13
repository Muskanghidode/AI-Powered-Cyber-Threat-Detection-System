import pandas as pd

# Load Dataset
data = pd.read_csv("data/raw/cicids2017_cleaned.csv")

print("Dataset Loaded Successfully")

# Check Missing Values
print("\nMissing Values:")
print(data.isnull().sum())

# Check Duplicate Rows
print("\nDuplicate Rows:")
print(data.duplicated().sum())

# Remove Duplicate Rows
data = data.drop_duplicates()

print("\nDataset Shape After Removing Duplicates:")
print(data.shape)