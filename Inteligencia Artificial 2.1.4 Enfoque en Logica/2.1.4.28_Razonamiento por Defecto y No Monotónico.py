# Definimos una clase para representar una regla
class Regla:
    def __init__(self, condicion, conclusion):
        self.condicion = condicion  # Condición de la regla
        self.conclusion = conclusion  # Conclusión de la regla

# Definimos un conjunto de reglas por defecto
reglas_por_defecto = [
    Regla("Es un pájaro", "Puede volar"),
    Regla("Es un pez", "Puede nadar"),
]

# Definimos una función para aplicar reglas por defecto
def aplicar_reglas(animal):
    for regla in reglas_por_defecto:
        if regla.condicion in animal['caracteristicas']:
            print(f"{animal['nombre']} {regla.conclusion}")

# Información sobre un animal
animal_1 = {
    "nombre": "Loro",
    "caracteristicas": ["Es un pájaro", "Es colorido"]
}

animal_2 = {
    "nombre": "Tiburón",
    "caracteristicas": ["Es un pez", "Es grande"]
}

# Aplicamos las reglas por defecto a los animales
aplicar_reglas(animal_1)  # Debería concluir que puede volar
aplicar_reglas(animal_2)  # Debería concluir que puede nadar

# Nueva información que cambia el razonamiento
animal_1["caracteristicas"].append("No puede volar")  # Actualizamos las características del loro

# Ahora aplicamos las reglas nuevamente
print("\nDespués de nueva información:")
aplicar_reglas(animal_1)  # No debería concluir que puede volar
