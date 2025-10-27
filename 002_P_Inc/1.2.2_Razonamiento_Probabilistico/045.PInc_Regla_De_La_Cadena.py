# Variables del ejemplo
P_Rain = 0.2                       # P(A)
P_Sprinkler_given_Rain = 0.01      # P(B|A)
P_Wet_given_Rain_Sprinkler = 0.99  # P(C|A,B)

# Aplicamos la Regla de la Cadena
P_Rain_Sprinkler_Wet = P_Rain * P_Sprinkler_given_Rain * P_Wet_given_Rain_Sprinkler

print(" Regla de la Cadena ")
print(f"P(Rain)                   = {P_Rain:.2f}")
print(f"P(Sprinkler | Rain)       = {P_Sprinkler_given_Rain:.2f}")
print(f"P(Wet | Rain, Sprinkler)  = {P_Wet_given_Rain_Sprinkler:.2f}")
print("------------------------------------------")
print(f"P(Rain, Sprinkler, Wet)   = {P_Rain_Sprinkler_Wet:.5f}")