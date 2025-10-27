# Variables:
# - Rain
# - Sprinkler
# - WetGrass

# Probabilidades base
P_Rain = 0.2
P_Sprinkler_given_Rain = 0.01
P_Sprinkler_given_noRain = 0.4
P_Wet_given_Rain_Sprinkler = 0.99
P_Wet_given_Rain_noSprinkler = 0.8
P_Wet_given_noRain_Sprinkler = 0.9
P_Wet_given_noRain_noSprinkler = 0.0

# Función auxiliar para calcular P(WetGrass, Rain)
def joint_probability(wet=True, rain=True):
    """ Calcula la probabilidad conjunta P(WetGrass, Rain) enumerando Sprinkler """
    if rain:
        P_Sprinkler_true = P_Sprinkler_given_Rain
        P_Sprinkler_false = 1 - P_Sprinkler_given_Rain
        P_Wet_true = (P_Wet_given_Rain_Sprinkler * P_Sprinkler_true) + \
                     (P_Wet_given_Rain_noSprinkler * P_Sprinkler_false)
        return P_Wet_true * P_Rain
    else:
        P_Sprinkler_true = P_Sprinkler_given_noRain
        P_Sprinkler_false = 1 - P_Sprinkler_given_noRain
        P_Wet_true = (P_Wet_given_noRain_Sprinkler * P_Sprinkler_true) + \
                     (P_Wet_given_noRain_noSprinkler * P_Sprinkler_false)
        return P_Wet_true * (1 - P_Rain)

# Paso 1: Calcular probabilidades conjuntas para lluvia y no lluvia
P_Wet_and_Rain = joint_probability(wet=True, rain=True)
P_Wet_and_noRain = joint_probability(wet=True, rain=False)

# Paso 2: Calcular P(Wet)
P_Wet = P_Wet_and_Rain + P_Wet_and_noRain

# Paso 3: Calcular P(Rain | Wet) = P(Wet, Rain) / P(Wet)
P_Rain_given_Wet = P_Wet_and_Rain / P_Wet

# Mostrar resultados
print(" Inferencia por Enumeración ")
print(f"P(Wet ∧ Rain)     = {P_Wet_and_Rain:.3f}")
print(f"P(Wet ∧ ¬Rain)    = {P_Wet_and_noRain:.3f}")
print(f"P(Wet)            = {P_Wet:.3f}")
print(f"P(Rain | Wet)     = {P_Rain_given_Wet:.3f}")