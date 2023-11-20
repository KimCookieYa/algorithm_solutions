t = int(input())

a = [25, 10, 5, 1]

for __ in range(t):
    c = int(input())

    for i in range(4):
        print(c // a[i], end=" ")
        c = c % a[i]
    print()
