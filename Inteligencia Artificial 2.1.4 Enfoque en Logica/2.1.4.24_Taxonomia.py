# Definimos una clase base para representar una categoría de animales
class CategoriaAnimal:
    def __init__(self, nombre):
        self.nombre = nombre  # Nombre de la categoría
        self.animales = []    # Lista para almacenar los animales de esta categoría

    # Método para agregar un animal a la categoría
    def agregar_animal(self, animal):
        self.animales.append(animal)

    # Método para mostrar los animales de la categoría
    def mostrar_animales(self):
        print(f"Categoría: {self.nombre}")
        for animal in self.animales:
            print(f"- {animal}")

# Creamos categorías de animales
mamiferos = CategoriaAnimal("Mamíferos")
aves = CategoriaAnimal("Aves")

# Agregamos animales a la categoría de mamíferos
mamiferos.agregar_animal("Perro")
mamiferos.agregar_animal("Gato")

# Agregamos animales a la categoría de aves
aves.agregar_animal("Loro")
aves.agregar_animal("Aguila")

# Mostramos las categorías y sus animales
mamiferos.mostrar_animales()
aves.mostrar_animales()
