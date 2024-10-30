# Importamos la biblioteca numpy para trabajar con matrices y operaciones matemáticas
import numpy as np

# Definimos una clase Neurona que representará una neurona simple (perceptrón)
class Neurona:
    def __init__(self, pesos, umbral):
        # pesos: los pesos de las conexiones a las entradas de la neurona
        # umbral: el valor que debe superarse para que la neurona se active
        self.pesos = np.array(pesos)
        self.umbral = umbral

    def activacion(self, entradas):
        # Calculamos la suma ponderada: la suma de las entradas multiplicadas por sus respectivos pesos
        suma_ponderada = np.dot(entradas, self.pesos)

        # Comparamos la suma ponderada con el umbral
        if suma_ponderada >= self.umbral:
            return 1  # Si la suma supera o iguala el umbral, la neurona se activa (retorna 1)
        else:
            return 0  # Si no, la neurona no se activa (retorna 0)

# Creamos una instancia de la neurona con 2 entradas, pesos y un umbral
# Por ejemplo, la neurona tendrá 2 entradas con pesos [0.5, 0.5] y umbral 0.75
neurona = Neurona(pesos=[0.5, 0.5], umbral=0.75)

# Probamos la neurona con diferentes conjuntos de entradas
entradas_1 = [1, 1]  # Ambas entradas activas
entradas_2 = [0, 1]  # Una entrada activa
entradas_3 = [0, 0]  # Ninguna entrada activa

# Hacemos que la neurona procese las entradas
resultado_1 = neurona.activacion(entradas_1)
resultado_2 = neurona.activacion(entradas_2)
resultado_3 = neurona.activacion(entradas_3)

# Imprimimos los resultados
print(f"Resultado con entradas {entradas_1}: {resultado_1}")  # Debería activarse (1)
print(f"Resultado con entradas {entradas_2}: {resultado_2}")  # No debería activarse (0)
print(f"Resultado con entradas {entradas_3}: {resultado_3}")  # No debería activarse (0)
