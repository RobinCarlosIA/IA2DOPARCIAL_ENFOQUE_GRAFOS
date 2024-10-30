import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np

# Datos de entrada (X) y salida esperada (y) para el problema de la compuerta XOR
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=np.float32)  # Entradas
y = np.array([[0], [1], [1], [0]], dtype=np.float32)              # Salidas deseadas

# Crear el modelo de red neuronal
model = Sequential()

# Capa de entrada con 2 neuronas y una capa oculta de 4 neuronas con función de activación ReLU
model.add(Dense(4, input_dim=2, activation='relu'))

# Capa de salida con 1 neurona y función de activación sigmoide (clasificación binaria)
model.add(Dense(1, activation='sigmoid'))

# Compilar el modelo con la función de pérdida y el optimizador para la retropropagación
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Entrenar el modelo: ajusta los pesos usando retropropagación del error para minimizar la pérdida
model.fit(X, y, epochs=1000, verbose=0)  # Entrenamiento silencioso (verbose=0) con 1000 épocas

# Evaluar el modelo con los datos de entrada para ver la precisión
loss, accuracy = model.evaluate(X, y)
print("Pérdida:", loss)
print("Precisión:", accuracy)

# Realizar predicciones en los mismos datos de entrada
predicciones = model.predict(X)
print("Predicciones:")
print(predicciones)
