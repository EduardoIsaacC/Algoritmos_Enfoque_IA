import numpy as np
import matplotlib.pyplot as plt

# Configuración inicial
np.random.seed(42)

# Tiempo y movimiento real
steps = 50
velocidad_real = 1.0  # m/s
posiciones_reales = np.linspace(0, velocidad_real * steps, steps)

# Mediciones ruidosas (simuladas)
ruido_sensor = np.random.normal(0, 2, size=steps)
mediciones = posiciones_reales + ruido_sensor

# Inicialización del Filtro de Kalman
x_est = 0.0        # estimación inicial de la posición
P = 1.0             # incertidumbre inicial
A = 1.0             # modelo de transición (movimiento constante)
H = 1.0             # relación entre estado y medición
Q = 0.001           # ruido del modelo
R = 4.0             # ruido del sensor

estimaciones = []

# Ciclo del filtro
for z in mediciones:
    # 1 Predicción
    x_pred = A * x_est
    P_pred = A * P * A + Q

    # 2 Ganancia de Kalman
    K = P_pred * H / (H * P_pred * H + R)

    # 3 Actualización
    x_est = x_pred + K * (z - H * x_pred)
    P = (1 - K * H) * P_pred

    estimaciones.append(x_est)

# Visualización
plt.figure(figsize=(9,4))
plt.plot(posiciones_reales, label="Posición Real", color="green")
plt.plot(mediciones, label="Medición (ruidosa)", color="red", linestyle="dotted")
plt.plot(estimaciones, label="Estimación (Kalman)", color="blue")
plt.xlabel("Tiempo (t)")
plt.ylabel("Posición (m)")
plt.legend()
plt.title("Filtro de Kalman 1D — Estimación de posición")
plt.grid()
plt.show()