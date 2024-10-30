class EspacioDeEstados:
    def __init__(self, ancho, alto):
        # Inicializamos el espacio de estados con un tamaño definido
        self.ancho = ancho
        self.alto = alto
        self.posicion = (0, 0)  # Posición inicial en la esquina superior izquierda

    # Método para mostrar la posición actual
    def mostrar_posicion(self):
        print(f"Posición actual: {self.posicion}")

    # Método para mover al agente
    def mover(self, direccion):
        x, y = self.posicion
        
        # Actualizamos la posición según la dirección
        if direccion == "arriba":
            if y < self.alto - 1:  # Verificamos los límites
                y += 1
        elif direccion == "abajo":
            if y > 0:  # Verificamos los límites
                y -= 1
        elif direccion == "izquierda":
            if x > 0:  # Verificamos los límites
                x -= 1
        elif direccion == "derecha":
            if x < self.ancho - 1:  # Verificamos los límites
                x += 1
        
        self.posicion = (x, y)  # Actualizamos la posición

# Creamos un espacio de estados de 3x3
espacio = EspacioDeEstados(3, 3)

# Mostramos la posición inicial
espacio.mostrar_posicion()

# Movemos al agente en diferentes direcciones
espacio.mover("arriba")
espacio.mostrar_posicion()

espacio.mover("derecha")
espacio.mostrar_posicion()

espacio.mover("abajo")
espacio.mostrar_posicion()
