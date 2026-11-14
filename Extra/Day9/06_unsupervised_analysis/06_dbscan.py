import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import AgglomerativeClustering, DBSCAN
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.datasets import make_moons

X_moons, _ = make_moons(n_samples=200, noise=0.05, random_state=42)

dbscan = DBSCAN(eps=0.2, min_samples=5)
clusters = dbscan.fit_predict(X_moons)

df_db = pd.DataFrame({'x1': X_moons[:, 0], 'x2': X_moons[:, 1], 'cluster': clusters})
print("DBSCAN Cluster Assignment Counts:\n", df_db['cluster'].value_counts())

# Visualization
plt.figure(figsize=(6, 3))
sns.scatterplot(x='x1', y='x2', hue='cluster', data=df_db, palette='Set1', s=50, legend='full')
plt.title('DBSCAN Density-Based Clustering (Arbitrary Shapes)')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.show()