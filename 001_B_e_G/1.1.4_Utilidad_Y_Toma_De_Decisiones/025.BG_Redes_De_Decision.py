# Descripción:
#   Simula una red de decisión simple con una variable aleatoria
#   (Clima), una decisión (Salir o No Salir) y una utilidad esperada.

# PROBABILIDADES DEL CLIMA

P_clima = {
    "Soleado": 0.7,
    "Lluvioso": 0.3
}

#  POSIBLES DECISIONES

acciones = ["Salir", "Quedarse"]

#  UTILIDAD SEGÚN DECISIÓN Y CLIMA

# U[acción][clima] = utilidad numérica
U = {
    "Salir": {"Soleado": 100, "Lluvioso": -50},
    "Quedarse": {"Soleado": 20, "Lluvioso": 40}
}

# FUNCIÓN: cálculo de utilidad esperada

def utilidad_esperada(accion):
    EU = 0
    for clima, prob in P_clima.items():
        EU += prob * U[accion][clima]
    return EU

# BLOQUE PRINCIPAL

if __name__ == "__main__":
    print("\n RED DE DECISIÓN: SALIR O NO SALIR \n")

    for accion in acciones:
        print(f"{accion}: Utilidad esperada = {utilidad_esperada(accion):.2f}")

    mejor_accion = max(acciones, key=utilidad_esperada)
    print(f"\n Decisión óptima: {mejor_accion}")