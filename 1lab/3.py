def main():
    X = int(input())
    Y = int(input())
    if 0 < X <= 20 and 0 < Y <= 22:
        time = ((X*2)*Y)
        print(time//60 + 8)
        print(time%60)

main()