import cv2
import numpy as np

#1. Cargar imagen
img = cv2.imread("Ladrillo.png")  # reemplaza por el nombre de tu imagen
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#2. Filtro de media (promedio)
media = cv2.blur(gray, (5,5))

#3. Filtro Gaussiano
gauss = cv2.GaussianBlur(gray, (5,5), 0)

#4. Filtro Mediana 
mediana = cv2.medianBlur(gray, 5)

#5. Filtro de Sobel (bordes en X y Y)
sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
sobel = cv2.magnitude(sobelx, sobely)

#6. Mostrar resultados
cv2.imshow("Original", gray)
cv2.imshow("Media (Promedio)", media)
cv2.imshow("Gaussiano", gauss)
cv2.imshow("Mediana", mediana)
cv2.imshow("Sobel (Bordes)", sobel / sobel.max())  # normalizado

cv2.waitKey(0)
cv2.destroyAllWindows()