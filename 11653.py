n = int(input())

if n != 1:
    k = 2
    while n != 1:
        if n % k == 0:
            print(k)
            n = n // k
        else:
            k += 1
