import random

# Definimos un diccionario que mapea las palabras habladas a su interpretación.
palabras_habladas = {
    "hola": "saludo",
    "adios": "despedida",
    "gracias": "agradecimiento",
    "perdon": "disculpa",
    "si": "afirmacion",
    "no": "negacion"
}

# Simulamos una función que reconoce la palabra hablada.
def reconocer_habla(entrada_habla):
    # Si la palabra está en el diccionario, devolvemos su interpretación.
    if entrada_habla in palabras_habladas:
        return palabras_habladas[entrada_habla]
    else:
        # Si no reconocemos la palabra, devolvemos "no reconocida".
        return "no reconocida"

# Simulamos el reconocimiento de algunas palabras.
palabras_posibles = ["hola", "adios", "gracias", "perdon", "si", "no", "quizas"]

# Vamos a simular que Fernanda dice una palabra aleatoria de las posibles.
palabra_hablada = random.choice(palabras_posibles)
print("Fernanda dijo:", palabra_hablada)

# Utilizamos la función de reconocimiento del habla.
resultado = reconocer_habla(palabra_hablada)
print("Interpretación de la palabra:", resultado)
