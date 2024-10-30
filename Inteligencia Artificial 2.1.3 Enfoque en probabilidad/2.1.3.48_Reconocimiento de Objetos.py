# Lista de nombres de personas que usaremos como "objetos"
nombres = ['Fernanda', 'Emmanuel', 'Emiliano', 'Eliott']

# Definimos una función para reconocer objetos
def reconocer_objetos(lista_nombres):
    # Creamos una lista de objetos conocidos
    objetos_conocidos = ['Fernanda', 'Emiliano']  # Estos son los "objetos" que reconocemos
    objetos_reconocidos = []  # Para almacenar los nombres reconocidos
    objetos_no_reconocidos = []  # Para almacenar los nombres no reconocidos

    # Iteramos sobre la lista de nombres
    for nombre in lista_nombres:
        if nombre in objetos_conocidos:  # Si el nombre está en la lista de objetos conocidos
            objetos_reconocidos.append(nombre)  # Se agrega a la lista de reconocidos
        else:
            objetos_no_reconocidos.append(nombre)  # Se agrega a la lista de no reconocidos

    return objetos_reconocidos, objetos_no_reconocidos  # Devolvemos ambas listas

# Aplicamos el reconocimiento de objetos a la lista de nombres
nombres_reconocidos, nombres_no_reconocidos = reconocer_objetos(nombres)

# Imprimimos los resultados
print("Nombres reconocidos:", nombres_reconocidos)  # Mostramos los nombres reconocidos
print("Nombres no reconocidos:", nombres_no_reconocidos)  # Mostramos los nombres no reconocidos
