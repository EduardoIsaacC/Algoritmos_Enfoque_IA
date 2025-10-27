# Descripción:
#   Inspirado en el proceso físico de enfriamiento del metal.
#   Busca minimizar una función, aceptando peores soluciones
#   con cierta probabilidad que disminuye conforme baja la temperatura.

import math
import random

# Función a minimizar:
# f(x) = x^2 + 10 * sin(5x)
# Tiene muchos mínimos locales.

def funcion_objetivo(x):
    return x**2 + 10 * math.sin(5 * x)

# Búsqueda por Temple Simulado
# Parámetros:
#   f: función objetivo
#   x_inicial: punto inicial
#   T_inicial: temperatura inicial
#   T_final: temperatura mínima (criterio de parada)
#   alfa: factor de enfriamiento (0 < alfa < 1)
#   pasos_por_T: iteraciones por temperatura

def temple_simulado(f, x_inicial=5, T_inicial=100, T_final=0.01, alfa=0.95, pasos_por_T=100):
    # Estado actual
    x_actual = x_inicial
    costo_actual = f(x_actual)

    # Mejor solución global
    mejor_x = x_actual
    mejor_costo = costo_actual

    T = T_inicial  # temperatura inicial

    iteracion = 0
    while T > T_final:
        for _ in range(pasos_por_T):
            # Generamos un vecino cercano aleatorio
            x_vecino = x_actual + random.uniform(-1, 1)
            costo_vecino = f(x_vecino)

            # Diferencia de costo
            delta_E = costo_vecino - costo_actual

            # Si mejora, lo aceptamos
            if delta_E < 0:
                x_actual, costo_actual = x_vecino, costo_vecino
            else:
                # Si empeora, lo aceptamos con cierta probabilidad
                prob = math.exp(-delta_E / T)
                if random.random() < prob:
                    x_actual, costo_actual = x_vecino, costo_vecino

            # Guardamos la mejor solución global encontrada
            if costo_actual < mejor_costo:
                mejor_x, mejor_costo = x_actual, costo_actual

        # Reducimos la temperatura (enfriamiento)
        T *= alfa
        iteracion += 1

        # Mostramos trazas cada ciertas iteraciones
        if iteracion % 10 == 0:
            print(f"Iter {iteracion:3d} | T={T:.3f} | x={x_actual:.3f} | f(x)={costo_actual:.3f}")

    return mejor_x, mejor_costo

# BLOQUE PRINCIPAL

if __name__ == "__main__":
    print("\n BÚSQUEDA DE TEMPLE SIMULADO \n")

    mejor_x, mejor_costo = temple_simulado(
        funcion_objetivo,
        x_inicial=5,
        T_inicial=100,
        T_final=0.001,
        alfa=0.90,
        pasos_por_T=50
    )

    print(f"\n Mejor solución encontrada: x = {mejor_x:.4f}")
    print(f" Valor mínimo de f(x): {mejor_costo:.4f}")