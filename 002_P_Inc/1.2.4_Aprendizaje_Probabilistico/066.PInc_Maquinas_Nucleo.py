import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.datasets import make_circles

# Generar datos no lineales
X, y = make_circles(n_samples=200, factor=0.4, noise=0.1, random_state=42)

# Entrenamiento SVM lineal
svm_lineal = svm.SVC(kernel='linear', C=1)
svm_lineal.fit(X, y)

# Entrenamiento SVM con núcleo RBF 
svm_rbf = svm.SVC(kernel='rbf', gamma=1, C=1)
svm_rbf.fit(X, y)

# Visualización
fig, axs = plt.subplots(1, 2, figsize=(9, 4))

# Crear malla para visualizar fronteras
xx, yy = np.meshgrid(np.linspace(-1.5, 1.5, 200),
                     np.linspace(-1.5, 1.5, 200))
Z_lin = svm_lineal.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)
Z_rbf = svm_rbf.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)

# Gráfico 1: Lineal
axs[0].contourf(xx, yy, Z_lin, cmap='coolwarm', alpha=0.3)
axs[0].scatter(X[:, 0], X[:, 1], c=y, cmap='coolwarm', edgecolors='k')
axs[0].set_title("SVM Lineal — Fallo en frontera")

# Gráfico 2: Núcleo RBF
axs[1].contourf(xx, yy, Z_rbf, cmap='coolwarm', alpha=0.3)
axs[1].scatter(X[:, 0], X[:, 1], c=y, cmap='coolwarm', edgecolors='k')
axs[1].set_title("SVM con Núcleo RBF — Frontera Curva")

plt.suptitle("Máquinas de Vectores de Soporte — Lineal vs. Núcleo", fontsize=12)
plt.tight_layout()
plt.show()