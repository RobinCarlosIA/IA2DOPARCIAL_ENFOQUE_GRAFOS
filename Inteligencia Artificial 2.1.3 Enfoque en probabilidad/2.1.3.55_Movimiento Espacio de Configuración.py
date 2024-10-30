# Definimos una clase Robot para simular su movimiento en un espacio 2D
class Robot:
    def __init__(self, nombre, x_inicial, y_inicial):
        self.nombre = nombre  # Nombre del robot
        self.x = x_inicial  # Posición inicial en el eje x
        self.y = y_inicial  # Posición inicial en el eje y
        self.historial_movimiento = [(self.x, self.y)]  # Lista para registrar los movimientos

    # Función para mover el robot a una nueva posición
    def mover(self, delta_x, delta_y):
        self.x += delta_x  # Cambio en x
        self.y += delta_y  # Cambio en y
        self.historial_movimiento.append((self.x, self.y))  # Guardamos el nuevo punto en el historial

# Creamos robots con los nombres Fernanda, Eliott y Emiliano y posiciones iniciales
fernanda = Robot("Fernanda", 0, 0)
eliott = Robot("Eliott", 1, 1)
emiliano = Robot("Emiliano", 2, 2)

# Movemos cada robot en el espacio de configuración
fernanda.mover(1, 1)
eliott.mover(-1, 2)
emiliano.mover(0, -1)

# Imprimimos el historial de movimientos para cada robot
print(f"Historial de movimiento de {fernanda.nombre}: {fernanda.historial_movimiento}")
print(f"Historial de movimiento de {eliott.nombre}: {eliott.historial_movimiento}")
print(f"Historial de movimiento de {emiliano.nombre}: {emiliano.historial_movimiento}")
