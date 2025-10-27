# Descripción:
#   Ejemplo simple de búsqueda estocástica de políticas.
#   El agente prueba políticas aleatorias y selecciona la mejor
#   según la recompensa promedio obtenida.

import random
import matplotlib.pyplot as plt

# Definimos un entorno simulado
# Política = probabilidad de elegir la acción "correcta"
# Recompensa = +1 si acierta, 0 si falla

def evaluar_politica(prob_correcta, intentos=100):
    recompensas = 0
    for _ in range(intentos):
        accion_correcta = random.random() < 0.7  # la acción "ideal" tiene 70% éxito
        accion_tomada = random.random() < prob_correcta
        if accion_tomada == accion_correcta:
            recompensas += 1
    return recompensas / intentos  # promedio de recompensas

# Parámetros de la búsqueda

iteraciones = 50
politicas = [random.random() for _ in range(iteraciones)]  # políticas aleatorias (0–1)
resultados = []

# Evaluar políticas y elegir la mejor

for p in politicas:
    resultado = evaluar_politica(p)
    resultados.append(resultado)
    print(f"Política probada (prob_correcta={p:.2f}) → Recompensa media: {resultado:.2f}")

mejor_indice = resultados.index(max(resultados))
mejor_politica = politicas[mejor_indice]
mejor_recompensa = resultados[mejor_indice]

print("\n MEJOR POLÍTICA ENCONTRADA ")
print(f"Probabilidad de acción correcta: {mejor_politica:.2f}")
print(f"Recompensa promedio: {mejor_recompensa:.2f}")

# Graficar evolución de la búsqueda

plt.figure(figsize=(8,4))
plt.plot(resultados, marker="o")
plt.axhline(max(resultados), color="green", linestyle="--", label="Mejor política encontrada")
plt.title("Búsqueda Estocástica de Política")
plt.xlabel("Iteración (política probada)")
plt.ylabel("Recompensa promedio")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()