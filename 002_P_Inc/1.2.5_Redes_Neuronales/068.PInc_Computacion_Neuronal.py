import numpy as np
import matplotlib.pyplot as plt

# Entradas y pesos
x = np.array([0.8, 0.4])   # entradas
w = np.array([0.6, 0.9])   # pesos sinápticos
b = -0.3                   # sesgo

# Suma ponderada 
u = np.dot(w, x) + b

# Funciones de activación
def escalon(x):
    return 1 if x >= 0 else 0

def sigmoide(x):
    return 1 / (1 + np.exp(-x))

def tanh(x):
    return np.tanh(x)

def relu(x):
    return max(0, x)

# Cálculos
print(f"Suma ponderada (u): {u:.3f}")
print(f"Escalón: {escalon(u)}")
print(f"Sigmoide: {sigmoide(u):.3f}")
print(f"Tanh: {tanh(u):.3f}")
print(f"ReLU: {relu(u):.3f}")

# Visualización de funciones
x_vals = np.linspace(-5, 5, 100)
plt.figure(figsize=(8,5))

plt.plot(x_vals, [escalon(i) for i in x_vals], label="Escalón")
plt.plot(x_vals, [sigmoide(i) for i in x_vals], label="Sigmoide")
plt.plot(x_vals, [tanh(i) for i in x_vals], label="Tanh")
plt.plot(x_vals, [relu(i) for i in x_vals], label="ReLU")
plt.title("Funciones de Activación Neuronal")
plt.xlabel("Entrada (x)")
plt.ylabel("Salida f(x)")
plt.legend()
plt.grid(True)
plt.show()