import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#1
athletes_info = pd.DataFrame(pd.read_csv('athlete_events.csv'))

#2
athletes_info.info()
athletes_info.count()

#3
print(athletes_info[['Age', 'Height', 'Weight']].describe())

#4.1
athletes_1992_info = athletes_info[athletes_info['Year'] == 1992] #маска
yong_atheletes_1992_info = athletes_1992_info.loc[athletes_1992_info['Age'].idxmin()]

print(yong_atheletes_1992_info['Name'],
      yong_atheletes_1992_info['Event'])

#4.2
print(athletes_info['Sport'].unique())

#4.3
female_tennis_2000_info = athletes_info[
    (athletes_info['Year'] == 2000) & 
    (athletes_info['Sex'] == "F") & 
    (athletes_info['Sport'] == "Tennis")]

print(female_tennis_2000_info["Weight"].mean())

#4.4
china_gold_table_tennis_summer_2008 = athletes_info[
    (athletes_info['Year'] == 2008) & 
    (athletes_info['Medal'] == "Gold") & 
    (athletes_info['NOC'] == "CHN") & 
    (athletes_info['Sport'] == "Table Tennis") & 
    (athletes_info['Season'] == "Summer")]

print(china_gold_table_tennis_summer_2008["Weight"].sum())

#4.5
summer_sports_1988_info = athletes_info[
    (athletes_info['Year'] == 1988) &
    (athletes_info['Season'] == "Summer")]
summer_sports_2004_info = athletes_info[
    (athletes_info['Year'] == 2004) &
    (athletes_info['Season'] == "Summer")]

print(summer_sports_1988_info['Sprots'].nunique(), 
      summer_sports_2004_info['Sprots'].nunique())

"Дописать сравнение"

#4.6
curling_male_2014_info = athletes_info[
    (athletes_info['Year'] == 2014) &
    (athletes_info['Sport'] == "Curling") &
    (athletes_info['Sex'] == "M")] 

plt.figure(figsize=(10, 6))
plt.hist(curling_male_2014_info['Age'].dropna(), bins=10, edgecolor='black')
plt.title('Распределение возраста мужчин-керлингистов на ОИ 2014')
plt.xlabel('Возраст')
plt.ylabel('Количество спортсменов')
plt.show()