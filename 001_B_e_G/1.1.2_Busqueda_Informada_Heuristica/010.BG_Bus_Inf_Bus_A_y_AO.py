# OBJETIVO:
#   Mostrar dos algoritmos de búsqueda informada:
#   1) A*  -> busca la ruta óptima en un grafo normal (camino secuencial).
#   2) AO* -> busca el plan óptimo en un grafo AND-OR (subtareas combinadas).
# DIFERENCIA CLAVE:
#   - A* asume que la solución es UN camino desde inicio hasta meta.
#   - AO* asume que la solución puede ser un CONJUNTO de pasos que
#     incluyen decisiones OR ("elige una opción") y pasos AND
#     ("tienes que hacer TODAS estas subtareas").
# NOTA:
#   Ambos usan heurísticas (estimaciones), pero las aplican en
#   estructuras distintas.

import heapq   # usado en A* para manejar la frontera como cola de prioridad
import math    # reservado por si quieres usar heurísticas más complejas

# PARTE 1: ALGORITMO A*

# Grafo dirigido con costos reales entre nodos.
# Aquí estamos modelando el clásico ejemplo de ciudades (tipo Rumania).
grafo_a_estrella = {
    'Arad': {'Sibiu': 140, 'Timisoara': 118, 'Zerind': 75},
    'Sibiu': {'Arad': 140, 'Fagaras': 99, 'Rimnicu Vilcea': 80},
    'Timisoara': {'Arad': 118},
    'Zerind': {'Arad': 75},
    'Fagaras': {'Sibiu': 99, 'Bucarest': 211},
    'Rimnicu Vilcea': {'Sibiu': 80, 'Pitesti': 97},
    'Pitesti': {'Rimnicu Vilcea': 97, 'Bucarest': 101},
    'Bucarest': {}
}

# Heurística h(n): "distancia estimada a la meta".
# Esta heurística debe ser optimista (no sobrestimar) para que A* sea óptimo.
heuristica = {
    'Arad': 366,
    'Sibiu': 253,
    'Timisoara': 329,
    'Zerind': 374,
    'Fagaras': 176,
    'Rimnicu Vilcea': 193,
    'Pitesti': 100,
    'Bucarest': 0
}

def busqueda_A_estrella(grafo, inicio, objetivo):
    """
    Implementación del algoritmo A*.
    Selecciona siempre expandir el nodo con menor f(n),
    donde f(n) = g(n) + h(n).

    grafo: diccionario {nodo: {vecino: costo_real, ...}}
    inicio: nodo inicial (ej. 'Arad')
    objetivo: nodo meta (ej. 'Bucarest')

    return: (ruta, costo_total)
    """

    # frontera es una cola de prioridad con elementos:
    # (f_total_estimado, g_acumulado_real, ruta_completa_hasta_ahora)
    frontera = []

    # Insertamos el punto inicial:
    # g = 0 (todavía no hemos viajado)
    # f = g + h(inicio) = 0 + heuristica[inicio]
    heapq.heappush(frontera, (heuristica[inicio], 0, [inicio]))

    visitados = set()  # Para no expandir el mismo nodo varias veces

    while frontera:
        # Sacamos la ruta más prometedora (la de menor f)
        f_actual, g_actual, ruta_actual = heapq.heappop(frontera)
        nodo_actual = ruta_actual[-1]  # Última ciudad de la ruta

        # Mensaje de depuración / explicación
        print(f"[A*] Visitando: {nodo_actual} (g={g_actual}, h={heuristica[nodo_actual]}, f={f_actual})")

        # ¿Ya llegamos a la meta?
        if nodo_actual == objetivo:
            print("[A*] ¡Objetivo encontrado!")
            return ruta_actual, g_actual  # ruta óptima y su costo real

        # Si ya lo habíamos visto antes, saltamos
        if nodo_actual in visitados:
            continue
        visitados.add(nodo_actual)

        # Expandimos todos los vecinos
        for vecino, costo in grafo[nodo_actual].items():
            if vecino not in visitados:
                # g(nuevo) = costo real acumulado hasta el vecino
                nuevo_g = g_actual + costo

                # f(nuevo) = g(nuevo) + h(nuevo)
                nuevo_f = nuevo_g + heuristica[vecino]

                # extendemos la ruta con el nuevo nodo
                nueva_ruta = list(ruta_actual)
                nueva_ruta.append(vecino)

                # Guardamos esta opción en la frontera
                heapq.heappush(frontera, (nuevo_f, nuevo_g, nueva_ruta))

    # Si se vacía la frontera sin llegar, no hay solución válida
    return None, None

# PARTE 2: ALGORITMO AO* (simplificado educativo)

