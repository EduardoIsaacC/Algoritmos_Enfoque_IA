import numpy as np
import matplotlib.pyplot as plt

# UTILIDADES GENERALES

def step(u):
    """Función de activación escalón binaria: 1 si u>=0, si no 0."""
    return 1 if u >= 0 else 0

def plot_decision_boundary(weights, bias, X, y, title):
    """
    Dibuja puntos y la recta de decisión de un modelo lineal 2D.
    Solo funciona si X tiene 2 características.
    """
    plt.figure()
    # Pinta los puntos de entrenamiento
    for i in range(len(X)):
        color = 'red' if y[i] == 1 else 'blue'
        plt.scatter(X[i][0], X[i][1], c=color)

    # Calcula la línea de separación (w1*x + w2*y + b = 0)
    # => y = -(w1*x + b)/w2
    x_line = np.linspace(-0.5, 1.5)
    if abs(weights[1]) < 1e-6:
        # Evitar división entre 0 si w2 es ~0
        y_line = np.zeros_like(x_line)
    else:
        y_line = -(weights[0]*x_line + bias)/weights[1]

    plt.plot(x_line, y_line, 'k--')
    plt.title(title)
    plt.xlabel("x1")
    plt.ylabel("x2")
    plt.grid()
    plt.show()

# 1) PERCEPTRÓN
#    - Aprende una compuerta lógica OR
#    - Salida binaria con función escalón
#    - Regla de aprendizaje del perceptrón

def entrenar_perceptron(X, d, lr=0.1, epochs=10):
    """
    X: entradas (N x 2)
    d: salidas deseadas (N)
    lr: learning rate
    epochs: épocas de entrenamiento
    """
    np.random.seed(42)
    w = np.random.rand(2)    # pesos iniciales
    b = np.random.rand()     # sesgo inicial

    for epoch in range(epochs):
        for i in range(len(X)):
            u = np.dot(X[i], w) + b
            y = 1 if u >= 0 else 0  # salida binaria
            error = d[i] - y
            # Regla de actualización del perceptrón
            w = w + lr * error * X[i]
            b = b + lr * error
        # Debug opcional por época
        # print(f"[Perceptrón] Época {epoch+1}: w={w}, b={b:.3f}")
    return w, b

def probar_perceptron(X, w, b):
    resultados = []
    for i in range(len(X)):
        u = np.dot(X[i], w) + b
        y = 1 if u >= 0 else 0
        resultados.append(y)
    return resultados

# 2) ADALINE
#    - Aprende AND
#    - Salida lineal (no aplica escalón en entrenamiento)
#    - Minimiza error cuadrático medio

def entrenar_adaline(X, d, lr=0.1, epochs=20):
    """
    ADALINE ajusta pesos usando gradiente del error cuadrático.
    """
    np.random.seed(42)
    w = np.random.rand(2)
    b = np.random.rand()

    errors_por_epoca = []

    for epoch in range(epochs):
        total_error = 0
        for i in range(len(X)):
            # Salida lineal
            y = np.dot(X[i], w) + b
            error = d[i] - y
            # Regla Widrow-Hoff (Delta rule)
            w += lr * error * X[i]
            b += lr * error
            total_error += error**2
        errors_por_epoca.append(total_error)
        # Debug opcional
        # print(f"[ADALINE] Época {epoch+1}: Error={total_error:.4f}")

    return w, b, errors_por_epoca

def probar_adaline(X, w, b, umbral=0.5):
    """
    Para tomar decisiones binarias al final,
    umbralizamos la salida lineal.
    """
    resultados_crisp = []
    salidas_reales = []
    for i in range(len(X)):
        y = np.dot(X[i], w) + b
        salidas_reales.append(y)
        resultados_crisp.append(1 if y >= umbral else 0)
    return resultados_crisp, salidas_reales

# 3) MADALINE
#    - Múltiples ADALINE + una capa de salida
#    - Objetivo clásico: resolver XOR
#
#    Arquitectura que vamos a usar (mínima):
#    Capa oculta: 2 neuronas tipo ADALINE con activación escalón
#    Capa salida: 1 neurona tipo ADALINE con activación escalón
#
#    Nota: MADALINE histórica usaba reglas específicas (Rule I, II).
#    Aquí haremos una aproximación entrenando por búsqueda simple
#    de pesos, solo con retroajuste manual pequeñito.

