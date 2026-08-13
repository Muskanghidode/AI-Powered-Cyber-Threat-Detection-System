import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

# Load Dataset
data = pd.read_csv("data/raw/cicids2017_cleaned.csv")

# Remove Duplicates
data = data.drop_duplicates()

print("Dataset Loaded Successfully")

# Features and Target
X = data.drop("Attack Type", axis=1)
y = data["Attack Type"]

# Encode Target
encoder = LabelEncoder()
y = encoder.fit_transform(y)

# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

# Random Forest Model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

print("\nTraining Random Forest Model...")

model.fit(X_train, y_train)

print("Training Completed")

# Prediction
prediction = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, prediction)

print("\nAccuracy :", accuracy)

# Classification Report
print("\nClassification Report\n")
print(classification_report(y_test, prediction))

# Confusion Matrix
print("\nConfusion Matrix\n")
print(confusion_matrix(y_test, prediction))
