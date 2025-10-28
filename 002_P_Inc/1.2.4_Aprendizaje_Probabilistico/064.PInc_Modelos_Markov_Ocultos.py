import numpy as np

# Definición de parámetros
estados = ["Soleado", "Lluvioso"]
observaciones = ["No", "Sí"]

# Inicialización de matrices (valores aproximados)
A = np.array([[0.7, 0.3],
              [0.4, 0.6]])  # transición
B = np.array([[0.9, 0.1],
              [0.3, 0.7]])  # emisión
pi = np.array([0.6, 0.4])   # inicialización

# Secuencia observada (evidencias)
O = [1, 0, 1, 1, 0, 0, 1]  # 1 = Sí (paraguas), 0 = No

# Función Baum-Welch (versión resumida)
def forward(O, A, B, pi):
    N = A.shape[0]
    T = len(O)
    alpha = np.zeros((T, N))
    alpha[0, :] = pi * B[:, O[0]]
    for t in range(1, T):
        for j in range(N):
            alpha[t, j] = B[j, O[t]] * np.sum(alpha[t-1] * A[:, j])
    return alpha

def backward(O, A, B):
    N = A.shape[0]
    T = len(O)
    beta = np.zeros((T, N))
    beta[T-1, :] = 1
    for t in range(T-2, -1, -1):
        for i in range(N):
            beta[t, i] = np.sum(A[i, :] * B[:, O[t+1]] * beta[t+1, :])
    return beta

def baum_welch(O, A, B, pi, iteraciones=10):
    N = A.shape[0]
    T = len(O)

    for _ in range(iteraciones):
        alpha = forward(O, A, B, pi)
        beta = backward(O, A, B)
        xi = np.zeros((T-1, N, N))
        gamma = np.zeros((T, N))

        for t in range(T-1):
            denom = np.sum(alpha[t, :] @ A * B[:, O[t+1]] * beta[t+1, :])
            for i in range(N):
                numer = alpha[t, i] * A[i, :] * B[:, O[t+1]] * beta[t+1, :]
                xi[t, i, :] = numer / denom
            gamma[t, :] = np.sum(xi[t, :, :], axis=1)
        gamma[T-1, :] = alpha[T-1, :] / np.sum(alpha[T-1, :])

        # Actualización de parámetros
        pi = gamma[0, :]
        A = np.sum(xi, axis=0) / np.sum(gamma[:-1, :], axis=0)[:, None]
        for j in range(N):
            for k in range(B.shape[1]):
                mask = np.array(O) == k
                B[j, k] = np.sum(gamma[mask, j]) / np.sum(gamma[:, j])

    return A, B, pi

# Entrenamiento
A_final, B_final, pi_final = baum_welch(O, A, B, pi)

print("Modelo de Markov Oculto (Baum – Welch)")
print("Matriz de transición (A):\n", np.round(A_final, 3))
print("Matriz de emisión (B):\n", np.round(B_final, 3))
print("Distribución inicial (π):\n", np.round(pi_final, 3))