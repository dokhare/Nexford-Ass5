# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# Load the dataset
data = load_breast_cancer()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = data.target  # Labels: 0 = malignant, 1 = benign

# Standardize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Apply PCA to reduce to 2 components
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# Create a DataFrame with the two principal components
df_pca = pd.DataFrame(X_pca, columns=['PC1', 'PC2'])
df_pca['target'] = y

# Plot the reduced dataset
plt.figure(figsize=(8, 6))
colors = ['red', 'blue']
labels = ['Malignant', 'Benign']

for label, color in zip([0, 1], colors):
    subset = df_pca[df_pca['target'] == label]
    plt.scatter(subset['PC1'], subset['PC2'], c=color, label=labels[label], alpha=0.6)

plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.title('PCA: Breast Cancer Dataset (2 Components)')
plt.legend()
plt.grid(True)
plt.show()
