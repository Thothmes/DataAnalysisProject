import re
from collections import Counter


def read_data():
    try:
        with open('mbox.txt', 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        print("Файл 'mbox.txt' не найден в директории программы.")
        return []


def main():
    counter: Counter = Counter()

    for line in read_data():
        if re.match(r"From .+@", line) is not None:
            line_split: list = line.split()
            if len(line_split) >= 2:
                counter[line_split[1].lower()] += 1

    max_count: int = 0
    most_common: list[tuple[str, int]] = []

    for email, count in counter.items():
        if count > max_count:
            most_common = [(email, count)]
            max_count = count
        elif count == max_count:
            most_common.append((email, count))

    if not most_common:
        print(f'\nНе найден ни один почтовый отправитель.')
        return
    elif len(most_common) == 1:
        key, count = most_common[0]
        print(f'\nСамый частый почтовый отправитель: "{key}" встречается {count} раз(а).')
    else:
        print(
            f'\nНайдено несколько самых частых почтовых отправителей, '
            f'каждый из которых встречается {most_common[0][1]} раз(а):'
        )
        for i in most_common:
            print(f'Отправитель: "{i[0]}".')

    keys_list = list(counter.keys())
    print("\nВсе почтовые отправители:", *keys_list, sep="\n")


if __name__ == '__main__':
    main()