import heapq

# Grafo de conexiones con sus costos reales (no usados directamente aquí)
grafo = {
    'Arad': {'Sibiu': 140, 'Timisoara': 118, 'Zerind': 75},
    'Sibiu': {'Arad': 140, 'Fagaras': 99, 'Rimnicu Vilcea': 80},
    'Timisoara': {'Arad': 118},
    'Zerind': {'Arad': 75},
    'Fagaras': {'Sibiu': 99, 'Bucarest': 211},
    'Rimnicu Vilcea': {'Sibiu': 80, 'Pitesti': 97},
    'Pitesti': {'Rimnicu Vilcea': 97, 'Bucarest': 101},
    'Bucarest': {}
}

# Heurística: distancia en línea recta a Bucarest
h = {
    'Arad': 366,
    'Sibiu': 253,
    'Timisoara': 329,
    'Zerind': 374,
    'Fagaras': 176,
    'Rimnicu Vilcea': 193,
    'Pitesti': 100,
    'Bucarest': 0
}

def busqueda_voraz(grafo, inicio, objetivo):
    frontera = []  # Cola de prioridad
    heapq.heappush(frontera, (h[inicio], [inicio]))  # (heurística, ruta)
    visitados = set()

    while frontera:
        heuristica_actual, ruta = heapq.heappop(frontera)
        nodo = ruta[-1]

        print(f"Visitando: {nodo} (h={heuristica_actual})")

        if nodo == objetivo:
            print("¡Objetivo encontrado!")
            return ruta

        visitados.add(nodo)

        for vecino in grafo[nodo]:
            if vecino not in visitados:
                nueva_ruta = list(ruta)
                nueva_ruta.append(vecino)
                heapq.heappush(frontera, (h[vecino], nueva_ruta))

    return None


# Ejemplo de uso 
if __name__ == "__main__":
    inicio = 'Arad'
    objetivo = 'Bucarest'

    ruta = busqueda_voraz(grafo, inicio, objetivo)
    print("\nRuta encontrada:", ruta)