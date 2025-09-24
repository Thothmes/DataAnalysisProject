def main():
    N = int(input())
    if N in range(1,101):
        result = 0
        for i in range(1,N+1):
            result += round((2*i)/(i+2), 3)
        print(result)

main()