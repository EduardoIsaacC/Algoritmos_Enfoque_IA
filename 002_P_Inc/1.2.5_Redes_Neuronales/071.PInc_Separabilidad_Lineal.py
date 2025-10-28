import numpy as np
import matplotlib.pyplot as plt

def plot_gate(X, y, title, w=None, b=None):
    """
    Dibuja los puntos (0/1) en 2D para una compuerta lógica.
    Si se dan w y b, dibuja también la frontera de decisión lineal:
        w1*x + w2*y + b = 0
    """
    plt.figure(figsize=(4,4))

    # Puntos clase 0 en azul, clase 1 en rojo
    for i in range(len(X)):
        color = 'red' if y[i] == 1 else 'blue'
        plt.scatter(X[i][0], X[i][1], c=color, s=80, edgecolors='k')

    # Dibuja frontera (si aplica)
    if w is not None and b is not None:
        x_line = np.linspace(-0.5, 1.5, 100)
        # evitar división por 0
        if abs(w[1]) < 1e-6:
            y_line = np.zeros_like(x_line)
        else:
            y_line = -(w[0]*x_line + b)/w[1]
        plt.plot(x_line, y_line, 'k--')

    plt.title(title)
    plt.xlim(-0.5, 1.5)
    plt.ylim(-0.5, 1.5)
    plt.xlabel("x1")
    plt.ylabel("x2")
    plt.grid(True)
    plt.show()

# AND

X_and = np.array([[0,0],[0,1],[1,0],[1,1]])
y_and = np.array([0,0,0,1])

# Para AND, una posible frontera lineal es algo como:
#  w = [1, 1], b = -1.5
# Checa: w·x + b >= 0 solo en (1,1)
w_and = np.array([1, 1])
b_and = -1.5

plot_gate(X_and, y_and, "Compuerta AND (linealmente separable)", w_and, b_and)

# OR

X_or = np.array([[0,0],[0,1],[1,0],[1,1]])
y_or = np.array([0,1,1,1])

# Para OR, una frontera sencilla:
#  w = [1, 1], b = -0.5
# Checa: w·x + b >=0 excepto en (0,0)
w_or = np.array([1, 1])
b_or = -0.5

plot_gate(X_or, y_or, "Compuerta OR (linealmente separable)", w_or, b_or)

# XOR

X_xor = np.array([[0,0],[0,1],[1,0],[1,1]])
y_xor = np.array([0,1,1,0])

# A XOR no le pasamos w,b porque NO existe una línea única que lo separe
plot_gate(X_xor, y_xor, "Compuerta XOR (NO linealmente separable)")