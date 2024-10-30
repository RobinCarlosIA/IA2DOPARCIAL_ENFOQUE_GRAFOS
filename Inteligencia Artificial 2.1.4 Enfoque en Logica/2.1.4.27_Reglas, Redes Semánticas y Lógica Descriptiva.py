# Definimos una clase para representar un Nodo en la red semántica
class Nodo:
    def __init__(self, nombre):
        self.nombre = nombre  # Nombre del nodo
        self.relaciones = {}   # Diccionario para almacenar relaciones con otros nodos

    # Método para agregar una relación entre nodos
    def agregar_relacion(self, otro_nodo, tipo_relacion):
        self.relaciones[otro_nodo] = tipo_relacion

    # Método para mostrar las relaciones del nodo
    def mostrar_relaciones(self):
        print(f"Nodo: {self.nombre}")
        for nodo, tipo in self.relaciones.items():
            print(f"- {self.nombre} {tipo} {nodo.nombre}")

# Creamos nodos para animales y sus características
perro = Nodo("Perro")
gato = Nodo("Gato")
mamifero = Nodo("Mamífero")

# Establecemos relaciones
perro.agregar_relacion(mamifero, "es un tipo de")
gato.agregar_relacion(mamifero, "es un tipo de")

# Función para mostrar la red semántica
def mostrar_red(nodos):
    for nodo in nodos:
        nodo.mostrar_relaciones()

# Creamos una lista de nodos
red_semantica = [perro, gato, mamifero]

# Mostramos la red semántica
mostrar_red(red_semantica)
