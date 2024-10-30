import random

# Definimos una clase para el modelo probabilista
class ModeloProbabilista:
    def __init__(self):
        # Probabilidades de que un evento ocurra
        self.probabilidades = {
            "evento_a": 0.8,  # 80% de probabilidad
            "evento_b": 0.5,  # 50% de probabilidad
            "evento_c": 0.2   # 20% de probabilidad
        }

    # Método para hacer una predicción basada en probabilidades
    def hacer_prediccion(self):
        print("Haciendo una predicción...")

        # Generamos un número aleatorio
        resultado = random.random()
        print(f"Número aleatorio generado: {resultado}")

        # Evaluamos el número aleatorio contra las probabilidades
        if resultado < self.probabilidades["evento_a"]:
            print("Se predice que ocurrirá el Evento A.")
        elif resultado < self.probabilidades["evento_a"] + self.probabilidades["evento_b"]:
            print("Se predice que ocurrirá el Evento B.")
        else:
            print("Se predice que ocurrirá el Evento C.")

# Creamos una instancia del modelo probabilista
modelo = ModeloProbabilista()

# Llamamos al método para hacer una predicción
modelo.hacer_prediccion()
