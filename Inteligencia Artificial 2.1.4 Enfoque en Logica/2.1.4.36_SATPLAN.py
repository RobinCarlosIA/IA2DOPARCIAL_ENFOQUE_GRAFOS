class SATPlan:
    def __init__(self):
        # Definimos las acciones y sus efectos
        self.acciones = {
            "ir_a_cocina": {"efectos": {"en_cocina"}},
            "hacer_comida": {"efectos": {"comida_hecha"}},
            "comer": {"efectos": {"comida_comida"}},
        }
        # Definimos las precondiciones de cada acción
        self.precondiciones = {
            "hacer_comida": {"en_cocina"},  # Necesitamos estar en la cocina
            "comer": {"comida_hecha"},      # Necesitamos que la comida esté hecha
        }
        self.estado_inicial = {"en_cocina"}  # Estado inicial
        self.objetivo = {"comida_comida"}     # Objetivo

    # Método para ejecutar el algoritmo SATPLAN
    def ejecutar(self):
        plan = []  # Lista para almacenar el plan
        
        # Verificamos las precondiciones para cada acción y construimos el plan
        for accion in self.acciones:
            # Comprobamos si las precondiciones están en el estado actual
            if accion in self.precondiciones:
                if self.precondiciones[accion].issubset(self.estado_inicial):
                    self.estado_inicial.update(self.acciones[accion]["efectos"])  # Actualizamos el estado
                    plan.append(accion)  # Añadimos la acción al plan
            
            # Verificamos si hemos alcanzado el objetivo
            if self.objetivo.issubset(self.estado_inicial):
                print("Objetivo alcanzado con el plan:", plan)
                return

        print("No se pudo alcanzar el objetivo con el plan actual.")

# Creamos una instancia del algoritmo SATPLAN
satplan = SATPlan()

# Ejecutamos el algoritmo
satplan.ejecutar()
