
import matplotlib.pyplot as plt

import dask.dataframe as dd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

# Cargar el conjunto de datos en un dataframe de Dask
df = dd.read_csv('C:/Trabajo-dask/dask/csvs/air_traffic_limpiado2.csv')

# Descripción general del conjunto de datos
print(df.describe().compute())

# Seleccionamos las características para el modelo
data = df[['Passenger Count', 'Year']]

# Información del dataset
data_info = data.compute().info()
print(data_info)

# Convertir Dask DataFrame a pandas DataFrame
data_pd = data.compute()

# Dividimos los datos en entrenamiento y prueba
X = data_pd[['Year']]
y = data_pd['Passenger Count']
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

# Creamos el modelo de Bosques Aleatorios (Random Forest) y configuramos los parámetros
RF_model = RandomForestRegressor(n_estimators=100, random_state=2016)

# Ajustamos el modelo a los datos de entrenamiento
RF_model.fit(X_train, y_train)

# Predecimos los valores de y para los datos de prueba
y_pred = RF_model.predict(X_test)

# Calculamos el error cuadrático medio (MSE)
mse = mean_squared_error(y_test, y_pred)
print("Error cuadrático medio (MSE): ", mse)

# Calculamos la precisión del modelo
accuracy = RF_model.score(X_test, y_test)
print("Precisión del modelo: ", accuracy)

# Graficar datos reales vs. predichos
plt.scatter(X_test, y_test, color='b', label='Datos reales')
plt.scatter(X_test, y_pred, color='r', label='Predicciones')
plt.xlabel('Year')
plt.ylabel('Passenger Count')
plt.legend()
plt.title('Predicciones de Pasajeros utilizando Bosques Aleatorios')
plt.savefig('C:/Trabajo-dask/dask/graficos/prediccion2.png')




