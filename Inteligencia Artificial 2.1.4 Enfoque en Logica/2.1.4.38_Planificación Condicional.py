class Accion:
    def __init__(self, nombre, condiciones, efecto):
        self.nombre = nombre  # Nombre de la acción
        self.condiciones = condiciones  # Condiciones necesarias para ejecutar la acción
        self.efecto = efecto  # Efecto de la acción si se ejecuta

    def puede_ejecutarse(self, estado_actual):
        # Verificamos si todas las condiciones están en el estado actual
        return all(condicion in estado_actual for condicion in self.condiciones)

    def ejecutar(self, estado_actual):
        # Si se puede ejecutar, actualizamos el estado
        if self.puede_ejecutarse(estado_actual):
            estado_actual.update(self.efecto)  # Aplicamos el efecto
            print(f"Ejecutando acción: {self.nombre}")
            print(f"Estado actualizado: {estado_actual}")
        else:
            print(f"No se puede ejecutar la acción: {self.nombre}. Condiciones no cumplidas.")


# Definimos un estado inicial
estado_actual = {"en_cocina", "comida_listo"}

# Creamos algunas acciones con condiciones y efectos
accion_hacer_comida = Accion("Hacer Comida", {"en_cocina"}, {"comida_hecha"})
accion_comer = Accion("Comer", {"comida_hecha"}, {"comida_comida"})

# Intentamos ejecutar las acciones
accion_hacer_comida.ejecutar(estado_actual)  # Esta acción se ejecutará
accion_comer.ejecutar(estado_actual)          # Esta acción también se ejecutará

# Agregamos un nuevo estado para mostrar una condición que falla
estado_actual.remove("comida_hecha")  # Quitamos la condición necesaria
accion_comer.ejecutar(estado_actual)  # Esta acción no se ejecutará
