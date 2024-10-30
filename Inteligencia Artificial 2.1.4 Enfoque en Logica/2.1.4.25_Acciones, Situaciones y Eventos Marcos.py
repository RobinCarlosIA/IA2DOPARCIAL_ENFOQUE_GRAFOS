# Definimos una clase para representar un Marco
class Marco:
    def __init__(self, nombre):
        self.nombre = nombre  # Nombre del marco
        self.acciones = []     # Lista para almacenar acciones en este marco
        self.situaciones = []  # Lista para almacenar situaciones en este marco

    # Método para agregar una acción al marco
    def agregar_accion(self, accion):
        self.acciones.append(accion)

    # Método para agregar una situación al marco
    def agregar_situacion(self, situacion):
        self.situaciones.append(situacion)

    # Método para mostrar el contenido del marco
    def mostrar_marco(self):
        print(f"Marco: {self.nombre}")
        print("Acciones:")
        for accion in self.acciones:
            print(f"- {accion}")
        print("Situaciones:")
        for situacion in self.situaciones:
            print(f"- {situacion}")

# Creamos un marco para una situación de "Comer"
marco_comer = Marco("Comer")

# Agregamos acciones y situaciones al marco
marco_comer.agregar_accion("Tomar un plato")
marco_comer.agregar_accion("Servir la comida")
marco_comer.agregar_situacion("El restaurante está lleno")
marco_comer.agregar_situacion("La comida está lista")

# Mostramos el contenido del marco
marco_comer.mostrar_marco()
