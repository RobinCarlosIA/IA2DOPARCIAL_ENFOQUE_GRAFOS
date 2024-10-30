# Definimos un diccionario para la base de conocimiento
base_de_conocimiento = {
    "Si llueve": "La calle está mojada",
    "Si hace sol": "La gente sale"
}

# Función para inferir el resultado de un hecho
def inferir(hecho):
    # Verificamos si el hecho está en la base de conocimiento
    return base_de_conocimiento.get(hecho, "No hay resultado para este hecho.")

# Hacemos algunas inferencias
hecho1 = "Si llueve"
resultado1 = inferir(hecho1)
print(f"Hecho: {hecho1} => Resultado: {resultado1}")

hecho2 = "Si hace sol"
resultado2 = inferir(hecho2)
print(f"Hecho: {hecho2} => Resultado: {resultado2}")

hecho3 = "Si nieva"
resultado3 = inferir(hecho3)
print(f"Hecho: {hecho3} => Resultado: {resultado3}")
