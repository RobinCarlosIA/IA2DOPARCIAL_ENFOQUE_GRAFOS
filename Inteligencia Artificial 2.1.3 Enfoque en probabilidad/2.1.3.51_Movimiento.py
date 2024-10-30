# Lista de nombres que usaremos para simular el movimiento
nombres = ['Fernanda', 'Emmanuel', 'Emiliano', 'Eliott']

# Definimos una función para simular el movimiento de los nombres
def simular_movimiento(lista_nombres):
    # Creamos dos listas para almacenar los nombres en movimiento y los estáticos
    en_movimiento = []  # Lista para nombres que "se mueven"
    estaticos = []      # Lista para nombres que "no se mueven"

    # Iteramos sobre la lista de nombres
    for nombre in lista_nombres:
        # Usamos un criterio simple: si el nombre empieza con una vocal, está "en movimiento"
        if nombre[0].lower() in 'aeiou':  # Comprobamos si la primera letra es una vocal
            en_movimiento.append(nombre)  # Agregamos a la lista de en movimiento
        else:
            estaticos.append(nombre)       # Si no, agregamos a la lista de estáticos

    return en_movimiento, estaticos  # Devolvemos ambas listas

# Aplicamos la función de simulación de movimiento a la lista de nombres
nombres_en_movimiento, nombres_estaticos = simular_movimiento(nombres)

# Imprimimos los resultados
print("Nombres en movimiento:", nombres_en_movimiento)  # Mostramos los nombres en movimiento
print("Nombres estáticos:", nombres_estaticos)          # Mostramos los nombres estáticos
