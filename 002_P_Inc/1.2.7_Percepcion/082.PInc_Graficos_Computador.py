import numpy as np
import matplotlib.pyplot as plt

#1. Definir un cuadrado
cuadrado = np.array([ [0, 0], [1, 0], [1, 1], [0, 1], [0, 0] ])

#2. Transformaciones
def rotar(puntos, angulo):
    """Rotación 2D en radianes"""
    R = np.array([
        [np.cos(angulo), -np.sin(angulo)],
        [np.sin(angulo),  np.cos(angulo)]
    ])
    return puntos @ R.T

def escalar(puntos, sx, sy):
    """Escalamiento"""
    S = np.array([[sx, 0], [0, sy]])
    return puntos @ S.T

def trasladar(puntos, tx, ty):
    """Traslación"""
    return puntos + np.array([tx, ty])

#3. Aplicar transformaciones
cuadrado_rotado = rotar(cuadrado, np.pi/4)
cuadrado_escalado = escalar(cuadrado, 1.5, 0.5)
cuadrado_trasladado = trasladar(cuadrado, 2, 1)

#4. Dibujar
plt.figure(figsize=(7,7))
plt.plot(cuadrado[:,0], cuadrado[:,1], 'b-', label='Original')
plt.plot(cuadrado_rotado[:,0], cuadrado_rotado[:,1], 'r--', label='Rotado')
plt.plot(cuadrado_escalado[:,0], cuadrado_escalado[:,1], 'g-.', label='Escalado')
plt.plot(cuadrado_trasladado[:,0], cuadrado_trasladado[:,1], 'm:', label='Trasladado')

plt.axis('equal')
plt.grid(True)
plt.legend()
plt.title('Transformaciones 2D — Gráficos por Computador')
plt.show()