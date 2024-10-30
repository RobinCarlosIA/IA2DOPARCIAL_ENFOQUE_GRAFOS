# Importamos la librería collections para contar elementos
from collections import defaultdict

# Definimos una clase para el clasificador Naïve-Bayes
class NaiveBayes:
    def __init__(self):
        # Diccionario para contar las veces que aparece cada clase
        self.clases = defaultdict(int)
        # Diccionario para contar las veces que aparece cada palabra en cada clase
        self.frecuencias = defaultdict(lambda: defaultdict(int))
        # Total de palabras en cada clase
        self.total_palabras_clase = defaultdict(int)
    
    # Método para entrenar el clasificador con datos
    def entrenar(self, datos, etiquetas):
        for i in range(len(datos)):
            # Actualizamos las frecuencias de cada palabra en su respectiva clase
            for palabra in datos[i]:
                self.frecuencias[etiquetas[i]][palabra] += 1
                self.total_palabras_clase[etiquetas[i]] += 1
            # Actualizamos el conteo de la clase
            self.clases[etiquetas[i]] += 1

    # Método para predecir la clase de un nuevo dato
    def predecir(self, dato):
        probabilidades = {}
        
        # Calculamos la probabilidad para cada clase
        for clase in self.clases:
            probabilidad_clase = self.clases[clase] / sum(self.clases.values())
            probabilidad_palabra_clase = 1.0
            for palabra in dato:
                # Asumimos que cada palabra es independiente (Naïve) y aplicamos probabilidad
                probabilidad_palabra_clase *= (self.frecuencias[clase][palabra] + 1) / (self.total_palabras_clase[clase] + len(self.frecuencias[clase]))
            probabilidades[clase] = probabilidad_clase * probabilidad_palabra_clase
        
        # Retornamos la clase con mayor probabilidad
        return max(probabilidades, key=probabilidades.get)

# Ejemplo de uso
# Datos de entrenamiento (listas de palabras) y sus etiquetas (clases)
datos_entrenamiento = [
    ['amor', 'feliz', 'vida'],
    ['odio', 'triste', 'muerte'],
    ['alegría', 'feliz', 'diversión'],
    ['miedo', 'triste', 'terror']
]

etiquetas_entrenamiento = ['positivo', 'negativo', 'positivo', 'negativo']

# Creamos una instancia de nuestro clasificador Naïve-Bayes
clasificador = NaiveBayes()

# Entrenamos el modelo con los datos
clasificador.entrenar(datos_entrenamiento, etiquetas_entrenamiento)

# Hacemos una predicción con un nuevo dato
nuevo_dato = ['feliz', 'vida']
prediccion = clasificador.predecir(nuevo_dato)

# Mostramos la predicción
print("La clase predicha es:", prediccion)
