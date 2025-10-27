# Descripción:
#   Ejemplo clásico de colorear un mapa con 3 colores
#   sin que dos regiones vecinas compartan el mismo color.

# Definimos las variables (regiones del mapa)

variables = ["A", "B", "C"]

# Dominios posibles (colores)
dominios = {
    "A": ["Rojo", "Verde", "Azul"],
    "B": ["Rojo", "Verde", "Azul"],
    "C": ["Rojo", "Verde", "Azul"]
}

# Restricciones: regiones vecinas
# (Cada par representa una relación "≠")
restricciones = [
    ("A", "B"),
    ("B", "C"),
    ("A", "C")
]

# Verificar si una asignación parcial satisface las restricciones

def es_valido(asignacion, var, valor):
    for (x, y) in restricciones:
        if y in asignacion and x == var:
            if asignacion[y] == valor:
                return False
        if x in asignacion and y == var:
            if asignacion[x] == valor:
                return False
    return True

# Backtracking (búsqueda recursiva)

def backtracking(asignacion):
    # Si todas las variables están asignadas → solución completa
    if len(asignacion) == len(variables):
        return asignacion

    # Elegimos la siguiente variable sin asignar
    var = [v for v in variables if v not in asignacion][0]

    for valor in dominios[var]:
        if es_valido(asignacion, var, valor):
            # Probar valor
            asignacion[var] = valor
            resultado = backtracking(asignacion)
            if resultado:
                return resultado
            # Si no funciona, retrocede (backtrack)
            del asignacion[var]

    return None

# BLOQUE PRINCIPAL

if __name__ == "__main__":
    print("\n PROBLEMAS DE SATISFACCIÓN DE RESTRICCIONES \n")
    solucion = backtracking({})

    if solucion:
        print(" Solución encontrada:")
        for v, val in solucion.items():
            print(f"  {v} = {val}")
    else:
        print(" No se encontró solución.")