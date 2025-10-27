# Descripción:
#   Calcula las utilidades óptimas de cada estado en un MDP
#   aplicando la ecuación de Bellman iterativamente hasta converger.
#   Esta versión:
#     - Propaga la recompensa del estado terminal D.
#     - Muestra la evolución de las utilidades en cada iteración.

import math

# Definición del entorno MDP

estados = ["A", "B", "C", "D"]

# Acciones posibles desde cada estado.
# Aquí usamos una cuadrícula lineal -> solo "Derecha"
acciones_por_estado = {
    "A": ["Derecha"],
    "B": ["Derecha"],
    "C": ["Derecha"],
    "D": ["Derecha"]  # D se queda en D
}

# Recompensas inmediatas por estar en cada estado
R = {
    "A": -0.04,
    "B": -0.04,
    "C": -0.04,
    "D": +1.0    # recompensa terminal positiva
}

# Modelo de transición:
# P[s][a] = { s_next: probabilidad }
P = {
    "A": {
        "Derecha": {"B": 0.8, "A": 0.2}
    },
    "B": {
        "Derecha": {"C": 0.8, "B": 0.2}
    },
    "C": {
        "Derecha": {"D": 0.8, "C": 0.2}
    },
    "D": {
        # En D ya estás "ganando"; si sigues actuando te quedas en D
        "Derecha": {"D": 1.0}
    }
}

gamma = 0.99      # factor de descuento (valora mucho el futuro)
epsilon = 1e-4    # criterio de parada para la convergencia

# Inicializamos las utilidades de todos los estados

U = {s: 0.0 for s in estados}

# Una iteración de Bellman para TODOS los estados
# Devuelve (nuevas_utilidades, cambio_maximo)

def paso_value_iteration(U_actual):
    nuevas_U = {}
    delta = 0.0

    for s in estados:
        # Para cada estado s:
        # U(s) = R(s) + gamma * max_a Σ_{s'} P(s'|s,a)*U(s')

        mejores_q = []

        for a in acciones_por_estado[s]:
            q_sa = 0.0
            for s_next, prob in P[s][a].items():
                q_sa += prob * U_actual[s_next]
            mejores_q.append(q_sa)

        # IMPORTANTE:
        # Incluso en D seguimos aplicando la misma fórmula,
        # lo que deja que la recompensa de D influya hacia atrás.
        nuevas_U[s] = R[s] + gamma * (max(mejores_q) if mejores_q else 0.0)

        # Seguimiento de cuánto cambió
        delta = max(delta, abs(nuevas_U[s] - U_actual[s]))

    return nuevas_U, delta

# Algoritmo de Iteración de Valores completo

def value_iteration():
    global U
    iteracion = 0
    while True:
        iteracion += 1
        U, delta = paso_value_iteration(U)

        # Mostrar progreso de convergencia
        print(f"\nIteración {iteracion}")
        for s in estados:
            print(f"U({s}) = {U[s]:.4f}")
        print(f"delta = {delta:.6f}")

        # Condición de parada:
        # cuando el cambio máximo es menor que epsilon*(1-gamma)/gamma,
        # que es una cota estándar de convergencia en MDP finitos
        if delta < epsilon * (1 - gamma) / gamma:
            break

    return U

# BLOQUE PRINCIPAL

if __name__ == "__main__":
    print("\n ITERACIÓN DE VALORES (Value Iteration) - Corregida ")

    U_opt = value_iteration()

    print("\n Valores Óptimos de los Estados ")
    for s in estados:
        print(f"U({s}) = {U_opt[s]:.4f}")