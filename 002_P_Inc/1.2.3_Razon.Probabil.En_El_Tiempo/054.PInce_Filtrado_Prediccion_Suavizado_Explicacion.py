# Estados: C (cargando), M (movimiento)
# Evidencia: Sensor de energía (ON/OFF)
# P(X_t | X_{t-1}) y P(E_t | X_t)

P_trans = {
    "C": {"C": 0.8, "M": 0.2},
    "M": {"C": 0.3, "M": 0.7}
}

P_sensor = {
    "C": {"ON": 0.9, "OFF": 0.1},
    "M": {"ON": 0.3, "OFF": 0.7}
}

# Creencia inicial
belief = {"C": 0.5, "M": 0.5}

# Secuencia de observaciones
evidencias = ["ON", "ON", "OFF", "ON"]

def filtrar_y_predecir(belief, evidencias):
    for t, e in enumerate(evidencias, start=1):
        # Predicción
        pred = {
            "C": P_trans["C"]["C"] * belief["C"] + P_trans["M"]["C"] * belief["M"],
            "M": P_trans["C"]["M"] * belief["C"] + P_trans["M"]["M"] * belief["M"]
        }

        # Filtrado
        bel_e = {
            "C": P_sensor["C"][e] * pred["C"],
            "M": P_sensor["M"][e] * pred["M"]
        }

        # Normalización
        alpha = 1 / (bel_e["C"] + bel_e["M"])
        belief = {s: bel_e[s] * alpha for s in belief}

        print(f"Paso {t}: evidencia={e}, creencia actualizada={belief}")
    return belief

print(" Filtrado y Predicción ")
final_belief = filtrar_y_predecir(belief, evidencias)