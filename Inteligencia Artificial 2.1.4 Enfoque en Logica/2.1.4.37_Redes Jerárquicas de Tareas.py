class Tarea:
    def __init__(self, nombre):
        self.nombre = nombre  # Nombre de la tarea
        self.dependencias = []  # Lista para almacenar dependencias
        self.finalizada = False  # Estado de la tarea

    def agregar_dependencia(self, tarea):
        self.dependencias.append(tarea)  # Agregar una tarea como dependencia

    def __str__(self):
        return self.nombre  # Retorna el nombre de la tarea


class RedDeTareas:
    def __init__(self):
        self.tareas = []  # Lista de todas las tareas en la red

    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)  # Agregar tarea a la red

    def planificar(self):
        plan = []  # Lista para almacenar el orden de ejecución de las tareas

        while len(plan) < len(self.tareas):
            for tarea in self.tareas:
                # Si la tarea no está finalizada y todas sus dependencias están en el plan
                if not tarea.finalizada and all(dep in plan for dep in tarea.dependencias):
                    plan.append(tarea)  # Agregar la tarea al plan
                    tarea.finalizada = True  # Marcar tarea como finalizada
                    print(f"Ejecutando tarea: {tarea}")  # Mostrar la tarea que se está ejecutando

        print("\nPlan final de tareas:", [str(t) for t in plan])  # Mostrar el plan final


# Crear una red de tareas
red = RedDeTareas()

# Crear tareas
tarea1 = Tarea("Tarea 1")
tarea2 = Tarea("Tarea 2")
tarea3 = Tarea("Tarea 3")
tarea4 = Tarea("Tarea 4")

# Definir dependencias
tarea2.agregar_dependencia(tarea1)  # Tarea 2 depende de Tarea 1
tarea3.agregar_dependencia(tarea1)  # Tarea 3 depende de Tarea 1
tarea4.agregar_dependencia(tarea2)  # Tarea 4 depende de Tarea 2
tarea4.agregar_dependencia(tarea3)  # Tarea 4 depende de Tarea 3

# Agregar tareas a la red
red.agregar_tarea(tarea1)
red.agregar_tarea(tarea2)
red.agregar_tarea(tarea3)
red.agregar_tarea(tarea4)

# Ejecutar la planificación
red.planificar()
