# Lista de nombres de personas
nombres = ['Fernanda', 'Emmanuel', 'Emiliano', 'Eliott']

# Definimos una función para preprocesar los nombres
def preprocesar_nombres(lista_nombres):
    # Usamos una lista por comprensión para aplicar los filtros
    nombres_procesados = [
        nombre.lower()  # Convertimos a minúsculas
        for nombre in lista_nombres if len(nombre) >= 6  # Filtramos nombres con longitud mayor o igual a 6
    ]
    return nombres_procesados

# Aplicamos el preprocesamiento a la lista de nombres
nombres_procesados = preprocesar_nombres(nombres)

# Imprimimos los nombres procesados
print("Nombres procesados:", nombres_procesados)
