import random

# Definimos una clase que simula un proceso estacionario
class ProcesoEstacionario:
    def __init__(self):
        # Las probabilidades de permanecer en los mismos estados son constantes.
        self.probabilidades = {
            'Fernanda': {'Fernanda': 0.6, 'Emmanuel': 0.2, 'Emiliano': 0.2},
            'Emmanuel': {'Fernanda': 0.1, 'Emmanuel': 0.8, 'Emiliano': 0.1},
            'Emiliano': {'Fernanda': 0.3, 'Emmanuel': 0.3, 'Emiliano': 0.4}
        }

    def siguiente_estado(self, estado_actual):
        """
        Determinamos el siguiente estado en función de las probabilidades estacionarias.
        """
        opciones = list(self.probabilidades[estado_actual].keys())  # Obtenemos los posibles estados
        pesos = list(self.probabilidades[estado_actual].values())  # Las probabilidades asociadas a esos estados
        return random.choices(opciones, pesos)[0]  # Seleccionamos el siguiente estado de forma aleatoria

    def simular(self, estado_inicial, pasos):
        """
        Simula el proceso durante un número de pasos, comenzando desde el estado inicial.
        """
        estado_actual = estado_inicial  # Empezamos en el estado inicial
        camino = [estado_actual]  # Aquí vamos a guardar el camino

        # Simulamos el proceso por el número de pasos indicados
        for _ in range(pasos):
            estado_actual = self.siguiente_estado(estado_actual)  # Determinamos el próximo estado
            camino.append(estado_actual)  # Guardamos el estado en el camino

        return camino  # Devolvemos el camino completo

# Ejemplo de uso:
proceso = ProcesoEstacionario()  # Creamos una instancia del proceso estacionario

# Simulamos el proceso, comenzando desde 'Fernanda' y con 10 pasos
camino = proceso.simular('Fernanda', 10)

# Mostramos el camino recorrido
print("Camino recorrido:", camino)
