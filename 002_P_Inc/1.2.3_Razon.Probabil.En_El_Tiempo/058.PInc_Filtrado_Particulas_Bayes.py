import numpy as np
import matplotlib.pyplot as plt

# Parámetros del sistema
N = 500                     # número de partículas
T = 30                      # pasos de tiempo
ruido_mov = 1.0             # ruido en movimiento
ruido_sensor = 2.0          # ruido en medición

# Estado real inicial
x_real = 0
velocidad_real = 1.2

# Inicialización de partículas
particulas = np.random.normal(x_real, 5, N)
pesos = np.ones(N) / N

# Historial para graficar
trayectoria_real = []
estimaciones = []
mediciones = []

for t in range(T):
    # Movimiento real con ruido
    x_real += velocidad_real + np.random.normal(0, ruido_mov)
    trayectoria_real.append(x_real)

    # Medición ruidosa
    z = x_real + np.random.normal(0, ruido_sensor)
    mediciones.append(z)

    # Predicción
    particulas += np.random.normal(velocidad_real, ruido_mov, N)

    # Actualización (ponderación por distancia al sensor)
    pesos *= np.exp(-0.5 * ((z - particulas) / ruido_sensor) ** 2)
    pesos += 1e-300  # evitar ceros
    pesos /= np.sum(pesos)

    # Re-muestreo (SIR)
    indices = np.random.choice(range(N), size=N, p=pesos)
    particulas = particulas[indices]
    pesos = np.ones(N) / N

    # Estimación como promedio ponderado
    estimacion = np.mean(particulas)
    estimaciones.append(estimacion)

# Gráficas 
plt.figure(figsize=(9,4))
plt.plot(trayectoria_real, 'g-', label='Posición Real')
plt.plot(mediciones, 'r.', alpha=0.5, label='Mediciones Ruidosas')
plt.plot(estimaciones, 'b-', label='Estimación (Filtro de Partículas)')
plt.legend()
plt.title("Red Bayesiana Dinámica — Filtrado de Partículas")
plt.xlabel("Tiempo")
plt.ylabel("Posición")
plt.grid()
plt.show()
