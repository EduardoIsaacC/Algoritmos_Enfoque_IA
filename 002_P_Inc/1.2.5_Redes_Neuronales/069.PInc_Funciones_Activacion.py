import numpy as np
import matplotlib.pyplot as plt

# Definiciones de funciones
def escalon(x):
    return np.where(x >= 0, 1, 0)

def lineal(x):
    return x

def sigmoide(x):
    return 1 / (1 + np.exp(-x))

def tanh(x):
    return np.tanh(x)

def relu(x):
    return np.maximum(0, x)

def leaky_relu(x, alpha=0.01):
    return np.where(x > 0, x, alpha * x)

# Rango de entrada
x = np.linspace(-5, 5, 200)

# Cálculos
activaciones = {
    "Escalón": escalon(x),
    "Lineal": lineal(x),
    "Sigmoide": sigmoide(x),
    "Tanh": tanh(x),
    "ReLU": relu(x),
    "Leaky ReLU": leaky_relu(x)
}

# Visualización
plt.figure(figsize=(10,6))
for nombre, y in activaciones.items():
    plt.plot(x, y, label=nombre)

plt.title("Funciones de Activación Neuronal")
plt.xlabel("Entrada (x)")
plt.ylabel("Salida f(x)")
plt.grid(True)
plt.legend()
plt.show()