import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Sample data (Features: [Hours studied])
X = np.array([[1], [2], [3], [4], [5]])

# Output (0 = Fail, 1 = Pass)
y = np.array([0, 0, 0, 1, 1])

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=0
)

# Create model
model = LogisticRegression()

# Train model
model.fit(X_train, y_train)

# Predict
prediction = model.predict(X_test)

# Accuracy
acc = accuracy_score(y_test, prediction)

print("Prediction:", prediction)
print("Accuracy:", acc)