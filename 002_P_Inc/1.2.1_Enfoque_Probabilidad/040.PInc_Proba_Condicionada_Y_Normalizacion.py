# Probabilidades base
P_Lluvia = 0.3                   # Probabilidad a priori de lluvia
P_Nublado_given_Lluvia = 0.8     # P(Nublado | Lluvia)
P_Nublado_given_noLluvia = 0.4   # P(Nublado | No Lluvia)

# Paso 1: Calcular P(Nublado) usando la regla de la suma
P_Nublado = (P_Nublado_given_Lluvia * P_Lluvia) + \
            (P_Nublado_given_noLluvia * (1 - P_Lluvia))

# Paso 2: Aplicar la fórmula de la probabilidad condicionada
P_Lluvia_given_Nublado = (P_Nublado_given_Lluvia * P_Lluvia) / P_Nublado
P_noLluvia_given_Nublado = (P_Nublado_given_noLluvia * (1 - P_Lluvia)) / P_Nublado

# Paso 3: Normalización explícita (solo para mostrar)
alpha = 1 / ((P_Nublado_given_Lluvia * P_Lluvia) + (P_Nublado_given_noLluvia * (1 - P_Lluvia)))
P_Lluvia_norm = alpha * P_Nublado_given_Lluvia * P_Lluvia
P_noLluvia_norm = alpha * P_Nublado_given_noLluvia * (1 - P_Lluvia)

# Resultados
print(" Probabilidad Condicionada y Normalización ")
print(f"P(Lluvia)                 = {P_Lluvia:.2f}")
print(f"P(Nublado | Lluvia)       = {P_Nublado_given_Lluvia:.2f}")
print(f"P(Nublado | No Lluvia)    = {P_Nublado_given_noLluvia:.2f}")
print(f"P(Nublado)                = {P_Nublado:.2f}\n")

print(f"P(Lluvia | Nublado)       = {P_Lluvia_given_Nublado:.2f}")
print(f"P(No Lluvia | Nublado)    = {P_noLluvia_given_Nublado:.2f}\n")

print("Normalización:")
print(f"α = {alpha:.2f}")
print(f"P(Lluvia)_normalizada     = {P_Lluvia_norm:.2f}")
print(f"P(No Lluvia)_normalizada  = {P_noLluvia_norm:.2f}")
print(f"Suma de probabilidades    = {P_Lluvia_norm + P_noLluvia_norm:.2f}")