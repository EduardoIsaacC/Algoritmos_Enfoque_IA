# Descripción:
#   Ejemplo completo de un MDP con:
#   - Estados, acciones, recompensas y transiciones.
#   - Evaluación de la política óptima usando Bellman.

import numpy as np

# Definición del entorno MDP

estados = ["A", "B", "C", "D"]   # Estados del entorno
acciones = ["Derecha"]           # Acción disponible (simplificada)

# Recompensas inmediatas de cada estado
R = {
    "A": -0.04,
    "B": -0.04,
    "C": -0.04,
    "D": +1.0  # Meta
}

# Modelo de transición probabilístico
P = {
    "A": {"Derecha": {"B": 0.8, "A": 0.2}},
    "B": {"Derecha": {"C": 0.8, "B": 0.2}},
    "C": {"Derecha": {"D": 0.8, "C": 0.2}},
    "D": {"Derecha": {"D": 1.0}}
}

gamma = 0.99   # Factor de descuento

# Cálculo de utilidad esperada con ecuación de Bellman

def bellman_update(U, s):
    """Actualiza la utilidad del estado s usando Bellman"""
    a = "Derecha"  # Solo una acción
    utilidad_esperada = 0
    for s_next, prob in P[s][a].items():
        utilidad_esperada += prob * U[s_next]
    return R[s] + gamma * utilidad_esperada

# Ciclo de evaluación hasta convergencia

U = {s: 0.0 for s in estados}
epsilon = 1e-4

for i in range(50):  # Máximo 50 iteraciones
    delta = 0
    nuevo_U = U.copy()
    for s in estados:
        nuevo_U[s] = bellman_update(U, s)
        delta = max(delta, abs(nuevo_U[s] - U[s]))
    U = nuevo_U
    print(f"Iter {i+1} -> {U}")
    if delta < epsilon:
        break

# Política óptima

politica = {s: "Derecha" for s in estados}

# Resultados

print("\n RESULTADOS FINALES DEL MDP ")
for s in estados:
    print(f"U({s}) = {U[s]:.4f}")
print(f"\nPolítica Óptima: {politica}")