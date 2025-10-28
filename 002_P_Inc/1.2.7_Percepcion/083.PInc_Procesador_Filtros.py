import cv2
import numpy as np

#1. Cargar imagen (EDITA ESTA RUTA SEGÚN TU PC)
RUTA_IMAGEN = "Ladrillo.png"  # pon ruta absoluta si hace falta

img = cv2.imread(RUTA_IMAGEN)

# Validar carga
if img is None:
    raise FileNotFoundError(f"No pude abrir la imagen '{RUTA_IMAGEN}'. Revisa la ruta o el nombre del archivo.")

# Convertir a escala de grises
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#2. Filtro de media (promedio)
media = cv2.blur(gray, (5,5))

#3. Filtro Gaussiano
gauss = cv2.GaussianBlur(gray, (5,5), 0)

#4. Filtro Mediana
mediana = cv2.medianBlur(gray, 5)

#5. Filtro de Sobel (bordes)
sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
sobel = cv2.magnitude(sobelx, sobely)

#6. Mostrar resultados 
cv2.imshow("Original (Gris)", gray)
cv2.imshow("Media (Promedio)", media)
cv2.imshow("Gaussiano", gauss)
cv2.imshow("Mediana", mediana)
cv2.imshow("Sobel (Bordes)", sobel / sobel.max())  # normalizado 0-1

cv2.waitKey(0)
cv2.destroyAllWindows()