# Descripción:
#   Simula el cálculo de utilidad esperada para diferentes agentes
#   (neutral, adverso y propenso al riesgo) y diferentes opciones.

import math

# FUNCIONES DE UTILIDAD

def U_neutral(x):   # Agente neutral al riesgo
    return x

def U_adverso(x):   # Agente adverso al riesgo (prefiere seguridad)
    return math.sqrt(x)

def U_propenso(x):  # Agente propenso al riesgo (le gusta arriesgar)
    return x**2 / 1000  # escalado para mantener proporciones

# OPCIONES: (valor, probabilidad)

opciones = {
    "A": [(1000, 1.0)],             # ganar $1000 seguro
    "B": [(2000, 0.5), (0, 0.5)],   # 50% ganar $2000, 50% nada
    "C": [(500, 0.9), (0, 0.1)]     # 90% ganar $500, 10% nada
}

# FUNCIÓN: calcular utilidad esperada

def utilidad_esperada(opcion, funcion_U):
    EU = 0
    for valor, prob in opciones[opcion]:
        EU += prob * funcion_U(valor)
    return EU

# BLOQUE PRINCIPAL

if __name__ == "__main__":
    print("\n TEORÍA DE LA UTILIDAD: FUNCIÓN DE UTILIDAD \n")

    agentes = {
        "Neutral": U_neutral,
        "Adverso al Riesgo": U_adverso,
        "Propenso al Riesgo": U_propenso
    }

    for nombre, funcion in agentes.items():
        print(f"\n {nombre}")
        for opcion in opciones:
            print(f"Opción {opcion}: EU = {utilidad_esperada(opcion, funcion):.2f}")