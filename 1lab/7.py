def main():
    a = int(input()) #масса заготовок
    b = int(input()) #опилки после одного изготовления детали
    n = int(input()) #кол-во заготовок изначально
    if 0 <= b < a <= 10**7 and 0 <= n <= 10**9:
        if a <= 10**5 or n <=10**7:
            details = n
            refuse = n*b
            n = 0
            while refuse >= a:
                n += refuse//a
                refuse = refuse%a
                details += n
                refuse += n * b
                n = 0
        else:
            x = (n*b)//a
            details = ((n*a)-b)//(a-b)
        print(details)

main()
