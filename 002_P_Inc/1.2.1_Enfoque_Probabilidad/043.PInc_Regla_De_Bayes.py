# Probabilidades base
P_Enfermo = 0.01                   # P(H)
P_TestPos_given_Enfermo = 0.9      # P(E|H)
P_TestPos_given_Sano = 0.05        # P(E|¬H)
P_Sano = 1 - P_Enfermo

# Paso 1: Calcular P(E) — probabilidad total del test positivo
P_TestPos = (P_TestPos_given_Enfermo * P_Enfermo) + \
            (P_TestPos_given_Sano * P_Sano)

# Paso 2: Aplicar Regla de Bayes
P_Enfermo_given_TestPos = (P_TestPos_given_Enfermo * P_Enfermo) / P_TestPos

# Paso 3: Mostrar resultados
print("=== Regla de Bayes ===")
print(f"P(Enfermo)                  = {P_Enfermo:.2f}")
print(f"P(Sano)                     = {P_Sano:.2f}")
print(f"P(Test positivo | Enfermo)  = {P_TestPos_given_Enfermo:.2f}")
print(f"P(Test positivo | Sano)     = {P_TestPos_given_Sano:.2f}")
print(f"P(Test positivo)            = {P_TestPos:.3f}")
print(f"\nProbabilidad real de estar enfermo dado test positivo:")
print(f"P(Enfermo | Test positivo)  = {P_Enfermo_given_TestPos:.3f}")