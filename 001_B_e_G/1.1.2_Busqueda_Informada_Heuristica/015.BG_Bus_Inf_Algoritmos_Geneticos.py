# Descripción:
#   Simula la evolución biológica para optimizar una función objetivo.
#   Usa población, selección, cruzamiento y mutación.

import random
import math

# Función objetivo (a maximizar)
# f(x) = x * sin(10x) + 1

def funcion_objetivo(x):
    return x * math.sin(10 * x) + 1

# Generar un individuo (número entre 0 y 1)

def crear_individuo():
    return random.uniform(0, 1)

# Crear población inicial de N individuos

def crear_poblacion(n):
    return [crear_individuo() for _ in range(n)]

# Evaluar fitness de cada individuo
# (Mientras más alto, mejor)

def evaluar_poblacion(poblacion):
    return [funcion_objetivo(ind) for ind in poblacion]

# Selección: ruleta proporcional al fitness
# (probabilidad de ser elegido proporcional a su calidad)

def seleccion_ruleta(poblacion, fitness):
    total = sum(fitness)
    if total == 0:
        return random.choice(poblacion)
    probas = [f / total for f in fitness]
    return random.choices(poblacion, weights=probas, k=1)[0]

# Cruzamiento: combinación de genes de dos padres
# Aquí hacemos un promedio ponderado

def cruzamiento(padre1, padre2):
    alpha = random.random()
    hijo = alpha * padre1 + (1 - alpha) * padre2
    return max(0, min(1, hijo))  # asegurar que esté dentro [0,1]

# Mutación: alterar un gen con pequeña variación

def mutacion(individuo, tasa=0.1):
    if random.random() < tasa:
        individuo += random.uniform(-0.1, 0.1)
        individuo = max(0, min(1, individuo))
    return individuo

# Algoritmo genético principal

def algoritmo_genetico(
    tam_poblacion=10,
    generaciones=30,
    tasa_mutacion=0.1,
):
    # Inicializar población aleatoria
    poblacion = crear_poblacion(tam_poblacion)

    for gen in range(generaciones):
        fitness = evaluar_poblacion(poblacion)

        # Mostrar el mejor individuo de esta generación
        mejor = poblacion[fitness.index(max(fitness))]
        print(f"Gen {gen+1:02d} | Mejor x={mejor:.4f} | f(x)={max(fitness):.4f}")

        nueva_poblacion = []

        # Reproducción
        for _ in range(tam_poblacion):
            # Selección de padres
            padre1 = seleccion_ruleta(poblacion, fitness)
            padre2 = seleccion_ruleta(poblacion, fitness)

            # Cruzamiento
            hijo = cruzamiento(padre1, padre2)

            # Mutación
            hijo = mutacion(hijo, tasa_mutacion)

            nueva_poblacion.append(hijo)

        # Reemplazar población antigua por la nueva
        poblacion = nueva_poblacion

    # Evaluar la población final y devolver el mejor resultado
    fitness_final = evaluar_poblacion(poblacion)
    mejor = poblacion[fitness_final.index(max(fitness_final))]
    return mejor, max(fitness_final)

# BLOQUE PRINCIPAL

if __name__ == "__main__":
    print("\n ALGORITMO GENÉTICO \n")

    mejor_x, mejor_valor = algoritmo_genetico(
        tam_poblacion=10,
        generaciones=20,
        tasa_mutacion=0.1
    )

    print(f"\n Mejor individuo encontrado: x = {mejor_x:.4f}")
    print(f" Fitness máximo f(x): {mejor_valor:.4f}")