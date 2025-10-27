from collections import deque

def busqueda_bidireccional(grafo, inicio, meta):
    if inicio == meta:
        return [inicio]

    # Colas para cada dirección
    cola_inicio = deque([[inicio]])
    cola_meta = deque([[meta]])

    # Conjuntos de visitados
    visitados_inicio = {inicio}
    visitados_meta = {meta}

    # Rutas parciales
    padres_inicio = {inicio: None}
    padres_meta = {meta: None}

    while cola_inicio and cola_meta:
        # Expansión hacia adelante 
        ruta = cola_inicio.popleft()
        nodo = ruta[-1]
        for vecino in grafo.get(nodo, []):
            if vecino not in visitados_inicio:
                visitados_inicio.add(vecino)
                padres_inicio[vecino] = nodo
                nueva_ruta = list(ruta)
                nueva_ruta.append(vecino)
                cola_inicio.append(nueva_ruta)

            # Verificamos si se cruzan las búsquedas
            if vecino in visitados_meta:
                return construir_camino(padres_inicio, padres_meta, vecino)

        #  Expansión hacia atrás 
        ruta = cola_meta.popleft()
        nodo = ruta[-1]
        for vecino in grafo.get(nodo, []):
            if vecino not in visitados_meta:
                visitados_meta.add(vecino)
                padres_meta[vecino] = nodo
                nueva_ruta = list(ruta)
                nueva_ruta.append(vecino)
                cola_meta.append(nueva_ruta)

            if vecino in visitados_inicio:
                return construir_camino(padres_inicio, padres_meta, vecino)

    return None


def construir_camino(padres_inicio, padres_meta, punto_encuentro):
    # Reconstruimos el camino completo
    camino_inicio = []
    nodo = punto_encuentro
    while nodo is not None:
        camino_inicio.append(nodo)
        nodo = padres_inicio.get(nodo)
    camino_inicio.reverse()

    camino_meta = []
    nodo = padres_meta.get(punto_encuentro)
    while nodo is not None:
        camino_meta.append(nodo)
        nodo = padres_meta.get(nodo)

    return camino_inicio + camino_meta


#Ejemplo
grafo = {
    'A': ['B'],
    'B': ['A', 'C'],
    'C': ['B', 'D'],
    'D': ['C', 'E'],
    'E': ['D', 'F'],
    'F': ['E', 'G'],
    'G': ['F']
}

camino = busqueda_bidireccional(grafo, 'A', 'G')
print("Camino encontrado:", camino)