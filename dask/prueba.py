import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
# Cargar el conjunto de datos en un dataframe de Dask
df = pd.read_csv('C:/Trabajo-dask/dask/csvs/air_traffic_limpiado2.csv')

# Selecciona las características relevantes
features = ['Activity Period', 'Operating Airline', 'GEO Region', 'Activity Type Code', 'Price Category Code', 'Terminal', 'Boarding Area', 'Month']
df = df[features]
# Aplica one-hot encoding a las características categóricas
df = pd.get_dummies(df, columns=['Operating Airline', 'GEO Region', 'Activity Type Code', 'Price Category Code', 'Terminal', 'Boarding Area'])
# Agrega los datos por mes
df['Count'] = 1  # Agrega una columna de recuento para realizar la agregación
df = df.groupby('Month').sum().reset_index()

y = df['Count']

# Divide los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(df.drop('Count', axis=1), y, test_size=0.2, random_state=42)
from sklearn.ensemble import RandomForestRegressor

# Crea una instancia del modelo RandomForestRegressor
rf = RandomForestRegressor()

# Entrena el modelo utilizando los datos de entrenamiento
rf.fit(X_train, y_train)


# Realiza predicciones sobre el conjunto de prueba
y_pred = rf.predict(X_test)

# Evalúa el rendimiento del modelo
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Error cuadrático medio (MSE):", mse)
print("Coeficiente de determinación (R^2):", r2)
