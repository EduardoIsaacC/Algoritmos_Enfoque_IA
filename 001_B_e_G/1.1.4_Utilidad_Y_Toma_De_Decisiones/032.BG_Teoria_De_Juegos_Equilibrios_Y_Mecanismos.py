# Descripción:
#   - Modela el Dilema del Prisionero (juego 2x2).
#   - Encuentra equilibrios de Nash.
#   - Muestra la matriz de pagos en texto.
#   - Genera un mapa de calor con matplotlib para ilustrar resultados.
#   El heatmap:
#     Cada celda = una combinación de estrategias (A,B)
#     El color representa la "suma de utilidades" A+B
#     El texto dentro muestra utilidad individual: (uA, uB)
#     Se marca con un recuadro la(s) celda(s) que son equilibrio de Nash

import itertools
import matplotlib.pyplot as plt
import numpy as np

# Definición del juego

jugadores = ["A", "B"]
estrategias = ["Coopera", "Traiciona"]

# Matriz de pagos: (estrategia_A, estrategia_B) -> (u_A, u_B)
pagos = {
    ("Coopera", "Coopera"): (-1, -1),
    ("Coopera", "Traiciona"): (-10, 0),
    ("Traiciona", "Coopera"): (0, -10),
    ("Traiciona", "Traiciona"): (-5, -5),
}

# Función para detectar equilibrio de Nash

def es_equilibrio_nash(a_estrategia, b_estrategia):
    u_a, u_b = pagos[(a_estrategia, b_estrategia)]

    # ¿Puede A mejorar cambiando solo él?
    mejor_a = max(pagos[(a_alt, b_estrategia)][0] for a_alt in estrategias)
    a_estable = (u_a == mejor_a)

    # ¿Puede B mejorar cambiando solo él?
    mejor_b = max(pagos[(a_estrategia, b_alt)][1] for b_alt in estrategias)
    b_estable = (u_b == mejor_b)

    return a_estable and b_estable

# Encuentra todas las combinaciones que son equilibrio de Nash
equilibrios = []
for a, b in itertools.product(estrategias, estrategias):
    if es_equilibrio_nash(a, b):
        equilibrios.append((a, b))

# Mostrar en texto para la terminal (útil para parcial/video)

print("\n TEORÍA DE JUEGOS: Equilibrio de Nash \n")

if equilibrios:
    for (a, b) in equilibrios:
        print(f"Equilibrio de Nash: (A={a}, B={b}) | Pagos = {pagos[(a,b)]}")
else:
    print("No hay equilibrio de Nash puro.")

print("\n Matriz de Pagos (uA, uB) ")
for a, b in itertools.product(estrategias, estrategias):
    print(f"A={a:9s} | B={b:9s} -> {pagos[(a,b)]}")
print()

# Preparar datos numéricos para la visualización
# Creamos una matriz 2x2 con la suma de utilidades (uA + uB) para cada par.
# Orden de filas: estrategia de A (Coopera, Traiciona)
# Orden de columnas: estrategia de B (Coopera, Traiciona)

suma_utilidades = np.zeros((len(estrategias), len(estrategias)))
texto_celdas = [["" for _ in estrategias] for _ in estrategias]
mask_equilibrio = np.zeros_like(suma_utilidades, dtype=bool)

for i, a in enumerate(estrategias):
    for j, b in enumerate(estrategias):
        u_a, u_b = pagos[(a, b)]
        suma_utilidades[i, j] = u_a + u_b
        texto_celdas[i][j] = f"A:{u_a}\nB:{u_b}"

        if (a, b) in equilibrios:
            mask_equilibrio[i, j] = True

# Graficar Heatmap

fig, ax = plt.subplots(figsize=(6, 5))

# Mostrar la matriz de suma de utilidades como colores
im = ax.imshow(suma_utilidades, cmap="coolwarm")

# Etiquetas de ejes
ax.set_xticks(range(len(estrategias)))
ax.set_yticks(range(len(estrategias)))
ax.set_xticklabels([f"B:{b}" for b in estrategias])
ax.set_yticklabels([f"A:{a}" for a in estrategias])

ax.set_title("Dilema del Prisionero\nMapa de Calor (A+B)\n")

# Escribir las utilidades individuales (uA, uB) dentro de cada celda
for i in range(len(estrategias)):
    for j in range(len(estrategias)):
        ax.text(
            j,
            i,
            texto_celdas[i][j],
            ha="center",
            va="center",
            fontsize=10,
            color="black",
            fontweight="bold"
        )

# Agregar recuadro alrededor de las celdas que son equilibrio de Nash
for i in range(len(estrategias)):
    for j in range(len(estrategias)):
        if mask_equilibrio[i, j]:
            # Dibujamos un rectángulo alrededor de esa celda
            rect = plt.Rectangle(
                (j - 0.5, i - 0.5),
                1, 1,
                fill=False,
                edgecolor="lime",
                linewidth=3
            )
            ax.add_patch(rect)

# Barra de color (legendita de cuán buena es la suma total)
cbar = plt.colorbar(im)
cbar.set_label("uA + uB (bienestar conjunto)")

plt.tight_layout()
plt.show()