class Madaline:
    """
    MADALINE de 2-2-1 hecha a mano para XOR.
    - capa_oculta: 2 unidades
    - capa_salida: 1 unidad
    Usaremos activación escalón (0/1) en cada neurona.
    Entrenamiento: ajuste muy básico por prueba y error local.
    (Esto es una versión educativa, NO es backprop moderno).
    """

    def __init__(self, lr=0.1, epochs=2000, seed=0):
        np.random.seed(seed)
        # Pesos de la capa oculta (2 neuronas ocultas, 2 entradas)
        self.W_hidden = np.random.uniform(-1, 1, (2, 2))  # shape (2_neuronas, 2_features)
        self.b_hidden = np.random.uniform(-1, 1, 2)       # shape (2,)
        # Pesos de la capa de salida (1 neurona, 2 entradas ocultas)
        self.W_out = np.random.uniform(-1, 1, (1, 2))     # shape (1, 2_hidden)
        self.b_out = np.random.uniform(-1, 1, 1)          # shape (1,)

        self.lr = lr
        self.epochs = epochs

    def activacion_binaria(self, u):
        return np.where(u >= 0, 1, 0)

    def forward(self, x):
        """
        Pasa hacia delante:
        x: (2,) -> salida_oculta: (2,) -> salida_final: escalar binario
        """
        u_hidden = np.dot(self.W_hidden, x) + self.b_hidden    # (2,)
        z_hidden = self.activacion_binaria(u_hidden)           # (2,)
        u_out = np.dot(self.W_out, z_hidden) + self.b_out      # (1,)
        y = self.activacion_binaria(u_out)[0]                  # escalar 0/1
        return y, z_hidden

    def train(self, X, d):
        """
        Entrenamiento muy simple estilo MADALINE:
        - Para cada patrón:
          * Calcula salida
          * Si hay error, intenta ajustar pesos de la capa de salida
            y luego (si sigue mal) de la capa oculta.
        Nota: Esto no es gradiente descendente clásico. Es didáctico.
        """
        for epoch in range(self.epochs):
            errores = 0
            for i in range(len(X)):
                x = X[i]
                target = d[i]

                y, z_hidden = self.forward(x)

                if y != target:
                    errores += 1

                    # Ajustar capa de salida como una ADALINE con regla delta binaria
                    # y <- step(W_out · z_hidden + b_out)
                    # error = target - y
                    error_out = target - y
                    self.W_out += self.lr * error_out * z_hidden.reshape(1, -1)
                    self.b_out += self.lr * error_out

                    # Volvemos a predecir después de cambiar salida
                    y2, z_hidden2 = self.forward(x)

                    # Si sigue mal, tratamos de ajustar la oculta neurona por neurona
                    if y2 != target:
                        # Ajuste local: probamos cambiar cada neurona oculta
                        # para que se alinee mejor al target final
                        for h in range(2):
                            # Si cambiando la activación de la neurona h
                            # ayudaría a la salida, empujamos pesos de esa neurona.
                            # Heurística sencilla:
                            deseado_en_hidden = 1 if (target == 1) else 0
                            if z_hidden[h] != deseado_en_hidden:
                                error_h = deseado_en_hidden - z_hidden[h]
                                self.W_hidden[h] += self.lr * error_h * x
                                self.b_hidden[h] += self.lr * error_h
            # Si ya no hay errores, podemos parar antes
            if errores == 0:
                break

    def predict(self, X):
        preds = []
        for i in range(len(X)):
            y, _ = self.forward(X[i])
            preds.append(y)
        return preds

# PROGRAMA DEMO

if __name__ == "__main__":

    # 1) PERCEPTRÓN con OR

    X_or = np.array([[0,0],[0,1],[1,0],[1,1]])
    y_or = np.array([0,1,1,1])  # verdad OR

    w_p, b_p = entrenar_perceptron(X_or, y_or, lr=0.1, epochs=10)
    resultados_perc = probar_perceptron(X_or, w_p, b_p)

    print(" PERCEPTRÓN (OR) ")
    for i in range(len(X_or)):
        print(f"Entrada {X_or[i]} -> Predicción {resultados_perc[i]} (Real {y_or[i]})")

    # Dibujar frontera de decisión del perceptrón
    plot_decision_boundary(w_p, b_p, X_or, y_or, "Perceptrón aprendiendo OR")

    # 2) ADALINE con AND
    
    X_and = np.array([[0,0],[0,1],[1,0],[1,1]])
    y_and = np.array([0,0,0,1])  # verdad AND

    w_a, b_a, errores = entrenar_adaline(X_and, y_and, lr=0.1, epochs=20)
    resultados_bin, salidas_reales = probar_adaline(X_and, w_a, b_a, umbral=0.5)

    print("\n ADALINE (AND) ")
    for i in range(len(X_and)):
        print(f"Entrada {X_and[i]} -> Salida real {salidas_reales[i]:.3f} -> Binaria {resultados_bin[i]} (Real {y_and[i]})")

    # Graficar error por época
    plt.figure()
    plt.plot(errores)
    plt.title("Evolución del Error Cuadrático - ADALINE (AND)")
    plt.xlabel("Época")
    plt.ylabel("Error total")
    plt.grid()
    plt.show()

    # Dibujar frontera final de ADALINE (umbralizada)
    plot_decision_boundary(w_a, b_a, X_and, y_and, "ADALINE aprendiendo AND (frontera aproximada)")

    # 3) MADALINE con XOR

    X_xor = np.array([[0,0],[0,1],[1,0],[1,1]])
    y_xor = np.array([0,1,1,0])  # verdad XOR

    mad = Madaline(lr=0.2, epochs=5000, seed=0)
    mad.train(X_xor, y_xor)
    preds_xor = mad.predict(X_xor)

    print("\n MADALINE (XOR) ")
    for i in range(len(X_xor)):
        print(f"Entrada {X_xor[i]} -> Predicción {preds_xor[i]} (Real {y_xor[i]})")

    # Nota: fronteras de decisión XOR ya no son una sola línea recta,
    # son regiones combinadas por dos neuronas ocultas, así que no
    # podemos graficarlo con una sola recta como en Perceptrón/ADALINE.
