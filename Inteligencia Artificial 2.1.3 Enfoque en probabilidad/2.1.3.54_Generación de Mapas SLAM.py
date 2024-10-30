import random  # Importamos para generar posiciones aleatorias

# Clase básica de un robot con posición y un mapa de obstáculos detectados
class RobotSLAM:
    def __init__(self, nombre):
        self.nombre = nombre  # Asignamos el nombre del robot
        self.x, self.y = 0, 0  # Posición inicial del robot
        self.mapa = []  # Lista para almacenar las posiciones de obstáculos

    # Función para mover el robot en una dirección aleatoria
    def mover(self):
        self.x += random.choice([-1, 1])  # Movimiento en x
        self.y += random.choice([-1, 1])  # Movimiento en y

    # Función para detectar "obstáculos" y registrarlos en el mapa
    def detectar_obstaculo(self):
        if random.random() < 0.3:  # 30% de probabilidad de detectar obstáculo
            obstaculo = (self.x, self.y)
            self.mapa.append(obstaculo)  # Agrega la posición del obstáculo al mapa

    # Función principal para ejecutar el mapeo
    def explorar(self, pasos):
        for _ in range(pasos):
            self.mover()  # Mueve el robot
            self.detectar_obstaculo()  # Detecta obstáculos

# Instancias de robots con los nombres Fernanda, Eliott y Emiliano
fernanda = RobotSLAM("Fernanda")
eliott = RobotSLAM("Eliott")
emiliano = RobotSLAM("Emiliano")

# Cada robot explora por 50 pasos
fernanda.explorar(50)
eliott.explorar(50)
emiliano.explorar(50)

# Imprimimos el mapa generado por cada robot
print(f"Mapa de {fernanda.nombre}: {fernanda.mapa}")
print(f"Mapa de {eliott.nombre}: {eliott.mapa}")
print(f"Mapa de {emiliano.nombre}: {emiliano.mapa}")
