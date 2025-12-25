def validate_orders_quanity(quanity_orders):

    if not (quanity_orders.isdigit()):
        print("В кол-ве заказов было введен не число")
        return False
    
    if int(quanity_orders) < 0:
        print("Кол-во закзов не может быть отрицательным")
        return False
    
    return True

def validate_pizza_name(pizza_name):

    if pizza_name == str():
        print("Вместо названия пиццы пришла пустая строка")
        return False

    if " " in pizza_name:
        print("В названии содержаться пробелы")
        return False
    
    if len(pizza_name) >= 30:
        print("Название пиццы слишком длинное")
        return False

    return True

def validate_mount(mount):

    if not (mount.isdigit()):
        print("В числе месяца было введен не число")
        return False
    
    if not (0 < int(mount) <= 12):
        print("Номер месяца должен находиться в диапазоне от 1 до 12")
        return False

    return True

def validate_day(day, mount):
    
    if not (day.isdigit()):
        print("В числе дня было введен не число")
        return False
    
    if int(mount) in (1,3,5,7,8,10,12):
        if not (1 <= int(day) <= 31):
            print("Кол-во дней не совпадает с месяцем")
            return False
    elif mount == 2:
        if not (1 <= int(day) <= 28):
            print("Кол-во дней не совпадает с месяцем")
            return False
    else:
        if not (1 <= int(day) <= 30):
            print("Кол-во дней не совпадает с месяцем")
            return False

    return True

def validate_sale(sale):

    try:
        if not (0 < float(sale) <= 1000000):
            print("Цена не может быть отрицательной или 0")
            return False
    except ValueError:
        print("На месте покупки указано не число")
        return False

    return True