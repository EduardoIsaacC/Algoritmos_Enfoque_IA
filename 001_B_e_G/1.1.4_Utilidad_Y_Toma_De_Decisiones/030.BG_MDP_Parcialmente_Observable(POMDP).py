# Descripción:
#   Simulación básica de un agente que mantiene una creencia sobre
#   su estado y la actualiza con base en observaciones ruidosas.

import numpy as np
import random

# Definición del entorno

estados = ["Izquierda", "Derecha"]
acciones = ["Mover_Izquierda", "Mover_Derecha"]
observaciones = ["Veo_Izquierda", "Veo_Derecha"]

# Modelo de transición P(s'|s,a)
P = {
    ("Izquierda", "Mover_Izquierda"): {"Izquierda": 0.8, "Derecha": 0.2},
    ("Izquierda", "Mover_Derecha"): {"Izquierda": 0.1, "Derecha": 0.9},
    ("Derecha", "Mover_Izquierda"): {"Izquierda": 0.9, "Derecha": 0.1},
    ("Derecha", "Mover_Derecha"): {"Izquierda": 0.2, "Derecha": 0.8},
}

# Modelo de observación O(o|s')
O = {
    "Izquierda": {"Veo_Izquierda": 0.9, "Veo_Derecha": 0.1},
    "Derecha": {"Veo_Izquierda": 0.2, "Veo_Derecha": 0.8},
}

# Recompensas
R = {
    "Izquierda": -0.04,
    "Derecha": +1.0
}

gamma = 0.9

# Creencia inicial (el agente no sabe dónde está)

b = {"Izquierda": 0.5, "Derecha": 0.5}

# Función para actualizar creencia (Bayes)

def actualizar_creencia(b, accion, observacion):
    nuevo_b = {}
    normalizador = 0

    for s_next in estados:
        prob_obs = O[s_next][observacion]
        suma = sum(P[(s, accion)][s_next] * b[s] for s in estados)
        nuevo_b[s_next] = prob_obs * suma
        normalizador += nuevo_b[s_next]

    # Normalizar para que las probabilidades sumen 1
    for s in estados:
        nuevo_b[s] /= normalizador

    return nuevo_b

# Simulación paso a paso

print("\n POMDP: Simulación de creencias \n")

for paso in range(5):
    accion = random.choice(acciones)
    observacion = random.choice(observaciones)
    b = actualizar_creencia(b, accion, observacion)

    print(f"Paso {paso+1}")
    print(f"Acción: {accion}")
    print(f"Observación: {observacion}")
    print(f"Creencia actualizada: {b}\n")