# Definimos una clase para representar una Creencia
class Creencia:
    def __init__(self, descripcion):
        self.descripcion = descripcion  # Descripción de la creencia
        self.eventos = []                # Lista para almacenar eventos relacionados con la creencia

    # Método para agregar un evento a la creencia
    def agregar_evento(self, evento):
        self.eventos.append(evento)

    # Método para mostrar la creencia y sus eventos
    def mostrar_creencia(self):
        print(f"Creencia: {self.descripcion}")
        print("Eventos asociados:")
        for evento in self.eventos:
            print(f"- {evento}")

# Creamos una creencia sobre el clima
creencia_clima = Creencia("El clima será soleado mañana")

# Agregamos eventos relacionados con esta creencia
creencia_clima.agregar_evento("El meteorólogo predijo sol")
creencia_clima.agregar_evento("La temperatura subió hoy")

# Mostramos la creencia y sus eventos
creencia_clima.mostrar_creencia()
