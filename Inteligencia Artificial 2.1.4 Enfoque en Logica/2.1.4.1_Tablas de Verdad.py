# Función para generar la tabla de verdad de una expresión lógica
def generar_tabla_verdad():
    # Mostramos los encabezados de la tabla
    print(" p | q | p Y q")
    print("---|---|-------")
    
    # Probamos todas las combinaciones posibles de p y q
    for p in [True, False]:  # p puede ser verdadero (True) o falso (False)
        for q in [True, False]:  # q también puede ser verdadero o falso
            # Calculamos el resultado de la expresión p Y q
            resultado = p and q
            # Mostramos los valores de p, q y el resultado de la expresión
            print(f" {int(p)} | {int(q)} |   {int(resultado)}")

# Llamamos a la función para que se muestre la tabla de verdad
generar_tabla_verdad()
