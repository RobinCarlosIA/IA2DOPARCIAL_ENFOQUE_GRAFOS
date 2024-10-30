from collections import Counter

# Definir el corpus como un conjunto de oraciones
corpus = [
    "Fernanda y Emmanuel son buenos amigos",
    "Emmanuel y Eliott estudian juntos",
    "Fernanda y Eliott también son amigos",
]

# Función para construir el modelo de lenguaje simple
def modelo_probabilistico(corpus):
    # Contar todas las palabras en el corpus
    palabras = " ".join(corpus).lower().split()
    conteo_palabras = Counter(palabras)
    
    # Calcular el total de palabras
    total_palabras = sum(conteo_palabras.values())
    
    # Calcular la probabilidad de cada palabra
    modelo_prob = {palabra: conteo / total_palabras for palabra, conteo in conteo_palabras.items()}
    
    # Mostrar el modelo probabilístico
    print("Modelo probabilístico del lenguaje basado en el corpus:")
    for palabra, prob in modelo_prob.items():
        print(f"Palabra: '{palabra}' - Probabilidad: {prob:.4f}")

# Llamamos a la función con nuestro corpus
modelo_probabilistico(corpus)
