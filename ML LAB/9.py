import numpy as np
from sklearn.cluster import KMeans

# Data points
X = np.array([
    [1, 2],
    [2, 3],
    [3, 4],
    [8, 7],
    [9, 8],
    [10, 9]
])

# Create model (k = 2)
kmeans = KMeans(n_clusters=2)

# Train model
kmeans.fit(X)

# Get cluster labels
labels = kmeans.labels_

# Get centroids
centroids = kmeans.cluster_centers_

# Output
print("Clusters:", labels)
print("Centroids:\n", centroids)