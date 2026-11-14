import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
# pip install kneed
from kneed import KneeLocator

np.random.seed(42)
df_raw = pd.DataFrame({
    'annual_income': np.random.normal(60000, 15000, 150),
    'spending_score': np.random.normal(50, 20, 150)
})
scaler = StandardScaler()
scaled_matrix = scaler.fit_transform(df_raw)
df_scaled = pd.DataFrame(scaled_matrix, columns=df_raw.columns)

inertia = []

k_range = range(1, 9)
for k in k_range:
    kmeans = KMeans(n_clusters=k, n_init='auto', random_state=42)
    kmeans.fit(df_scaled)
    inertia.append(kmeans.inertia_)

df_elbow = pd.DataFrame({'k': list(k_range), 'inertia': inertia})
print("Elbow Inertia Summary:\n", df_elbow)

kl = KneeLocator(
    x = df_elbow['k'],
    y = df_elbow['inertia'],
    curve='convex',
    direction='decreasing'
)

optimal_k = kl.elbow
print(f"Optimal Cluster Count (k) identified by kneed: {optimal_k}")


