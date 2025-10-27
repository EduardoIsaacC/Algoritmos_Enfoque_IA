import heapq  # para la cola de prioridad

# Grafo con pesos (costos)
grafo = {
    'A': {'B': 1, 'C': 4, 'D': 3},
    'B': {'D': 2},
    'C': {'D': 1},
    'D': {'G': 5},
    'G': {}
}

def costo_uniforme(grafo, inicio, objetivo):
    # Cola de prioridad: (costo acumulado, ruta)
    cola = [(0, [inicio])]
    visitados = {}

    while cola:
        costo, ruta = heapq.heappop(cola)
        nodo = ruta[-1]

        # Si ya lo visitamos con un costo menor, lo ignoramos
        if nodo in visitados and visitados[nodo] <= costo:
            continue

        visitados[nodo] = costo
        print(f"Visitando: {nodo} con costo {costo}")

        if nodo == objetivo:
            print("¡Objetivo encontrado!")
            return ruta, costo

        for vecino, peso in grafo[nodo].items():
            nueva_ruta = list(ruta)
            nueva_ruta.append(vecino)
            heapq.heappush(cola, (costo + peso, nueva_ruta))

    return None, float('inf')

# Ejemplo de uso 
camino, costo = costo_uniforme(grafo, 'A', 'G')

print("\nCamino más barato:", camino)
print("Costo total:", costo)
