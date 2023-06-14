import sys
input = sys.stdin.readline

n = int(input())
area = [[0, 0]] * n
for i in range(n):
    c, r = map(int, input().split())
    area[i] = [c-r, c+r]

#area.sort(key=lambda x: (x[0], -x[1]))
area += [0] * n
k = 0
for i in range(n-1):
    for j in range(i+1, n):
        if area[i][1] == area[j][0]:
            area[n+k-1] = [area[i][0], area[j][1]]
            k += 1
        elif area[i][0] == area[j][1]:
            area[n+k-1] = [area[j][0], area[i][1]]
            k += 1

answer = n+1
for item in area[n:]:
    if item in area[:n]:
        answer += 1

print(answer)