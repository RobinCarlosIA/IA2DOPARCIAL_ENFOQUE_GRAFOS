# Base de conocimiento: Hechos
hechos = {
    "animal(tigre)": True,
    "animal(gato)": True,
    "animal(perro)": True,
    "felino(tigre)": True,
    "felino(gato)": True,
    "mamifero(perro)": True,
}

# Reglas para el encadenamiento hacia adelante
def encadenamiento_hacia_adelante(hechos):
    # Regla 1: Si algo es un felino, es un animal
    for clave in hechos:
        if clave.startswith("felino"):
            animal = clave.replace("felino(", "").replace(")", "")
            hechos[f"animal({animal})"] = True
            print(f"Regla activada: {animal} es un animal porque es un felino.")

    # Regla 2: Si algo es un mamífero, también es un animal
    for clave in hechos:
        if clave.startswith("mamifero"):
            animal = clave.replace("mamifero(", "").replace(")", "")
            hechos[f"animal({animal})"] = True
            print(f"Regla activada: {animal} es un animal porque es un mamífero.")

    return hechos

# Función para encadenamiento hacia atrás
def encadenamiento_hacia_atras(pregunta):
    # Verificamos si la pregunta se puede responder con los hechos
    return hechos.get(pregunta, False)

# Ejecutamos el encadenamiento hacia adelante
hechos = encadenamiento_hacia_adelante(hechos)

# Hacemos algunas preguntas usando encadenamiento hacia atrás
pregunta_1 = "animal(tigre)"
resultado_1 = encadenamiento_hacia_atras(pregunta_1)
print(f"¿Es tigre un animal? {'Sí' if resultado_1 else 'No'}")

pregunta_2 = "animal(gato)"
resultado_2 = encadenamiento_hacia_atras(pregunta_2)
print(f"¿Es gato un animal? {'Sí' if resultado_2 else 'No'}")

pregunta_3 = "animal(delfin)"
resultado_3 = encadenamiento_hacia_atras("animal(delfin)")
print(f"¿Es delfín un animal? {'Sí' if resultado_3 else 'No'}")
