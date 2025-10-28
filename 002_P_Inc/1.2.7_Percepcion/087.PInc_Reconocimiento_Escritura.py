import cv2
import pytesseract
#Reconocimiento de escritura (No manuscrita)
#1. Configurar ruta del motor Tesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

#2. Cargar imagen
img = cv2.imread("texto.png")
if img is None:
    raise FileNotFoundError("No se encontró la imagen. Verifica la ruta.")

#3. Preprocesamiento
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (3,3), 0)
_, binaria = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

#4. Detección de texto con pytesseract
texto_detectado = pytesseract.image_to_string(binaria, lang='spa')  # idioma español

#5. Mostrar resultados
cv2.imshow("Imagen Original", img)
cv2.imshow("Procesada", binaria)
print("\n Texto detectado:\n")
print(texto_detectado)

cv2.waitKey(0)
cv2.destroyAllWindows()
