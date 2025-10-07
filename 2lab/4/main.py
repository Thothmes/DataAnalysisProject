"""
Мысль: это банальная задача коммивояжера (поиск лучшего пути из всех возможных), 
просто с кучей условий и удобной для восприятия оберткой. 
Скорость тут растет экспоненциально, потому надо применять жадные алгоритмы 
"""


import input_data as inp
import validate_data as val
import specific_func as spec


def main():

    names = inp.input_names()
    if not val.validate_names(names):
        print("Список имён не прошёл проверку")
        return

    num_bays = inp.input_num_bays()
    if not val.validate_num_bays(num_bays):
        print("Кол-во покупок не прошло проверку")
        return

    bays = inp.input_bays(int(num_bays))
    if not val.validate_bays(bays, names):
        print("Список покупок не прошёл проверку")
        return
    
    names, num_bays, bays = spec.convertor(names, num_bays, bays)

    #print(names, num_bays, bays)

    transactions = spec.abcd(names, num_bays, bays)

    print(len(transactions))

    for transaction in transactions:
        print(transaction[0], transaction[1], transaction[2])

if __name__ == "__main__":
    main()