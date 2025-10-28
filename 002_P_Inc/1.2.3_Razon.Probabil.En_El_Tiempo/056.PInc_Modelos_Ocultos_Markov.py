import random

# Definición del modelo
estados = ["Soleado", "Lluvioso"]
observaciones = ["Yes", "No"]

# Distribución inicial
P_inicial = {"Soleado": 0.5, "Lluvioso": 0.5}

# Matriz de transición P(X_t | X_{t-1})
P_trans = {
    "Soleado": {"Soleado": 0.8, "Lluvioso": 0.2},
    "Lluvioso": {"Soleado": 0.3, "Lluvioso": 0.7}
}

# Matriz de emisión P(E_t | X_t)
P_emision = {
    "Soleado": {"Yes": 0.2, "No": 0.8},
    "Lluvioso": {"Yes": 0.9, "No": 0.1}
}

# Simulación de secuencia
def generar_hmm(num_dias=10):
    estado = random.choices(list(P_inicial.keys()), weights=P_inicial.values())[0]
    sec_estados = [estado]
    sec_observaciones = []

    for _ in range(num_dias):
        # Emitir observación según estado actual
        observacion = random.choices(list(P_emision[estado].keys()),
                                     weights=P_emision[estado].values())[0]
        sec_observaciones.append(observacion)

        # Transición al siguiente estado
        estado = random.choices(list(P_trans[estado].keys()),
                                weights=P_trans[estado].values())[0]
        sec_estados.append(estado)

    return sec_estados[:-1], sec_observaciones

# Ejecución
estados_seq, obs_seq = generar_hmm(10)
print(" Simulación de HMM ")
print("Estados ocultos reales:    ", " → ".join(estados_seq))
print("Observaciones emitidas:    ", " → ".join(obs_seq))