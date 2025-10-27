# Descripción:
#   Alterna entre evaluación de política y mejora de política
#   hasta encontrar la política óptima en un MDP.
#     - Incluye transición terminal consistente.
#     - Propaga la recompensa positiva del estado D.
#     - Muestra la política y las utilidades en cada ciclo.

import math

# Definición del entorno MDP

estados = ["A", "B", "C", "D"]

acciones_por_estado = {
    "A": ["Derecha"],
    "B": ["Derecha"],
    "C": ["Derecha"],
    "D": ["Derecha"]  # terminal se queda igual
}

R = {
    "A": -0.04,
    "B": -0.04,
    "C": -0.04,
    "D": +1.0
}

P = {
    "A": {
        "Derecha": {"B": 0.8, "A": 0.2}
    },
    "B": {
        "Derecha": {"C": 0.8, "B": 0.2}
    },
    "C": {
        "Derecha": {"D": 0.8, "C": 0.2}
    },
    "D": {
        "Derecha": {"D": 1.0}
    }
}

gamma = 0.99   # más enfocado al largo plazo
theta = 1e-6   # umbral de convergencia para evaluación de política

# Inicializamos utilidades y política (arbitraria)

U = {s: 0.0 for s in estados}
politica = {s: "Derecha" for s in estados}

# Evaluar política actual:
# Resolver U(s) = R(s) + gamma * Σ P(s'|s, π(s)) * U(s')
# hasta convergencia.

def evaluar_politica():
    while True:
        delta = 0.0
        for s in estados:
            a = politica[s]

            # Calcular utilidad esperada al seguir ESTA política
            utilidad_esperada = 0.0
            for s_next, prob in P[s][a].items():
                utilidad_esperada += prob * U[s_next]

            nueva_U = R[s] + gamma * utilidad_esperada

            delta = max(delta, abs(nueva_U - U[s]))
            U[s] = nueva_U

        if delta < theta:
            break

# Mejorar política:
# Para cada estado, busca la acción que maximiza la utilidad esperada.
# Si ninguna acción cambia, la política es estable (óptima).

def mejorar_politica():
    estable = True

    for s in estados:
        mejor_accion = None
        mejor_valor = float("-inf")

        # probamos TODAS las acciones posibles en s
        for a in acciones_por_estado[s]:
            utilidad_esperada = 0.0
            for s_next, prob in P[s][a].items():
                utilidad_esperada += prob * U[s_next]

            if utilidad_esperada > mejor_valor:
                mejor_valor = utilidad_esperada
                mejor_accion = a

        # si la mejor acción encontrada cambia la política actual -> no estable
        if politica[s] != mejor_accion:
            politica[s] = mejor_accion
            estable = False

    return estable

# Bucle principal de Iteración de Políticas

def policy_iteration():
    iteracion = 0
    while True:
        iteracion += 1

        # 1. Evalúa la política actual (para obtener buenas U)
        evaluar_politica()

        # 2. Mejora la política en base a esas U
        estable = mejorar_politica()

        # Mostrar progreso
        print(f"\nIteración de Política {iteracion}")
        for s in estados:
            print(f"U({s}) = {U[s]:.4f}")
        print(f"Política actual: {politica}")

        # 3. Si la política ya no cambia, ya es óptima
        if estable:
            break

    return U, politica

# BLOQUE PRINCIPAL

if __name__ == "__main__":
    print("\nITERACIÓN DE POLÍTICAS (Policy Iteration) - Corregida ")

    U_opt, pi_opt = policy_iteration()

    print("\n Resultados Finales ")
    for s in estados:
        print(f"U({s}) = {U_opt[s]:.4f}")
    print(f"\nPolítica Óptima: {pi_opt}")