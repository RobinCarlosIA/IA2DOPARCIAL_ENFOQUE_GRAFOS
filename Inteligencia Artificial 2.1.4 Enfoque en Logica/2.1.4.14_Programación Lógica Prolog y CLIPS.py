# Base de conocimiento: Hechos sobre animales
hechos = {
    "perro": "mamífero",
    "gato": "mamífero",
    "lobo": "mamífero",
    "salmon": "pez",
    "aguila": "ave"
}

# Regla para verificar si un animal es un mamífero
def es_mamifero(animal):
    return hechos.get(animal) == "mamífero"

# Regla para obtener la categoría de un animal
def obtener_categoria(animal):
    return hechos.get(animal, "No se conoce la categoría")

# Ejemplo de uso
animales_a_verificar = ["perro", "gato", "salmon", "tortuga"]

# Verificamos cada animal
for animal in animales_a_verificar:
    if es_mamifero(animal):
        print(f"{animal.capitalize()} es un mamífero.")
    else:
        print(f"{animal.capitalize()} no es un mamífero.")
    
    # Mostramos la categoría del animal
    categoria = obtener_categoria(animal)
    print(f"La categoría de {animal} es: {categoria}")
