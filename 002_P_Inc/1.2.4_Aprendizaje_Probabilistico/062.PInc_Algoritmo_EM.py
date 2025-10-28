import numpy as np
import matplotlib.pyplot as plt

# Datos simulados (dos grupos)
np.random.seed(42)
x1 = np.random.normal(5, 1, 100)
x2 = np.random.normal(10, 1.5, 100)
X = np.concatenate([x1, x2])

# Inicialización
n = len(X)
k = 2  # número de grupos
mu = np.random.choice(X, k)      # medias iniciales
sigma = np.random.random(k) + 1  # desviaciones iniciales
pi = np.ones(k) / k              # pesos iniciales

def gauss(x, mu, sigma):
    return (1 / (np.sqrt(2 * np.pi) * sigma)) * np.exp(-0.5 * ((x - mu)/sigma)**2)

# Algoritmo EM
for iteration in range(20):
    # E-step: calcular probabilidades de pertenencia
    gamma = np.zeros((n, k))
    for i in range(k):
        gamma[:, i] = pi[i] * gauss(X, mu[i], sigma[i])
    gamma /= np.sum(gamma, axis=1, keepdims=True)
    
    # M-step: actualizar parámetros
    N_k = np.sum(gamma, axis=0)
    for i in range(k):
        mu[i] = np.sum(gamma[:, i] * X) / N_k[i]
        sigma[i] = np.sqrt(np.sum(gamma[:, i] * (X - mu[i])**2) / N_k[i])
        pi[i] = N_k[i] / n

# Resultados
print(" Algoritmo EM (GMM) ")
for i in range(k):
    print(f"Componente {i+1}: μ={mu[i]:.2f}, σ={sigma[i]:.2f}, peso={pi[i]:.2f}")

# Visualización
x_grid = np.linspace(min(X)-2, max(X)+2, 200)
y = np.zeros_like(x_grid)
for i in range(k):
    y += pi[i] * gauss(x_grid, mu[i], sigma[i])

plt.hist(X, bins=25, density=True, alpha=0.6, color='gray', label='Datos')
plt.plot(x_grid, y, 'r-', label='Mezcla EM')
plt.title("Aprendizaje Probabilístico — Algoritmo EM")
plt.legend()
plt.show()