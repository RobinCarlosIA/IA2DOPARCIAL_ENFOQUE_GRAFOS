# Base de conocimiento: clasificaciones de animales
base_conocimiento = {
    "perro": "mamífero, domesticado",
    "gato": "mamífero, domesticado",
    "lobo": "mamífero, salvaje",
    "salmon": "pez, acuático",
    "aguila": "ave, volador"
}

# Función para responder preguntas sobre animales
def obtener_informacion_animal(animal):
    # Convertimos el nombre del animal a minúsculas para evitar errores
    animal = animal.lower()
    
    # Buscamos en la base de conocimiento
    if animal in base_conocimiento:
        return f"{animal.capitalize()} es un {base_conocimiento[animal]}."
    else:
        return "No tengo información sobre ese animal."

# Ejemplo de uso
animal_a_consultar = "Perro"  # Preguntamos por el perro
resultado = obtener_informacion_animal(animal_a_consultar)
print(resultado)

animal_a_consultar = "Tortuga"  # Preguntamos por un animal no conocido
resultado = obtener_informacion_animal(animal_a_consultar)
print(resultado)
