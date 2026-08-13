import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# Load Dataset
data = pd.read_csv("data/raw/cicids2017_cleaned.csv")

# Remove Duplicate Rows
data = data.drop_duplicates()

print("Dataset Loaded Successfully")

# Separate Features and Target
X = data.drop("Attack Type", axis=1)
y = data["Attack Type"]

print("\nFeature Shape:")
print(X.shape)

print("\nTarget Shape:")
print(y.shape)

# Encode Target Labels
encoder = LabelEncoder()

y = encoder.fit_transform(y)

print("\nTarget Labels Encoded Successfully")

# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining Data Shape:")
print(X_train.shape)

print("\nTesting Data Shape:")
print(X_test.shape)