from collections import deque

#Grafo representado como un diccionario
# Cada clave es un nodo y su valor es la lista de vecinos
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'E'],
    'D': ['B', 'G'],
    'E': ['B', 'C', 'F'],
    'F': ['E'],
    'G': ['D']
}

# Algoritmo de Búsqueda en Anchura
def busqueda_anchura(grafo, inicio, objetivo):
    # Cola (FIFO) que almacena rutas completas
    cola = deque([[inicio]])
    # Conjunto de nodos visitados
    visitados = set()

    while cola:
        # Extraemos la primera ruta de la cola
        ruta = cola.popleft()
        nodo = ruta[-1]  # Último nodo de la ruta actual

        # Si ya visitamos el nodo, lo ignoramos
        if nodo in visitados:
            continue

        # Marcamos el nodo como visitado
        visitados.add(nodo)
        print(f"Visitando: {nodo}")

        # Si encontramos el objetivo, devolvemos la ruta
        if nodo == objetivo:
            print("¡Objetivo encontrado!")
            return ruta

        # Agregamos las rutas con los vecinos del nodo actual
        for vecino in grafo[nodo]:
            nueva_ruta = list(ruta)
            nueva_ruta.append(vecino)
            cola.append(nueva_ruta)

    return None  # Si no hay camino

# Ejemplo de uso 
inicio = 'A'
objetivo = 'G'
camino = busqueda_anchura(grafo, inicio, objetivo)

print("\nCamino encontrado:", camino)