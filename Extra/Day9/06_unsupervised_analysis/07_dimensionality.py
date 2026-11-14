import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE

# Visual styling settings
sns.set_theme(style="whitegrid", palette="muted")
plt.rcParams["figure.dpi"] = 120
plt.rcParams["figure.figsize"] = (8, 4)
plt.rcParams["axes.titlesize"] = 12
plt.rcParams["axes.labelsize"] = 10

print("Global libraries for PCA and t-SNE dimensionality reduction loaded successfully.")

np.random.seed(42)
df_high_dim = pd.DataFrame(np.random.randn(100, 5), columns=['f1', 'f2', 'f3', 'f4', 'f5'])
# print(df_high_dim.head())
print("=" * 60)
scaler = StandardScaler()
scaled_data = scaler.fit_transform(df_high_dim)
# print(scaled_data[:5])
print("=" * 60)
pca = PCA(n_components=2)
pca_transformed = pca.fit_transform(scaled_data)
print("Explained Variance Ratio per Principal Component:", pca.explained_variance_ratio_.round(2))
print(pca_transformed)
print("=" * 60)

loadings = pd.DataFrame(pca.components_.T, columns=['PC1', 'PC2'], index=df_high_dim.columns)
print("Principal Component Loadings Matrix:\n", loadings.round(2))

# plt.figure(figsize=(6, 3))
# sns.heatmap(loadings, annot=True, cmap='Purples', fmt='.2f')
# plt.title('Feature Loadings Heatmap across Principal Components')
# plt.ylabel('Original Features')
# plt.show()

# TSNE - T-stochastic neighbour embedding (non linear projector)
tsne = TSNE(n_components=2, perplexity=30, random_state=42, max_iter=300)
tsne_transformed = tsne.fit_transform(scaled_data)

df_tsne = pd.DataFrame({'tsne1': tsne_transformed[:, 0], 'tsne2': tsne_transformed[:, 1]})
print("t-SNE Transformed Matrix Shape:", df_tsne.shape)

# # Visualization
# plt.figure(figsize=(6, 3))
# sns.scatterplot(x='tsne1', y='tsne2', data=df_tsne, color='teal', alpha=0.8)
# plt.title('t-SNE Non-Linear 2D Projection')
# plt.xlabel('t-SNE Dimension 1')
# plt.ylabel('t-SNE Dimension 2')
# plt.show()

df_comp = pd.DataFrame({'pca1': pca_transformed[:, 0], 'pca2': pca_transformed[:, 1]})
df_comp['group'] = np.random.choice(['Segment A', 'Segment B'], 100)
print(
    "Compressed Feature Head:\n",
    df_comp.head(3),
)

# Visualization
plt.figure(figsize=(6, 3))
sns.scatterplot(x='pca1', y='pca2', hue='group', data=df_comp, palette='Set1', s=60)
plt.title('Compressed 2D PCA Feature Space by Segment')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.show()