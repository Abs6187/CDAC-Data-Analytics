import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import IsolationForest
from sklearn.neighbors import LocalOutlierFactor


# Visual styling settings
sns.set_theme(style="whitegrid", palette="muted")
plt.rcParams["figure.dpi"] = 120
plt.rcParams["figure.figsize"] = (8, 4)
plt.rcParams["axes.titlesize"] = 12
plt.rcParams["axes.labelsize"] = 10

print("Global libraries for unsupervised anomaly detection loaded successfully.")
np.random.seed(42)
X_normal = np.random.normal(0, 1, (180, 2))
X_outliers = np.random.uniform(low=-5, high=5, size=(20, 2))
X_data = np.vstack([X_normal, X_outliers])

# contamination : 0.1 is 10% anamoly expected
iso = IsolationForest(contamination=0.1, random_state=42)
preds = iso.fit_predict(X_data) # 1 for inliers, -1 for outliers

df_iso = pd.DataFrame({'x1': X_data[:, 0], 'x2': X_data[:, 1], 'anomaly': preds})
print("Isolation Forest Prediction Counts:\n", df_iso['anomaly'].value_counts())

# Visualization
# plt.figure(figsize=(6, 3))
# sns.scatterplot(x='x1', y='x2', hue='anomaly', data=df_iso, palette={1: 'teal', -1: 'red'}, s=60)
# plt.title('Isolation Forest Outlier Detection (Red = Anomalies)')
# plt.xlabel('Feature 1')
# plt.ylabel('Feature 2')
# plt.show()

'''
Isolation Forest is an tree-based ensemble algorithm that isolates anomalies by randomly
 selecting features and split values; because anomalies are few and distinct, they 
 require fewer random splits to isolate than normal data points.
'''
'''
Local Outlier Factor (LOF) is a density-based algorithm that measures the local density 
deviation of a given data point with respect to its surrounding k-nearest neighbors, 
identifying points that reside in significantly lower density regions than their neighbors.
'''
# LOF (Local Outlier Factor )
print("=" * 60)
lof = LocalOutlierFactor(n_neighbors=20, contamination=0.1)
lof_preds = lof.fit_predict(X_data)

df_lof = pd.DataFrame({'x1': X_data[:, 0], 'x2': X_data[:, 1], 'anomaly': lof_preds})
print("Local Outlier Factor Prediction Counts:\n", df_lof['anomaly'].value_counts())
print("=" * 60)

df_tx = pd.DataFrame({
    'tx_amount': [45, 120, 3500, 50, 4800, 80],
    'tx_velocity': [1, 2, 12, 1, 15, 2]
})
iso_tx = IsolationForest(contamination=0.3, random_state=42)
df_tx['fraud_flag'] = iso_tx.fit_predict(df_tx[['tx_amount', 'tx_velocity']])
print(
    "Transaction Fraud Workflow Results:\n",
    df_tx,
)

# Visualization
plt.figure(figsize=(6, 3))
sns.scatterplot(x='tx_amount', y='tx_velocity', hue='fraud_flag', data=df_tx, palette={1: 'teal', -1: 'red'}, s=100)
plt.title('Transaction Fraud Detection Workflow (Red = Flagged)')
plt.xlabel('Transaction Amount ($)')
plt.ylabel('Transaction Velocity')
plt.show()