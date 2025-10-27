# Descripción:
#   Versión avanzada del algoritmo de backtracking para CSP.
#   Permite retroceder directamente a la variable que causó el conflicto,
#   en lugar de hacerlo paso a paso.

# VARIABLES, DOMINIOS Y RESTRICCIONES

variables = ["A", "B", "C", "D"]

dominios = {
    "A": ["Rojo", "Verde", "Azul"],
    "B": ["Rojo", "Verde", "Azul"],
    "C": ["Rojo", "Verde", "Azul"],
    "D": ["Rojo", "Verde", "Azul"]
}

# Vecindad: pares que no pueden tener el mismo color
restricciones = [
    ("A", "B"), ("A", "C"),
    ("B", "C"), ("B", "D"),
    ("C", "D")
]

# FUNCIÓN: verifica si una asignación es válida (sin conflicto)

def es_valido(asignacion, var, valor):
    for (x, y) in restricciones:
        if x == var and y in asignacion and asignacion[y] == valor:
            return False
        if y == var and x in asignacion and asignacion[x] == valor:
            return False
    return True

# FUNCIÓN PRINCIPAL: CBJ recursivo

def cbj(asignacion, variable_index, conflictos):
    """
    asignacion: diccionario de variables -> valores
    variable_index: índice de la variable actual
    conflictos: diccionario que almacena las causas de conflicto
    """
    if len(asignacion) == len(variables):
        return asignacion, None  # solución completa

    var = variables[variable_index]

    for valor in dominios[var]:
        if es_valido(asignacion, var, valor):
            asignacion[var] = valor
            print(f"Asignar {var} = {valor}  →  Parcial: {asignacion}")

            resultado, salto = cbj(asignacion, variable_index + 1, conflictos)

            if resultado:
                return resultado, None  # éxito

            # Si debe saltar hacia atrás a otra variable
            if salto is not None and salto < variable_index:
                print(f" Saltando atrás desde {var} hasta {variables[salto]}")
                del asignacion[var]
                return None, salto

            del asignacion[var]

        else:
            # Registrar conflicto: con quién falló esta asignación
            for (x, y) in restricciones:
                if (x == var and y in asignacion) or (y == var and x in asignacion):
                    conflictos[var].add(y if x == var else x)

    # Si ningún valor es válido, regresar conflicto
    if variable_index == 0:
        return None, None  # No hay solución

    # Encontrar la variable más reciente con la que hubo conflicto
    if conflictos[var]:
        salto = max(variables.index(v) for v in conflictos[var])
        conflictos[variables[salto]].update(conflictos[var])
        print(f"  Conflicto en {var} → saltar a {variables[salto]}")
        del asignacion[var]
        return None, salto
    else:
        del asignacion[var]
        return None, variable_index - 1  # salto normal

# BLOQUE PRINCIPAL

if __name__ == "__main__":
    print("\n SALTO ATRÁS DIRIGIDO POR CONFLICTOS (CBJ) \n")

    conflictos = {v: set() for v in variables}
    solucion, _ = cbj({}, 0, conflictos)

    if solucion:
        print("\n Solución encontrada:")
        for v, val in solucion.items():
            print(f"  {v} = {val}")
    else:
        print("\n No se encontró solución.")
