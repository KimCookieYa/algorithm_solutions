n = int(input())
a = list(map(int, input().split()))
a.sort()

## 순열 조합
temp = [[x] for x in range(n)]
for i in range(n-1):
    buff = []
    for j in range(n):
        for t in temp:
            if j not in t:
                buff.append(t + [j])
    
    temp = buff

buff = []
for i in range(len(temp)):
    buff = [a[x] for x in temp[i]]
    temp[i] = buff
print(temp)
print(len(temp))

## 최대값
answer = -1
for t in temp:
    result = 0
    for i in range(n-1):
        result += abs(t[i] - t[i+1])
    answer = max(result, answer)

print(answer)