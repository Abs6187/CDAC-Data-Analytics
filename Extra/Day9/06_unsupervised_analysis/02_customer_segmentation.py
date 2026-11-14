import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

np.random.seed(42)
df_raw = pd.DataFrame({
    'annual_income': np.random.normal(60000, 15000, 150),
    'spending_score': np.random.normal(50, 20, 150)
})

print('=' * 60)
print(df_raw.head())
print('=' * 60)
scaler = StandardScaler()
scaled_matrix = scaler.fit_transform(df_raw)
df_scaled = pd.DataFrame(scaled_matrix, columns=df_raw.columns)
print(df_scaled.describe().round(2))
print('=' * 60)
print(df_scaled.head())

print('=' * 60)

# Elbow Method and Silhouette Analysis for Optimal K
# Elbow Method : Inertia (WCSS) => within-cluster sum of squares 
# Silhouette : Cluster cohesion and separation validation metric ($[-1, 1]$)

inertia = []

k_range = range(1, 7)
for k in k_range:
    kmeans = KMeans(n_clusters=k, n_init='auto', random_state=42)
    kmeans.fit(df_scaled)
    inertia.append(kmeans.inertia_)

df_elbow = pd.DataFrame({'k': list(k_range), 'inertia': inertia})
print("Elbow Inertia Summary:\n", df_elbow)

import matplotlib.pyplot as plt
import seaborn as sns

# Visual styling settings
# sns.set_theme(style="whitegrid", palette="muted")
# plt.rcParams["figure.dpi"] = 120
# plt.rcParams["figure.figsize"] = (8, 4)
# plt.rcParams["axes.titlesize"] = 12
# plt.rcParams["axes.labelsize"] = 10

# print("Global libraries for K-Means customer segmentation loaded successfully.")

# plt.figure(figsize=(6,3))
# sns.lineplot(x='k',y='inertia', data=df_elbow, marker='o', color = 'purple', linewidth=2)
# plt.title("Elbow (K) selectin")
# plt.xlabel("# Clusters")
# plt.ylabel("wcss")
# plt.show()


kmeans_opt = KMeans(n_clusters=3, n_init='auto', random_state=42)
df_raw['cluster'] = kmeans_opt.fit_predict(df_scaled)
cluster_profile = df_raw.groupby('cluster').mean().reset_index()
print("Cluster Profiling Centroids:\n", cluster_profile.round(2))

# Visualization
plt.figure(figsize=(6, 3))
sns.scatterplot(x='annual_income', y='spending_score', hue='cluster', data=df_raw, palette='Set1', s=80)
plt.title('K-Means Cluster Segmentation Profiles')
plt.xlabel('Annual Income ($)')
plt.ylabel('Spending Score')
plt.show()