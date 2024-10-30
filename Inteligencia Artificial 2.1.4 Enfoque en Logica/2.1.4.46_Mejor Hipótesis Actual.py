from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Cargamos el conjunto de datos de iris
X, y = load_iris(return_X_y=True)

# Dividimos los datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Creamos el clasificador de regresión logística
modelo = LogisticRegression(max_iter=200)

# Entrenamos el modelo con los datos de entrenamiento
modelo.fit(X_train, y_train)

# Hacemos predicciones con los datos de prueba
predicciones = modelo.predict(X_test)

# Calculamos la precisión del modelo
precision = accuracy_score(y_test, predicciones)

print("Precisión de la Mejor Hipótesis Actual (Regresión Logística):", precision)
