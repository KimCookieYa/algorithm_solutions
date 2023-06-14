import sys
n = int(input())
city = [[]] * n
for i in range(n):
    city[i] = list(map(int, sys.stdin.readline().split()))

def func(n, r):
    result = 1
    for i in range(n-r, n+1):
        result *= i
    return result

temp = [[x] for x in range(n)]
for i in range(n-1):
    buff = [None] * func(n, i+1)
    idx = 0
    for j in range(n):
        for t in temp:
            if j not in t and city[t[-1]][j] > 0:
                #print(idx)
                buff[idx] = t + [j]
                idx += 1
    
    temp = buff
    del buff 

answer = 10000000
for t in temp:
    if city[t[-1]][t[0]] > 0:
        t = t + [t[0]]
    else:
        continue

    result = 0
    for i in range(n):
        result += city[t[i]][t[i+1]]
    answer = min(result, answer)

print(answer)