# Aquí modelamos un problema AND-OR.
#
# Estructura:
#   Cada meta puede resolverse con uno o más "planes".
#   Un plan puede ser de tipo:
#   - "OR": basta con hacer esa acción/ submeta
#   - "AND": tienes que completar TODAS las subacciones listadas
#
# Cada subacción tiene un costo asociado (si es terminal).
#
# Ejemplo:
#   META
#    ├─ PlanA (OR): haz solo A, cuesta 7
#    └─ PlanB (AND): haz B1 y B2, cuestan 3 y 2 → total 5
#
# AO* debe elegir el plan completo más barato (PlanB en este caso).

problema_and_or = {
    "META": [
        {"tipo": "OR",  "acciones": ["PlanA"]},
        {"tipo": "AND", "acciones": ["PlanB1", "PlanB2"]}
    ],

    # PlanA es una solución directa con costo 7
    "PlanA": [
        {"tipo": "OR", "acciones": [], "costo": 7}
    ],

    # PlanB1 y PlanB2 son sub-tareas que también tienen costo directo
    "PlanB1": [
        {"tipo": "OR", "acciones": [], "costo": 3}
    ],
    "PlanB2": [
        {"tipo": "OR", "acciones": [], "costo": 2}
    ]
}

def costo_de_plan(nodo, plan, memo):
    """
    Calcula el costo total de seguir 'plan' para resolver 'nodo'.

    nodo: (string) nombre de la meta (por claridad semántica)
    plan: (dict) con llaves:
          - "tipo": "OR" o "AND"
          - "acciones": lista de sub-acciones requeridas
          - "costo" (opcional): costo directo si ya es terminal
    memo: diccionario usado como caché para no recalcular costos

    return: costo numérico total de ese plan
    """
    # Caso 1: plan OR con costo directo. Ej: PlanA cuesta 7
    if plan["tipo"] == "OR" and "costo" in plan:
        return plan["costo"]

    # Caso 2: plan OR que NO tiene costo directo,
    # pero apunta a otra submeta ("acciones": ["PlanA"])
    # Aquí tomamos el costo mínimo de esa submeta.
    if plan["tipo"] == "OR" and plan["acciones"]:
        subaccion = plan["acciones"][0]  # elegimos esa sub-acción
        return costo_minimo(subaccion, memo)

    # Caso 3: plan AND.
    # Se deben cumplir TODAS las sub-acciones listadas.
    # El costo total es la SUMA de resolver cada sub-acción.
    if plan["tipo"] == "AND":
        total = 0
        for subaccion in plan["acciones"]:
            total += costo_minimo(subaccion, memo)
        return total

    # Si algo está mal definido, devolvemos infinito (irrealizable).
    return float('inf')


def costo_minimo(nodo, memo=None):
    """
    Devuelve el costo mínimo necesario para cumplir la meta 'nodo',
    evaluando todos los planes posibles y escogiendo el más barato.

    nodo: string, como "META", "PlanA", etc.
    memo: caché de resultados ya calculados {nodo: costo_minimo}

    return: costo numérico más bajo para lograr 'nodo'
    """
    if memo is None:
        memo = {}

    # Si ya calculamos antes este nodo, reuse
    if nodo in memo:
        return memo[nodo]

    planes = problema_and_or.get(nodo, [])

    if not planes:
        # No hay forma de lograr este nodo
        memo[nodo] = float('inf')
        return memo[nodo]

    # Calculamos el costo total de cada plan alternativo
    # y luego elegimos el más barato.
    costos_posibles = []
    for plan in planes:
        c = costo_de_plan(nodo, plan, memo)
        costos_posibles.append(c)

    mejor_costo = min(costos_posibles)
    memo[nodo] = mejor_costo
    return mejor_costo

# BLOQUE PRINCIPAL (DEMO DE AMBOS ALGORITMOS)

if __name__ == "__main__":
    print(" DEMOSTRACIÓN CONJUNTA: A* y AO*")

    # --- A* ---
    print(">>> EJECUTANDO A* (ruta en mapa)\n")
    ruta_optima, costo_total = busqueda_A_estrella(
        grafo_a_estrella,
        inicio='Arad',
        objetivo='Bucarest'
    )
    print("\n[A*] Ruta óptima encontrada:", ruta_optima)
    print("[A*] Costo total real:", costo_total)

    # AO*
    print(">>> EJECUTANDO AO* (plan AND-OR)\n")
    costo_meta = costo_minimo("META")
    print(f"[AO*] Costo mínimo para lograr META:", costo_meta)

    # Interpretación pedagógica:
    # En este problema:
    #   META puede lograrse con PlanA (costo=7)
    #   o con PlanB1+PlanB2 (costo=3+2=5)
    # AO* debe escoger la combinación más barata.
    print("[AO*] Interpretación: se prefiere 'PlanB1 + PlanB2' sobre 'PlanA'")
    print("[AO*] porque 5 < 7 (más barato resolver las subtareas combinadas).")