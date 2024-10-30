import random

# Definimos una clase para simular un proceso de Markov
class ProcesoDeMarkov:
    def __init__(self):
        # Matriz de transición: probabilidades de moverse entre estados
        self.transiciones = {
            'Fernanda': {'Fernanda': 0.5, 'Emmanuel': 0.3, 'Emiliano': 0.2},
            'Emmanuel': {'Fernanda': 0.4, 'Emmanuel': 0.4, 'Emiliano': 0.2},
            'Emiliano': {'Fernanda': 0.3, 'Emmanuel': 0.3, 'Emiliano': 0.4}
        }

    def siguiente_estado(self, estado_actual):
        """
        Seleccionamos el siguiente estado basado en las probabilidades
        de transición del estado actual.
        """
        opciones = list(self.transiciones[estado_actual].keys())  # Estados posibles
        probabilidades = list(self.transiciones[estado_actual].values())  # Sus probabilidades
        return random.choices(opciones, probabilidades)[0]  # Elegimos el siguiente estado

    def simular(self, estado_inicial, pasos):
        """
        Simulamos el proceso de Markov desde un estado inicial y con un número de pasos.
        """
        estado_actual = estado_inicial  # Empezamos desde el estado inicial
        camino = [estado_actual]  # Guardamos el camino recorrido

        # Repetimos el proceso por el número de pasos
        for _ in range(pasos):
            estado_actual = self.siguiente_estado(estado_actual)  # Calculamos el siguiente estado
            camino.append(estado_actual)  # Lo agregamos al camino

        return camino  # Devolvemos el camino completo

# Ejemplo de uso:
proceso = ProcesoDeMarkov()  # Creamos una instancia del proceso de Markov

# Simulamos el proceso, empezando en 'Fernanda' y haciendo 10 pasos
camino = proceso.simular('Fernanda', 10)

# Mostramos el camino recorrido
print("Camino recorrido:", camino)
