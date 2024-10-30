# Importamos las bibliotecas necesarias
import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.datasets import mnist  # Conjunto de datos MNIST

# 1. Cargar el conjunto de datos MNIST
# Este conjunto de datos contiene imágenes de dígitos (0-9)
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# 2. Normalizar las imágenes para que los valores estén entre 0 y 1
# Las imágenes son de 28x28 píxeles, y sus valores están entre 0 y 255
x_train = x_train / 255.0
x_test = x_test / 255.0

# 3. Crear el modelo de la red neuronal
modelo = models.Sequential()

# 4. Añadir una capa de entrada (Flatten) que convierte cada imagen 28x28 en un vector de 784 valores
modelo.add(layers.Flatten(input_shape=(28, 28)))

# 5. Añadir una capa oculta completamente conectada con 128 neuronas y la activación ReLU
modelo.add(layers.Dense(128, activation='relu'))

# 6. Añadir una capa de salida con 10 neuronas (una por cada dígito, de 0 a 9) y activación softmax
modelo.add(layers.Dense(10, activation='softmax'))

# 7. Compilar el modelo, usando la función de pérdida de entropía cruzada categórica, el optimizador Adam y la métrica de precisión
modelo.compile(optimizer='adam',
               loss='sparse_categorical_crossentropy',
               metrics=['accuracy'])

# 8. Entrenar el modelo con los datos de entrenamiento (imágenes y etiquetas), durante 5 épocas
modelo.fit(x_train, y_train, epochs=5)

# 9. Evaluar el modelo con los datos de prueba
test_loss, test_acc = modelo.evaluate(x_test, y_test)
print(f'Precisión en el conjunto de prueba: {test_acc:.2f}')

# 10. Clasificar una imagen de ejemplo del conjunto de prueba
import numpy as np
imagen_ejemplo = np.expand_dims(x_test[0], axis=0)  # Expandimos la imagen para que tenga la forma correcta
prediccion = modelo.predict(imagen_ejemplo)
print(f'El modelo predice que la imagen es un: {np.argmax(prediccion)}')

