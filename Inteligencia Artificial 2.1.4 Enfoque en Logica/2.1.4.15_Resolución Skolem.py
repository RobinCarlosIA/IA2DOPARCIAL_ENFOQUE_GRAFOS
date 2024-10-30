# Hechos iniciales en un formato simple
# Aquí simulamos una estructura de hechos en lógica
hechos = [
    "animal(gato)",
    "animal(perro)",
    "come(gato, pescado)",
    "existe(y, perro(y) ∧ come(gato, y))"  # Existencia de un perro que come gato
]

# Función para convertir a forma Skolem
def forma_skolem(hechos):
    skolem_hechos = []  # Lista para almacenar los nuevos hechos en forma Skolem
    contador = 1  # Contador para las funciones Skolem

    for hecho in hechos:
        # Si encontramos una expresión que representa una existencia
        if "existe" in hecho:
            # Generamos un nombre para la función Skolem
            skolem_funcion = f"skolem_{contador}()"
            contador += 1  # Incrementamos el contador
            
            # Reemplazamos el hecho existencial
            nuevo_hecho = hecho.replace("existe(y", f"{skolem_funcion}")
            skolem_hechos.append(nuevo_hecho)
        else:
            # Para hechos que no son existenciales, los agregamos tal cual
            skolem_hechos.append(hecho)

    return skolem_hechos

# Ejemplo de uso
print("Hechos originales:")
for hecho in hechos:
    print(hecho)

# Convertimos la expresión a forma Skolem
resultados_skolem = forma_skolem(hechos)

# Mostramos los resultados
print("\nHechos en forma Skolem:")
for resultado in resultados_skolem:
    print(resultado)

