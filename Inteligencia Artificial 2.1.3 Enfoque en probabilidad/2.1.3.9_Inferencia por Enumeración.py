# Clase simple para representar el Manto de Markov con tres personas
class MantoDeMarkov:
    def __init__(self):
        # Diccionario para almacenar las conexiones entre personas
        self.conexiones = {}

    # Método para agregar conexiones directas entre personas
    def agregar_conexion(self, persona1, persona2):
        """
        Agrega una conexión directa entre dos personas.
        """
        if persona1 not in self.conexiones:
            self.conexiones[persona1] = []
        if persona2 not in self.conexiones:
            self.conexiones[persona2] = []
        
        self.conexiones[persona1].append(persona2)  # Conectamos persona1 con persona2
        self.conexiones[persona2].append(persona1)  # Conectamos persona2 con persona1

    # Método para obtener el Manto de Markov de una persona
    def obtener_manto_de_markov(self, persona):
        """
        Devuelve el conjunto del Manto de Markov de la persona especificada.
        """
        if persona in self.conexiones:
            # El Manto de Markov son las conexiones directas de la persona
            return self.conexiones[persona]
        else:
            return []

# Creamos una instancia de MantoDeMarkov
manto = MantoDeMarkov()

# Agregamos conexiones entre las personas
manto.agregar_conexion('Fernanda', 'Emmanuel')
manto.agregar_conexion('Emmanuel', 'Emiliano')

# Obtenemos el Manto de Markov de cada persona
manto_fernanda = manto.obtener_manto_de_markov('Fernanda')
manto_emmanuel = manto.obtener_manto_de_markov('Emmanuel')
manto_emiliano = manto.obtener_manto_de_markov('Emiliano')

# Mostramos los mantos de Markov de cada persona
print(f"El Manto de Markov de Fernanda es: {manto_fernanda}")
print(f"El Manto de Markov de Emmanuel es: {manto_emmanuel}")
print(f"El Manto de Markov de Emiliano es: {manto_emiliano}")
