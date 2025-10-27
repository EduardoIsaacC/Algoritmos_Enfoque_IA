# Descripción:
#   Simula un agente que explora un entorno parcialmente desconocido.
#   Aprende los costos del entorno y actualiza su heurística en tiempo real.

import random

# Crear un entorno (laberinto) como matriz
# 0 = espacio libre, 1 = obstáculo

def crear_mapa(ancho, alto, obstaculos=0.2):
    mapa = []
    for _ in range(alto):
        fila = []
        for _ in range(ancho):
            if random.random() < obstaculos:
                fila.append(1)
            else:
                fila.append(0)
        mapa.append(fila)
    return mapa

# Mostrar el mapa

def mostrar_mapa(mapa, agente=None, meta=None):
    for y, fila in enumerate(mapa):
        linea = ""
        for x, celda in enumerate(fila):
            if agente == (x, y):
                linea += "🤖"
            elif meta == (x, y):
                linea += "🏁"
            elif celda == 1:
                linea += "⬛"
            else:
                linea += "⬜"
        print(linea)
    print()

# Heurística simple: distancia Manhattan a la meta

def heuristica(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# Búsqueda Online (tipo LRTA*)

def busqueda_online(mapa, inicio, meta, max_pasos=100):
    # Inicializamos heurística conocida (se irá aprendiendo)
    H = {}
    actual = inicio

    for paso in range(max_pasos):
        mostrar_mapa(mapa, agente=actual, meta=meta)

        # Si llegamos a la meta → fin
        if actual == meta:
            print(f" Meta alcanzada en {paso} pasos!")
            return

        # Generar vecinos válidos (no salir del mapa ni cruzar muros)
        vecinos = []
        movimientos = [(1,0),(-1,0),(0,1),(0,-1)]
        for dx, dy in movimientos:
            nx, ny = actual[0]+dx, actual[1]+dy
            if 0 <= nx < len(mapa[0]) and 0 <= ny < len(mapa) and mapa[ny][nx] == 0:
                vecinos.append((nx, ny))

        if not vecinos:
            print(" Sin movimientos posibles, atascado.")
            return

        # Estimar heurísticas para vecinos (o inicializar)
        for v in vecinos:
            if v not in H:
                H[v] = heuristica(v, meta)

        # Elegir el vecino con menor (1 + H(v))
        # (1 representa el costo de moverse)
        siguiente = min(vecinos, key=lambda v: 1 + H[v])

        # Actualizar heurística del nodo actual
        # "Aprende" que su costo real es 1 + el de su mejor vecino
        H[actual] = 1 + H[siguiente]

        # Mover al siguiente nodo
        actual = siguiente

    print(" Límite de pasos alcanzado, meta no encontrada.")

# BLOQUE PRINCIPAL

if __name__ == "__main__":
    print("\n BÚSQUEDA ONLINE (LRTA*) \n")

    ancho, alto = 8, 6
    mapa = crear_mapa(ancho, alto, obstaculos=0.2)

    inicio = (0, 0)
    meta = (7, 5)

    mostrar_mapa(mapa, agente=inicio, meta=meta)
    busqueda_online(mapa, inicio, meta, max_pasos=50)
