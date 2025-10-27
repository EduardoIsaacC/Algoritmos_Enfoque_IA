# Probabilidad a priori de que un paciente esté enfermo
P_enfermo = 0.05     # 5% de la población tiene la enfermedad
P_sano = 0.95        # 95% no la tiene

# Comprobamos que las probabilidades suman 1
assert abs(P_enfermo + P_sano - 1) < 1e-6, "Las probabilidades no suman 1."

print("=== Probabilidad a Priori ===")
print(f"P(Enfermo) = {P_enfermo:.2f}")
print(f"P(Sano)    = {P_sano:.2f}\n")

# Simulación de 20 pacientes aleatorios basados en esas probabilidades
import random

pacientes = []
for i in range(1, 21):
    estado = "Enfermo" if random.random() < P_enfermo else "Sano"
    pacientes.append(estado)
    print(f"Paciente {i:02d}: {estado}")

# Contamos los resultados
num_enfermos = pacientes.count("Enfermo")
num_sanos = pacientes.count("Sano")

print("\nResumen:")
print(f"Total de enfermos detectados (sin evidencia): {num_enfermos}")
print(f"Total de sanos detectados (sin evidencia):    {num_sanos}")
print("\nNota: Estas probabilidades son 'a priori', antes de ver resultados de pruebas.")