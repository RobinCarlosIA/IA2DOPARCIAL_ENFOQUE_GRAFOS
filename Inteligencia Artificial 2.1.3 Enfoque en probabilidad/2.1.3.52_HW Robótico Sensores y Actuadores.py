# Programa básico en Python que simula sensores y actuadores

# Función que simula la lectura de un sensor de temperatura
def leer_sensor_temperatura():
    # Aquí simulamos la lectura con un valor entre 15 y 30 grados
    return random.randint(15, 30)

# Función que controla un ventilador (actuador) según la temperatura medida
def controlar_ventilador(temp, umbral):
    if temp > umbral:
        print("Temperatura alta, encendiendo ventilador.")
    else:
        print("Temperatura normal, ventilador apagado.")

# Programa principal
import random  # Importamos random para simulación de valores

umbral_temperatura = 25  # Umbral para el ventilador

# Realizamos 5 lecturas y activamos/desactivamos el ventilador
for _ in range(5):
    temperatura = leer_sensor_temperatura()  # Leer el valor de temperatura
    print(f"Temperatura medida: {temperatura}°C")  # Mostrar la temperatura
    controlar_ventilador(temperatura, umbral_temperatura)  # Controlar ventilador
