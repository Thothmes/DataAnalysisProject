def main():
    X = int(input())
    Y = int(input())
    hours_of_reading = 0
    readed_pages = 0
    day = 0
    while readed_pages < Y:
        if day != 0:
            X += 2
        hours_of_reading += 1
        readed_pages += X*hours_of_reading
        day += 1
    print(day)

main()