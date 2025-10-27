# Descripción:
#   Simula un proceso temporal donde el clima evoluciona con el tiempo
#   y se observan evidencias ruidosas (suelo mojado o seco).

import random

# Definición de los estados y probabilidades

estados = ["Lluvia", "No_Lluvia"]

# Probabilidades de transición P(X_t+1 | X_t)
transicion = {
    "Lluvia": {"Lluvia": 0.7, "No_Lluvia": 0.3},
    "No_Lluvia": {"Lluvia": 0.3, "No_Lluvia": 0.7}
}

# Probabilidades de observación P(Evidencia | Estado)
# (sensor: suelo mojado)
observacion = {
    "Lluvia": {"Mojado": 0.9, "Seco": 0.1},
    "No_Lluvia": {"Mojado": 0.2, "Seco": 0.8}
}

# Probabilidad inicial P(X_0)
creencia = {"Lluvia": 0.5, "No_Lluvia": 0.5}

# Función para actualizar la creencia (filtrado Bayesiano)

def actualizar_creencia(creencia, evidencia):
    nueva_creencia = {}
    for estado_actual in estados:
        # Paso de predicción
        pred = sum(creencia[prev] * transicion[prev][estado_actual] for prev in estados)
        # Incorporar evidencia (Bayes)
        nueva_creencia[estado_actual] = observacion[estado_actual][evidencia] * pred

    # Normalizar para que sume 1
    normalizador = sum(nueva_creencia.values())
    for s in estados:
        nueva_creencia[s] /= normalizador
    return nueva_creencia

# Simulación temporal

print("\n RED BAYESIANA DINÁMICA: Predicción de Lluvia \n")

# Secuencia de evidencias observadas (ruidosas)
evidencias = ["Mojado", "Mojado", "Seco", "Mojado", "Seco"]

for t, evidencia in enumerate(evidencias):
    creencia = actualizar_creencia(creencia, evidencia)
    print(f"Día {t+1} | Evidencia: {evidencia}")
    print(f"Probabilidad Lluvia: {creencia['Lluvia']:.3f} | No Lluvia: {creencia['No_Lluvia']:.3f}\n")