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

# haz un csv que en una columna muestre la media de pasajeros por año y en otar columna los años
df.groupby('Year')['Passenger Count'].mean().compute().to_csv('C:/Trabajo-dask/dask/csvs/air_traffic_mean.csv')