def busqueda_profundidad_limitada(grafo, nodo, objetivo, limite, profundidad=0):
    print(f"Visitando: {nodo} (profundidad {profundidad})")

    # Si encontramos el objetivo
    if nodo == objetivo:
        print("¡Objetivo encontrado!")
        return [nodo]

    # Si alcanzamos el límite, no bajamos más
    if profundidad >= limite:
        return None

    # Exploramos los vecinos
    for vecino in grafo.get(nodo, []):
        resultado = busqueda_profundidad_limitada(grafo, vecino, objetivo, limite, profundidad + 1)
        if resultado:
            return [nodo] + resultado

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

# Probemos con límite 2
camino = busqueda_profundidad_limitada(grafo, 'A', 'G', limite=2)

if camino:
    print("\nCamino encontrado:", camino)
else:
    print("\nNo se encontró solución dentro del límite.")