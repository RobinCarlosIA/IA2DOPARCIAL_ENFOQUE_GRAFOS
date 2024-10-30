import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np

# Generamos datos simples: un conjunto de entradas (X) y salidas esperadas (y)
# Aquí, X representa las entradas y y representa las salidas deseadas.
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=np.float32)  # Datos de entrada
y = np.array([[0], [1], [1], [0]], dtype=np.float32)              # Salida deseada para una compuerta XOR

# Creamos el modelo de red neuronal multicapa
model = Sequential()

# Capa de entrada (2 neuronas) y capa oculta (con 4 neuronas y función de activación ReLU)
model.add(Dense(4, input_dim=2, activation='relu'))

# Capa de salida (1 neurona, para la salida de XOR) con activación sigmoide para clasificación binaria
model.add(Dense(1, activation='sigmoid'))

# Compilamos el modelo usando un optimizador, una función de pérdida y métricas de precisión
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Entrenamos el modelo con nuestros datos X e y, durante 500 iteraciones (epochs)
model.fit(X, y, epochs=500, verbose=0)

# Evaluamos el modelo para ver su precisión con los mismos datos de entrada
loss, accuracy = model.evaluate(X, y)
print("Pérdida:", loss)
print("Precisión:", accuracy)

# Probamos la red con las entradas originales para ver sus predicciones
predicciones = model.predict(X)
print("Predicciones:")
print(predicciones)
