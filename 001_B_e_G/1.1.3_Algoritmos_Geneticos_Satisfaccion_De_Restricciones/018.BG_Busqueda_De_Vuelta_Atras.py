# Descripción:
#   Implementa el algoritmo clásico de backtracking para resolver
#   problemas de satisfacción de restricciones (CSP).
#   Ejemplo: colorear un mapa con 3 colores sin que regiones vecinas
#   compartan el mismo color.

# VARIABLES Y DOMINIOS

variables = ["A", "B", "C", "D"]

dominios = {
    "A": ["Rojo", "Verde", "Azul"],
    "B": ["Rojo", "Verde", "Azul"],
    "C": ["Rojo", "Verde", "Azul"],
    "D": ["Rojo", "Verde", "Azul"]
}

# Restricciones (regiones vecinas no pueden tener el mismo color)
restricciones = [
    ("A", "B"), ("A", "C"),
    ("B", "C"), ("B", "D"),
    ("C", "D")
]

# FUNCIÓN: Verifica si una asignación parcial es válida

def es_consistente(asignacion, var, valor):
    """
    Comprueba que la variable actual no viole restricciones
    con las variables ya asignadas.
    """
    for (x, y) in restricciones:
        # Si la variable actual está relacionada con otra ya asignada
        if x == var and y in asignacion:
            if asignacion[y] == valor:
                return False
        if y == var and x in asignacion:
            if asignacion[x] == valor:
                return False
    return True

# FUNCIÓN: Búsqueda recursiva de vuelta atrás

def backtracking(asignacion):
    """
    Asigna valores a las variables una por una.
    Si se viola una restricción, retrocede (vuelta atrás).
    """
    # Caso base: todas las variables asignadas → solución completa
    if len(asignacion) == len(variables):
        return asignacion

    # Elegir una variable no asignada aún
    var = [v for v in variables if v not in asignacion][0]

    for valor in dominios[var]:
        if es_consistente(asignacion, var, valor):
            # Intentar asignar valor
            asignacion[var] = valor
            print(f"Asignar {var} = {valor}  →  Parcial: {asignacion}")

            # Llamada recursiva
            resultado = backtracking(asignacion)
            if resultado:
                return resultado

            # Si falla, eliminar asignación (vuelta atrás)
            print(f" Backtrack en {var} (quitar {valor})")
            del asignacion[var]

    # Si ningún valor funcionó → retroceder
    return None

# BLOQUE PRINCIPAL

if __name__ == "__main__":
    print("\n BÚSQUEDA DE VUELTA ATRÁS \n")

    solucion = backtracking({})

    if solucion:
        print("\n Solución encontrada:")
        for v, val in solucion.items():
            print(f"  {v} = {val}")
    else:
        print("\n No se encontró ninguna solución.")