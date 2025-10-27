# Ejemplo: Lluvia, Aspersor y Césped Mojado

# Probabilidades base
P_Rain = 0.2                    # P(Lluvia)
P_Sprinkler_given_Rain = 0.01   # P(Aspersor | Lluvia)
P_Sprinkler_given_noRain = 0.4  # P(Aspersor | ¬Lluvia)

# Probabilidades condicionales de césped mojado
P_Wet_given_Rain_Sprinkler = 0.99
P_Wet_given_Rain_noSprinkler = 0.8
P_Wet_given_noRain_Sprinkler = 0.9
P_Wet_given_noRain_noSprinkler = 0.0

# Paso 1: Calcular la probabilidad total de que el césped esté mojado (usando regla de la suma)
def prob_Wet():
    total = 0
    # Casos posibles (Rain, Sprinkler)
    total += P_Rain * P_Sprinkler_given_Rain * P_Wet_given_Rain_Sprinkler
    total += P_Rain * (1 - P_Sprinkler_given_Rain) * P_Wet_given_Rain_noSprinkler
    total += (1 - P_Rain) * P_Sprinkler_given_noRain * P_Wet_given_noRain_Sprinkler
    total += (1 - P_Rain) * (1 - P_Sprinkler_given_noRain) * P_Wet_given_noRain_noSprinkler
    return total

P_Wet = prob_Wet()
print(f"Probabilidad total de césped mojado: {P_Wet:.3f}")

# Paso 2: Aplicar la Regla de Bayes para inferir P(Rain | Wet)
# P(Rain | Wet) = [P(Wet | Rain) * P(Rain)] / P(Wet)

# Para calcular P(Wet | Rain), sumamos los casos posibles del aspersor
P_Wet_given_Rain = (
    P_Sprinkler_given_Rain * P_Wet_given_Rain_Sprinkler +
    (1 - P_Sprinkler_given_Rain) * P_Wet_given_Rain_noSprinkler
)

P_Rain_given_Wet = (P_Wet_given_Rain * P_Rain) / P_Wet

print(f"Probabilidad de que esté lloviendo dado que el césped está mojado: {P_Rain_given_Wet:.3f}")