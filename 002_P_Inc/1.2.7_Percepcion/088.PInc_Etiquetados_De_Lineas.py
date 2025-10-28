import cv2
import numpy as np

#1. Cargar imagen
img = cv2.imread("formas.png", cv2.IMREAD_GRAYSCALE)
if img is None:
    raise FileNotFoundError("No se encontró 'formas.png'")

#2. Binarización
_, binaria = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

#3. Etiquetado de componentes conectados
num_labels, etiquetas = cv2.connectedComponents(binaria)

print(f"🔹 Número de componentes detectados: {num_labels - 1}")

#4. Colorear cada componente diferente
etiquetas_color = cv2.applyColorMap((etiquetas * 20).astype(np.uint8), cv2.COLORMAP_JET)

#5. Mostrar resultados
cv2.imshow("Original", img)
cv2.imshow("Binaria", binaria)
cv2.imshow("Componentes Etiquetados", etiquetas_color)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Cada forma fue:

# Detectada como componente conectado,

# Asignada con un número (1, 2, 3, …),

# Coloreada con applyColorMap para visualización.

# El fondo azul corresponde a la etiqueta 0.
# Cada color distinto representa una figura con su propia etiqueta.
# En la consola se muestra
# Componentes detectados: 10