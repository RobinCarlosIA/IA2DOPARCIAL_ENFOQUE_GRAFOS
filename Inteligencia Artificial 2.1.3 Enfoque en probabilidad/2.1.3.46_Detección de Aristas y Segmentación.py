# Lista de nombres de personas
nombres = ['Fernanda', 'Emmanuel', 'Emiliano', 'Eliott']

# Definimos una función para detectar aristas (relaciones) y segmentar los nombres
def detectar_aristas_y_segmentar(lista_nombres):
    # Creamos un diccionario para guardar las relaciones entre nombres
    relaciones = {}
    # Creamos dos listas para almacenar los segmentos de nombres
    nombres_cortos = []  # Para nombres con menos de 7 letras
    nombres_largos = []  # Para nombres con 7 letras o más

    # Iteramos sobre la lista de nombres
    for nombre in lista_nombres:
        # Establecemos relaciones con otros nombres
        for otro_nombre in lista_nombres:
            if nombre != otro_nombre:  # Evitamos la relación consigo mismo
                # Agregamos el nombre a la lista de relaciones
                if nombre not in relaciones:
                    relaciones[nombre] = []  # Inicializamos la lista de relaciones
                relaciones[nombre].append(otro_nombre)  # Agregamos el otro nombre

        # Segmentamos los nombres según su longitud
        if len(nombre) < 7:  # Si el nombre tiene menos de 7 letras
            nombres_cortos.append(nombre)  # Agregamos a la lista de nombres cortos
        else:  # Si el nombre tiene 7 letras o más
            nombres_largos.append(nombre)  # Agregamos a la lista de nombres largos

    return relaciones, nombres_cortos, nombres_largos  # Devolvemos las relaciones y segmentos

# Aplicamos la detección de aristas y segmentación a la lista de nombres
relaciones, nombres_cortos, nombres_largos = detectar_aristas_y_segmentar(nombres)

# Imprimimos los resultados
print("Relaciones entre nombres:")
for nombre, relacion in relaciones.items():
    print(f"{nombre} tiene relaciones con: {', '.join(relacion)}")  # Mostramos las relaciones
print("\nNombres cortos (menos de 7 letras):", nombres_cortos)  # Mostramos nombres cortos
print("Nombres largos (7 letras o más):", nombres_largos)  # Mostramos nombres largos
