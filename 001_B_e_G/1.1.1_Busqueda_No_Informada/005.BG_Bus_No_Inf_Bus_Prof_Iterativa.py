#Búsqueda en profundidad limitada
def busqueda_profundidad_limitada(grafo, nodo, objetivo, limite, profundidad=0):
    if nodo == objetivo:
        return [nodo]
    if profundidad >= limite:
        return None

    for vecino in grafo.get(nodo, []):
        resultado = busqueda_profundidad_limitada(grafo, vecino, objetivo, limite, profundidad + 1)
        if resultado:
            return [nodo] + resultado

    return None


#Búsqueda en profundidad iterativa
def busqueda_profundidad_iterativa(grafo, inicio, objetivo, limite_max):
    for limite in range(limite_max + 1):
        print(f"\n🔹 Iteración con límite = {limite}")
        resultado = busqueda_profundidad_limitada(grafo, inicio, objetivo, limite)
        if resultado:
            print("¡Objetivo encontrado!")
            return resultado
    print("No se encontró el objetivo dentro del límite máximo.")
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

camino = busqueda_profundidad_iterativa(grafo, 'A', 'G', limite_max=5)
print("\nCamino encontrado:", camino)