# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# Load the cancer dataset
data = load_breast_cancer()
df = pd.DataFrame(data.data, columns=data.feature_names)

# Step 1: Standardize the data
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df)

# Step 2: Apply PCA
pca = PCA()
pca_components = pca.fit_transform(df_scaled)

# Step 3: Explained Variance
explained_variance = pca.explained_variance_ratio_

# Step 4: Plot the variance explained by each principal component
plt.figure(figsize=(10, 6))
plt.plot(np.cumsum(explained_variance), marker='o')
plt.xlabel('Number of Principal Components')
plt.ylabel('Cumulative Explained Variance')
plt.title('PCA - Cumulative Explained Variance')
plt.grid(True)
plt.axhline(y=0.90, color='r', linestyle='--', label='90% Explained Variance')
plt.legend()
plt.show()

# Step 5: Determine top contributing variables to the first few PCs
n_components = 3  # Example: focus on first 3 principal components
pca = PCA(n_components=n_components)
pca.fit(df_scaled)

# Get loading scores for the first principal component
loadings = pd.DataFrame(pca.components_.T,
                        columns=[f'PC{i+1}' for i in range(n_components)],
                        index=data.feature_names)

# Step 6: Show top contributing features to PC1 (and optionally PC2, PC3)
top_features_pc1 = loadings['PC1'].abs().sort_values(ascending=False).head(10)
print("🔍 Top contributing variables to PC1:")
print(top_features_pc1)
