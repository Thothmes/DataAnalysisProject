import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


#1
weather_dataframe = pd.DataFrame(pd.read_csv('weather1.csv', 
                                             sep=';', 
                                             usecols=["Местное время в Перми", "T", "Po", "U", "Ff", "N", "H", "VV"]))

weather_dataframe.info()

weather_dataframe['T'] = pd.to_datetime(weather_dataframe['T'])
weather_dataframe['N'] = weather_dataframe['N'].str.replace('%','', regex=False)

for column in ['T', 'Po', 'U', 'Ff', 'N','VV']:
        weather_dataframe[column] = pd.to_numeric(weather_dataframe[column], errors='coerce')

weather_dataframe.info()

sns.scatterplot(
    x='T', y='U',
    data=weather_dataframe,
    hue='N'
)
plt.xlabel('Температура')
plt.ylabel('Относительная влажность')
plt.show

