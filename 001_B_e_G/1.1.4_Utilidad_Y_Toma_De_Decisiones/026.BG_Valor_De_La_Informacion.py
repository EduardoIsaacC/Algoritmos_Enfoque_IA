# Descripción:
#   Calcula la utilidad esperada con y sin información
#   para determinar el valor de obtener información adicional.

# Variables aleatorias y utilidades

P_clima = {
    "Soleado": 0.7,
    "Lluvioso": 0.3
}

acciones = ["Salir", "Quedarse"]

U = {
    "Salir": {"Soleado": 100, "Lluvioso": -50},
    "Quedarse": {"Soleado": 20, "Lluvioso": 40}
}

# Función: utilidad esperada sin información

def EU_sin_informacion():
    mejor_EU = float("-inf")
    for accion in acciones:
        EU = sum(P_clima[clima] * U[accion][clima] for clima in P_clima)
        if EU > mejor_EU:
            mejor_EU = EU
    return mejor_EU

# Función: utilidad esperada con información perfecta

def EU_con_informacion():
    EU = 0
    for clima in P_clima:
        mejor_accion = max(acciones, key=lambda a: U[a][clima])
        EU += P_clima[clima] * U[mejor_accion][clima]
    return EU

# BLOQUE PRINCIPAL

if __name__ == "__main__":
    print("\n VALOR DE LA INFORMACIÓN \n")

    sin_info = EU_sin_informacion()
    con_info = EU_con_informacion()
    VOI = con_info - sin_info

    print(f"EU sin información = {sin_info:.2f}")
    print(f"EU con información = {con_info:.2f}")
    print(f"\n Valor de la Información (VOI) = {VOI:.2f}")

    if VOI > 0:
        print(" La información tiene valor. Deberías obtenerla.")
    else:
        print(" La información no cambia tu decisión.")