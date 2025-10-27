# Supongamos tres variables:
# - Rain (lluvia)
# - Sprinkler (aspersor)
# - WetGrass (césped mojado)

# Probabilidades base
P_Rain = 0.3
P_Sprinkler_given_Rain = 0.01
P_Sprinkler_given_noRain = 0.4

# Probabilidades condicionales de césped mojado
P_Wet_given_Rain_Sprinkler = 0.99
P_Wet_given_Rain_noSprinkler = 0.8
P_Wet_given_noRain_Sprinkler = 0.9
P_Wet_given_noRain_noSprinkler = 0.0

# Calcular P(Wet | Rain, Sprinkler)
P_Wet_given_Rain_and_Sprinkler = P_Wet_given_Rain_Sprinkler

# Calcular P(Wet | Rain)
P_Wet_given_Rain = (P_Sprinkler_given_Rain * P_Wet_given_Rain_Sprinkler) + \
                   ((1 - P_Sprinkler_given_Rain) * P_Wet_given_Rain_noSprinkler)

# Comparar resultados
print(" Independencia Condicional ")
print(f"P(Wet | Rain, Sprinkler) = {P_Wet_given_Rain_and_Sprinkler:.2f}")
print(f"P(Wet | Rain)             = {P_Wet_given_Rain:.2f}")

# Conclusión
if abs(P_Wet_given_Rain_and_Sprinkler - P_Wet_given_Rain) < 0.05:
    print("\nConclusión: 'Wet' y 'Sprinkler' son aproximadamente independientes dado 'Rain'.")
else:
    print("\nConclusión: 'Wet' y 'Sprinkler' NO son independientes dado 'Rain'.")
