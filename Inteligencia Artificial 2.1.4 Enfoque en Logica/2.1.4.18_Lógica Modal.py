# Definimos un diccionario para representar hechos
hechos = {
    "llueve": True,       # Hecho: está lloviendo
    "tiene_paraguas": False,  # Hecho: no tiene paraguas
    "sale": False        # Hecho: no sale
}

# Función para evaluar la necesidad (es necesario que ocurra un evento)
def es_necesario(hecho):
    if hecho == "sale":
        # Es necesario salir si está lloviendo y no tiene paraguas
        return hechos["llueve"] and not hechos["tiene_paraguas"]
    return False

# Función para evaluar la posibilidad (es posible que ocurra un evento)
def es_posible(hecho):
    if hecho == "sale":
        # Es posible que salga si no llueve
        return not hechos["llueve"]
    return False

# Ejemplo de uso
hechos_actuales = ["llueve", "tiene_paraguas", "sale"]

print("Hechos actuales:")
for hecho in hechos_actuales:
    print(f"{hecho}: {'Sí' if hechos[hecho] else 'No'}")

# Evaluamos si es necesario y posible salir
necesidad = es_necesario("sale")
posibilidad = es_posible("sale")

print("\nEvaluación modal:")
print(f"¿Es necesario salir? {'Sí' if necesidad else 'No'}")
print(f"¿Es posible salir? {'Sí' if posibilidad else 'No'}")
