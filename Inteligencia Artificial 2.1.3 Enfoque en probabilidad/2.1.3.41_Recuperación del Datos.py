# Definimos un diccionario para almacenar información sobre varias personas
datos_personas = {
    'Fernanda': {'edad': 25, 'ciudad': 'Guadalajara'},
    'Emmanuel': {'edad': 30, 'ciudad': 'Zapopan'},
    'Emiliano': {'edad': 28, 'ciudad': 'Tlaquepaque'},
    'Eliott': {'edad': 22, 'ciudad': 'Tonala'}
}

def recuperar_datos(nombre):
    """
    Función para recuperar datos de una persona dado su nombre.
    
    Args:
        nombre (str): El nombre de la persona a buscar.
    
    Returns:
        str: Mensaje con los datos de la persona o un mensaje de error si no se encuentra.
    """
    # Verificamos si el nombre está en el diccionario
    if nombre in datos_personas:
        datos = datos_personas[nombre]  # Obtenemos los datos de la persona
        return f"{nombre} tiene {datos['edad']} años y vive en {datos['ciudad']}."  # Retornamos los datos formateados
    else:
        return "No se encontraron datos para el nombre proporcionado."  # Mensaje de error si no se encuentra el nombre

# Ejemplo de uso de la función
nombre_a_buscar = 'Fernanda'  # Nombre que queremos buscar
resultado = recuperar_datos(nombre_a_buscar)  # Llamamos a la función
print(resultado)  # Imprimimos el resultado
