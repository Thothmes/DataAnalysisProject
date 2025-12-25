import validate_data as val


def special_func(notebook):

    print(notebook)

    print(f"\n————————————————————————————————————————————————————————————————\n"
          f"\nа) список всех пицц:")
    
    pizza_counts = {}
    for order in notebook:
        name = order[0]
        pizza_counts[name] = pizza_counts.get(name, 0) + 1
    
    sorted_pizzas = sorted(pizza_counts.items(), key=lambda x: (-x[1], x[0]))
    print(sorted_pizzas)

    print(f"\n————————————————————————————————————————————————————————————————\n"
          f"\nб) список всех дат:")

    date_sales = {}
    for order in notebook:
        date = (order[2], order[1])
        date_sales[date] = date_sales.get(date, 0) + order[3]
    
    sorted_dates = sorted(date_sales.items(), key=lambda x: (x[0][0], x[0][1]))
    print(sorted_dates)
    
    print(f"\n————————————————————————————————————————————————————————————————\n"
          f"\nв) самая дорогая пицца:")
    
    print(max(notebook, key=lambda x: x[3]))
    
    print(f"\n————————————————————————————————————————————————————————————————\n"
          f"\nг) средняя стоимость заказа:")
    
    print(round((sum(map(lambda val: val[3], notebook))/len(notebook)), 2))

    return

def main():

    notebook = list()

    print("Введите кол-во покупок пиццы")
    quanity_orders = input()
    if not val.validate_orders_quanity(quanity_orders):
        print("Число заказов не соответствует условиям")
        return
    
    for num in range(int(quanity_orders)):

        print(f"Введите данные для {num+1} заказа")

        print("Введите название пиццы. При необходимости - замените пробелы нижним подчеркванием и не более 30 символов")
        pizza_name = input()
        if not val.validate_pizza_name(pizza_name):
            print("Название пиццы не соответствует условиям")
            return    
    
        print("Введите месяц, в который был сделан заказ")
        mount = input()
        if not val.validate_mount(mount):
            print("Число месяца не соответствует условиям")
            return
        
        print("Введите день, в который был сделан заказ. В 1, 3, 5, 7, 8, 10 и 12 месяцах - 31 день, в 2 - 28, в остальных по 30")
        day = input()
        if not val.validate_day(day, mount):
            print("Число дня не соответствует условиям")
            return
        
        print("Введите цену пиццы, но не более 1 миллиона. (Если цена пиццы содержит копейки - пишите через точку)")
        sale = input()
        if not val.validate_sale(sale):
            print("Цена не соответствует условиям")
            return

        notebook.append([pizza_name, int(day), int(mount), float(sale)])

    special_func(notebook)

    return

if __name__ == "__main__":
    main()