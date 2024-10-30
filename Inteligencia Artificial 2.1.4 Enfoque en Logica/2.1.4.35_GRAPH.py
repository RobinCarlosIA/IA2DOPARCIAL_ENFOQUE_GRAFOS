class GraphPlan:
    def __init__(self):
        # Inicializamos los estados y las acciones
        self.estados = set()  # Conjunto de estados
        self.acciones = []    # Lista de acciones

    # Método para añadir un estado
    def añadir_estado(self, estado):
        self.estados.add(estado)

    # Método para añadir una acción
    def añadir_accion(self, accion, precondiciones, efectos):
        # Guardamos la acción junto con sus precondiciones y efectos
        self.acciones.append({"accion": accion, "precondiciones": precondiciones, "efectos": efectos})

    # Método para ejecutar GRAPHPLAN
    def planificar(self):
        # Inicializamos el conjunto de estados alcanzables
        estados_alcanzables = set()

        # Añadimos los estados iniciales al conjunto
        for estado in self.estados:
            estados_alcanzables.add(estado)

        # Intentamos aplicar cada acción a los estados alcanzables
        for accion in self.acciones:
            if all(pre in estados_alcanzables for pre in accion["precondiciones"]):
                # Si todas las precondiciones están satisfechas, aplicamos la acción
                for efecto in accion["efectos"]:
                    estados_alcanzables.add(efecto)  # Añadimos los efectos al conjunto de estados alcanzables
                print(f"Ejecutando acción: {accion['accion']}")

        return estados_alcanzables  # Devolvemos los estados alcanzables

# Creamos una instancia de GraphPlan
graph_plan = GraphPlan()

# Añadimos algunos estados iniciales
graph_plan.añadir_estado("A")
graph_plan.añadir_estado("B")

# Añadimos acciones con sus precondiciones y efectos
graph_plan.añadir_accion("Acción 1", ["A"], ["C"])
graph_plan.añadir_accion("Acción 2", ["B"], ["D"])
graph_plan.añadir_accion("Acción 3", ["C", "D"], ["E"])

# Llamamos al método para planificar
estados_resultantes = graph_plan.planificar()

# Mostramos los estados alcanzables después de la planificación
print("Estados alcanzables:", estados_resultantes)
