import numpy as np
import matplotlib.pyplot as plt

# Generar datos simulados
np.random.seed(42)
grupo1 = np.random.normal([2, 2], 0.6, (100, 2))
grupo2 = np.random.normal([8, 3], 0.8, (100, 2))
grupo3 = np.random.normal([5, 8], 0.7, (100, 2))
X = np.vstack((grupo1, grupo2, grupo3))

# Parámetros 
k = 3  # número de grupos
n = len(X)

# Inicialización aleatoria de centroides 
centroides = X[np.random.choice(n, k, replace=False)]

# Algoritmo K-means
for _ in range(20):
    # Asignar cada punto al centroide más cercano
    distancias = np.linalg.norm(X[:, np.newaxis] - centroides, axis=2)
    etiquetas = np.argmin(distancias, axis=1)
    
    # Recalcular centroides
    nuevos_centroides = np.array([X[etiquetas == i].mean(axis=0) for i in range(k)])
    
    # Condición de convergencia
    if np.allclose(centroides, nuevos_centroides):
        break
    centroides = nuevos_centroides

# Visualización
colores = ['red', 'green', 'blue']
for i in range(k):
    plt.scatter(X[etiquetas == i, 0], X[etiquetas == i, 1], color=colores[i], alpha=0.6, label=f'Cluster {i+1}')

plt.scatter(centroides[:, 0], centroides[:, 1], color='black', marker='x', s=100, label='Centroides')
plt.title("Agrupamiento No Supervisado — K-Means")
plt.xlabel("X₁")
plt.ylabel("X₂")
plt.legend()
plt.grid()
plt.show()