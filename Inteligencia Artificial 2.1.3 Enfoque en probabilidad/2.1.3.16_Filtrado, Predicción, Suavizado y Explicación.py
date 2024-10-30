import random

# Definimos una clase que representa el sistema de estimaciones probabilísticas
class EstimacionProbabilistica:
    def __init__(self):
        # Definimos las probabilidades de transición entre los estados (las personas).
        self.transiciones = {
            'Fernanda': {'Fernanda': 0.6, 'Emmanuel': 0.3, 'Emiliano': 0.1},
            'Emmanuel': {'Fernanda': 0.2, 'Emmanuel': 0.5, 'Emiliano': 0.3},
            'Emiliano': {'Fernanda': 0.4, 'Emmanuel': 0.2, 'Emiliano': 0.4}
        }

    def filtrar(self, estado_actual):
        """
        Filtrado: Estimamos el estado actual basado en el estado previo.
        """
        return random.choices(list(self.transiciones[estado_actual].keys()), 
                              list(self.transiciones[estado_actual].values()))[0]

    def predecir(self, estado_actual):
        """
        Predicción: Intentamos prever el siguiente estado basado en el actual.
        """
        return self.filtrar(estado_actual)

    def suavizar(self, historia):
        """
        Suavizado: Ajustamos la estimación usando información previa y futura.
        """
        return historia[-1]  # En este caso, suavizamos el último estado con el presente

    def explicar(self, historia):
        """
        Explicación: Mostramos una posible explicación de la secuencia de estados.
        """
        explicacion = " -> ".join(historia)
        return f"Camino seguido: {explicacion}"

# Ejemplo de uso:
sistema = EstimacionProbabilistica()

# Estado inicial
estado_inicial = 'Fernanda'

# Filtramos el estado inicial
estado_filtrado = sistema.filtrar(estado_inicial)
print("Estado filtrado:", estado_filtrado)

# Hacemos una predicción del siguiente estado
estado_predicho = sistema.predecir(estado_filtrado)
print("Estado predicho:", estado_predicho)

# Guardamos la historia de los estados para suavizado
historia = [estado_inicial, estado_filtrado, estado_predicho]

# Suavizamos el estado final con la historia
estado_suavizado = sistema.suavizar(historia)
print("Estado suavizado:", estado_suavizado)

# Explicamos el camino recorrido
explicacion = sistema.explicar(historia)
print(explicacion)
