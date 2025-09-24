def main():
    N = int(input())
    if 1 <= N <= 100000:
        if len(set(list(str(N)))) == len(str(N)):
            print(N)
        else:
            N_copy = N
            while len(set(list(str(N_copy)))) != len(str(N_copy)):
                N_copy -= 1
            print(N_copy)

main()