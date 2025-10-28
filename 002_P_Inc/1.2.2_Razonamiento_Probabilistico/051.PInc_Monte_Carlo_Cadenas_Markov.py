import random

# Probabilidades base
P_Rain = 0.2
P_Sprinkler_given_Rain = 0.01
P_Sprinkler_given_noRain = 0.4
P_Wet_given_Rain_Sprinkler = 0.99
P_Wet_given_Rain_noSprinkler = 0.8
P_Wet_given_noRain_Sprinkler = 0.9
P_Wet_given_noRain_noSprinkler = 0.0

def conditional_P_Wet(rain, sprinkler):
    """Devuelve P(WetGrass=True | Rain, Sprinkler)"""
    if rain and sprinkler:
        return P_Wet_given_Rain_Sprinkler
    elif rain and not sprinkler:
        return P_Wet_given_Rain_noSprinkler
    elif not rain and sprinkler:
        return P_Wet_given_noRain_Sprinkler
    else:
        return P_Wet_given_noRain_noSprinkler

def gibbs_sampling(evidence_key, evidence_value, N=10000):
    """MCMC mediante Gibbs Sampling"""
    # Inicializamos variables
    rain = random.choice([True, False])
    sprinkler = random.choice([True, False])
    wet = evidence_value  # Fijamos la evidencia (WetGrass)

    counts_rain_true = 0

    for _ in range(N):
        # Actualizar Rain condicionado en Sprinkler y WetGrass
        P_wet_given_rain = conditional_P_Wet(True, sprinkler)
        P_wet_given_noRain = conditional_P_Wet(False, sprinkler)

        # Calcular probabilidad condicional de Rain dado la evidencia
        num = P_wet_given_rain * (P_Sprinkler_given_Rain if sprinkler else (1 - P_Sprinkler_given_Rain)) * P_Rain
        den = num + P_wet_given_noRain * (P_Sprinkler_given_noRain if sprinkler else (1 - P_Sprinkler_given_noRain)) * (1 - P_Rain)
        P_rain_given = num / den

        rain = random.random() < P_rain_given  # Muestra nuevo valor de Rain

        # Actualizar Sprinkler condicionado en Rain y WetGrass
        P_wet_given_sprinkler = conditional_P_Wet(rain, True)
        P_wet_given_noSprinkler = conditional_P_Wet(rain, False)

        num = P_wet_given_sprinkler * (P_Sprinkler_given_Rain if rain else P_Sprinkler_given_noRain)
        den = num + P_wet_given_noSprinkler * ((1 - P_Sprinkler_given_Rain) if rain else (1 - P_Sprinkler_given_noRain))
        P_sprinkler_given = num / den

        sprinkler = random.random() < P_sprinkler_given  # Muestra nuevo valor de Sprinkler

        if rain:
            counts_rain_true += 1

    return counts_rain_true / N

# Ejecución
print(" Monte Carlo para Cadenas de Markov (Gibbs Sampling) ")
p_estimada = gibbs_sampling("WetGrass", True, N=10000)
print(f"P(Rain | WetGrass = True) ≈ {p_estimada:.3f}")