def main():
    N = int(input())
    S = int(input())
    high_border = ''
    if 1 <= N <= 20 and 1 <= S <= 100:
        for i in range(N+1):
            if i == 0:
                high_border += '1'
            else:
                high_border += '0'
        low_border = high_border[:-1]
        for i in range(int(low_border),int(high_border)):
            print(i)
            if sum(list(map(int, str(i)))) == S:
                print(i, "yes")
                break



main()