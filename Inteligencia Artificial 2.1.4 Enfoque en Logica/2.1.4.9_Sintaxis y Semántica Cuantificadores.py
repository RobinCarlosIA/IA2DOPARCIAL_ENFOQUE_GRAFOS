# Definimos una lista de personas
personas = ["Juan", "Ana", "Luis", "María"]

# Definimos una función que usa un cuantificador existencial
def existe_persona_con_nombre(nombre):
    # Verificamos si existe alguna persona con el nombre dado
    for persona in personas:
        if persona == nombre:
            return True  # Encontramos la persona
    return False  # No se encontró la persona

# Definimos una función que usa un cuantificador universal
def todas_las_personas_tienen_nombre():
    # Comprobamos si todas las personas en la lista tienen un nombre
    for persona in personas:
        if persona == "":
            return False  # Encontramos a alguien sin nombre
    return True  # Todas las personas tienen nombre

# Probamos las funciones
nombre_a_buscar = "Ana"
if existe_persona_con_nombre(nombre_a_buscar):
    print(f"Existe una persona llamada {nombre_a_buscar}.")
else:
    print(f"No existe ninguna persona llamada {nombre_a_buscar}.")

if todas_las_personas_tienen_nombre():
    print("Todas las personas tienen nombre.")
else:
    print("Hay personas sin nombre.")
