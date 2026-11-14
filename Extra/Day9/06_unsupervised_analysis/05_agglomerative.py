import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import AgglomerativeClustering, DBSCAN
from scipy.cluster.hierarchy import dendrogram, linkage

# Visual styling settings
sns.set_theme(style="whitegrid", palette="muted")
plt.rcParams["figure.dpi"] = 120
plt.rcParams["figure.figsize"] = (8, 4)
plt.rcParams["axes.titlesize"] = 12
plt.rcParams["axes.labelsize"] = 10

print("Global libraries for hierarchical and density-based clustering loaded successfully.")

np.random.seed(42)
X_hier = np.random.rand(30, 2)
Z = linkage(X_hier, method='ward')
print("Hierarchical Linkage Matrix Shape:", Z.shape)

# Visualization
plt.figure(figsize=(6, 3))
dendrogram(Z, truncate_mode='lastp', p=10)
plt.title('Agglomerative Hierarchical Dendrogram')
plt.xlabel('Sample Index or Cluster Size')
plt.ylabel('Distance Threshold')
plt.show()