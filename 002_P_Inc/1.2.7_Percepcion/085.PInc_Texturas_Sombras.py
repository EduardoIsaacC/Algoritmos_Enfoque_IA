import cv2
import numpy as np
import matplotlib.pyplot as plt

#1. Cargar imagen
RUTA = "Ladrillo.png"  # Cambia por tu imagen
img = cv2.imread(RUTA)
if img is None:
    raise FileNotFoundError("No se encontró la imagen. Revisa la ruta.")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#2. Análisis de textura: LBP (Local Binary Pattern)
def LBP(img):
    """Calcula el patrón binario local (LBP) de una imagen."""
    lbp = np.zeros_like(img)
    for i in range(1, img.shape[0]-1):
        for j in range(1, img.shape[1]-1):
            centro = img[i, j]
            binario = (img[i-1:i+2, j-1:j+2] >= centro).astype(int)
            binario = np.delete(binario.flatten(), 4)  # quitar centro
            lbp[i, j] = int("".join(binario.astype(str)), 2)
    return lbp

lbp_img = LBP(gray)

#3. Detección de sombra (zonas oscuras)
# Convertir a HSV para analizar brillo
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
v = hsv[:,:,2]  # canal de brillo

# Umbral adaptativo: zonas oscuras se consideran sombra
_, sombras = cv2.threshold(v, 60, 255, cv2.THRESH_BINARY_INV)

#4. Bordes para resaltar textura ---
sobel = cv2.Sobel(gray, cv2.CV_64F, 1, 1, ksize=3)
sobel = cv2.convertScaleAbs(sobel)

#5. Mostrar resultados
cv2.imshow("Original", img)
cv2.imshow("LBP (Textura Local)", lbp_img)
cv2.imshow("Sobel (Relieve)", sobel)
cv2.imshow("Sombras Detectadas", sombras)
cv2.waitKey(0)
cv2.destroyAllWindows()