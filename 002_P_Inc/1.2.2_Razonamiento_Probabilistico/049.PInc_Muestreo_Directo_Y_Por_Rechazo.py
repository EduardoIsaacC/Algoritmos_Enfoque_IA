import random

# Probabilidades base
P_Rain = 0.2
P_Sprinkler_given_Rain = 0.01
P_Sprinkler_given_noRain = 0.4
P_Wet_given_Rain_Sprinkler = 0.99
P_Wet_given_Rain_noSprinkler = 0.8
P_Wet_given_noRain_Sprinkler = 0.9
P_Wet_given_noRain_noSprinkler = 0.0

# Muestreo directo
def sample_once():
    """Genera una muestra siguiendo el orden causal de la red"""
    rain = random.random() < P_Rain
    sprinkler = random.random() < (P_Sprinkler_given_Rain if rain else P_Sprinkler_given_noRain)
    
    if rain and sprinkler:
        wet = random.random() < P_Wet_given_Rain_Sprinkler
    elif rain and not sprinkler:
        wet = random.random() < P_Wet_given_Rain_noSprinkler
    elif not rain and sprinkler:
        wet = random.random() < P_Wet_given_noRain_Sprinkler
    else:
        wet = random.random() < P_Wet_given_noRain_noSprinkler
        
    return {"Rain": rain, "Sprinkler": sprinkler, "WetGrass": wet}

# Muestreo por rechazo
def rejection_sampling(evidence_key, evidence_value, N=10000):
    """Genera N muestras y descarta las que no cumplen la evidencia"""
    count_rain_given_evidence = 0
    count_evidence = 0

    for _ in range(N):
        sample = sample_once()
        if sample[evidence_key] == evidence_value:
            count_evidence += 1
            if sample["Rain"]:
                count_rain_given_evidence += 1

    if count_evidence == 0:
        return 0.0  # No se cumplió la evidencia en ninguna muestra

    return count_rain_given_evidence / count_evidence

# Ejecución
print(" Muestreo por Rechazo ")
p_estimada = rejection_sampling("WetGrass", True, N=10000)
print(f"P(Rain | WetGrass = True) ≈ {p_estimada:.3f}")