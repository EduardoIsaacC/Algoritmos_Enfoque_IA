import random

# Definimos la matriz de transición
transition_matrix = {
    "A": {"A": 0.6, "B": 0.3, "C": 0.1},
    "B": {"A": 0.2, "B": 0.5, "C": 0.3},
    "C": {"A": 0.1, "B": 0.4, "C": 0.5}
}

# Estado inicial
state = "A"
history = [state]

# Simulamos 15 pasos
for t in range(1, 16):
    rand = random.random()
    cumulative = 0
    for next_state, prob in transition_matrix[state].items():
        cumulative += prob
        if rand < cumulative:
            state = next_state
            break
    history.append(state)

print(" Proceso de Markov (Hipótesis de Markov) ")
print("Secuencia de estados:")
print(" → ".join(history))

# Contamos la frecuencia de cada estado
freq = {s: history.count(s)/len(history) for s in transition_matrix}
print("\nFrecuencia aproximada:")
for s, f in freq.items():
    print(f"{s}: {f:.2f}")