import numpy as np

# Definición del modelo
estados = ["u", "n", "o"]           # fonemas ocultos
observaciones = ["e1", "e2", "e3", "e4", "e5"]  # fragmentos acústicos posibles

# Distribución inicial
pi = {"u": 1.0, "n": 0.0, "o": 0.0}

# Probabilidad de transición entre fonemas
A = {
    "u": {"u": 0.1, "n": 0.9, "o": 0.0},
    "n": {"u": 0.0, "n": 0.1, "o": 0.9},
    "o": {"u": 0.0, "n": 0.0, "o": 1.0}
}

# Probabilidades de emisión (qué tan probable es escuchar un sonido según el fonema)
B = {
    "u": {"e1": 0.5, "e2": 0.4, "e3": 0.1, "e4": 0.0, "e5": 0.0},
    "n": {"e1": 0.0, "e2": 0.3, "e3": 0.6, "e4": 0.1, "e5": 0.0},
    "o": {"e1": 0.0, "e2": 0.0, "e3": 0.2, "e4": 0.4, "e5": 0.4}
}

# Observaciones recibidas (fragmentos acústicos)
O = ["e1", "e2", "e3", "e4", "e5"]

# Algoritmo de Viterbi
T = len(O)
V = [{} for _ in range(T)]
path = {}

# Inicialización
for s in estados:
    V[0][s] = pi[s] * B[s][O[0]]
    path[s] = [s]

# Iteración
for t in range(1, T):
    new_path = {}
    for s in estados:
        (prob, estado_prev) = max(
            (V[t-1][s_prev] * A[s_prev][s] * B[s][O[t]], s_prev)
            for s_prev in estados
        )
        V[t][s] = prob
        new_path[s] = path[estado_prev] + [s]
    path = new_path

# Resultado final
(prob_final, estado_final) = max((V[T-1][s], s) for s in estados)
print(" Reconocimiento del Habla (HMM simplificado) ")
print(f"Secuencia observada: {' → '.join(O)}")
print(f"Fonemas más probables: {' → '.join(path[estado_final])}")
print(f"Probabilidad total: {prob_final:.6f}")