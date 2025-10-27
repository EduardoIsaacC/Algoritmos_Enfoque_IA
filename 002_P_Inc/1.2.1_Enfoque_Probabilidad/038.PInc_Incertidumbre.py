# Probabilidades base
P_Gas = 0.3                # Probabilidad de que haya gas (a priori)
P_Alarm_given_Gas = 0.9    # Probabilidad de que la alarma suene si hay gas
P_Alarm_given_noGas = 0.1  # Probabilidad de que la alarma suene por error (falso positivo)

# Paso 1: Calcular la probabilidad total de que la alarma suene (regla de la suma)
P_Alarm = (P_Alarm_given_Gas * P_Gas) + (P_Alarm_given_noGas * (1 - P_Gas))

# Paso 2: Aplicar Regla de Bayes
# P(Gas | Alarma) = [P(Alarma | Gas) * P(Gas)] / P(Alarma)
P_Gas_given_Alarm = (P_Alarm_given_Gas * P_Gas) / P_Alarm

print(" Razonamiento bajo incertidumbre ")
print(f"Probabilidad de que haya gas (a priori): {P_Gas:.2f}")
print(f"Probabilidad total de que suene la alarma: {P_Alarm:.2f}")
print(f"Probabilidad de que haya gas dado que la alarma sonó: {P_Gas_given_Alarm:.2f}")
