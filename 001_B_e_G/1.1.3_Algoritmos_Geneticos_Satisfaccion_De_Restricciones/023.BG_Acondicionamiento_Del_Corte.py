# Descripción:
#   Divide un problema CSP en subproblemas más simples al eliminar
#   un conjunto de variables "cutset" que conectan las demás partes.

import itertools

# VARIABLES Y DOMINIOS

variables = ["A", "B", "C", "D", "E"]

dominios = {
    "A": ["Rojo", "Verde"],
    "B": ["Rojo", "Verde"],
    "C": ["Rojo", "Verde"],
    "D": ["Rojo", "Verde"],
    "E": ["Rojo", "Verde"]
}

# Restricciones (arcos del grafo)
restricciones = [
    ("A", "B"), ("A", "C"),
    ("B", "D"),
    ("C", "E")
]

# Verificar si una asignación parcial cumple restricciones

def es_consistente(asignacion, var, valor):
    for (x, y) in restricciones:
        if x == var and y in asignacion and asignacion[y] == valor:
            return False
        if y == var and x in asignacion and asignacion[x] == valor:
            return False
    return True

# Resolver un subproblema con Backtracking

def backtracking(asignacion, sub_vars):
    if len(asignacion) == len(sub_vars):
        return asignacion

    var = [v for v in sub_vars if v not in asignacion][0]
    for valor in dominios[var]:
        if es_consistente(asignacion, var, valor):
            asignacion[var] = valor
            resultado = backtracking(asignacion, sub_vars)
            if resultado:
                return resultado
            del asignacion[var]
    return None

# Acondicionamiento del corte

def cutset_conditioning(cutset):
    soluciones = []

    # 1️⃣ Todas las combinaciones posibles de valores para el cutset
    valores_cutset = [dominios[v] for v in cutset]
    for combinacion in itertools.product(*valores_cutset):
        asignacion_cut = dict(zip(cutset, combinacion))
        print(f"\n Probando cutset {asignacion_cut}")

        # 2️⃣ Variables restantes (subproblema)
        sub_vars = [v for v in variables if v not in cutset]

        # 3️⃣ Resolver subproblema dado el cutset fijo
        resultado = backtracking(asignacion_cut.copy(), sub_vars)
        if resultado:
            soluciones.append(resultado)

    return soluciones

# BLOQUE PRINCIPAL

if __name__ == "__main__":
    print("\n ACONDICIONAMIENTO DEL CORTE (Cutset Conditioning) \n")

    cutset = ["A"]  # variable que desconecta el grafo
    soluciones = cutset_conditioning(cutset)

    if soluciones:
        print("\n Soluciones encontradas:")
        for sol in soluciones:
            print(sol)
    else:
        print("\n No se encontraron soluciones.")