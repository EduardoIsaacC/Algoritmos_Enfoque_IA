# Descripción:
#   El agente aprende la mejor política explorando el entorno.
#   Se usa la regla Q-Learning y política epsilon-greedy.

import random
import matplotlib.pyplot as plt
import numpy as np

# Definir entorno

estados = ["S1", "S2", "S3", "S4"]
acciones = ["Izquierda", "Derecha"]

# Recompensas asociadas a cada estado (solo la meta tiene +1)
recompensas = {"S1": 0, "S2": 0, "S3": 0, "S4": 1}

# Transiciones deterministas simplificadas
transiciones = {
    "S1": {"Derecha": "S2", "Izquierda": "S1"},
    "S2": {"Derecha": "S3", "Izquierda": "S1"},
    "S3": {"Derecha": "S4", "Izquierda": "S2"},
    "S4": {"Derecha": "S4", "Izquierda": "S4"},
}

# Inicialización de parámetros

alpha = 0.1      # tasa de aprendizaje
gamma = 0.9      # descuento futuro
epsilon = 0.2    # probabilidad de exploración
episodios = 50   # número de episodios

# Inicializar Q(s,a) = 0
Q = {s: {a: 0.0 for a in acciones} for s in estados}

# Guardar promedios para graficar
hist_recompensas = []

# Algoritmo principal Q-Learning

print("\n APRENDIZAJE POR REFUERZO ACTIVO (Q-Learning) \n")

for ep in range(episodios):
    s = "S1"
    total_reward = 0

    while s != "S4":
        # Política ε-greedy
        if random.random() < epsilon:
            a = random.choice(acciones)  # explorar
        else:
            a = max(Q[s], key=Q[s].get)  # explotar

        s_next = transiciones[s][a]
        r = recompensas[s_next]
        total_reward += r

        # Actualización de Q según la ecuación de Q-learning
        Q[s][a] = Q[s][a] + alpha * (
            r + gamma * max(Q[s_next].values()) - Q[s][a]
        )

        s = s_next

    hist_recompensas.append(total_reward)

    print(f"Episodio {ep+1:02d} → Recompensa total: {total_reward}")

# Mostrar la Q-table final

print("\n Q-Table Final ")
for s in estados:
    print(f"{s}: {Q[s]}")

# Derivar política óptima

politica = {s: max(Q[s], key=Q[s].get) for s in estados}
print("\nPolítica aprendida (óptima):")
for s in politica:
    print(f"π({s}) = {politica[s]}")

# Graficar la recompensa acumulada

plt.figure(figsize=(7,4))
plt.plot(hist_recompensas, marker='o')
plt.title("Aprendizaje por Refuerzo Activo (Q-Learning)\nRecompensa por Episodio")
plt.xlabel("Episodio")
plt.ylabel("Recompensa Total")
plt.grid(True)
plt.tight_layout()
plt.show()