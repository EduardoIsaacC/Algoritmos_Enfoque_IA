import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cluster import KMeans

# Generar datos simulados
np.random.seed(42)
grupo1 = np.random.normal([2, 2], 0.5, (50, 2))
grupo2 = np.random.normal([6, 6], 0.6, (50, 2))
X = np.vstack((grupo1, grupo2))
y = np.array([0]*50 + [1]*50)  # etiquetas verdaderas

# Clasificación con k-NN 
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X, y)

nuevo_punto = np.array([[4, 3]])  # punto a clasificar
prediccion = knn.predict(nuevo_punto)[0]

# Agrupamiento con k-Means 
kmeans = KMeans(n_clusters=2, random_state=42)
etiquetas_km = kmeans.fit_predict(X)
centroides = kmeans.cluster_centers_

# Visualización
plt.figure(figsize=(9,4))

# Subgráfico 1: k-NN
plt.subplot(1,2,1)
plt.scatter(X[:,0], X[:,1], c=y, cmap='coolwarm', alpha=0.6)
plt.scatter(nuevo_punto[:,0], nuevo_punto[:,1], c='black', marker='*', s=150, label='Nuevo punto')
plt.title(f"k-NN (predicción = Clase {prediccion})")
plt.legend()
plt.grid()

# Subgráfico 2: k-Means
plt.subplot(1,2,2)
plt.scatter(X[:,0], X[:,1], c=etiquetas_km, cmap='viridis', alpha=0.6)
plt.scatter(centroides[:,0], centroides[:,1], c='red', marker='x', s=100, label='Centroides')
plt.title("k-Means — Agrupamiento no supervisado")
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()