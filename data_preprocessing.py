import pandas as pd

# Load Dataset
data = pd.read_csv("data/raw/cicids2017_cleaned.csv")

print("========== DATA PREPROCESSING ==========")

# Dataset Shape
print("\nDataset Shape:")
print(data.shape)

# Missing Values
print("\nMissing Values:")
print(data.isnull().sum())

# Duplicate Values
print("\nDuplicate Rows:")
print(data.duplicated().sum())

# Class Distribution
print("\nAttack Type Distribution:")
print(data["Attack Type"].value_counts())