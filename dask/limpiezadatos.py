import dask.dataframe as dd
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


# Cargar el conjunto de datos en un dataframe de Dask
df = dd.read_csv('C:/Trabajo-dask/dask/csvs/air_traffic_data (1).csv')
df.info()


print(df.dtypes)
# ¿Cuántas compañías diferentes aparecen en el fichero?
num_companias = df['Operating Airline'].nunique().compute()
print(f"Número de compañías diferentes: {num_companias}")

# ¿Cuántos pasajeros tienen de media los vuelos de cada compañía?
pasajeros_media = df.groupby('Operating Airline')['Passenger Count'].mean().compute()
print("Media de pasajeros por compañía:")
print(pasajeros_media)

# Eliminar los registros duplicados por el campo "GEO Región",
# manteniendo únicamente aquel con mayor número de pasajeros.
df_sin_duplicados = df.drop_duplicates(subset='GEO Region', keep='last')
df = df.drop_duplicates()
# dime los valores vacios de cada columna
print('------Valores vacios------')
print(df.isnull().sum().compute())
# borra los valores vacios
df = df.dropna()
# dime los valores vacios de cada columna
print('------Valores vacios------')
print(df.isnull().sum().compute())


# Volcar los resultados a un archivo CSV
df_sin_duplicados.to_csv('C:/Trabajo-dask/dask/csvs/resultados.csv', index=False)

# Lista de columnas a eliminar ya que no son necesarias
columnas_a_eliminar = ['Published Airline', 'Published Airline IATA Code', 'Adjusted Passenger Count','Adjusted Activity Type Code']

# Eliminar las columnas especificadas
df_sin_columnas = df.drop(columnas_a_eliminar, axis=1)

# Mostrar el numero de columnas  del dataframe y el tipo de dato de cada una
print(f"Número de columnas: {len(df_sin_columnas.columns)}")
print(df_sin_columnas.dtypes)
# GEO Summary
print('------GEO Summary------')
# dime los valores unicos de la columna Operating Airline y cuantas veces aparece cada uno
print(df_sin_columnas['GEO Summary'].unique().compute())
print(df_sin_columnas['GEO Summary'].value_counts().compute())
# cambia los si y no por 1 y 0
df_sin_columnas['GEO Summary'] = df_sin_columnas['GEO Summary'].replace({'International': 1, 'Domestic': 0})

print('------GEO Region------')
# dime los valores unicos de la columna Operating Airline y cuantas veces aparece cada uno
print(df_sin_columnas['GEO Region'].unique().compute())
print(df_sin_columnas['GEO Region'].value_counts().compute())
df_sin_columnas['GEO Region'] = df_sin_columnas['GEO Summary'].replace({'US': 0, 'Asia': 1,'Europe': 2, 'Canada': 3,'Mexico': 4, 'Australia / Oceania': 5,'Central America': 6, 'Middle East':7, 'South America': 8})




# Activity Type Code
print('------Activity Type Code------')
# dime los valores unicos de la columna Activity Type Code
print(df_sin_columnas['Activity Type Code'].unique().compute())
# dime cuantas veces aparece cada valor
print(df_sin_columnas['Activity Type Code'].value_counts().compute())
df_sin_columnas['Activity Type Code'] = df_sin_columnas['Activity Type Code'].replace({'Deplaned': 0, 'Enplaned': 1, 'Thru / Transit': 2})

#Price Category Code
print('------Price Category Code------')
print(df_sin_columnas['Price Category Code'].unique().compute())
print(df_sin_columnas['Price Category Code'].value_counts().compute())
df_sin_columnas['Price Category Code'] = df_sin_columnas['Price Category Code'].replace({'Low Fare': 0, 'Other': 1})


#Terminal
print('------Terminal------')
print(df_sin_columnas['Terminal'].unique().compute())
# sime cuantas veces aparece cada valor
print(df_sin_columnas['Terminal'].value_counts().compute())
# borra los que sean other
df_sin_columnas = df_sin_columnas[df_sin_columnas['Terminal'] != 'Other']
df_sin_columnas['Terminal'] = df_sin_columnas['Terminal'].replace({'Terminal 1': 0, 'Terminal 2': 1,'Terminal 3': 2, 'International': 3})


