import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
data = pd.read_csv("data/raw/cicids2017_cleaned.csv")

# Remove duplicates
data = data.drop_duplicates()

# Attack Type Distribution
plt.figure(figsize=(10,5))
sns.countplot(x="Attack Type", data=data)
plt.xticks(rotation=90)
plt.title("Attack Type Distribution")
plt.tight_layout()
plt.show()