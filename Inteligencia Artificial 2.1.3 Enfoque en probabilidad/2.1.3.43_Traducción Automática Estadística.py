# Definimos un diccionario que simula una base de datos de traducciones.
diccionario_traducciones = {
    'Fernanda': 'Fernanda',
    'Emmanuel': 'Emmanuel',
    'Emiliano': 'Emiliano',
    'Eliott': 'Eliott',
    'Hola': 'Hello',
    'Mundo': 'World',
    '¿Cómo estás?': 'How are you?',
    'Bien, gracias.': 'I am fine, thank you.'
}

def traducir_frase(frase):
    """
    Función para traducir una frase del español al inglés utilizando un diccionario de traducción.
    
    Args:
        frase (str): La frase en español que se desea traducir.
    
    Returns:
        str: La traducción en inglés o un mensaje de error si no se encuentra.
    """
    # Separamos la frase en palabras
    palabras = frase.split()  # Dividimos la frase en palabras
    traduccion = []  # Lista para almacenar las traducciones

    # Iteramos sobre cada palabra de la frase
    for palabra in palabras:
        # Buscamos la traducción en el diccionario
        if palabra in diccionario_traducciones:
            # Añadimos la traducción a la lista
            traduccion.append(diccionario_traducciones[palabra])
        else:
            # Si no encontramos la palabra, la agregamos tal cual
            traduccion.append(f"[{palabra} no encontrado]")

    # Unimos las traducciones en una sola cadena
    return ' '.join(traduccion)

# Ejemplo de uso de la función
frase_a_traducir = 'Hola Mundo'  # Frase que queremos traducir
resultado_traduccion = traducir_frase(frase_a_traducir)  # Llamamos a la función
print("Traducción:", resultado_traduccion)  # Imprimimos el resultado
