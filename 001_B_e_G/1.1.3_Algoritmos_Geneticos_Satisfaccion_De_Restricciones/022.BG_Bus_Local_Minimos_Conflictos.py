# Descripción:
#   Algoritmo heurístico para resolver CSPs ajustando valores
#   de variables en conflicto hasta eliminar todas las restricciones violadas.

import random

# VARIABLES, DOMINIOS Y RESTRICCIONES

variables = ["A", "B", "C", "D"]

dominios = {
    "A": ["Rojo", "Verde", "Azul"],
    "B": ["Rojo", "Verde", "Azul"],
    "C": ["Rojo", "Verde", "Azul"],
    "D": ["Rojo", "Verde", "Azul"]
}

# Vecindades: no pueden tener el mismo color
restricciones = [
    ("A", "B"), ("A", "C"),
    ("B", "C"), ("B", "D"),
    ("C", "D")
]

# FUNCIÓN: cuenta cuántos conflictos tiene una variable dada

def contar_conflictos(var, valor, asignacion):
    conflictos = 0
    for (x, y) in restricciones:
        if x == var and y in asignacion and asignacion[y] == valor:
            conflictos += 1
        if y == var and x in asignacion and asignacion[x] == valor:
            conflictos += 1
    return conflictos

# FUNCIÓN PRINCIPAL: Algoritmo de Mínimos Conflictos

def min_conflicts(max_iter=1000):
    # 1️⃣ Asignación inicial aleatoria
    asignacion = {v: random.choice(dominios[v]) for v in variables}

    for paso in range(max_iter):
        # Detectar variables en conflicto
        conflictuadas = [
            v for v in variables
            if contar_conflictos(v, asignacion[v], asignacion) > 0
        ]

        # Si no hay conflictos → éxito
        if not conflictuadas:
            print(f"\n Solución encontrada en {paso} iteraciones.")
            return asignacion

        # Elegir una variable en conflicto al azar
        var = random.choice(conflictuadas)

        # Probar cada valor posible y elegir el que genere menos conflictos
        mejor_valor = min(
            dominios[var],
            key=lambda val: contar_conflictos(var, val, asignacion)
        )

        # Asignar nuevo valor
        asignacion[var] = mejor_valor

        # Mostrar progreso cada cierto número de pasos
        if paso % 50 == 0:
            print(f"Iteración {paso:3d}: {asignacion}")

    print("\n No se encontró solución (límite de iteraciones alcanzado).")
    return None

# BLOQUE PRINCIPAL

if __name__ == "__main__":
    print("\n BÚSQUEDA LOCAL: MÍNIMOS CONFLICTOS \n")
    solucion = min_conflicts(max_iter=500)

    if solucion:
        for v, val in solucion.items():
            print(f"  {v} = {val}")