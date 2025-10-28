import numpy as np

# Datos de entrenamiento (XOR)
X = np.array([[0,0],
              [0,1],
              [1,0],
              [1,1]])
y = np.array([[0],
              [1],
              [1],
              [0]])

# Inicialización de pesos aleatorios
np.random.seed(42)
W1 = np.random.uniform(-1, 1, (2, 2))  # capa oculta
b1 = np.random.uniform(-1, 1, (1, 2))
W2 = np.random.uniform(-1, 1, (2, 1))  # capa de salida
b2 = np.random.uniform(-1, 1, (1, 1))

# Funciones
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_deriv(x):
    return x * (1 - x)

# Entrenamiento
eta = 0.5
epochs = 10000

for epoch in range(epochs):
    # FORWARD 
    z1 = np.dot(X, W1) + b1
    a1 = sigmoid(z1)
    z2 = np.dot(a1, W2) + b2
    y_pred = sigmoid(z2)

    # BACKWARD 
    error = y - y_pred
    d_output = error * sigmoid_deriv(y_pred)     # capa de salida
    d_hidden = d_output.dot(W2.T) * sigmoid_deriv(a1)  # capa oculta

    # ACTUALIZAR PESOS 
    W2 += a1.T.dot(d_output) * eta
    b2 += np.sum(d_output, axis=0, keepdims=True) * eta
    W1 += X.T.dot(d_hidden) * eta
    b1 += np.sum(d_hidden, axis=0, keepdims=True) * eta

    if epoch % 2000 == 0:
        loss = np.mean(np.abs(error))
        print(f"Época {epoch}: Error promedio = {loss:.4f}")

#  Resultados finales 
print("\n Resultados finales (XOR) ")
for i in range(len(X)):
    print(f"Entrada: {X[i]} → Predicción: {y_pred[i][0]:.3f} (Real: {y[i][0]})")