#Boarding Area
print('------Boarding Area------')
print(df_sin_columnas['Boarding Area'].unique().compute())
print(df_sin_columnas['Boarding Area'].value_counts().compute())
df_sin_columnas['Boarding Area'] = df_sin_columnas['Boarding Area'].replace({'B': 0, 'C': 1,'A': 2, 'D': 3, 'E': 4, 'G': 5, 'F': 6})


# Month
print('------Month------')
print(df_sin_columnas['Month'].unique().compute())
print(df_sin_columnas['Month'].value_counts().compute())
# cambia los meses por numeros
df_sin_columnas['Month'] = df_sin_columnas['Month'].replace({'January': 1, 'February': 2,'March': 3, 'April': 4, 'May': 5, 'June': 6, 'July': 7,'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12})
# Operating Airline IATA Code


# Operating Airline
print('------Operating Airline------')
# dime los valores unicos de la columna Operating Airline y cuantas veces aparece cada uno
print(df_sin_columnas['Operating Airline'].unique().compute())
print(df_sin_columnas['Operating Airline'].value_counts().compute())





# Mapea cada palabra única a un número único
word_to_number = {word: number for number, word in enumerate(df_sin_columnas['Operating Airline'].unique())}

# Reemplaza los valores de la columna con los números correspondientes
df_sin_columnas['Operating Airline'] = df_sin_columnas['Operating Airline'].map(word_to_number)

# Operating Airline
print('------Operating Airline IATA Code------')
# dime los valores unicos de la columna Operating Airline y cuantas veces aparece cada uno
print(df_sin_columnas['Operating Airline IATA Code'].unique().compute())
print(df_sin_columnas['Operating Airline IATA Code'].value_counts().compute())





# Mapea cada palabra única a un número único
word_to_number = {word: number for number, word in enumerate(df_sin_columnas['Operating Airline IATA Code'].unique())}

# Reemplaza los valores de la columna con los números correspondientes
df_sin_columnas['Operating Airline IATA Code'] = df_sin_columnas['Operating Airline IATA Code'].map(word_to_number)

# borramos la columna Operating Airline IATA Code ya que aporta lo mismo que la columna Operating Airline
df_sin_columnas = df_sin_columnas.drop(columns=['Operating Airline IATA Code'])





# cambia las columnas object por numeros para poder trabajar con ellas


df_sin_columnas['Operating Airline'] = df_sin_columnas['Operating Airline'].astype(float)
df_sin_columnas['GEO Summary'] = df_sin_columnas['GEO Summary'].astype(int)
df_sin_columnas['GEO Region'] = df_sin_columnas['GEO Region'].astype(int)
df_sin_columnas['Activity Type Code'] = df_sin_columnas['Activity Type Code'].astype(int)
df_sin_columnas['Price Category Code'] = df_sin_columnas['Price Category Code'].astype(int)
df_sin_columnas['Terminal'] = df_sin_columnas['Terminal'].astype(int)
df_sin_columnas['Boarding Area'] = df_sin_columnas['Boarding Area'].astype(int)
df_sin_columnas['Month'] = df_sin_columnas['Month'].astype(int)



# dime los tipos de datos de cada columna
print(df_sin_columnas.dtypes)




# borra la columna year ya que no da la misma información que activity period
df_sin_columnas = df_sin_columnas.drop('Year', axis=1)
# borra la columna Geo Summary ya que no da la misma información que Geo Region pero Geo Region tiene mas informacion
df_sin_columnas = df_sin_columnas.drop('GEO Summary', axis=1)

print(f"Número de columnas: {len(df_sin_columnas.columns)}")

# guardalo en un csv
df_sin_columnas.to_csv('C:/Trabajo-dask/dask/csvs/air_traffic_limpiado.csv', index=False)
    
correlacion = df_sin_columnas.corr()
sns.heatmap(correlacion, xticklabels=correlacion.columns, yticklabels=correlacion.columns, annot=True)

# guardame la matriz de correlacion en una imagen
plt.savefig('C:/Trabajo-dask/dask/graficos/matrizcorrelacion.png')


