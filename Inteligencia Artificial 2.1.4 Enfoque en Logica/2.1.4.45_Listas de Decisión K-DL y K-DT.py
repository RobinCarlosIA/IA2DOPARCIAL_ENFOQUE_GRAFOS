from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Cargamos el conjunto de datos de iris
X, y = load_iris(return_X_y=True)

# Dividimos los datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 1. Usamos K-DL: Clasificación por vecinos más cercanos
# Creamos el clasificador KNN (K-Nearest Neighbors) con K=3
modelo_knn = KNeighborsClassifier(n_neighbors=3)

# Entrenamos el modelo KNN
modelo_knn.fit(X_train, y_train)

# Hacemos predicciones con KNN
predicciones_knn = modelo_knn.predict(X_test)

# Calculamos la precisión del modelo KNN
precision_knn = accuracy_score(y_test, predicciones_knn)

print("Precisión del modelo K-DL (KNN):", precision_knn)


# 2. Usamos K-DT: Árbol de decisión
# Creamos el clasificador de árbol de decisión
modelo_dt = DecisionTreeClassifier()

# Entrenamos el modelo de árbol de decisión
modelo_dt.fit(X_train, y_train)

# Hacemos predicciones con el árbol de decisión
predicciones_dt = modelo_dt.predict(X_test)

# Calculamos la precisión del modelo de árbol de decisión
precision_dt = accuracy_score(y_test, predicciones_dt)

print("Precisión del modelo K-DT (Árbol de decisión):", precision_dt)
