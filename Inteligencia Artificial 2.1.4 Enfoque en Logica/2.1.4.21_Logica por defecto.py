# Inicializamos una lista de hechos
hechos = ["animal(gato)", "animal(perro)"]

# Definimos una regla por defecto
def es_animal(hecho):
    if "animal" in hecho:
        return True  # Suponemos que cualquier cosa con "animal" es un animal
    return False

# Función para mostrar los hechos actuales
def mostrar_hechos():
    print("Hechos actuales:")
    for hecho in hechos:
        print(hecho)

# Ejemplo de uso
mostrar_hechos()  # Mostramos los hechos iniciales

# Verificamos si un hecho es un animal
hecho_a_verificar = "animal(gato)"
if es_animal(hecho_a_verificar):
    print(f"\nPor defecto, '{hecho_a_verificar}' se considera un animal.")
else:
    print(f"\n'{hecho_a_verificar}' no se considera un animal por defecto.")

# Agregamos un nuevo hecho
hechos.append("animal(pájaro)")
print(f"\nAgregamos un nuevo hecho: 'animal(pájaro)'.")

# Verificamos el nuevo hecho
nuevo_hecho = "animal(pájaro)"
if es_animal(nuevo_hecho):
    print(f"Por defecto, '{nuevo_hecho}' se considera un animal.")
