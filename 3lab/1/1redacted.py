import numpy as np

el_array = [np.genfromtxt(fname='global-electricity-consumption.csv',
                          dtype=str,
                          skip_header=1,
                          delimiter=',',
                          usecols=(0,)),

            np.genfromtxt(fname='global-electricity-generation.csv',
                          skip_header=1,
                          delimiter=',',
                          usecols=([i for i in range(1,31)])),

            np.genfromtxt(fname='global-electricity-consumption.csv',
                          skip_header=1,
                          delimiter=',',
                          usecols=([i for i in range(1,31)]))
            ]

mean_con_for_last_5 = np.mean(el_array[2][:,-5:], axis=1)
mean_gen_for_last_5 = np.mean(el_array[1][:,-5:], axis=1)

# Векторизованный вывод данных
countries = el_array[0]
results = np.column_stack((countries,
                          np.round(mean_gen_for_last_5, 2),
                          np.round(mean_con_for_last_5, 2)))
print("Средние показатели за последние 5 лет:")
for row in results:
    print(f"{row[0]} - генерация: {row[1]}, потребление: {row[2]}")

sum_con_by_years = np.nansum(el_array[2], axis=0)

# Векторизованный расчет годовых сумм
years = np.arange(1992, 1992 + len(sum_con_by_years))
consumption_data = np.column_stack((years, np.round(sum_con_by_years, 2)))
print("\nМировое потребление по годам:")
for year, consumption in consumption_data:
    print(f"За {int(year)} год мировое потребление электричества составило: {consumption} млрд. кВт*ч.")

max_gen_by_country = np.nanmax(el_array[1], axis=1)

# Векторизованный расчет максимальных значений
max_gen_data = np.column_stack((countries, np.round(max_gen_by_country, 2)))
print("\nМаксимальная генерация по странам:")
for country, max_val in max_gen_data:
    print(f"Страна: {country}, максимальное кол-во эл-ва, произведенного за год: {max_val}")

# Векторизованная фильтрация стран с генерацией > 500
country_gen_more_500_mask = mean_gen_for_last_5 > 500
country_gen_more_500 = np.column_stack((countries[country_gen_more_500_mask],
                                       mean_gen_for_last_5[country_gen_more_500_mask]))
print("\nСтраны с генерацией > 500:")
for country, gen in country_gen_more_500:
    print(f"Страна: {country}, кол-во произведенного эл-ва: {gen}")

# Векторизованный расчет процентилей
p90 = np.percentile(mean_con_for_last_5, 90)
high_consumption_mask = mean_con_for_last_5 > p90
high_consumption_countries = np.column_stack((countries[high_consumption_mask],
                                             mean_con_for_last_5[high_consumption_mask]))
print(f"\nСтраны в верхнем 10% по потреблению (P90 = {p90:.2f}):")
for country, consumption in high_consumption_countries:
    print(f"Страна {country}, среднее потребление: {consumption}")

# Векторизованное сравнение показателей роста
growth_mask = el_array[1][:, -1] >= el_array[1][:, 0] * 10
growth_countries = np.column_stack((countries[growth_mask],
                                   el_array[1][growth_mask, 0],
                                   el_array[1][growth_mask, -1]))
print("\nСтраны с ростом генерации в 10+ раз:")
for country, gen_1992, gen_2021 in growth_countries:
    print(f"Производство энергии у страны {country} в 1992 было - {gen_1992}, а в 2021 - {gen_2021}")

comb_mask = np.logical_and(np.nansum(el_array[1], axis=1) < np.nansum(el_array[2], axis=1),
                           np.nansum(el_array[2], axis=1) > 100)
print(countries[comb_mask])

max_con_country_2020 = np.nanmax(el_array[1][:,-2])
target_mask = el_array[1][:,-2] == max_con_country_2020
print(np.column_stack((countries[target_mask],
                      el_array[1][:,-2][target_mask]))[0][0])
