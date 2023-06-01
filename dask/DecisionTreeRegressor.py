import dask.dataframe as dd
import dask.array as da
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

# Cargar el conjunto de datos
df = dd.read_csv('C:/Trabajo-dask/dask/csvs/air_traffic_limpiado2.csv')

# Descripción general del conjunto de datos
print(df.describe().compute())

# Seleccionamos las características para el modelo
data = df[['Year', 'Passenger Count']]

# Información del dataset
data_info = data.compute().info()
print(data_info)

# Dividimos los datos en entrenamiento y prueba
X = data[['Year']].compute()
y = data['Passenger Count'].compute()
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

# Creamos el modelo de Regresión de Árbol de Decisión
regression = DecisionTreeRegressor(max_leaf_nodes=10)
regression.fit(X_train, y_train)

# Predecimos los valores de y para los datos de prueba
y_pred = regression.predict(X_test)

# Calculamos la precisión del modelo
accuracy = regression.score(X_test, y_test)
print("Precisión del modelo: ", accuracy)

# Calcular el error cuadrático medio (MSE)
mse = mean_squared_error(y_test, y_pred)
print("Error cuadrático medio (MSE): ", mse)

# Graficar datos reales vs. predichos
plt.scatter(X_test, y_test, color='b', label='Datos reales')
plt.scatter(X_test, y_pred, color='r', label='Predicciones')
plt.xlabel('Year')
plt.ylabel('Passenger Count')
plt.legend()
plt.title('Predicciones de Pasajeros utilizando Regresión de Árbol de Decisión')
plt.savefig('C:/Trabajo-dask/dask/graficos/prediccion.png')



