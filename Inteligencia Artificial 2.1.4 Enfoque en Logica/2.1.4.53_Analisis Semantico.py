# Definimos una clase para representar el análisis semántico
class AnalisisSemantico:
    def __init__(self):
        # Almacenamos las variables definidas en el contexto
        self.variables_definidas = set()  # Usamos un conjunto para las variables

    def definir_variable(self, nombre_variable):
        # Agregamos la variable al conjunto de variables definidas
        self.variables_definidas.add(nombre_variable)

    def usar_variable(self, nombre_variable):
        # Verificamos si la variable ha sido definida
        if nombre_variable not in self.variables_definidas:
            print(f"Error: La variable '{nombre_variable}' no ha sido definida.")
        else:
            print(f"Variable '{nombre_variable}' utilizada correctamente.")

# Creamos una instancia del análisis semántico
analizador = AnalisisSemantico()

# Definimos algunas variables
analizador.definir_variable("x")
analizador.definir_variable("y")

# Usamos variables definidas y no definidas
analizador.usar_variable("x")  # Debería ser correcto
analizador.usar_variable("y")  # Debería ser correcto
analizador.usar_variable("z")  # Debería mostrar un error
