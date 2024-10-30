import threading  # Importamos el módulo threading para ejecutar tareas en paralelo
import time

class Tarea:
    def __init__(self, nombre):
        self.nombre = nombre  # Nombre de la tarea
        self.estado = "pendiente"  # Estado inicial de la tarea

    def ejecutar(self):
        print(f"Iniciando la tarea: {self.nombre}")
        time.sleep(2)  # Simulamos tiempo de ejecución (2 segundos)
        self.estado = "completada"  # Cambiamos el estado a completada
        print(f"Tarea completada: {self.nombre}")


class Vigilancia:
    def __init__(self, tarea):
        self.tarea = tarea  # La tarea que vamos a vigilar

    def vigilar(self):
        print("Vigilando la tarea...")
        while self.tarea.estado == "pendiente":
            print("La tarea sigue pendiente...")
            time.sleep(0.5)  # Esperar medio segundo antes de volver a verificar

        print("La tarea ha cambiado de estado. Verificando...")
        if self.tarea.estado == "completada":
            print("No se necesita replanificación. La tarea se completó correctamente.")
        else:
            print("Se necesita replanificar la tarea.")


# Creamos una tarea
tarea1 = Tarea("Preparar Informe")

# Creamos un objeto de vigilancia para esta tarea
vigilancia = Vigilancia(tarea1)

# Creamos un hilo para ejecutar la tarea
hilo_tarea = threading.Thread(target=tarea1.ejecutar)

# Iniciamos la vigilancia en un hilo separado
hilo_vigilancia = threading.Thread(target=vigilancia.vigilar)

# Iniciamos los hilos
hilo_vigilancia.start()
hilo_tarea.start()

# Esperamos a que ambos hilos terminen
hilo_tarea.join()
hilo_vigilancia.join()
