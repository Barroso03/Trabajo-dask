import dask.dataframe as dd
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

class DataAnalysis:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None

    def load_data(self):
        self.df = dd.read_csv(self.file_path)
        self.df.info()

    def print_data_types(self):
        print(self.df.dtypes)

    def count_unique_companies(self):
        num_companies = self.df['Operating Airline'].nunique().compute()
        print(f"Número de compañías diferentes: {num_companies}")

    def average_passengers_per_company(self):
        passengers_mean = self.df.groupby('Operating Airline')['Passenger Count'].mean().compute()
        print("Media de pasajeros por compañía:")
        print(passengers_mean)

    def remove_duplicates(self):
        df_without_duplicates = self.df.drop_duplicates(subset='GEO Region', keep='last')
        self.df = self.df.drop_duplicates()
        print('------Valores vacíos------')
        print(self.df.isnull().sum().compute())
        self.df = self.df.dropna()
        print('------Valores vacíos------')
        print(self.df.isnull().sum().compute())
        df_without_duplicates.to_csv('C:/Trabajo-dask/dask/csvs/resultados.csv', index=False)

    def remove_columns(self):
        columns_to_remove = ['Published Airline', 'Published Airline IATA Code','Adjusted Passenger Count', 'Adjusted Activity Type Code']
        self.df = self.df.drop(columns_to_remove, axis=1)
        print(f"Número de columnas: {len(self.df.columns)}")
        print(self.df.dtypes)

    def analyze_geo_summary(self):
        print('------GEO Summary------')
        print(self.df['GEO Summary'].unique().compute())
        print(self.df['GEO Summary'].value_counts().compute())
        word_to_number = {word: number for number, word in enumerate(self.df['GEO Summary'].unique())}
        self.df['GEO Summary'] = self.df['GEO Summary'].map(word_to_number)

    def analyze_geo_region(self):
        print('------GEO Region------')
        print(self.df['GEO Region'].unique().compute())
        print(self.df['GEO Region'].value_counts().compute())
        word_to_number = {word: number for number, word in enumerate(self.df['GEO Region'].unique())}
        self.df['GEO Region'] = self.df['GEO Region'].map(word_to_number)

    def analyze_activity_type_code(self):
        print('------Activity Type Code------')
        print(self.df['Activity Type Code'].unique().compute())
        print(self.df['Activity Type Code'].value_counts().compute())
        word_to_number = {word: number for number, word in enumerate(self.df['Activity Type Code'].unique())}
        self.df['Activity Type Code'] = self.df['Activity Type Code'].map(word_to_number)

    def analyze_price_category_code(self):
        print('------Price Category Code------')
        print(self.df['Price Category Code'].unique().compute())
        print(self.df['Price Category Code'].value_counts().compute())
        word_to_number = {word: number for number, word in enumerate(self.df['Price Category Code'].unique())}
        self.df['Price Category Code'] = self.df['Price Category Code'].map(word_to_number)

    def analyze_terminal(self):
        print('------Terminal------')
        print(self.df['Terminal'].unique().compute())
        print(self.df['Terminal'].value_counts().compute())
        word_to_number = {word: number for number, word in enumerate(self.df['Terminal'].unique())}
        self.df['Terminal'] = self.df['Terminal'].map(word_to_number)

    def analyze_boarding_area(self):
        print('------Boarding Area------')
        print(self.df['Boarding Area'].unique().compute())
        print(self.df['Boarding Area'].value_counts().compute())
        word_to_number = {word: number for number, word in enumerate(self.df['Boarding Area'].unique())}
        self.df['Boarding Area'] = self.df['Boarding Area'].map(word_to_number)

    def analyze_month(self):
        print('------Month------')
        print(self.df['Month'].unique().compute())
        print(self.df['Month'].value_counts().compute())
        word_to_number = {word: number for number, word in enumerate(self.df['Month'].unique())}
        self.df['Month'] = self.df['Month'].map(word_to_number)

    def analyze_operating_airline(self):
        print('------Operating Airline------')
        print(self.df['Operating Airline'].unique().compute())
        print(self.df['Operating Airline'].value_counts().compute())
        word_to_number = {word: number for number, word in enumerate(self.df['Operating Airline'].unique())}
        self.df['Operating Airline'] = self.df['Operating Airline'].map(word_to_number)

    def analyze_operating_airline_iata_code(self):
        print('------Operating Airline IATA Code------')
        print(self.df['Operating Airline IATA Code'].unique().compute())
        print(self.df['Operating Airline IATA Code'].value_counts().compute())
        word_to_number = {word: number for number, word in enumerate(self.df['Operating Airline IATA Code'].unique())}
        self.df['Operating Airline IATA Code'] = self.df['Operating Airline IATA Code'].map(word_to_number)
        self.df = self.df.drop(columns=['Operating Airline IATA Code'])
        
    
    def guardar_csv(self):
        self.df.to_csv('C:/Trabajo-dask/dask/csvs/air_traffic_limpiado.csv', index=False)
    
    def borrar_activity_period(self):
        self.df = self.df.drop(columns=['Activity Period'])
        
    def resumen(self):    
        print(self.df.dtypes)
        num_columnas = len(self.df.columns)
        print(f"Número de columnas: {num_columnas}")
        
    def matriz_correlacion(self):
        correlacion = self.df.corr()
        sns.heatmap(correlacion, xticklabels=correlacion.columns, yticklabels=correlacion.columns, annot=True)
        plt.savefig('C:/Trabajo-dask/dask/graficos/matrizcorrelacion.png')
        
    
   
    


# Función principal (main)
def main():
    path = 'C:/Trabajo-dask/dask/csvs/air_traffic_data (1).csv'
    data_analyzer = DataAnalysis(path)
    data_analyzer.load_data()
    data_analyzer.print_data_types()
    data_analyzer.count_unique_companies()
    data_analyzer.average_passengers_per_company()
    data_analyzer.remove_duplicates()
    data_analyzer.remove_columns()
    
    data_analyzer.analyze_geo_summary()
    data_analyzer.analyze_geo_region()
    data_analyzer.analyze_activity_type_code()
    data_analyzer.analyze_price_category_code()
    data_analyzer.analyze_terminal()
    data_analyzer.analyze_boarding_area()
    data_analyzer.analyze_month()
    data_analyzer.analyze_operating_airline()
    data_analyzer.analyze_operating_airline_iata_code()
    data_analyzer.borrar_activity_period()
    data_analyzer.resumen()
    data_analyzer.guardar_csv()
    data_analyzer.matriz_correlacion()
   
    
main()
