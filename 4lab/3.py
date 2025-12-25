import pandas as pd


#1
telecom_info = pd.DataFrame(pd.read_csv('telecom_churn.csv'))

telecom_info.info()
# Пропущенных значений нет, согласно данным 

#2
all_clients = telecom_info.value_counts('Churn')
clients_churn_false = (all_clients[False]/all_clients.sum())*100
clients_churn_true = (all_clients[True]/all_clients.sum())*100

print(f'Кол-во всех клиентов: {all_clients.sum()}, процент активных клиентов: {round(clients_churn_false, 2)}%, процент потерянных клиентов: {round(clients_churn_true, 2)}%')

#3
total_minutes = telecom_info['Total day minutes'] + telecom_info['Total eve minutes'] + telecom_info['Total night minutes']
total_calls = telecom_info['Total day calls'] + telecom_info['Total eve calls'] + telecom_info['Total night calls']
telecom_info['Average call duration'] = (total_minutes / total_calls)

print(telecom_info.sort_values(by='Average call duration', ascending=False).head(10))

#4
print(telecom_info.groupby('Churn')['Average call duration'].mean())

#5
print(telecom_info.groupby('Churn')['Customer service calls'].mean())

#6
cross_telecom_info_1 = pd.crosstab(telecom_info['Customer service calls'], telecom_info['Churn']) #Порядок имеет значение. 1 - значения по вертикали, 2 - по горизонтали
print(cross_telecom_info_1[True])
cross_telecom_info_1['Churn percent'] = (cross_telecom_info_1[True]/(cross_telecom_info_1[True]+cross_telecom_info_1[False]))*100
print(cross_telecom_info_1[cross_telecom_info_1['Churn percent'] >= 40])
# С 4 звонков идет резкое увеличение ушедших клиентов.

#7
cross_telecom_info_2 = pd.crosstab(telecom_info['International plan'], telecom_info['Churn']) #Порядок имеет значение. 1 - значения по вертикали, 2 - по горизонтали
print(cross_telecom_info_2)
cross_telecom_info_2['Churn percent'] = (cross_telecom_info_2[True]/(cross_telecom_info_2[True]+cross_telecom_info_2[False]))*100
print(cross_telecom_info_2)
# Да, можно, кол-во ушедших и использовавших при этом международный роуминг более 42%

#8
print('\n')
telecom_info['Predictable churn'] = (telecom_info['International plan'] == 'Yes') | (telecom_info['Customer service calls'] >= 4) # | -или, & - и

false_positive= ((telecom_info['Predictable churn'] == True) & (telecom_info['Churn'])).sum()
false_positive_rate = false_positive / (telecom_info['Churn'] == False).sum()

false_negative = ((telecom_info['Predictable churn'] == False) & (telecom_info['Churn'] == True)).sum()
false_negative_rate = false_negative / (telecom_info['Churn'] == True).sum()

print("--- Оценка простого прогноза ---")
print(f"Всего ложноположительных срабатываний (ошибка I рода): {false_positive}")
print(f"Процент ошибок I рода (от всех лояльных клиентов): {false_positive_rate:.2%}")
print(f"\nВсего ложноотрицательных срабатываний (ошибка II рода): {false_negative}")
print(f"Процент ошибок II рода (от всех ушедших клиентов): {false_negative_rate:.2%}")
