import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split


# Sample data
X = np.array([
    [25, 30000],
    [35, 60000],
    [45, 80000],
    [20, 20000],
    [50, 90000]
])

y = np.array([0, 1, 1, 0, 1])

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Model with parameter tuning
model = DecisionTreeClassifier(max_depth=3, criterion='gini')

# Train model
model.fit(X_train, y_train)

# Predict
prediction = model.predict(X_test)

# Accuracy

print("Prediction:", prediction)

plt.figure(figsize=(8, 6))
plot_tree(model, filled=True)
plt.show()