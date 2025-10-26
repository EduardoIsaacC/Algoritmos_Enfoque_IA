def busqueda_profundidad(grafo, inicio, objetivo):
    # pila de rutas completas
    pila = [[inicio]]
    visitados = set()

    while pila:
        # sacamos la última ruta agregada (LIFO)
        ruta = pila.pop()
        nodo = ruta[-1]

        if nodo in visitados:
            continue

        visitados.add(nodo)
        print(f"Visitando: {nodo}")

        # si encontramos el objetivo
        if nodo == objetivo:
            print("¡Objetivo encontrado!")
            return ruta

        # agregamos los vecinos a la pila
        for vecino in grafo.get(nodo, []):
            nueva_ruta = list(ruta)
            nueva_ruta.append(vecino)
            pila.append(nueva_ruta)

    return None


# Ejemplo
grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}

camino = busqueda_profundidad(grafo, 'A', 'G')
print("\nCamino encontrado:", camino)