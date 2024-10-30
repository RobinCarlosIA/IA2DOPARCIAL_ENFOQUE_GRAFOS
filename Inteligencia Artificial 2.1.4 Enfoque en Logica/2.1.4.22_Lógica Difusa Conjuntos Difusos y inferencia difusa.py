# Definimos una función para calcular el grado de pertenencia al conjunto "frío"
def grado_frio(temperatura):
    if temperatura < 0:
        return 0  # No pertenece al conjunto "frío"
    elif 0 <= temperatura <= 20:
        return (20 - temperatura) / 20  # Grado de pertenencia
    else:
        return 0  # No pertenece al conjunto "frío"

# Definimos una función para calcular el grado de pertenencia al conjunto "ideal"
def grado_ideal(temperatura):
    if 15 <= temperatura <= 25:
        return 1  # Pertenece completamente al conjunto "ideal"
    elif 10 <= temperatura < 15:
        return (temperatura - 10) / 5  # Grado de pertenencia
    elif 25 < temperatura <= 30:
        return (30 - temperatura) / 5  # Grado de pertenencia
    else:
        return 0  # No pertenece al conjunto "ideal"

# Definimos una función para calcular el grado de pertenencia al conjunto "caliente"
def grado_caliente(temperatura):
    if temperatura < 30:
        return 0  # No pertenece al conjunto "caliente"
    elif 30 <= temperatura <= 40:
        return (temperatura - 30) / 10  # Grado de pertenencia
    else:
        return 1  # Pertenece completamente al conjunto "caliente"

# Función para evaluar el estado de confort
def evaluar_confort(temperatura):
    frio = grado_frio(temperatura)
    ideal = grado_ideal(temperatura)
    caliente = grado_caliente(temperatura)

    # Inferencia simple basada en los grados de pertenencia
    if frio > ideal and frio > caliente:
        return "Frío"
    elif caliente > frio and caliente > ideal:
        return "Caliente"
    else:
        return "Confortable"

# Ejemplo de uso
temp_a_evaluar = 28  # Temperatura a evaluar
estado_confort = evaluar_confort(temp_a_evaluar)
print(f"Temperatura: {temp_a_evaluar}°C")
print(f"Estado de confort: {estado_confort}")
