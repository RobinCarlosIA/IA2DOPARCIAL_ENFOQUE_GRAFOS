# Importamos las bibliotecas necesarias
from sklearn import datasets  # Conjunto de datos de ejemplo
from sklearn.model_selection import train_test_split  # Para dividir los datos
from sklearn.svm import SVC  # El modelo SVM
from sklearn.metrics import accuracy_score  # Para evaluar el modelo

# 1. Cargamos un conjunto de datos simple (el dataset de iris)
iris = datasets.load_iris()

# 2. Seleccionamos solo dos clases (para hacerlo más simple)
X = iris.data[iris.target != 2]  # Características de las primeras dos clases
y = iris.target[iris.target != 2]  # Etiquetas de las primeras dos clases

# 3. Dividimos los datos en entrenamiento (70%) y prueba (30%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 4. Creamos un modelo SVM con el kernel RBF (Radial Basis Function)
modelo_svm = SVC(kernel='rbf')

# 5. Entrenamos el modelo con los datos de entrenamiento
modelo_svm.fit(X_train, y_train)

# 6. Hacemos predicciones con los datos de prueba
y_pred = modelo_svm.predict(X_test)

# 7. Evaluamos el modelo usando la precisión (accuracy)
precision = accuracy_score(y_test, y_pred)
print(f'Precisión del modelo: {precision:.2f}')

# 8. Clasificación de un nuevo punto (ejemplo)
nuevo_punto = [[5.0, 3.5, 1.5, 0.2]]  # Un nuevo punto para clasificar
clasificacion = modelo_svm.predict(nuevo_punto)
print(f'El nuevo punto {nuevo_punto} se clasifica como: {clasificacion}')
