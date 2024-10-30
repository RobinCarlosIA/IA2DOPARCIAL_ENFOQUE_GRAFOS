import random

# Definimos una clase para la simulación de la cadena de Markov
class CadenaMarkovMonteCarlo:
    def __init__(self):
        # Definimos las transiciones de estado, en este caso entre Fernanda, Emmanuel y Emiliano.
        self.transiciones = {
            'Fernanda': {'Fernanda': 0.5, 'Emmanuel': 0.3, 'Emiliano': 0.2},
            'Emmanuel': {'Fernanda': 0.1, 'Emmanuel': 0.6, 'Emiliano': 0.3},
            'Emiliano': {'Fernanda': 0.2, 'Emmanuel': 0.3, 'Emiliano': 0.5}
        }
    
    def siguiente_estado(self, estado_actual):
        """
        Método que determina el siguiente estado según las probabilidades de transición.
        """
        probabilidades = self.transiciones[estado_actual]  # Obtenemos las probabilidades del estado actual
        siguiente = random.choices(list(probabilidades.keys()), list(probabilidades.values()))[0]  # Elegimos el próximo estado
        return siguiente

    def simular(self, estado_inicial, pasos):
        """
        Método que realiza la simulación de la cadena de Markov durante un número dado de pasos.
        """
        estado_actual = estado_inicial  # Iniciamos desde el estado inicial
        camino = [estado_actual]  # Guardamos la secuencia de estados

        # Recorremos tantos pasos como se nos indique
        for _ in range(pasos):
            estado_actual = self.siguiente_estado(estado_actual)  # Determinamos el próximo estado
            camino.append(estado_actual)  # Añadimos el estado al camino

        return camino  # Retornamos el camino completo

# Ejemplo de uso:
markov = CadenaMarkovMonteCarlo()  # Creamos una instancia de la cadena de Markov

# Simulamos la cadena de Markov, comenzando desde 'Fernanda' con 10 pasos
camino = markov.simular('Fernanda', 10)

# Mostramos el camino resultante
print("Camino de estados:", camino)
