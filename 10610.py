n = input().strip()

list_n = [int(x) for x in list(n)]

if sum(list_n)%3 == 0 and 0 in list_n:
    for x in sorted(list_n, reverse=True):
        print(x, end='')
else:
    print(-1)