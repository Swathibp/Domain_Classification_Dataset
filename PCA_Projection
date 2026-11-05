from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import numpy as np

pca = PCA(n_components=2)
reduced = pca.fit_transform(embeddings)

plt.figure()
for domain in set(labels):
    indices = [i for i, d in enumerate(labels) if d == domain]
    plt.scatter(reduced[indices, 0], reduced[indices, 1], label=domain)

#plt.title("PCA Projection of Query Embeddings by Domain")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.legend(fontsize=6)
plt.tight_layout()
plt.show()
