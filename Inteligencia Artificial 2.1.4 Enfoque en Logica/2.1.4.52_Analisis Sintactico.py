# Definimos una clase para el analizador sintáctico
class AnalizadorSintactico:
    def __init__(self, entrada):
        # Inicializamos el analizador con la entrada
        self.entrada = entrada
        self.posicion = 0  # Posición actual en la entrada

    def siguiente_token(self):
        # Devuelve el siguiente token en la entrada
        if self.posicion < len(self.entrada):
            token = self.entrada[self.posicion]
            self.posicion += 1
            return token
        return None  # Fin de la entrada

    def factor(self):
        # Analiza un factor (número)
        token = self.siguiente_token()
        if token is not None and token.isdigit():  # Verificamos si es un dígito
            return int(token)  # Retornamos el número como entero
        raise Exception("Error de análisis: Se esperaba un número")

    def termino(self):
        # Analiza un término (factor o productos)
        resultado = self.factor()  # Obtenemos el primer factor
        while True:
            token = self.siguiente_token()
            if token == '*':
                resultado *= self.factor()  # Multiplicación
            else:
                self.posicion -= 1  # Volvemos a la posición anterior
                break  # Salimos del ciclo
        return resultado

    def expresion(self):
        # Analiza una expresión (suma de términos)
        resultado = self.termino()  # Obtenemos el primer término
        while True:
            token = self.siguiente_token()
            if token == '+':
                resultado += self.termino()  # Suma
            else:
                self.posicion -= 1  # Volvemos a la posición anterior
                break  # Salimos del ciclo
        return resultado

# Código de ejemplo para analizar
entrada = "3 + 5 * 2"

# Creamos el analizador sintáctico
analizador = AnalizadorSintactico(entrada)

# Realizamos el análisis sintáctico y mostramos el resultado
resultado = analizador.expresion()
print("Resultado de la expresión:", resultado)
