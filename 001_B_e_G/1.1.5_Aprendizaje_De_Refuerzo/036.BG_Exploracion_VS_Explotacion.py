# Descripción:
#   Simula cómo un agente balancea explorar y explotar
#   usando una política epsilon-greedy.

import random
import matplotlib.pyplot as plt

# Definir entorno
# Acción 0 = buena (recompensa promedio 0.8)
# Acción 1 = mala (recompensa promedio 0.3)
def obtener_recompensa(accion):
    if accion == 0:
        return random.gauss(0.8, 0.1)  # buena
    else:
        return random.gauss(0.3, 0.1)  # mala

# Parámetros de simulación

episodios = 200
epsilon = 0.2          # 20% del tiempo explorará
alpha = 0.1            # tasa de aprendizaje

# Inicializar valores estimados Q(a)
Q = [0.0, 0.0]
recompensas_prom = []

# Bucle de interacción (ε-Greedy)

for ep in range(episodios):
    # Selección ε-greedy
    if random.random() < epsilon:
        a = random.choice([0, 1])  # Explorar
    else:
        a = Q.index(max(Q))        # Explotar

    r = obtener_recompensa(a)

    # Actualizar valor Q(a)
    Q[a] = Q[a] + alpha * (r - Q[a])

    # Guardar recompensa media
    recompensas_prom.append(r)

# Resultados

print("\n EXPLORACIÓN vs EXPLOTACIÓN ")
print(f"Valor estimado acción 0: {Q[0]:.3f}")
print(f"Valor estimado acción 1: {Q[1]:.3f}")

# Gráfica

plt.figure(figsize=(8,4))
plt.plot(recompensas_prom, label="Recompensa obtenida")
plt.axhline(0.8, color='green', linestyle='--', label="Recompensa óptima (acción buena)")
plt.axhline(0.3, color='red', linestyle='--', label="Recompensa baja (acción mala)")
plt.title("Exploración vs Explotación (ε = 0.2)")
plt.xlabel("Episodio")
plt.ylabel("Recompensa")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()