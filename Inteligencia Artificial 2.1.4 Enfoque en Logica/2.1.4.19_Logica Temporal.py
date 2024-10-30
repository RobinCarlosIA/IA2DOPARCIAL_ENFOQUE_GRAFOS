# Definimos una lista para representar los eventos en el tiempo
eventos_tiempo = [
    {"momento": 1, "evento": "Despertar"},
    {"momento": 2, "evento": "Desayunar"},
    {"momento": 3, "evento": "Ir al trabajo"},
    {"momento": 4, "evento": "Trabajar"},
    {"momento": 5, "evento": "Regresar a casa"},
]

# Función para obtener el evento que ocurre en un momento específico
def evento_en_momento(momento):
    for evento in eventos_tiempo:
        if evento["momento"] == momento:
            return evento["evento"]
    return "No hay evento en este momento."

# Función para evaluar si un evento ocurre antes de otro
def evento_antes(momento1, momento2):
    return momento1 < momento2

# Ejemplo de uso
print("Eventos programados:")
for evento in eventos_tiempo:
    print(f"Momento {evento['momento']}: {evento['evento']}")

# Verificamos el evento que ocurre en el momento 3
momento_consultado = 3
evento_actual = evento_en_momento(momento_consultado)
print(f"\nEvento en el momento {momento_consultado}: {evento_actual}")

# Verificamos si el evento en el momento 2 ocurre antes del evento en el momento 4
if evento_antes(2, 4):
    print("El evento en el momento 2 ocurre antes del evento en el momento 4.")
else:
    print("El evento en el momento 2 no ocurre antes del evento en el momento 4.")
