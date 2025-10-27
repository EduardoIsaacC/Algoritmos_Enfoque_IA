import heapq  # para cola de prioridad

# Grafo de conexiones (costo real entre nodos)
grafo = {
    'Arad': {'Sibiu': 140, 'Timisoara': 118},
    'Sibiu': {'Arad': 140, 'Fagaras': 99, 'Pitesti': 80},
    'Fagaras': {'Sibiu': 99, 'Bucarest': 211},
    'Pitesti': {'Sibiu': 80, 'Bucarest': 101},
    'Timisoara': {'Arad': 118},
    'Bucarest': {}
}

# Heurística: distancia en línea recta aproximada a Bucarest
heuristica = {
    'Arad': 366,
    'Sibiu': 253,
    'Fagaras': 176,
    'Pitesti': 100,
    'Timisoara': 329,
    'Bucarest': 0
}

def expandir_por_heuristica(nodo_actual):
    # Tomamos los vecinos y los ordenamos por h(n)
    vecinos = grafo[nodo_actual].keys()
    vecinos_ordenados = sorted(vecinos, key=lambda v: heuristica[v])
    return vecinos_ordenados

# Ejemplo: estoy parado en Arad, ¿a dónde parece "mejor" ir?
print("Estoy en Arad.")
print("Vecinos posibles:", list(grafo['Arad'].keys()))
print("Valores h(n):")
for v in grafo['Arad'].keys():
    print(f"  {v}: h={heuristica[v]}")

print("\nOrden sugerido por la heurística (de más prometedor a menos):")
print(expandir_por_heuristica("Arad")) 