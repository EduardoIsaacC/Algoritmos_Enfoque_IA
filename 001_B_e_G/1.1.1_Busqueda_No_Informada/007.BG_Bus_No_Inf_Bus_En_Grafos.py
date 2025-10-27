from collections import deque  # Importa deque para usar colas eficientes

# Función principal: búsqueda en grafos genérica
def busqueda_en_grafo(problema, inicio, objetivo, tipo="anchura"):
    """
    Realiza búsqueda en grafos (BFS o DFS).
    Parámetros:
        - problema: diccionario con los nodos y sus conexiones.
        - inicio: nodo inicial.
        - objetivo: nodo meta a alcanzar.
        - tipo: "anchura" (BFS) o "profundidad" (DFS).
    Devuelve la ruta si se encuentra el objetivo.
    """

    # Selecciona la estructura de frontera según el tipo
    if tipo == "anchura":
        frontera = deque([[inicio]])  # Cola (BFS) -> saca por la izquierda
    else:
        frontera = [[inicio]]         # Pila (DFS) -> saca por el final

    visitados = set()  # Conjunto para registrar los nodos ya visitados

    # Mientras haya rutas por explorar en la frontera
    while frontera:
        # Extrae la siguiente ruta dependiendo del tipo de búsqueda
        if tipo == "anchura":
            ruta = frontera.popleft()   # Saca el primer elemento (cola FIFO)
        else:
            ruta = frontera.pop()       # Saca el último (pila LIFO)

        nodo = ruta[-1]  # Último nodo en la ruta actual

        # Si ya visitamos el nodo, lo ignoramos
        if nodo in visitados:
            continue
        visitados.add(nodo)  # Marcamos el nodo como visitado

        print(f"Visitando: {nodo}")  # Muestra el progreso

        # Si encontramos el objetivo, devolvemos la ruta completa
        if nodo == objetivo:
            print("¡Objetivo encontrado!")
            return ruta

        # Expande los vecinos del nodo actual
        for vecino in problema.get(nodo, []):
            nueva_ruta = list(ruta)     # Copiamos la ruta actual
            nueva_ruta.append(vecino)   # Agregamos el vecino al final
            frontera.append(nueva_ruta) # Guardamos la nueva ruta en la frontera

    # Si se termina la frontera sin encontrar el objetivo
    return None


# Bloque principal: se ejecuta solo al correr el script
if __name__ == "__main__":
    # Definimos un grafo simple (no dirigido)
    grafo = {
        'A': ['B', 'C'],   # A conecta con B y C
        'B': ['A', 'D', 'E'],
        'C': ['A', 'E'],
        'D': ['B'],
        'E': ['B', 'C', 'F'],
        'F': ['E'],
        'G': ['F']         # G conectado con F
    }

    inicio = 'A'       # Nodo de partida
    objetivo = 'G'     # Nodo meta

    # Búsqueda en Anchura (BFS) 
    print("\n Búsqueda en Anchura (BFS) ")
    ruta_bfs = busqueda_en_grafo(grafo, inicio, objetivo, tipo="anchura")
    print("Ruta BFS encontrada:", ruta_bfs)

    #  Búsqueda en Profundidad (DFS) 
    print("\n Búsqueda en Profundidad (DFS) ")
    ruta_dfs = busqueda_en_grafo(grafo, inicio, objetivo, tipo="profundidad")
    print("Ruta DFS encontrada:", ruta_dfs)