# Lista de nombres que usaremos para el reconocimiento de escritura
nombres = ['Fernanda', 'Emmanuel', 'Emiliano', 'Eliott']

# Definimos una función para simular el reconocimiento de escritura
def reconocimiento_escritura(lista_nombres):
    # Creamos una lista de nombres escritos (reconocidos)
    nombres_reconocidos = ['Fernanda', 'Eliott']  # Estos son los nombres que podemos reconocer
    reconocidos = []  # Lista para almacenar los nombres reconocidos
    no_reconocidos = []  # Lista para almacenar los nombres no reconocidos

    # Iteramos sobre la lista de nombres
    for nombre in lista_nombres:
        if nombre in nombres_reconocidos:  # Si el nombre está en la lista de nombres reconocidos
            reconocidos.append(nombre)  # Agregamos a la lista de reconocidos
        else:
            no_reconocidos.append(nombre)  # Agregamos a la lista de no reconocidos

    return reconocidos, no_reconocidos  # Devolvemos ambas listas

# Aplicamos el reconocimiento de escritura a la lista de nombres
nombres_reconocidos, nombres_no_reconocidos = reconocimiento_escritura(nombres)

# Imprimimos los resultados
print("Nombres reconocidos:", nombres_reconocidos)  # Mostramos los nombres que fueron reconocidos
print("Nombres no reconocidos:", nombres_no_reconocidos)  # Mostramos los nombres que no fueron reconocidos
