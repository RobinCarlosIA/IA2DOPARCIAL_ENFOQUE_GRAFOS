import numpy as np

# Definimos la clase del Perceptrón
class Perceptron:
    def __init__(self, pesos, umbral=0):
        self.pesos = pesos  # Lista de pesos para cada entrada
        self.umbral = umbral  # Umbral para activar la salida

    def predecir(self, entrada):
        # Calcula la salida usando la suma ponderada y el umbral
        suma = np.dot(entrada, self.pesos)  # Producto punto
        return 1 if suma >= self.umbral else 0  # Activa si supera el umbral


# Definimos la clase ADALINE
class ADALINE:
    def __init__(self, pesos, tasa_aprendizaje=0.01):
        self.pesos = pesos  # Lista de pesos
        self.tasa_aprendizaje = tasa_aprendizaje  # Tasa de ajuste para los pesos

    def entrenar(self, entrada, objetivo):
        # Calcula la salida y ajusta los pesos
        salida = np.dot(entrada, self.pesos)  # Suma ponderada
        error = objetivo - salida  # Calcula el error
        self.pesos += self.tasa_aprendizaje * error * entrada  # Ajusta los pesos según el error
        return salida  # Devuelve la salida calculada


# Definimos la clase MADALINE
class MADALINE:
    def __init__(self, neuronas):
        self.neuronas = neuronas  # Lista de instancias ADALINE

    def predecir(self, entrada):
        # Cada ADALINE hace una predicción y se toma la mayoría
        salidas = [neurona.entrenar(entrada, 1) for neurona in self.neuronas]
        return 1 if sum(salidas) > len(salidas) / 2 else 0  # Activa si mayoría lo hace


# Creamos una instancia del Perceptrón
perceptron = Perceptron(pesos=np.array([0.5, -0.5]), umbral=0.1)

# Creamos una instancia de ADALINE con tasa de aprendizaje
adaline = ADALINE(pesos=np.array([0.5, -0.5]), tasa_aprendizaje=0.01)

# Creamos una instancia de MADALINE con dos ADALINEs
madaline = MADALINE(neuronas=[ADALINE(np.array([0.5, -0.5])), ADALINE(np.array([0.3, -0.3]))])

# Entrada de prueba
entrada = np.array([1, -1])

# Probamos el Perceptrón
print("Salida Perceptrón:", perceptron.predecir(entrada))

# Probamos el ADALINE
print("Salida ADALINE:", adaline.entrenar(entrada, 1))

# Probamos el MADALINE
print("Salida MADALINE:", madaline.predecir(entrada))
