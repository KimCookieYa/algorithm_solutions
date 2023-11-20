while True:
    n = int(input())

    if n == -1:
        break

    l = []
    v = 0
    for i in range(1, n):
        if n % i == 0:
            l.append(i)
            v += i

    if v == n:
        print(f"{n} = ", end="")
        for j in l[:-1]:
            print(f"{j} + ", end="")
        print(l[-1])
    else:
        print(f"{n} is NOT perfect.")
