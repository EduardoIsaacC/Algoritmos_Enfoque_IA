import cv2
import numpy as np

#1. Cargar imagen
RUTA = "objetos.png"  # Cambia por tu imagen
img = cv2.imread(RUTA)
if img is None:
    raise FileNotFoundError("No se encontró la imagen. Revisa la ruta.")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5,5), 0)

#2. Detección de bordes
bordes = cv2.Canny(blur, 50, 150)

#3. Encontrar contornos
contornos, _ = cv2.findContours(bordes, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
resultado = img.copy()

#4. Dibujar y clasificar formas
for c in contornos:
    area = cv2.contourArea(c)
    if area > 500:  # evitar ruido pequeño
        approx = cv2.approxPolyDP(c, 0.02 * cv2.arcLength(c, True), True)
        x, y, w, h = cv2.boundingRect(approx)
        
        if len(approx) == 3:
            forma = "Triángulo"
        elif len(approx) == 4:
            forma = "Rectángulo"
        elif len(approx) > 4:
            forma = "Círculo"
        else:
            forma = "Objeto"
        
        cv2.drawContours(resultado, [approx], -1, (0,255,0), 2)
        cv2.putText(resultado, forma, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255), 2)

cv2.imshow("Original", img)
cv2.imshow("Bordes", bordes)
cv2.imshow("Objetos Reconocidos", resultado)
cv2.waitKey(0)
cv2.destroyAllWindows()