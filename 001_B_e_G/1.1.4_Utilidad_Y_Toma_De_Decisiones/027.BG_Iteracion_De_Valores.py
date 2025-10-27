# Descripción:
#   Calcula las utilidades óptimas de cada estado en un MDP
#   mediante la ecuación de Bellman.

import numpy as np

# Definición del entorno (estados, acciones, recompensas)

estados = ["A", "B", "C", "D"]
acciones = ["Arriba", "Abajo", "Izquierda", "Derecha"]

# Recompensas de cada estado
R = {
    "A": -0.04,
    "B": -0.04,
    "C": -0.04,
    "D": +1.0  # estado terminal
}

# Probabilidades de transición (simplificadas)
# Cada acción lleva con 0.8 de probabilidad al destino esperado
# y con 0.2 de probabilidad permanece igual
P = {
    "A": {"Derecha": {"B": 0.8, "A": 0.2}},
    "B": {"Derecha": {"C": 0.8, "B": 0.2}},
    "C": {"Derecha": {"D": 0.8, "C": 0.2}},
    "D": {}
}

# Parámetros del MDP
gamma = 0.9     # factor de descuento
epsilon = 0.001 # criterio de convergencia

# Inicializar utilidades

U = {s: 0 for s in estados}

# Iteración de valores

def value_iteration():
    while True:
        delta = 0
        nuevo_U = U.copy()

        for s in estados:
            if s == "D":  # estado terminal
                continue

            # Calcular utilidad esperada para cada acción
            utilidades_acciones = []
            for a in P[s]:
                utilidad_accion = 0
                for s_next, prob in P[s][a].items():
                    utilidad_accion += prob * U[s_next]
                utilidades_acciones.append(utilidad_accion)

            # Aplicar la ecuación de Bellman
            nuevo_U[s] = R[s] + gamma * max(utilidades_acciones)
            delta = max(delta, abs(nuevo_U[s] - U[s]))

        U.update(nuevo_U)

        if delta < epsilon:
            break

    return U

# BLOQUE PRINCIPAL

if __name__ == "__main__":
    print("\n ITERACIÓN DE VALORES (Value Iteration) \n")

    U_opt = value_iteration()

    print(" Valores Óptimos de los Estados ")
    for s, val in U_opt.items():
        print(f"U({s}) = {val:.3f}")