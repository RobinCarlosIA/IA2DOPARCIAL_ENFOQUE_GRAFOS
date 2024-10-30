class Planificacion:
    def __init__(self):
        # Definimos las tareas y sus dependencias
        self.tareas = {
            "A": [],
            "B": ["A"],  # B depende de A
            "C": ["A"],  # C depende de A
            "D": ["B", "C"],  # D depende de B y C
        }
        self.plan = []  # Lista para almacenar el plan

    # Método para crear el plan
    def crear_plan(self):
        # Lista de tareas que ya se han completado
        completadas = set()

        # Mientras haya tareas por ejecutar
        while len(completadas) < len(self.tareas):
            for tarea, dependencias in self.tareas.items():
                # Verificamos si todas las dependencias están completadas
                if tarea not in completadas and all(dep in completadas for dep in dependencias):
                    self.plan.append(tarea)  # Añadimos la tarea al plan
                    completadas.add(tarea)    # Marcamos la tarea como completada
                    print(f"Ejecutando tarea: {tarea}")  # Mostramos qué tarea se está ejecutando

# Creamos una instancia de la planificación
planificacion = Planificacion()

# Llamamos al método para crear el plan
planificacion.crear_plan()

# Mostramos el plan final
print("\nPlan final:", planificacion.plan)
