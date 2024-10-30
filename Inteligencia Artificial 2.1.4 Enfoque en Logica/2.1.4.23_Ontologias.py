# Definimos una clase para representar un Animal
class Animal:
    def __init__(self, nombre, color):
        self.nombre = nombre  # Nombre del animal
        self.color = color    # Color del animal

# Creamos una lista para almacenar nuestros animales
animales = []

# Creamos algunos objetos de tipo Animal
perro = Animal("Perro", "Marrón")
gato = Animal("Gato", "Negro")

# Agregamos los animales a la lista
animales.append(perro)
animales.append(gato)

# Función para mostrar la información de los animales
def mostrar_animales(animales):
    print("Lista de Animales:")
    for animal in animales:
        print(f"Nombre: {animal.nombre}, Color: {animal.color}")

# Llamamos a la función para mostrar la información
mostrar_animales(animales)
