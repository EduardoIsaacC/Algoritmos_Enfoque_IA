#   Estrategia de búsqueda local que intenta maximizar una función
#   moviéndose siempre hacia un vecino con mejor valor heurístico.

import random
import math

# Función heurística (a maximizar)
# En este ejemplo usamos una función matemática continua:
#     f(x) = x * sin(10πx) + 1
# Esta tiene muchos máximos locales entre 0 y 1.

def funcion(x):
    return x * math.sin(10 * math.pi * x) + 1

# Función principal: búsqueda de ascensión de colinas
# Parámetros:
#   - f: función heurística a maximizar.
#   - pasos: número máximo de iteraciones.
#   - delta: tamaño del cambio entre vecinos.
# Devuelve:
#   - mejor solución encontrada y su valor.

def hill_climbing(f, pasos=1000, delta=0.01):
    # Generamos un punto inicial aleatorio entre 0 y 1
    actual = random.uniform(0, 1)
    valor_actual = f(actual)

    for i in range(pasos):
        # Generamos dos vecinos cercanos
        vecino1 = actual + random.uniform(-delta, delta)
        vecino2 = actual + random.uniform(-delta, delta)

        # Limitamos los valores dentro del rango permitido
        vecino1 = max(0, min(vecino1, 1))
        vecino2 = max(0, min(vecino2, 1))

        # Calculamos los valores heurísticos de los vecinos
        valor1 = f(vecino1)
        valor2 = f(vecino2)

        # Elegimos el mejor vecino
        mejor_vecino = vecino1 if valor1 > valor2 else vecino2
        mejor_valor = max(valor1, valor2)

        # Si el mejor vecino mejora la situación actual → nos movemos
        if mejor_valor > valor_actual:
            actual, valor_actual = mejor_vecino, mejor_valor
            print(f"Iteración {i}: nuevo mejor x={actual:.4f}, f(x)={valor_actual:.4f}")
        else:
            # Si no mejora, nos detenemos (óptimo local)
            print(f"Detenido en iteración {i}: óptimo local alcanzado.")
            break

    return actual, valor_actual

# BLOQUE PRINCIPAL

if __name__ == "__main__":
    print("\n BÚSQUEDA DE ASCENSIÓN DE COLINAS \n")
    mejor_x, mejor_valor = hill_climbing(funcion, pasos=200)
    print(f"\n Mejor solución encontrada: x={mejor_x:.4f}, f(x)={mejor_valor:.4f}")