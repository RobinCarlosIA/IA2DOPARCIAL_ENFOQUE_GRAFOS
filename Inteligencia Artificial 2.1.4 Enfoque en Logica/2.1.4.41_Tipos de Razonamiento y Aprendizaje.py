# Definimos una clase para representar un sistema de reglas
class SistemaDeReglas:
    def __init__(self):
        self.reglas = []  # Inicializamos una lista para almacenar las reglas

    def agregar_regla(self, condicion, accion):
        # Añadimos una nueva regla al sistema
        self.reglas.append((condicion, accion))

    def razonar(self, entrada):
        # Revisamos las reglas para encontrar una que coincida con la entrada
        for condicion, accion in self.reglas:
            if condicion(entrada):
                print(f"Condición cumplida: {entrada}. Se ejecuta acción: {accion.__name__}")
                accion()  # Ejecutamos la acción asociada a la regla
                return  # Salimos después de ejecutar la primera acción

        print(f"No se encontró ninguna regla que coincida con: {entrada}")

# Definimos algunas acciones simples
def accion_a():
    print("Ejecutando acción A.")

def accion_b():
    print("Ejecutando acción B.")

# Creamos un sistema de reglas
sistema = SistemaDeReglas()

# Agregamos reglas al sistema
sistema.agregar_regla(lambda x: x > 10, accion_a)  # Si la entrada es mayor a 10, ejecuta acción A
sistema.agregar_regla(lambda x: x <= 10, accion_b)  # Si la entrada es menor o igual a 10, ejecuta acción B

# Probamos el sistema con diferentes entradas
print("Probando el sistema con la entrada 5:")
sistema.razonar(5)  # Debe ejecutar acción B

print("\nProbando el sistema con la entrada 15:")
sistema.razonar(15)  # Debe ejecutar acción A
