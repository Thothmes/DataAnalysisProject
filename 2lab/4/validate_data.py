"""Проверка введёных пользователем кол-ва покупок"""
def validate_num_bays(num_bays):

    if not (num_bays.isdigit()):
        print("В кол-ве покупок было введен не число")
        return False
    
    #int_num_bays = int(num_bays)

    if 1 > int(num_bays):
        print("Кол-во покупок не может быть меньше одной")
        return False

    return True


"""Проверка введёных пользователем списка покупок"""
def validate_bays(bays, names):

    for i in range(len(bays)):

        if not (' ' in bays[i]):
            print("Невозможно разделить")
            return False

        bay_num_i = bays[i].split()

        #print(bays, bay_num_i)

        if len(bay_num_i) != 2:
            print("Неверно разделиться")
            return False
        
        if not (bay_num_i[0] in names):
            print("Такого человека нет")
            return False
        
        if not (bay_num_i[1].isdigit()):
            print("На месте покупки указано не число")
            return False
        
        if int(bay_num_i[1]) < 1:
            print("Сумма покупки не может быть отрицательной или 0")
            return False
    
    return True


"""Проверка введёных пользователем списка имён"""
def validate_names(names):

    if names == str():
        print("Вместо имён пришла пустая строка")
        return False
    
    #print(list(names), list(set(list(names))))

    if " " == list(set(list(names)))[0]:
        print("Вместо имён пришла строка только с пробелами")
        return False
    
    if " " in names:
        list_names = names.split()
    else:
        list_names = [names]
    
    if len(list_names) > 100:
        print("Кол-во имён больше чем было указано в условии")
        return False
    
    if not (len(list_names) == len(set(list_names))):
        print("В списке имеются повторяющиеся имена, это может вызвать потом проблемы")
        return False
    
    for name in list_names:

        if not (len(name) in range(1,21)):
            print("Длина одного из имён превышает допустимое значение в условии")
            return False
        
        if not (name.isalpha()):
            print("Имена содержат что-то ещё, кроме латинских букв")
            return False
        
        if not (name[0].isupper()) or not (name[1:].islower()):
            print("Имя не начинается с заглавной буквы или заглавными буквами являются остальные")
            return False
        
    return True
        