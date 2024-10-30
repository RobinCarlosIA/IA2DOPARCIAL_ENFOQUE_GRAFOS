# Lista de nombres de personas
nombres = ['Fernanda', 'Emmanuel', 'Emiliano', 'Eliott']

# Definimos una función para clasificar los nombres según su longitud
def clasificar_nombres_por_textura_y_sombra(lista_nombres):
    # Creamos listas para almacenar los nombres con "textura" y "sombra"
    nombres_con_textura = []  # Para nombres largos
    nombres_con_sombra = []    # Para nombres cortos

    # Iteramos sobre la lista de nombres
    for nombre in lista_nombres:
        if len(nombre) >= 7:  # Si el nombre tiene 7 letras o más
            nombres_con_textura.append(nombre)  # Se clasifica como textura
        else:  # Si el nombre tiene menos de 7 letras
            nombres_con_sombra.append(nombre)  # Se clasifica como sombra

    return nombres_con_textura, nombres_con_sombra  # Devolvemos ambas listas

# Aplicamos la clasificación a la lista de nombres
nombres_textura, nombres_sombra = clasificar_nombres_por_textura_y_sombra(nombres)

# Imprimimos los resultados
print("Nombres con textura (7 letras o más):", nombres_textura)  # Mostramos nombres con textura
print("Nombres con sombra (menos de 7 letras):", nombres_sombra)  # Mostramos nombres con sombra
