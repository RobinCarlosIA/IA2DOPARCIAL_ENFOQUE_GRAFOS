# Lista de nombres que usaremos para el etiquetado de líneas
nombres = ['Fernanda', 'Emmanuel', 'Emiliano', 'Eliott']

# Definimos una función para etiquetar los nombres
def etiquetar_nombres(lista_nombres):
    # Creamos dos listas para almacenar nombres etiquetados
    nombres_cortos = []  # Lista para nombres cortos (menos de 8 caracteres)
    nombres_largos = []  # Lista para nombres largos (8 caracteres o más)

    # Iteramos sobre la lista de nombres
    for nombre in lista_nombres:
        if len(nombre) < 8:  # Si el nombre tiene menos de 8 caracteres
            nombres_cortos.append(nombre)  # Agregamos a la lista de nombres cortos
        else:
            nombres_largos.append(nombre)  # Si es 8 o más, agregamos a la lista de nombres largos

    return nombres_cortos, nombres_largos  # Devolvemos ambas listas

# Aplicamos la función de etiquetado a la lista de nombres
nombres_cortos, nombres_largos = etiquetar_nombres(nombres)

# Imprimimos los resultados
print("Nombres cortos:", nombres_cortos)  # Mostramos los nombres que son cortos
print("Nombres largos:", nombres_largos)  # Mostramos los nombres que son largos
