# Descripción:
#   El agente aprende una política óptima mediante exploración
#   y actualización de la función de acción-valor Q(s,a).

import random
import matplotlib.pyplot as plt
import numpy as np

# Definición del entorno

estados = ["S1", "S2", "S3", "S4"]
acciones = ["Izquierda", "Derecha"]

# Recompensas por estado
recompensas = {"S1": 0, "S2": 0, "S3": 0, "S4": 1}

# Transiciones deterministas
transiciones = {
    "S1": {"Derecha": "S2", "Izquierda": "S1"},
    "S2": {"Derecha": "S3", "Izquierda": "S1"},
    "S3": {"Derecha": "S4", "Izquierda": "S2"},
    "S4": {"Derecha": "S4", "Izquierda": "S4"},
}

# Parámetros del algoritmo

alpha = 0.1      # tasa de aprendizaje
gamma = 0.9      # factor de descuento
epsilon = 0.2    # probabilidad de exploración
episodios = 80   # número de episodios

# Inicializar Q-table
Q = {s: {a: 0.0 for a in acciones} for s in estados}

# Historial de recompensas
hist_recompensas = []

# Bucle principal de aprendizaje (Q-Learning)

print("\n Q-LEARNING: ENTRENAMIENTO \n")

for ep in range(episodios):
    s = "S1"
    total_reward = 0

    while s != "S4":
        # Política ε-greedy
        if random.random() < epsilon:
            a = random.choice(acciones)  # Explora
        else:
            a = max(Q[s], key=Q[s].get)  # Explota

        s_next = transiciones[s][a]
        r = recompensas[s_next]
        total_reward += r

        # Actualización Q(s,a)
        Q[s][a] = Q[s][a] + alpha * (r + gamma * max(Q[s_next].values()) - Q[s][a])

        s = s_next

    hist_recompensas.append(total_reward)
    print(f"Episodio {ep+1:02d}: Recompensa total = {total_reward}")

# Mostrar tabla Q resultante

print("\n Q-Table Final ")
for s in estados:
    print(f"{s}: {Q[s]}")

# Política aprendida

politica = {s: max(Q[s], key=Q[s].get) for s in estados}
print("\nPolítica Óptima Aprendida:")
for s in politica:
    print(f"π({s}) = {politica[s]}")

# Gráfica: Recompensa por episodio

plt.figure(figsize=(7,4))
plt.plot(hist_recompensas, marker='o')
plt.title("Q-Learning\nRecompensa Total por Episodio")
plt.xlabel("Episodio")
plt.ylabel("Recompensa Total")
plt.grid(True)
plt.tight_layout()
plt.show()

# Gráfica: Valores Q de cada estado

plt.figure(figsize=(8,5))
for a in acciones:
    valores = [Q[s][a] for s in estados]
    plt.plot(estados, valores, marker='o', label=f"Acción: {a}")

plt.title("Valores Q(s,a) por Estado")
plt.xlabel("Estado")
plt.ylabel("Valor Q")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()