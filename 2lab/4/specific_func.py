"""Функция для выполнения задачи"""
def abcd(names, num_bays, bays):

    sum_by_names = []
    plus_sum_by_names = []
    minus_sum_by_names = []
    transactions = []

    all_sum_value = sum(map(lambda val : val[1], bays ))
    med_value = round((all_sum_value/num_bays), 2)

    print(all_sum_value, med_value)

    for name in names:
        sum_by_names.append([name, sum(map(lambda val: val[1], filter(lambda item: item[0] == name, bays)))])

    print(sum_by_names)
    
    sum_by_names = sorted(map(lambda val: [val[0], -(round((val[1]-med_value), 2))], sum_by_names), key=lambda val: val[1]) #Мы получаем список того, насколько откланяется от среднего значения потраченных денег на человека. Если он потратил меньше - у него осталось на какое-то кол-во денег больше, и именно разницу мы и увидим.

    print(sum_by_names)

    for sum_by_name in sum_by_names:
        if sum_by_name[1] > 0:
            plus_sum_by_names.append(sum_by_name)
        elif sum_by_name[1] < 0:
            minus_sum_by_names.append(sum_by_name)

    plus_sum_by_names.reverse()
    print (plus_sum_by_names, minus_sum_by_names)

    for plus_sum_by_name in plus_sum_by_names:
        for minus_sum_by_name in minus_sum_by_names:

            if minus_sum_by_name[1] != 0:

                if plus_sum_by_name[1] >= abs(minus_sum_by_name[1]):
                    transactions.append(
                        [plus_sum_by_name[0], minus_sum_by_name[0], abs(minus_sum_by_name[1])])
                    plus_sum_by_name[1] = plus_sum_by_name[1] - minus_sum_by_name[1]
                    minus_sum_by_name[1] = 0
                            
                elif plus_sum_by_name[1] < abs(minus_sum_by_name[1]):
                    transactions.append(
                        [plus_sum_by_name[0], minus_sum_by_name[0], plus_sum_by_name[1]])
                    plus_sum_by_name[1] = 0
                    minus_sum_by_name[1] = -(abs(minus_sum_by_name[1]) - plus_sum_by_name[1])

                if plus_sum_by_name[1] == 0:
                    break 

    return transactions


"""Функция для перевода полученных в результате ввода значений переменных в рабочий вид"""
def convertor(names, num_bays, bays):

    names = names.split()

    num_bays = float(num_bays) 

    for i in range(len(bays)):
        bays[i] = bays[i].split()
        bays[i][1] = float(bays[i][1])

    return names, num_bays, bays