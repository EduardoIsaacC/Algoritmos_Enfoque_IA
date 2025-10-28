import random

# Probabilidades base
P_Rain = 0.2
P_Sprinkler_given_Rain = 0.01
P_Sprinkler_given_noRain = 0.4
P_Wet_given_Rain_Sprinkler = 0.99
P_Wet_given_Rain_noSprinkler = 0.8
P_Wet_given_noRain_Sprinkler = 0.9
P_Wet_given_noRain_noSprinkler = 0.0

def likelihood_weighting(evidence_key, evidence_value, N=10000):
    """
    Implementa el algoritmo de Ponderación de Verosimilitud.
    evidence_key: variable observada (ej. 'WetGrass')
    evidence_value: valor observado (True o False)
    """
    weighted_rain_true = 0
    weighted_total = 0

    for _ in range(N):
        # 1 Generamos valores siguiendo el orden causal
        rain = random.random() < P_Rain
        sprinkler = random.random() < (P_Sprinkler_given_Rain if rain else P_Sprinkler_given_noRain)
        
        # 2 Fijamos la evidencia y calculamos su peso
        if evidence_key == "WetGrass":
            if rain and sprinkler:
                weight = P_Wet_given_Rain_Sprinkler if evidence_value else (1 - P_Wet_given_Rain_Sprinkler)
            elif rain and not sprinkler:
                weight = P_Wet_given_Rain_noSprinkler if evidence_value else (1 - P_Wet_given_Rain_noSprinkler)
            elif not rain and sprinkler:
                weight = P_Wet_given_noRain_Sprinkler if evidence_value else (1 - P_Wet_given_noRain_Sprinkler)
            else:
                weight = P_Wet_given_noRain_noSprinkler if evidence_value else (1 - P_Wet_given_noRain_noSprinkler)
        else:
            weight = 1  # No hay evidencia relevante

        # 3 Acumulamos pesos según si Rain es True o False
        if rain:
            weighted_rain_true += weight
        weighted_total += weight

    # 4 Resultado final: probabilidad ponderada
    return weighted_rain_true / weighted_total

# Ejecución del algoritmo
print(" Ponderación de Verosimilitud ")
p_estimada = likelihood_weighting("WetGrass", True, N=10000)
print(f"P(Rain | WetGrass = True) ≈ {p_estimada:.3f}")