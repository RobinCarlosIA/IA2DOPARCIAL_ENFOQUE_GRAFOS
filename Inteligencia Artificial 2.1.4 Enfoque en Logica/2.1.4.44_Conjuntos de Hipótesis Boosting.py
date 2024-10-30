from sklearn.ensemble import AdaBoostClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Cargamos un conjunto de datos simple, en este caso, el dataset de iris
X, y = load_iris(return_X_y=True)

# Dividimos los datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Configuramos el modelo AdaBoost con 10 clasificadores simples
modelo_boosting = AdaBoostClassifier(n_estimators=10, random_state=42)

# Entrenamos el modelo
modelo_boosting.fit(X_train, y_train)

# Hacemos predicciones
predicciones = modelo_boosting.predict(X_test)

# Calculamos la precisión
precision = accuracy_score(y_test, predicciones)

print("Precisión del modelo de Boosting:", precision)
