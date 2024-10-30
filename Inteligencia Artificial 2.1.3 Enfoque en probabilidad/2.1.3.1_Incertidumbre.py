import random  # Importamos la librería random para simular la incertidumbre.

# Definimos una clase para manejar decisiones con incertidumbre.
class Incertidumbre:
    def __init__(self):
        # Inicializamos un diccionario para almacenar las decisiones de cada persona.
        self.decisiones = {}

    def agregar_decision(self, nombre, decision):
        """Método para agregar una decisión de una persona."""
        self.decisiones[nombre] = decision  # Almacenamos la decisión de la persona.

    def tomar_decision(self, nombre):
        """Método para tomar una decisión basada en la incertidumbre."""
        # Verificamos si la persona tiene una decisión.
        if nombre in self.decisiones:
            decision = self.decisiones[nombre]
            # Simulamos un resultado aleatorio (éxito o fracaso) basado en la decisión.
            resultado = random.choice(['éxito', 'fracaso'])  # Elegimos aleatoriamente entre éxito o fracaso.
            print(f"{nombre} decidió: {decision}. Resultado: {resultado}")  # Mostramos la decisión y el resultado.
        else:
            print(f"{nombre} no tiene una decisión registrada.")  # Mensaje si no hay decisión.

# Creamos una instancia de Incertidumbre.
incertidumbre = Incertidumbre()

# Agregamos decisiones para cada persona.
incertidumbre.agregar_decision('Fernanda', 'Iniciar un nuevo proyecto')
incertidumbre.agregar_decision('Emmanuel', 'Invertir en una startup')
incertidumbre.agregar_decision('Emiliano', 'Tomar un curso en línea')

# Tomamos decisiones para cada persona y mostramos los resultados.
for nombre in ['Fernanda', 'Emmanuel', 'Emiliano']:
    incertidumbre.tomar_decision(nombre)  # Llamamos al método para tomar la decisión de la persona.
