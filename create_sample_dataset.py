import pandas as pd

data = pd.read_csv("data/raw/cicids2017_cleaned.csv")

sample = data.sample(n=5000, random_state=42)

sample.to_csv("data/raw/sample_dataset.csv", index=False)

print("Sample dataset created successfully!")