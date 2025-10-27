import random

# Probabilidad de que el sensor funcione correctamente
P_sensor_correcto = 0.9

# Estados posibles: hay obstáculo o no
estados = ["obstaculo", "libre"]

# Simularemos 20 lecturas del sensor
n = 20
print("=== Simulación de sensor con incertidumbre ===\n")

for i in range(1, n + 1):
    # Estado real del entorno (50% de probabilidad)
    estado_real = random.choice(estados)
    
    # El sensor da una lectura, pero puede fallar con 10% de probabilidad
    if random.random() < P_sensor_correcto:
        lectura = estado_real
    else:
        # Se equivoca (reporta el contrario)
        lectura = "libre" if estado_real == "obstaculo" else "obstaculo"
    
    # Resultado
    print(f"Lectura {i:02d}: Sensor -> {lectura:10s} | Real -> {estado_real:10s}")

print("\nNota: Observa cómo a veces el sensor se equivoca.")
print("La probabilidad (0.9) nos ayuda a modelar esta incertidumbre.")