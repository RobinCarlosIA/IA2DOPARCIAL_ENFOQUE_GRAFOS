# Definimos una lista de diccionarios con información sobre personas
personas = [
    {'nombre': 'Juan', 'edad': 28, 'ciudad': 'Guadalajara'},
    {'nombre': 'Ana', 'edad': 22, 'ciudad': 'Zapopan'},
    {'nombre': 'Luis', 'edad': 35, 'ciudad': 'Tlaquepaque'},
    {'nombre': 'María', 'edad': 30, 'ciudad': 'Tlajomulco'},
]

# Función para mostrar información relevante sobre las personas
def mostrar_informacion(personas):
    print("Información de Personas:")
    print("-----------------------")
    
    # Recorremos cada persona en la lista
    for persona in personas:
        # Mostramos los datos de la persona
        print(f"Nombre: {persona['nombre']}")
        print(f"Edad: {persona['edad']}")
        print(f"Ciudad: {persona['ciudad']}")
        print()  # Línea en blanco para mayor claridad

# Llamamos a la función para mostrar la información
mostrar_informacion(personas)

# Información adicional sobre el grupo
def informacion_adicional(personas):
    print("Información Adicional:")
    print("-----------------------")
    
    # Calculamos la edad promedio
    edades = [persona['edad'] for persona in personas]
    edad_promedio = sum(edades) / len(edades)
    
    print(f"La edad promedio del grupo es: {edad_promedio:.2f} años.")
    
# Llamamos a la función para mostrar información adicional
informacion_adicional(personas)
