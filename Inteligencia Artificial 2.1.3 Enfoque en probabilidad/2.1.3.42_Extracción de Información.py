# Definimos un diccionario que contiene información sobre varias personas.
informacion_personas = {
    'Fernanda': {'edad': 25, 'ciudad': 'Guadalajara'},
    'Emmanuel': {'edad': 30, 'ciudad': 'Zapopan'},
    'Emiliano': {'edad': 28, 'ciudad': 'Tlaquepaque'},
    'Eliott': {'edad': 22, 'ciudad': 'Tonala'}
}

def extraer_informacion(nombre):
    """
    Función para extraer información de una persona dada su nombre.
    
    Args:
        nombre (str): El nombre de la persona de la cual queremos extraer información.
    
    Returns:
        str: Mensaje con la información de la persona o un mensaje de error si no se encuentra.
    """
    # Verificamos si el nombre está en el diccionario
    if nombre in informacion_personas:
        # Obtenemos la información de la persona
        datos = informacion_personas[nombre]
        # Retornamos la información formateada
        return f"{nombre} tiene {datos['edad']} años y vive en {datos['ciudad']}."
    else:
        # Mensaje de error si no se encuentra el nombre
        return "No se encontraron datos para el nombre proporcionado."

# Ejemplo de uso de la función
nombre_a_extraer = 'Emmanuel'  # Nombre que queremos extraer
resultado = extraer_informacion(nombre_a_extraer)  # Llamamos a la función
print(resultado)  # Imprimimos el resultado
