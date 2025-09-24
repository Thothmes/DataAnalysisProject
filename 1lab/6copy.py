def main():
    N = int(input())
    S = int(input())
    if 1 <= N <= 20 and 1 <= S <= 100:
        result = ''
        if N == 1 and S <= 9:
            print(S)
        else:
            last_num = 0
            while S > 9:
                S -= 9
                result += '9'
            if 0 <= S < 9 and len(result)+1 != N:
                last_num = S - 1
            elif S == 9 or len(result)+1 == N:
                last_num = S
            result += str(last_num)
            S -= (last_num)
            if len(result) != N:
                next_num = len(result)
                for i in range(next_num, N):
                    if i == N-1 and S == 1:
                        result += '1'
                    elif i < N-1 and S == 1:
                        result += '0'
            if len(result) == N:
                result = (''.join(reversed(str(result))))
                print(int(result))
            else:
                print('NO')

main()