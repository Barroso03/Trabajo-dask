import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from mlxtend.plotting import plot_confusion_matrix
from sklearn.metrics import confusion_matrix

# Cargar el conjunto de datos en un dataframe de Dask
df = pd.read_csv('C:/Trabajo-dask/dask/csvs/air_traffic_limpiado2.csv')
# Descripción genereal del conjunto de datos
print(df.describe())
# Seleccionamos las características para el modelo
data = df[['Operating Airline',  'GEO Region', 'Activity Type Code', 'Price Category Code', 'Terminal', 'Boarding Area','Passenger Count', 'Month', 'Activity Period']]
# Información del dataset
data.info()

# Dividimos los datos en entrenamiento y prueba
from sklearn.model_selection import train_test_split
# X son nuestras variables independientes
X = data.drop(['Activity Period'],axis = 1)

# y es nuestra variable dependiente
y = data['Activity Period']

# División 75% de datos para entrenamiento, 25% de daatos para test
X_train, X_test, y_train, y_test = train_test_split(X, y,random_state=0)

# Creaamos el modelo de Bosques Aleatorios (y configuramos el número de estimadores (árboles de decisión))
BA_model = RandomForestClassifier(n_estimators = 19, 
                                  random_state = 2016,
                                  min_samples_leaf = 8,)
BA_model.fit(X_train, y_train)
print(BA_model.fit(X_train, y_train))



print("Precisión del modelo: ", BA_model.score(X_test, y_test))

# Matriz de confusión
# Predicción del modelo usando los datos de prueba
y_pred = BA_model.predict(X_test)
matriz = confusion_matrix(y_test,y_pred)

plot_confusion_matrix(conf_mat=matriz, figsize=(6,6), show_normed=False)

     
plt.show()