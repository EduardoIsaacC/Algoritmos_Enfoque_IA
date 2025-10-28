import numpy as np
import matplotlib.pyplot as plt

# Parámetros del SOM 
mapa_tamano = (10, 10)  # cuadrícula 10x10
dim_entrada = 3         # (ejemplo RGB o 3 características)
eta_inicial = 0.5       # tasa de aprendizaje inicial
radio_inicial = 5       # vecindad inicial
epocas = 100

# Inicialización de pesos aleatorios
np.random.seed(42)
W = np.random.rand(mapa_tamano[0], mapa_tamano[1], dim_entrada)

# Datos de ejemplo: colores RGB básicos 
datos = np.array([
    [1, 0, 0],  # rojo
    [0, 1, 0],  # verde
    [0, 0, 1],  # azul
    [1, 1, 0],  # amarillo
    [1, 0, 1],  # magenta
    [0, 1, 1],  # cian
    [0.5, 0.5, 0.5],  # gris
    [1, 1, 1],  # blanco
    [0, 0, 0],  # negro
])

# Función para encontrar la BMU
def encontrar_BMU(W, x):
    distancias = np.linalg.norm(W - x, axis=2)
    indice = np.unravel_index(np.argmin(distancias), distancias.shape)
    return indice

# Entrenamiento
for epoca in range(epocas):
    # Disminuye parámetros con el tiempo
    eta = eta_inicial * np.exp(-epoca / epocas)
    radio = radio_inicial * np.exp(-epoca / (epocas / np.log(radio_inicial)))

    for x in datos:
        # 1. Encuentra la BMU
        bmu = encontrar_BMU(W, x)

        # 2. Ajusta pesos de neuronas vecinas
        for i in range(mapa_tamano[0]):
            for j in range(mapa_tamano[1]):
                # Distancia al BMU en el mapa
                dist = np.sqrt((i - bmu[0])**2 + (j - bmu[1])**2)
                if dist <= radio:
                    # Función de vecindad gaussiana
                    h = np.exp(-dist**2 / (2 * (radio**2)))
                    # Actualiza el peso
                    W[i, j] += eta * h * (x - W[i, j])

# Visualización final
plt.figure(figsize=(6,6))
plt.imshow(W)
plt.title("Mapa Autoorganizado de Kohonen (SOM) - Colores")
plt.axis('off')
plt.show()