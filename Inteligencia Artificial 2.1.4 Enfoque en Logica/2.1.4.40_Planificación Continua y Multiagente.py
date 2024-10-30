import time  # Importamos time para simular demoras

class Agente:
    def __init__(self, nombre):
        self.nombre = nombre  # Nombre del agente

    def trabajar(self):
        print(f"{self.nombre} ha comenzado a trabajar.")
        time.sleep(2)  # Simulamos un trabajo de 2 segundos
        print(f"{self.nombre} ha terminado de trabajar.")

# Creamos dos agentes
agente1 = Agente("Agente A")
agente2 = Agente("Agente B")

# Simulamos la planificación continua
print("Iniciando la planificación continua...")

# Hacemos que los agentes trabajen uno tras otro
agente1.trabajar()  # Agente A trabaja
agente2.trabajar()  # Agente B trabaja

print("Todos los agentes han completado su trabajo.")
