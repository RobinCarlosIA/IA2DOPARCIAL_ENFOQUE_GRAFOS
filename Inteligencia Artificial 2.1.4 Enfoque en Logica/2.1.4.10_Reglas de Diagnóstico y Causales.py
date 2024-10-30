# Definimos los síntomas del paciente
sintomas = {
    "fiebre": True,
    "tos": True,
    "dolor_cabeza": False
}

# Reglas de diagnóstico
def diagnosticar(sintomas):
    # Regla 1: Si tiene fiebre y tos, podría tener gripe
    if sintomas["fiebre"] and sintomas["tos"]:
        return "Posible gripe."
    
    # Regla 2: Si tiene fiebre y dolor de cabeza, podría tener migraña
    if sintomas["fiebre"] and sintomas["dolor_cabeza"]:
        return "Posible migraña."
    
    # Regla 3: Si tiene tos y no fiebre, podría tener resfriado
    if sintomas["tos"] and not sintomas["fiebre"]:
        return "Posible resfriado."
    
    # Si no se cumplen ninguna de las reglas
    return "No se pudo determinar el diagnóstico."

# Ejecutamos el diagnóstico
resultado = diagnosticar(sintomas)
print("Diagnóstico:", resultado)
