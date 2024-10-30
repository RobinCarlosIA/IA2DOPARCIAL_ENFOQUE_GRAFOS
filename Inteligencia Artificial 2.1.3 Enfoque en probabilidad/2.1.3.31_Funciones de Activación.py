import numpy as np

# Definimos una clase simple para representar una Neurona con diferentes funciones de activación
class Neurona:
    def __init__(self, peso):
        # La neurona tiene un solo peso que multiplicará la entrada
        self.peso = peso

    def sigmoide(self, entrada):
        # La función sigmoide devuelve un valor entre 0 y 1
        return 1 / (1 + np.exp(-entrada * self.peso))

    def relu(self, entrada):
        # La función ReLU devuelve 0 si la entrada es negativa, o la misma entrada si es positiva
        return max(0, entrada * self.peso)

    def tanh(self, entrada):
        # La función tanh devuelve valores entre -1 y 1
        return np.tanh(entrada * self.peso)

# Creamos una instancia de la neurona con un peso de 0.5
neurona = Neurona(peso=0.5)

# Probamos diferentes entradas en las funciones de activación
entradas = [-2, -1, 0, 1, 2]  # Conjunto de entradas para probar los efectos de las funciones de activación

# Calculamos y mostramos los resultados de cada función de activación para cada entrada
for entrada in entradas:
    print(f"\nEntrada: {entrada}")
    print(f"Salida Sigmoide: {neurona.sigmoide(entrada):.4f}")
    print(f"Salida ReLU: {neurona.relu(entrada):.4f}")
    print(f"Salida Tanh: {neurona.tanh(entrada):.4f}")
