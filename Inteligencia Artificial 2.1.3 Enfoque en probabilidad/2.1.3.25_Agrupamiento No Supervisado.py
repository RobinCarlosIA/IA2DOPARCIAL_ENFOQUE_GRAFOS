# Datos simples que queremos agrupar
datos = [1, 3, 5, 6, 8, 12, 15, 18]

# Definimos un umbral (línea) para agrupar los datos
umbral = 10

# Función que separa los datos en dos grupos según el umbral
def agrupar_datos(datos, umbral):
    grupo1 = []  # Grupo de datos menores o iguales al umbral
    grupo2 = []  # Grupo de datos mayores al umbral
    
    # Recorrer cada dato y asignarlo a un grupo
    for dato in datos:
        if dato <= umbral:
            grupo1.append(dato)  # Va al grupo1
        else:
            grupo2.append(dato)  # Va al grupo2

    return grupo1, grupo2

# Llamamos la función para agrupar los datos
grupo1, grupo2 = agrupar_datos(datos, umbral)

# Mostramos los resultados
print("Grupo 1 (<= 10):", grupo1)
print("Grupo 2 (> 10):", grupo2)
