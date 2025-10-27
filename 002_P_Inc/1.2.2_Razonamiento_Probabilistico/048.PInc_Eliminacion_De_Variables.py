# Red Bayesiana del jardín:
# Rain → Sprinkler → WetGrass

# Probabilidades base
P_Rain = 0.2
P_Sprinkler_given_Rain = 0.01
P_Sprinkler_given_noRain = 0.4
P_Wet_given_Rain_Sprinkler = 0.99
P_Wet_given_Rain_noSprinkler = 0.8
P_Wet_given_noRain_Sprinkler = 0.9
P_Wet_given_noRain_noSprinkler = 0.0

# Paso 1: Definimos función para eliminar la variable "Sprinkler"
def eliminar_sprinkler(rain=True):
    """
    Elimina la variable Sprinkler sumando sobre sus valores posibles (True/False)
    y devuelve el factor resultante: P(Wet | Rain)
    """
    if rain:
        factor = (P_Sprinkler_given_Rain * P_Wet_given_Rain_Sprinkler) + \
                 ((1 - P_Sprinkler_given_Rain) * P_Wet_given_Rain_noSprinkler)
    else:
        factor = (P_Sprinkler_given_noRain * P_Wet_given_noRain_Sprinkler) + \
                 ((1 - P_Sprinkler_given_noRain) * P_Wet_given_noRain_noSprinkler)
    return factor

# Paso 2: Calculamos los factores reducidos
P_Wet_given_Rain = eliminar_sprinkler(True)
P_Wet_given_noRain = eliminar_sprinkler(False)

# Paso 3: Combinamos con P(Rain) y normalizamos
P_Wet_and_Rain = P_Wet_given_Rain * P_Rain
P_Wet_and_noRain = P_Wet_given_noRain * (1 - P_Rain)
P_Wet = P_Wet_and_Rain + P_Wet_and_noRain

P_Rain_given_Wet = P_Wet_and_Rain / P_Wet

# Paso 4: Mostrar resultados
print(" Eliminación de Variables ")
print(f"P(Wet | Rain)        = {P_Wet_given_Rain:.3f}")
print(f"P(Wet | ¬Rain)       = {P_Wet_given_noRain:.3f}")
print(f"P(Wet ∧ Rain)        = {P_Wet_and_Rain:.3f}")
print(f"P(Wet ∧ ¬Rain)       = {P_Wet_and_noRain:.3f}")
print(f"P(Wet)               = {P_Wet:.3f}")
print(f"P(Rain | Wet)        = {P_Rain_given_Wet:.3f}")