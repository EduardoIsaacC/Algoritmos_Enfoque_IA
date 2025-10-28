import numpy as np

# Datos XOR 
X = np.array([[0,0],[0,1],[1,0],[1,1]])
y = np.array([[0],[1],[1],[0]])  # salida esperada

# Inicialización de pesos
np.random.seed(42)
W1 = np.random.uniform(-1, 1, (2, 2))  # capa oculta (2 neuronas, 2 entradas)
b1 = np.random.uniform(-1, 1, (1, 2))
W2 = np.random.uniform(-1, 1, (2, 1))  # capa salida (1 neurona, 2 entradas)
b2 = np.random.uniform(-1, 1, (1, 1))

# Funciones auxiliares
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_deriv(x):
    return x * (1 - x)

# Entrenamiento
lr = 0.5
epochs = 10000

for epoch in range(epochs):
    # Forward
    z1 = np.dot(X, W1) + b1
    a1 = sigmoid(z1)
    z2 = np.dot(a1, W2) + b2
    y_pred = sigmoid(z2)

    # Error
    error = y - y_pred

    # Backprop
    d2 = error * sigmoid_deriv(y_pred)
    d1 = d2.dot(W2.T) * sigmoid_deriv(a1)

    # Actualización de pesos
    W2 += a1.T.dot(d2) * lr
    b2 += np.sum(d2, axis=0, keepdims=True) * lr
    W1 += X.T.dot(d1) * lr
    b1 += np.sum(d1, axis=0, keepdims=True) * lr

    # Mostrar cada 2000 épocas
    if epoch % 2000 == 0:
        loss = np.mean(np.abs(error))
        print(f"Época {epoch}: Error promedio = {loss:.4f}")

# Resultados
print("\n Resultados finales (XOR) ")
for i in range(len(X)):
    print(f"Entrada: {X[i]} -> Predicción: {y_pred[i][0]:.3f} (Real: {y[i][0]})")