# Probabilidades base
P_Rain = 0.2                    # P(Lluvia)
P_Sprinkler_given_Rain = 0.01   # P(Aspersor | Lluvia)
P_Sprinkler_given_noRain = 0.4  # P(Aspersor | No lluvia)

# Probabilidades condicionales del césped mojado
P_Wet_given_Rain_Sprinkler = 0.99
P_Wet_given_Rain_noSprinkler = 0.8
P_Wet_given_noRain_Sprinkler = 0.9
P_Wet_given_noRain_noSprinkler = 0.0

# Paso 1: Calcular P(Wet) (probabilidad total de césped mojado)
def prob_Wet():
    total = 0
    # Casos posibles: combinaciones de lluvia y aspersor
    total += P_Rain * P_Sprinkler_given_Rain * P_Wet_given_Rain_Sprinkler
    total += P_Rain * (1 - P_Sprinkler_given_Rain) * P_Wet_given_Rain_noSprinkler
    total += (1 - P_Rain) * P_Sprinkler_given_noRain * P_Wet_given_noRain_Sprinkler
    total += (1 - P_Rain) * (1 - P_Sprinkler_given_noRain) * P_Wet_given_noRain_noSprinkler
    return total

P_Wet = prob_Wet()

# Paso 2: Calcular P(Wet | Rain)
P_Wet_given_Rain = (
    P_Sprinkler_given_Rain * P_Wet_given_Rain_Sprinkler +
    (1 - P_Sprinkler_given_Rain) * P_Wet_given_Rain_noSprinkler
)

# Paso 3: Aplicar la Regla de Bayes para inferir P(Rain | Wet)
P_Rain_given_Wet = (P_Wet_given_Rain * P_Rain) / P_Wet

# Mostrar resultados
print(" Red Bayesiana: Ejemplo del Césped Mojado ")
print(f"P(Rain)                     = {P_Rain:.2f}")
print(f"P(Sprinkler | Rain)         = {P_Sprinkler_given_Rain:.2f}")
print(f"P(Sprinkler | No Rain)      = {P_Sprinkler_given_noRain:.2f}")
print(f"P(Wet)                      = {P_Wet:.3f}")
print(f"P(Wet | Rain)               = {P_Wet_given_Rain:.3f}")
print(f"\nProbabilidad posterior:")
print(f"P(Rain | Wet)               = {P_Rain_given_Wet:.3f}")