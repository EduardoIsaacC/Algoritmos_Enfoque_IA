import random

# Matriz de transición (constante en el tiempo)
# Estados: A (cargando), B (explorando)
transition_matrix = {
    "A": {"A": 0.8, "B": 0.2},
    "B": {"A": 0.4, "B": 0.6}
}

# Estado inicial
state = "A"

# Simulación del proceso durante 20 pasos
history = [state]

for t in range(1, 21):
    rand = random.random()
    if rand < transition_matrix[state]["A"]:
        state = "A"
    else:
        state = "B"
    history.append(state)

# Contar frecuencia de estados
freq_A = history.count("A") / len(history)
freq_B = history.count("B") / len(history)

print(" Proceso Estacionario ")
print("Evolución de estados en el tiempo:")
print(" → ".join(history))
print(f"\nFrecuencia aproximada de A: {freq_A:.2f}")
print(f"Frecuencia aproximada de B: {freq_B:.2f}")