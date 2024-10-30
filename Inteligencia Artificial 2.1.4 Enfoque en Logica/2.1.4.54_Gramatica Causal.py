# Definimos una clase para representar una gramática causal
class GramaticaCausal:
    def __init__(self):
        # Diccionario para almacenar las reglas causales
        self.reglas = {}

    def agregar_regla(self, causa, efecto):
        # Agregamos una regla causal al diccionario
        self.reglas[causa] = efecto

    def evaluar(self, hechos):
        # Evaluamos los efectos basados en los hechos proporcionados
        efectos = []
        for causa, efecto in self.reglas.items():
            if causa in hechos:
                efectos.append(efecto)  # Agregamos el efecto si la causa está en los hechos
        return efectos

# Creamos una instancia de la gramática causal
gramatica = GramaticaCausal()

# Agregamos algunas reglas causales
gramatica.agregar_regla("Lluvia", "Calles mojadas")
gramatica.agregar_regla("Nieve", "Calles resbaladizas")
gramatica.agregar_regla("Sol", "Gente feliz")

# Definimos los hechos actuales
hechos_actuales = ["Lluvia", "Sol"]

# Evaluamos los efectos basados en los hechos
efectos_obtenidos = gramatica.evaluar(hechos_actuales)

# Mostramos los efectos obtenidos
print("Efectos derivados de los hechos actuales:", efectos_obtenidos)
