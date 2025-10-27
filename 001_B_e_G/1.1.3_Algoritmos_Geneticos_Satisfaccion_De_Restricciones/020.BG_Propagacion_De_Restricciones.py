# Descripción:
#   Implementa el algoritmo AC-3 para establecer consistencia de arcos
#   en un problema de satisfacción de restricciones (CSP).

from collections import deque

# VARIABLES Y DOMINIOS

variables = ["A", "B", "C", "D"]

dominios = {
    "A": [1, 2, 3],
    "B": [1, 2, 3],
    "C": [1, 2, 3],
    "D": [1, 2, 3]
}

# Restricciones binarias: vecinos no pueden tener el mismo valor
restricciones = [
    ("A", "B"),
    ("A", "C"),
    ("B", "C"),
    ("B", "D"),
    ("C", "D")
]

# FUNCIÓN: Verifica si (Xi, Xj) es consistente

def revisar(Xi, Xj, dominios):
    eliminado = False
    for x in dominios[Xi][:]:  # iteramos sobre una copia del dominio
        # Si no hay ningún valor en Xj compatible con x, lo eliminamos
        if not any(x != y for y in dominios[Xj]):
            dominios[Xi].remove(x)
            eliminado = True
            print(f" Eliminado {x} del dominio de {Xi} (por conflicto con {Xj})")
    return eliminado

# FUNCIÓN PRINCIPAL: Algoritmo AC-3

def ac3(variables, dominios, restricciones):
    cola = deque(restricciones)  # todos los arcos iniciales

    while cola:
        (Xi, Xj) = cola.popleft()

        if revisar(Xi, Xj, dominios):
            if len(dominios[Xi]) == 0:
                print(f" El dominio de {Xi} quedó vacío. No hay solución.")
                return False

            # Si se modificó el dominio, volver a añadir sus vecinos a la cola
            for (Xk, Xl) in restricciones:
                if Xl == Xi and Xk != Xj:
                    cola.append((Xk, Xi))
    return True

# BLOQUE PRINCIPAL

if __name__ == "__main__":
    print("\n PROPAGACIÓN DE RESTRICCIONES (AC-3) \n")

    dominios_filtrados = {v: list(vals) for v, vals in dominios.items()}
    resultado = ac3(variables, dominios_filtrados, restricciones)

    print("\n Resultado final de los dominios:")
    for var, dom in dominios_filtrados.items():
        print(f"  {var}: {dom}")