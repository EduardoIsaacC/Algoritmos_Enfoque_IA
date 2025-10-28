import numpy as np
import matplotlib.pyplot as plt

# Imports de Keras dentro de TensorFlow
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam

print("TensorFlow:", tf.__version__)
print("Keras:", tf.keras.__version__)

# 1) Generar datos simulados
np.random.seed(42)
X = np.random.rand(500, 2)  # 500 puntos en 2D (x1, x2)

# Regla para la etiqueta:
# si x1 + x2 > 1 => clase 1
# si x1 + x2 <= 1 => clase 0
y = np.array([1 if x1 + x2 > 1 else 0 for x1, x2 in X])

# 2) Construir la red neuronal
modelo = Sequential([
    Dense(8, input_dim=2, activation='relu'),   # capa oculta con 8 neuronas
    Dense(1, activation='sigmoid')              # salida binaria (0/1)
])

# 3) Compilar (definimos cómo aprende)
modelo.compile(
    optimizer=Adam(learning_rate=0.05),
    loss='binary_crossentropy',
    metrics=['accuracy']
)

# 4) Entrenar
hist = modelo.fit(
    X, y,
    epochs=100,
    verbose=0  # 0 = no spam en consola; pon 1 si quieres ver el progreso
)

# 5) Evaluar desempeño
loss, acc = modelo.evaluate(X, y, verbose=0)
print(f"Precisión del modelo: {acc*100:.2f}%")

# 6) Visualizar frontera de decisión aprendida
x_min, x_max = X[:,0].min() - 0.1, X[:,0].max() + 0.1
y_min, y_max = X[:,1].min() - 0.1, X[:,1].max() + 0.1
xx, yy = np.meshgrid(
    np.linspace(x_min, x_max, 200),
    np.linspace(y_min, y_max, 200)
)

# Para cada punto de la malla, la red predice probabilidad de clase 1
Z = modelo.predict(np.c_[xx.ravel(), yy.ravel()], verbose=0)
Z = Z.reshape(xx.shape)

plt.figure(figsize=(6,5))
plt.contourf(xx, yy, Z, cmap='coolwarm', alpha=0.4)
plt.scatter(X[:,0], X[:,1], c=y, cmap='coolwarm', edgecolors='k')
plt.title("Red Neuronal — Frontera de Decisión")
plt.xlabel("X1")
plt.ylabel("X2")
plt.show()