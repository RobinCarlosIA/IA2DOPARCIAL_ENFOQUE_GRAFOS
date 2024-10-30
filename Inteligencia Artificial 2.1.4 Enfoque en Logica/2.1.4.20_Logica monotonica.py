# Inicializamos una lista de hechos
hechos = ["animal(gato)", "animal(perro)"]

# Función para agregar un hecho
def agregar_hecho(hecho):
    hechos.append(hecho)  # Agregamos el hecho a la lista
    print(f"Hecho agregado: {hecho}")

# Función para retractar (eliminar) un hecho
def retractar_hecho(hecho):
    if hecho in hechos:
        hechos.remove(hecho)  # Eliminamos el hecho de la lista
        print(f"Hecho retractado: {hecho}")
    else:
        print(f"Hecho no encontrado: {hecho}")

# Función para mostrar los hechos actuales
def mostrar_hechos():
    print("Hechos actuales:")
    for hecho in hechos:
        print(hecho)

# Ejemplo de uso
mostrar_hechos()  # Mostramos los hechos iniciales

# Agregamos un nuevo hecho
agregar_hecho("animal(pájaro)")

# Retractamos un hecho existente
retractar_hecho("animal(gato)")

# Mostramos los hechos actuales después de los cambios
mostrar_hechos()
