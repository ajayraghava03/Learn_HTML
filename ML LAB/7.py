import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Sample data (Features: [Height, Weight])
X = np.array([
    [150, 50],
    [160, 60],
    [170, 65],
    [180, 80],
    [155, 55]
])

# Output (0 = Female, 1 = Male)
y = np.array([0, 0, 1, 1, 0])

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Create model (k = 3)
model = KNeighborsClassifier(n_neighbors=3)

# Train model
model.fit(X_train, y_train)

# Predict
prediction = model.predict(X_test)

# Accuracy
acc = accuracy_score(y_test, prediction)

print("Prediction:", prediction)
print("Accuracy:", acc)