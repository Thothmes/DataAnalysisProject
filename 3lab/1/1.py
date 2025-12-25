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

for i in range(len(el_array[1])):
    print(f"{el_array[0][i]} - генерация: {round(mean_gen_for_last_5[i],2)}, потребление: {round(mean_con_for_last_5[i],2)}")

sum_con_by_years = np.nansum(el_array[2],axis=0)

for i in range(len(sum_con_by_years)):
    print(f"За {i+1992} год мировое потребление электричества составило: {round(sum_con_by_years[i], 2)} млрд. кВт*ч.")

max_gen_by_country = np.nanmax(el_array[1],axis=1)

for i in range(len(max_gen_by_country)):
    print(f"Страна: {el_array[0][i]}, максимальное кол-во эл-ва, произведенного за год: {round(max_gen_by_country[i], 2)}")

print("")
country_gen_more_500 = list()
for i in range(len(mean_gen_for_last_5)):
    if mean_gen_for_last_5[i] > 500:
        country_gen_more_500.append([el_array[0][i], mean_gen_for_last_5[i]])
        print(f"Страна: {el_array[0][i]}, кол-во произведенного эл-ва: {mean_gen_for_last_5[i]}")

p90 = np.percentile(mean_con_for_last_5, 90)
for i in range(len(mean_con_for_last_5)):
    if mean_gen_for_last_5[i] > p90:
        print(f"Страна {el_array[0][i]}, входит в 10% стран с наибольшим средним энергопотреблением за последние 5 лет, равным {mean_con_for_last_5[i]}, при процентиле 90%, равному {p90}")

for i in range(len(el_array[1])):
    if el_array[1][i][-1] >= el_array[1][i][0]*10:
        print(f"Производство энергии у страны {el_array[0][i]} в 1992 было - {el_array[1][i][0]}, а в 2021 - {el_array[1][i][-1]}")

