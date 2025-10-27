# BÚSQUEDA TABÚ (Tabu Search)
# Autor: Eduardo (Enfoque IA)
#
# Descripción:
#   Heurística de búsqueda local con memoria.
#   Intenta mejorar una solución iterativamente, evitando ciclos
#   mediante una "lista tabú" de movimientos prohibidos temporalmente.

import random

# Función de costo:
# Dada una ruta (lista de números), calculamos un "costo".
# En un caso real esto sería, por ejemplo, la distancia total
# recorrida al visitar las ciudades en ese orden.
# Aquí inventamos una matriz de distancias simétrica pequeña.

distancias = [
    #   0   1   2   3   4
    [  0, 10, 15, 20, 18],  # desde 0
    [ 10,  0, 35, 25, 17],  # desde 1
    [ 15, 35,  0, 30, 28],  # desde 2
    [ 20, 25, 30,  0, 22],  # desde 3
    [ 18, 17, 28, 22,  0]   # desde 4
]

def costo_ruta(ruta):
    """
    Calcula el costo total de recorrer la ruta en orden.
    Suma las distancias consecutivas.
    """
    costo_total = 0
    for i in range(len(ruta) - 1):
        a = ruta[i]
        b = ruta[i + 1]
        costo_total += distancias[a][b]
    return costo_total

# Generar vecinos:
# Dada una ruta, generamos vecinos intercambiando dos posiciones.
# También devolvemos el "movimiento" (i, j) que hicimos, para
# poder marcarlo como tabú.

def generar_vecinos(ruta):
    vecinos = []
    n = len(ruta)
    for i in range(n):
        for j in range(i + 1, n):
            nueva = ruta.copy()
            # swap (intercambio de dos ciudades)
            nueva[i], nueva[j] = nueva[j], nueva[i]
            movimiento = (ruta[i], ruta[j])  # qué intercambié
            vecinos.append((nueva, movimiento))
    return vecinos

# Búsqueda Tabú
# Parámetros:
#   - ruta_inicial: lista inicial, por ejemplo [0,1,2,3,4]
#   - iter_max: cuántas iteraciones intentamos
#   - tabu_tam: tamaño máximo de la lista tabú (memoria)
# Devuelve:
#   - mejor_ruta_global
#   - mejor_costo_global

def busqueda_tabu(ruta_inicial, iter_max=100, tabu_tam=5):
    # Solución actual
    actual = ruta_inicial[:]
    costo_actual = costo_ruta(actual)

    # Mejor solución encontrada hasta ahora (global)
    mejor_global = actual[:]
    mejor_costo_global = costo_actual

    # Lista tabú: recordamos últimos movimientos prohibidos
    lista_tabu = []

    for it in range(iter_max):
        vecinos = generar_vecinos(actual)

        # Evaluamos cada vecino:
        # - Si su movimiento está en tabú, lo saltamos (en general).
        # - Pero si ese vecino es MEJOR que el mejor global, lo permitimos
        #   (regla de aspiración).

        mejor_vecino = None
        mejor_costo_vecino = float('inf')
        mejor_mov = None

        for ruta_candidata, mov in vecinos:
            c = costo_ruta(ruta_candidata)

            # Regla tabú:
            if mov in lista_tabu and c >= mejor_costo_global:
                # movimiento tabú y no mejora lo mejor global → lo brincamos
                continue

            # Guardar al mejor candidato de esta iteración
            if c < mejor_costo_vecino:
                mejor_vecino = ruta_candidata
                mejor_costo_vecino = c
                mejor_mov = mov

        # Si no encontramos vecino válido (extremadamente raro), paramos
        if mejor_vecino is None:
            print("Sin movimientos válidos, deteniendo.")
            break

        # Aplicamos el mejor vecino encontrado
        actual = mejor_vecino
        costo_actual = mejor_costo_vecino

        # Actualizamos memoria tabú:
        lista_tabu.append(mejor_mov)
        # Si la lista tabú se pasa de tamaño, sacamos el más viejo
        if len(lista_tabu) > tabu_tam:
            lista_tabu.pop(0)

        # Revisamos si mejoró la mejor solución global
        if costo_actual < mejor_costo_global:
            mejor_global = actual[:]
            mejor_costo_global = costo_actual

        # Mostramos trazas de la iteración
        print(f"Iter {it}: ruta={actual} costo={costo_actual} tabu={lista_tabu}")

    return mejor_global, mejor_costo_global

# Bloque principal de demostración

if __name__ == "__main__":
    print("\nBÚSQUEDA TABÚ ")

    # Creamos una ruta inicial aleatoria, por ejemplo visitar 5 nodos [0..4]
    ruta_inicial = [0, 1, 2, 3, 4]
    random.shuffle(ruta_inicial)

    print("Ruta inicial:", ruta_inicial, "Costo:", costo_ruta(ruta_inicial))

    mejor_ruta, mejor_costo = busqueda_tabu(
        ruta_inicial,
        iter_max=30,   # número de iteraciones de mejora
        tabu_tam=5     # memoria tabú
    )

    print("\n Mejor ruta encontrada:", mejor_ruta)
    print(" Costo de esa ruta:", mejor_costo)
