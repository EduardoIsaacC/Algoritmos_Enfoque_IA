import random
import math

#  Distribución Discreta 
print(" Distribución Discreta: Lanzar un dado ")

valores = [1, 2, 3, 4, 5, 6]
probabilidades = [1/6] * 6  # Dado justo

print(f"Suma total de probabilidades: {sum(probabilidades):.2f}")

for i in range(1, 11):
    lanzamiento = random.choices(valores, weights=probabilidades)[0]  # <-- Corregido
    print(f"Lanzamiento {i:02d}: {lanzamiento}")

# Distribución Continua
print("\n Distribución Continua: Altura simulada (Normal) ")

media = 170
desviacion = 10

def f_normal(x):
    return (1 / (desviacion * math.sqrt(2 * math.pi))) * \
           math.exp(-0.5 * ((x - media) / desviacion) ** 2)

for x in [150, 160, 170, 180, 190]:
    print(f"f({x}) = {f_normal(x):.5f}")

print("\nNota: En una distribución continua, la 'probabilidad exacta' de un valor es 0.")
print("La función f(x) indica qué tan probable es estar CERCA de ese valor.")