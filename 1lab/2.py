def main():
    X = int(input())
    Y = int(input())
    N = int(input())
    if 0 <= Y < X and 1 <= N < 10**10:
        day = (N - Y) // (X - Y) + 1
        if day < 1:
            print(1)
        else:
            print(day)
main()