class Planificador:
    def __init__(self):
        # Estado inicial
        self.estado = {
            "luz_encendida": False,
            "puerta_abierta": False
        }

    # Método para abrir la puerta
    def abrir_puerta(self):
        print("Abriendo la puerta...")
        self.estado["puerta_abierta"] = True

    # Método para encender la luz
    def encender_luz(self):
        if self.estado["puerta_abierta"]:
            print("Encendiendo la luz...")
            self.estado["luz_encendida"] = True
        else:
            print("No se puede encender la luz, la puerta está cerrada.")

    # Método para planificar las acciones
    def planificar(self):
        print("Planificando acciones...")
        self.abrir_puerta()   # Primero abrir la puerta
        self.encender_luz()   # Luego encender la luz

# Creamos una instancia del planificador
planificador = Planificador()

# Llamamos al método de planificación
planificador.planificar()
