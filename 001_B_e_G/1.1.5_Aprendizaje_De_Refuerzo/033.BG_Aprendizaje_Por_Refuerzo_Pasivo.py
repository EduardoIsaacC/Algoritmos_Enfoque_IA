# Descripción:
#   Evalúa una política fija aprendiendo la utilidad de cada estado
#   con TD(0), y grafica cómo convergen esas utilidades episodio a episodio.
#
#   Cambios vs versión anterior:
#     - Se guarda la evolución de U(S1), U(S2), U(S3), U(S4) en listas.
#     - Se usa matplotlib para graficar la convergencia.

import random
import matplotlib.pyplot as plt

# Entorno lineal (S1 -> S2 -> S3 -> S4)

estados = ["S1", "S2", "S3", "S4"]  # S4 es terminal
recompensas = {
    "S1": 0,
    "S2": 0,
    "S3": 0,
    "S4": 1   # recompensa al llegar a la meta
}

# Transiciones deterministas bajo la política fija "ir a la derecha"
transiciones = {
    "S1": "S2",
    "S2": "S3",
    "S3": "S4",
    "S4": "S4"  # quedarse en terminal
}

# Política fija (pasivo): siempre avanzar
politica = {s: "Derecha" for s in estados}

# Hiperparámetros del aprendizaje TD

gamma = 0.9      # descuento futuro
alpha = 0.1      # tasa de aprendizaje
episodios = 30   # episodios de experiencia

# Utilidad estimada inicial de cada estado
U = {s: 0.0 for s in estados}
U["S4"] = 1.0  # le decimos al agente que la meta vale 1 (opcional pero común)

# Listas para guardar la evolución (historial)
hist_S1 = []
hist_S2 = []
hist_S3 = []
hist_S4 = []

# Bucle de aprendizaje pasivo (TD(0))

print("\n APRENDIZAJE POR REFUERZO PASIVO (TD) \n")

for ep in range(episodios):
    s = "S1"  # siempre empezamos en S1

    while s != "S4":  # hasta llegar al estado terminal
        s_next = transiciones[s]
        r = recompensas[s_next]

        # Regla TD(0):
        # U(s) ← U(s) + α * [ r + γ * U(s_next) − U(s) ]
        U[s] = U[s] + alpha * (r + gamma * U[s_next] - U[s])

        # avanzar
        s = s_next

    # Guardar el snapshot de utilidades después de cada episodio
    hist_S1.append(U["S1"])
    hist_S2.append(U["S2"])
    hist_S3.append(U["S3"])
    hist_S4.append(U["S4"])

    print(f"Episodio {ep+1:02d} → U = {U}")

# Resultados finales en texto

print("\n RESULTADOS FINALES ")
for s in estados:
    print(f"U({s}) = {U[s]:.3f}")

# GRÁFICA DE CONVERGENCIA

plt.figure(figsize=(8,4))
plt.plot(hist_S1, label="U(S1)")
plt.plot(hist_S2, label="U(S2)")
plt.plot(hist_S3, label="U(S3)")
plt.plot(hist_S4, label="U(S4)")

plt.title("Aprendizaje por Refuerzo Pasivo (TD)\nConvergencia de Utilidades por Estado")
plt.xlabel("Episodio")
plt.ylabel("Utilidad estimada U(s)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()