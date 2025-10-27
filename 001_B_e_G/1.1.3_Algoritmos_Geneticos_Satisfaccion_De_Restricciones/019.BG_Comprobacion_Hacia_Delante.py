# Descripción:
#   Versión mejorada del algoritmo de Backtracking para CSP.
#   Antes de asignar una variable, elimina de los dominios
#   futuros los valores incompatibles con la asignación actual.

import copy

# VARIABLES Y DOMINIOS

variables = ["A", "B", "C", "D"]

dominios_iniciales = {
    "A": ["Rojo", "Verde", "Azul"],
    "B": ["Rojo", "Verde", "Azul"],
    "C": ["Rojo", "Verde", "Azul"],
    "D": ["Rojo", "Verde", "Azul"]
}

# Restricciones: regiones vecinas no pueden tener el mismo color
restricciones = [
    ("A", "B"), ("A", "C"),
    ("B", "C"), ("B", "D"),
    ("C", "D")
]

# FUNCIÓN: verifica si una asignación parcial cumple las restricciones

def es_consistente(asignacion, var, valor):
    for (x, y) in restricciones:
        if x == var and y in asignacion and asignacion[y] == valor:
            return False
        if y == var and x in asignacion and asignacion[x] == valor:
            return False
    return True

# FUNCIÓN: aplica la comprobación hacia adelante
#   Elimina valores incompatibles de los dominios futuros.

def forward_check(var, valor, dominios, asignacion):
    # Hacemos copia de los dominios (para no modificar global)
    nuevos_dominios = copy.deepcopy(dominios)

    for (x, y) in restricciones:
        # Si la variable actual afecta a otra no asignada
        if x == var and y not in asignacion:
            if valor in nuevos_dominios[y]:
                nuevos_dominios[y].remove(valor)
        if y == var and x not in asignacion:
            if valor in nuevos_dominios[x]:
                nuevos_dominios[x].remove(valor)

    return nuevos_dominios

# FUNCIÓN PRINCIPAL: Backtracking con Forward Checking

def backtracking_fc(asignacion, dominios):
    # Caso base: todas las variables asignadas
    if len(asignacion) == len(variables):
        return asignacion

    # Elegimos la primera variable no asignada
    var = [v for v in variables if v not in asignacion][0]

    for valor in dominios[var]:
        if es_consistente(asignacion, var, valor):
            print(f"Intentando {var} = {valor}")
            asignacion[var] = valor

            # Aplicar comprobación hacia adelante
            nuevos_dominios = forward_check(var, valor, dominios, asignacion)

            # Si algún dominio queda vacío → no es válido
            vacio = any(len(nuevos_dominios[v]) == 0 for v in variables if v not in asignacion)
            if not vacio:
                resultado = backtracking_fc(asignacion, nuevos_dominios)
                if resultado:
                    return resultado

            # Si falla, retrocede
            print(f"🔙 Retrocediendo en {var}")
            del asignacion[var]

    return None

# BLOQUE PRINCIPAL

if __name__ == "__main__":
    print("\n COMPROBACIÓN HACIA DELANTE (Forward Checking) \n")

    solucion = backtracking_fc({}, dominios_iniciales)

    if solucion:
        print("\n Solución encontrada:")
        for v, val in solucion.items():
            print(f"  {v} = {val}")
    else:
        print("\n No se encontró solución.")
