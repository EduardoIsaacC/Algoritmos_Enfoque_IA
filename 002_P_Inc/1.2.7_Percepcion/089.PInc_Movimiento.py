import cv2

#1. Cargar video o cámara
# Puedes usar un archivo: cv2.VideoCapture("video.mp4")
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
ret, frame1 = cap.read()
ret, frame2 = cap.read()

while cap.isOpened():
    #2. Calcular diferencia entre cuadros consecutivos
    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilatada = cv2.dilate(thresh, None, iterations=3)

    #3. Encontrar contornos del movimiento
    contornos, _ = cv2.findContours(dilatada, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for c in contornos:
        if cv2.contourArea(c) < 900:
            continue
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame1, "Movimiento Detectado", (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2)

    #4. Mostrar resultados
    cv2.imshow("Movimiento", frame1)
    cv2.imshow("Mascara", dilatada)

    frame1 = frame2
    ret, frame2 = cap.read()
    if not ret or cv2.waitKey(40) == 27:  # ESC para salir
        break

cap.release()
cv2.destroyAllWindows()