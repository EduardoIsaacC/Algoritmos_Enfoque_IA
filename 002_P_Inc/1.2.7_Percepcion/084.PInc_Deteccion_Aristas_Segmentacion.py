import cv2
import numpy as np

#1. Cargar imagen
RUTA = "Ladrillo.png"  # cámbiala según tu caso
img = cv2.imread(RUTA)
if img is None:
    raise FileNotFoundError("No se encontró la imagen. Verifica la ruta.")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#2. Detección de aristas
# Sobel
sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
sobel = cv2.magnitude(sobelx, sobely)

# Laplaciano
laplaciano = cv2.Laplacian(gray, cv2.CV_64F)

# Canny (más avanzado)
canny = cv2.Canny(gray, 100, 200)

#3. Segmentación básica
# a) Umbralización (binario)
_, umbral = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

#b) Detección de contornos
contornos, _ = cv2.findContours(umbral, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
segmentada = img.copy()
cv2.drawContours(segmentada, contornos, -1, (0,255,0), 2)

# 4. Mostrar resultados
cv2.imshow("Original", img)
cv2.imshow("Grises", gray)
cv2.imshow("Sobel", sobel / sobel.max())
cv2.imshow("Laplaciano", laplaciano / laplaciano.max())
cv2.imshow("Canny", canny)
cv2.imshow("Umbralización", umbral)
cv2.imshow("Segmentación (Contornos)", segmentada)

cv2.waitKey(0)
cv2.destroyAllWindows()