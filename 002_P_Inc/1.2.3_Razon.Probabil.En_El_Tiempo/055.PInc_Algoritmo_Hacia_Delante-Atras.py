# Estados: Soleado (S), Lluvioso (L)
# Evidencia: Uso de paraguas (yes/no)

# Distribución inicial
P_inicial = {"S": 0.5, "L": 0.5}

# Transición P(X_t | X_{t-1})
P_trans = {
    "S": {"S": 0.8, "L": 0.2},
    "L": {"S": 0.3, "L": 0.7}
}

# Emisión P(E_t | X_t)
P_emision = {
    "S": {"yes": 0.2, "no": 0.8},
    "L": {"yes": 0.9, "no": 0.1}
}

# Evidencias observadas
evidencias = ["yes", "yes", "no"]
T = len(evidencias)

# FORWARD
alpha = [{} for _ in range(T)]

# Inicialización
for x in P_inicial:
    alpha[0][x] = P_emision[x][evidencias[0]] * P_inicial[x]

# Recursión
for t in range(1, T):
    for x in P_inicial:
        alpha[t][x] = P_emision[x][evidencias[t]] * sum(
            P_trans[x_prev][x] * alpha[t-1][x_prev] for x_prev in P_inicial
        )

# Normalización
for t in range(T):
    factor = sum(alpha[t].values())
    for x in alpha[t]:
        alpha[t][x] /= factor

# --- BACKWARD ---
beta = [{} for _ in range(T)]
for x in P_inicial:
    beta[T-1][x] = 1  # Inicialización

for t in range(T-2, -1, -1):
    for x in P_inicial:
        beta[t][x] = sum(
            P_trans[x][x_next] * P_emision[x_next][evidencias[t+1]] * beta[t+1][x_next]
            for x_next in P_inicial
        )

# SUAVIZADO
posterior = [{} for _ in range(T)]
for t in range(T):
    for x in P_inicial:
        posterior[t][x] = alpha[t][x] * beta[t][x]
    # Normalizar
    factor = sum(posterior[t].values())
    for x in posterior[t]:
        posterior[t][x] /= factor

# Resultados
print(" Algoritmo Hacia Delante–Atrás \n")
for t in range(T):
    print(f"Tiempo {t+1} | Evidencia: {evidencias[t]}")
    print(f"  P(Soleado) = {posterior[t]['S']:.3f}")
    print(f"  P(Lluvioso) = {posterior[t]['L']:.3f}\n")