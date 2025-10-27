# Descripción:
#   Variante de búsqueda local que mantiene K soluciones simultáneamente.
#   En cada iteración genera todos sus vecinos y conserva los K mejores.

import math
import random

# Función objetivo a minimizar

def funcion_objetivo(x):
    return x**2 + 10 * math.sin(5 * x)

# Función principal: Búsqueda de Haz Local
# Parámetros:
#   f: función objetivo
#   k: número de soluciones mantenidas en paralelo
#   iter_max: número de iteraciones
#   rango: límites de búsqueda (min, max)
#   delta: amplitud del vecindario (cambio permitido)

def busqueda_haz_local(f, k=5, iter_max=50, rango=(-10, 10), delta=0.5):
    # Inicializamos K estados aleatorios
    estados = [random.uniform(*rango) for _ in range(k)]
    valores = [f(x) for x in estados]

    # Mejor solución global
    mejor_x = estados[valores.index(min(valores))]
    mejor_valor = min(valores)

    for it in range(iter_max):
        vecinos = []

        # Generamos vecinos de cada estado actual
        for x in estados:
            for _ in range(3):  # 3 vecinos por cada estado
                x_vecino = x + random.uniform(-delta, delta)
                x_vecino = max(rango[0], min(x_vecino, rango[1]))  # limitar rango
                vecinos.append(x_vecino)

        # Evaluamos todos los vecinos
        vecinos_val = [(xv, f(xv)) for xv in vecinos]

        # Ordenamos por valor de la función (buscamos mínimo)
        vecinos_val.sort(key=lambda t: t[1])

        # Elegimos los K mejores para la siguiente iteración
        estados = [t[0] for t in vecinos_val[:k]]
        valores = [t[1] for t in vecinos_val[:k]]

        # Actualizamos el mejor global
        if min(valores) < mejor_valor:
            mejor_valor = min(valores)
            mejor_x = estados[valores.index(mejor_valor)]

        # Mostrar progreso
        print(f"Iter {it+1:2d} | Mejores X: {[round(e,2) for e in estados]} | f(x) min={mejor_valor:.4f}")

    return mejor_x, mejor_valor

# BLOQUE PRINCIPAL

if __name__ == "__main__":
    print("\n BÚSQUEDA DE HAZ LOCAL \n")

    mejor_x, mejor_valor = busqueda_haz_local(
        funcion_objetivo,
        k=5,          # número de soluciones paralelas
        iter_max=30,  # número de iteraciones
        rango=(-10, 10),
        delta=0.5     # amplitud de los saltos locales
    )

    print(f"\n Mejor solución encontrada: x = {mejor_x:.4f}")
    print(f" Valor mínimo de f(x): {mejor_valor:.4f}")