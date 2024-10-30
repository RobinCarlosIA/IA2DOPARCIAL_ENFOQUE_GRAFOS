# Definimos una clase simple para representar el proceso de Eliminación de Variables
class RedProbabilistica:
    def __init__(self):
        # Diccionario para guardar las probabilidades condicionales
        self.probabilidades = {}

    def agregar_probabilidad(self, variable, condicion, valor):
        """
        Agrega la probabilidad de una variable dada una condición.
        """
        if variable not in self.probabilidades:
            self.probabilidades[variable] = {}
        self.probabilidades[variable][condicion] = valor  # Guardamos la probabilidad condicional

    def eliminar_variable(self, variable):
        """
        Realiza la eliminación de una variable, combinando las probabilidades que dependen de ella.
        """
        if variable in self.probabilidades:
            del self.probabilidades[variable]  # Eliminamos la variable del diccionario

    def obtener_probabilidad(self, variable, condicion):
        """
        Devuelve la probabilidad de una variable dada una condición.
        """
        if variable in self.probabilidades and condicion in self.probabilidades[variable]:
            return self.probabilidades[variable][condicion]
        return 0  # Si no existe, devolvemos 0

# Creamos una instancia de la Red Probabilística
red = RedProbabilistica()

# Agregamos probabilidades condicionales para Fernanda, Emmanuel y Emiliano
red.agregar_probabilidad('Fernanda', 'Emmanuel', 0.8)
red.agregar_probabilidad('Fernanda', 'No_Emmanuel', 0.2)
red.agregar_probabilidad('Emmanuel', 'Emiliano', 0.7)
red.agregar_probabilidad('Emmanuel', 'No_Emiliano', 0.3)

# Obtenemos las probabilidades actuales antes de la eliminación
print("Probabilidad de Fernanda dado Emmanuel:", red.obtener_probabilidad('Fernanda', 'Emmanuel'))
print("Probabilidad de Emmanuel dado Emiliano:", red.obtener_probabilidad('Emmanuel', 'Emiliano'))

# Realizamos la eliminación de la variable 'Emiliano' para simplificar los cálculos
red.eliminar_variable('Emiliano')

# Tratamos de obtener las probabilidades nuevamente, pero ahora sin 'Emiliano'
print("Probabilidad de Emmanuel dado Emiliano después de eliminar Emiliano:", red.obtener_probabilidad('Emmanuel', 'Emiliano'))
