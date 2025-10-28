import numpy as np

# UTILIDAD GENERAL

def signo_binario(x):
    """
    Convierte a +1 / -1 con regla de signo.
    Si x == 0, devolvemos 1 por conveniencia.
    """
    return np.where(x >= 0, 1, -1)

print("           REDES NEURONALES CLÁSICAS        ")
print("   Hebb | Hopfield | Hamming | Boltzmann    ")

# 1) RED DE HEBB

print(" 1) RED DE HEBB ")

# Patrones a memorizar (usamos +1 / -1 en vez de 1 / 0)
patrones_hebb = np.array([
    [ 1, -1,  1, -1],
    [-1,  1, -1,  1]
])

# Regla de Hebb:
# W = suma outer(x, x) para cada patrón x
W_hebb = np.zeros((4, 4))
for x in patrones_hebb:
    W_hebb += np.outer(x, x)

# Quitamos auto-conexiones
np.fill_diagonal(W_hebb, 0)

print("Matriz de pesos W (Hebb):")
print(W_hebb)

# Probemos recuperar un patrón conocido
x_prueba_hebb = np.array([ 1, -1,  1, -1])
salida_hebb = np.sign(W_hebb @ x_prueba_hebb)
salida_hebb[salida_hebb == 0] = 1  # por estabilidad

print("Patrón de entrada:    ", x_prueba_hebb)
print("Patrón recordado Hebb:", salida_hebb, "\n")

# 2) RED DE HOPFIELD

print(" 2) RED DE HOPFIELD ")

# Patrones a almacenar en la red Hopfield (también en +1/-1)
patrones_hopfield = np.array([
    [ 1, -1,  1, -1],
    [-1,  1, -1,  1]
])

# Construcción de la matriz de pesos usando regla tipo Hebb
W_hop = np.zeros((4, 4))
for p in patrones_hopfield:
    W_hop += np.outer(p, p)

# Sin auto-conexiones
np.fill_diagonal(W_hop, 0)

def actualizar_hopfield(x, W, pasos=5):
    """
    Actualización síncrona básica:
    x(t+1) = sign(W x(t))
    Repite 'pasos' iteraciones.
    """
    x = x.copy()
    for _ in range(pasos):
        x = np.sign(W @ x)
        x[x == 0] = 1
    return x

# Patrón de entrada con ruido
x_ruidoso = np.array([ 1, -1, -1, -1 ])
print("Entrada ruidosa:      ", x_ruidoso)

recuperado = actualizar_hopfield(x_ruidoso, W_hop, pasos=5)
print("Patrón recordado Hopfield:", recuperado, "\n")

# 3) RED DE HAMMING

print("3) RED DE HAMMING ")

# La red de Hamming clasifica una entrada comparándola con
# patrones almacenados y elige el más similar.
# Usaremos patrones binarios (+1/-1 también para consistencia).

patrones_hamming = np.array([
    [ 1, -1,  1, -1],
    [ 1,  1, -1, -1]
])

# Entrada "ruidosa" que queremos clasificar
x_prueba_hamming = np.array([ 1, -1,  1,  1 ])

# Capa 1: similitud (producto punto)
similitudes = patrones_hamming @ x_prueba_hamming

# Ganador = patrón más parecido
indice_ganador = np.argmax(similitudes)
patron_ganador = patrones_hamming[indice_ganador]

print("Patrones aprendidos (Hamming):")
print(patrones_hamming)
print("Entrada a clasificar:       ", x_prueba_hamming)
print("Similitudes:", similitudes)
print("Patrón reconocido (Hamming):", patron_ganador, "\n")

# 4) RED DE BOLTZMANN (Versión simplificada)

print(" 4) RED DE BOLTZMANN (simplificada) ")

# La Red de Boltzmann es una red estocástica que busca un estado
# de baja energía. Aquí simulamos una mini red de 3 neuronas.

np.random.seed(42)

# Matriz de pesos simétrica (sin auto-conexiones en diagonal)
W_boltz = np.array([
    [ 0.0,  1.0, -1.0],
    [ 1.0,  0.0,  1.0],
    [-1.0,  1.0,  0.0]
])

# Bias/umbrales (uno por neurona)
b_boltz = np.array([0.1, 0.0, -0.1])

# "Temperatura" del sistema (controla aleatoriedad)
T = 1.0

# Estado inicial aleatorio en {-1, +1}
estado = np.random.choice([-1, 1], size=3)
print("Estado inicial Boltzmann:", estado)

def energia_boltzmann(W, b, s):
    """
    Energía clásica de una red de Boltzmann:
    E = -1/2 * sum_ij w_ij s_i s_j  - sum_i b_i s_i
    """
    return -0.5 * np.sum(W * np.outer(s, s)) - np.dot(b, s)

# Simulación de unas cuantas iteraciones de actualización estocástica
for epoch in range(5):
    for i in range(len(estado)):
        # Cambio de energía si volteamos la neurona i
        delta_E = 2 * (np.dot(W_boltz[i], estado) + b_boltz[i]) * estado[i]

        # Probabilidad logística de flip
        prob_flip = 1 / (1 + np.exp(delta_E / T))

        # "Lanzamos" para decidir si volteamos el estado de la neurona i
        if np.random.rand() < prob_flip:
            estado[i] *= -1  # invertimos el estado

    print(f"Iteración {epoch+1}: Estado = {estado}, Energía = {energia_boltzmann(W_boltz, b_boltz, estado):.4f}")

print("\nEstado final Boltzmann:", estado)
print("Energía final:", energia_boltzmann(W_boltz, b_boltz, estado), "\n")

# RESUMEN FINAL

print(" RESUMEN:")
print(" - Hebb:    Aprende asociaciones directas con regla de correlación.")
print(" - Hopfield: Memoria autoasociativa; corrige ruido y cae en un estado estable.")
print(" - Hamming: Clasifica por similitud (gana el patrón más parecido).")
print(" - Boltzmann: Red estocástica que busca mínimos de energía global.")
