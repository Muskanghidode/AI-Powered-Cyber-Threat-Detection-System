import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Load Dataset
data = pd.read_csv("data/raw/cicids2017_cleaned.csv")

# Remove Duplicates
data = data.drop_duplicates()

# Features and Target
X = data.drop("Attack Type", axis=1)
y = data["Attack Type"]

# Encode Labels
encoder = LabelEncoder()
y = encoder.fit_transform(y)

# Train Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

# Train Model
model = DecisionTreeClassifier()

model.fit(X_train, y_train)

# Prediction
prediction = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, prediction)

print("Accuracy :", accuracy)